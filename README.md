# Long-text-conversion-AI-lens-keyword-text-translation
"Long Text Conversion to AI Lens Keyword Text" refers to transforming lengthy text into concise keywords that capture essential details, using AI to identify key elements like characters, scenes, and actions for quick understanding.

# 项目简介
该项目使用基于 Transformer 的预训练语言大模型，通过输入自然语言文段来生成镜头画面描述。用户可以通过 Gradio 界面与模型进行交互，输入文本后，模型将生成对应的镜头画面描述。

# 运行网站

![aa70a88b6fa36c870d135fb4c5a1286](https://github.com/user-attachments/assets/9610f403-03b1-41ad-9422-f0b41d57cab9)

# 克隆项目：

git clone https://github.com/zqmi/Long-text-conversion-AI-lens-keyword-text-translation.git

cd Long-text-conversion-AI-lens-keyword-text-translation

# 安装依赖：

pip install -r requirements.txt

# 下载预训练模型：

将预训练模型文件（Qwen2.5-0.5B）放置在项目根目录中。

使用方法

在项目目录下运行以下命令启动应用：

python web.py

启动后，您可以在浏览器中访问本地地址：http://127.0.0.1:7860

# 模型功能介绍

该模型是基于Qwen2.5系列进行微调而成，擅长将一段文本故事转换为AI绘画所需要的镜头关键词，适用于小说生成一系列镜头画面的辅助工具。

# 案例一
输入：

天亮时分，送行的船在江上渐行渐远，孤山独立于江天之间，显得格外寂寥。站在岸上的人久久凝望，目光穿过雨幕，似要将这离别的场景深深刻入记忆。
输出：

main_body:站于岸上的男子，着朴素长衫，目光深邃，上体紧握船桨，下脚稳固支撑，神态沉静而略显孤独。

main_body_motion:他目光穿过雨雾向孤山远望，手握船桨轻摇。

environment:江上船渐行渐远，孤山立于天际，雨雾中显得更加孤立。

camera:镜头拉近，聚焦于男子凝望的瞬间，雨雾中山影隐约可见，最后定格于其背影。

light:夕阳余晖洒在水面，微光穿透雨雾，色调温暖而略带忧伤。

feeling_describe:寂静、孤独与怀旧感将画面拉至最末，烘托出深深的依恋与不舍。

# 案例二
输入：

谢家最小的女儿自小备受宠爱，娇俏灵慧，父母视若掌上明珠。然而，命运却与她作对，嫁给了一个名叫黔娄的书生后，生活并未如她所愿，反而事事不顺。
输出：

main_body:少女娇艳、眼含温柔微笑，父母宠爱有加，她却冷淡独立。

main_body_motion:她嬉笑穿梭，父静默远望。

environment:深夜，屋内昏暗，外街空旷，微风轻拂。

camera:镜头缓缓拉近，定格于她轻蔑的笑颜，镜头渐远。

light:昏暗中，光线忽明忽暗，室内一片昏暗。

feeling_describe:孤独、失望，静谧中充满无望的沉寂。

# 案例三
输入：

家中贫寒，常常入不敷出。一次，她看到丈夫因寒冷无衣可穿，便翻遍画箧，将仅存的一点绢帛取出为他缝补。而为了给丈夫买一壶酒暖身，她忍痛摘下自己最心爱的金钗，换来些许铜钱。

输出：

main_body:少女，素衣，青色长袍，发丝凌乱，衣着单薄，眼神空洞。

main_body_motion:她紧握金钗，低头缝补，双手无力，双肩微微发抖。

environment:家中昏暗、空荡，外面寒风呼啸，室内一片死寂。

camera:镜头拉近，捕捉她紧握金钗的细节，背景模糊。

light:昏暗光线，室内微弱的火光打亮微弱的灯，映得她的脸庞更加苍白。

feeling_describe:焦虑、孤独、艰难。








