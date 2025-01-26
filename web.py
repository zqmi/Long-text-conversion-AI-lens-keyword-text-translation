import gradio as gr
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from peft import PeftModel

lora_path = './output/Qwen2_Poems/checkpoint-1500'

# 1. 加载预训练语言大模型
MODEL_NAME = './Qwen2.5-0.5B'
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained('./Qwen2.5-0.5B', device_map="auto",torch_dtype=torch.bfloat16)
model = PeftModel.from_pretrained(model, model_id=lora_path)

# 2. 定义聊天函数
def chat_with_model(prompt, max_length=800):
    try:
        # 构建输入
        inputs = tokenizer.apply_chat_template(
            [
                {"role": "user", "content": "你要将各种文段改成镜头画面描述格式"},
                {"role": "user", "content": prompt}
            ],
            add_generation_prompt=True,  # 添加生成标记
            tokenize=True,
            return_tensors="pt",
            return_dict=True
        ).to('cuda')  # 移动到 GPU 上

        # 生成参数
        gen_kwargs = {
            "max_length": max_length,
            "do_sample": True,
            "top_k": 1
        }

        # 模型生成输出
        with torch.no_grad():
            outputs = model.generate(**inputs, **gen_kwargs)
            outputs = outputs[:, inputs['input_ids'].shape[1]:]  # 跳过输入部分
            output = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return output

    except Exception as e:
        return f"Error: {e}"
    
interface = gr.Interface(
    fn=chat_with_model,
    inputs=[
        gr.Textbox(label="请输入文段", placeholder="临别时，朋友握住手嘱托：“若回洛阳见到亲友，替我告诉他们，我依旧初心如玉，胸怀清明，就像那冰冷却纯净的玉壶。”言毕，转身登船，孤帆远影，渐消于江雾之中。"),
        gr.Slider(minimum=100, maximum=2500, step=100, value=800, label="生成最大长度")
    ],
    outputs=gr.Textbox(label="输出镜头画面描述"),
    title="语言大模型镜头画面生成器(该微调模型适合用于AI绘画中的关键词生成)",
    description="输入文段后，模型将生成对应的镜头画面描述。",
    examples=[
        ["天亮时分，送行的船在江上渐行渐远，孤山独立于江天之间，显得格外寂寥。站在岸上的人久久凝望，目光穿过雨幕，似要将这离别的场景深深刻入记忆。。", 1000],
        ["谢家最小的女儿自小备受宠爱，娇俏灵慧，父母视若掌上明珠。然而，命运却与她作对，嫁给了一个名叫黔娄的书生后，生活并未如她所愿，反而事事不顺。", 1000],
        ["家中贫寒，常常入不敷出。一次，她看到丈夫因寒冷无衣可穿，便翻遍画箧，将仅存的一点绢帛取出为他缝补。而为了给丈夫买一壶酒暖身，她忍痛摘下自己最心爱的金钗，换来些许铜钱。", 1000],
        ["生活虽苦，她却并未埋怨，而是以田野间的野菜充作膳食，用飘零的落叶作为薪柴，靠院子里那棵古槐庇佑着一家人的艰难岁月。", 1000],
        ["多年后，丈夫寒窗苦读终成正果，俸禄高达十万。夫妻二人终于摆脱了贫困的阴影。他握住她的手，柔声说道：“今日已有余裕，且让我为你备下供奉的酒菜，答谢你的无悔付出。”两人相视一笑，仿佛一切艰难都化为眼前的温暖与幸福。", 1000],
    ]
)

if __name__ == "__main__":
    interface.launch()  # 设置为共享模式以生成公网访问链接