# Long-text-conversion-AI-lens-keyword-text-translation
"Long Text Conversion to AI Lens Keyword Text" refers to transforming lengthy text into concise keywords that capture essential details, using AI to identify key elements like characters, scenes, and actions for quick understanding.

项目简介
该项目使用基于 Transformer 的预训练语言大模型，通过输入自然语言文段来生成镜头画面描述。用户可以通过 Gradio 界面与模型进行交互，输入文本后，模型将生成对应的镜头画面描述。

项目结构
.
├── web.py                    # 主程序文件，包含模型加载与 Gradio 界面
├── Qwen2.5-0.5B/             # 预训练模型文件
├── README.md                 # 项目的说明文档
└── requirements.txt          # 项目依赖

克隆项目：
git clone https://github.com/your-username/your-repository.git
cd your-repository

安装依赖：
pip install -r requirements.txt

requirements.txt 文件内容：

下载预训练模型：
将预训练模型文件（Qwen2.5-0.5B）放置在项目根目录中，或者根据需要修改 MODEL_NAME 路径。

使用方法
在项目目录下运行以下命令启动应用：
python app.py

启动后，您可以在浏览器中访问本地地址：http://127.0.0.1:7860

