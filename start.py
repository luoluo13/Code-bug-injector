import gradio as gr
from bug_injector import inject_bugs
from utils import SUPPORTED_LANGUAGES
from ollama_handler import inject_bugs_with_ollama, is_ollama_available, get_ollama_models

def process_code(input_code, language, injection_method, ollama_model=None):
    """
    处理输入代码，根据选择的方法注入bug后返回
    """
    try:
        if injection_method == "preset":
            # 使用预设方法注入bug
            buggy_code = inject_bugs(input_code, language)
            return buggy_code
        elif injection_method == "ollama":
            # 使用Ollama模型注入bug
            if not ollama_model:
                return "错误: 请选择一个Ollama模型"
            buggy_code = inject_bugs_with_ollama(input_code, language, ollama_model)
            return buggy_code
        else:
            return "错误: 未知的注入方法"
    except Exception as e:
        return f"错误: {str(e)}"

def update_model_dropdown():
    """
    更新模型下拉列表
    """
    if is_ollama_available():
        models = get_ollama_models()
        return gr.update(choices=models, value=models[0] if models else None, visible=True)
    else:
        return gr.update(choices=[], value=None, visible=False)

# 自定义CSS样式 - 更加精致的粉蓝色系二次元风格
custom_css = """
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@300;400;700&family=Comic+Neue:ital,wght@0,400;0,700;1,400;1,700&display=swap');

body {
    background: linear-gradient(135deg, #f0f9ff 0%, #e6f7ff 100%);
    font-family: 'Noto Sans SC', 'Comic Neue', cursive, sans-serif;
    overflow-x: hidden;
}

.container {
    max-width: 1200px !important;
    margin: 0 auto;
    padding: 20px;
}

.gradio-container {
    background: rgba(255, 255, 255, 0.85) !important;
    backdrop-filter: blur(10px);
    border-radius: 25px !important;
    box-shadow: 0 12px 40px rgba(173, 216, 230, 0.4) !important;
    border: 2px solid rgba(173, 216, 230, 0.6) !important;
    position: relative;
    overflow: hidden;
}

.gradio-container::before {
    content: "";
    position: absolute;
    top: -50px;
    right: -50px;
    width: 200px;
    height: 200px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(255, 182, 193, 0.3) 0%, transparent 70%);
    z-index: -1;
}

.gradio-container::after {
    content: "";
    position: absolute;
    bottom: -80px;
    left: -30px;
    width: 250px;
    height: 250px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(173, 216, 230, 0.3) 0%, transparent 70%);
    z-index: -1;
}

/* 标题样式 */
h1 {
    color: #ff69b4 !important;
    text-align: center;
    font-weight: 700 !important;
    text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.1);
    background: linear-gradient(45deg, #ff69b4, #87ceeb, #dda0dd);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    font-size: 2.8rem !important;
    margin-top: 10px !important;
    margin-bottom: 10px !important;
    letter-spacing: 1px;
}

/* 描述文字样式 */
.markdown p {
    color: #6a7b8c;
    text-align: center;
    font-size: 18px;
    margin-bottom: 25px;
    font-weight: 500;
}

/* 按钮样式 */
button {
    background: linear-gradient(45deg, #ff69b4, #87ceeb) !important;
    border: none !important;
    color: white !important;
    font-weight: bold !important;
    transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1) !important;
    border-radius: 50px !important;
    padding: 12px 30px !important;
    box-shadow: 0 6px 20px rgba(135, 206, 235, 0.5) !important;
    font-size: 16px !important;
    position: relative;
    overflow: hidden;
}

button:hover {
    transform: translateY(-5px) scale(1.03);
    box-shadow: 0 10px 25px rgba(255, 105, 180, 0.7) !important;
}

button:active {
    transform: translateY(0) scale(0.98);
}

button::after {
    content: "";
    position: absolute;
    top: -50%;
    left: -60%;
    width: 20px;
    height: 200%;
    background: rgba(255, 255, 255, 0.3);
    transform: rotate(30deg);
    transition: all 0.6s;
}

button:hover::after {
    left: 120%;
}

/* 下拉菜单和输入框样式 */
select, .code-editor, input {
    border: 2px solid #d0e8ff !important;
    border-radius: 18px !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 4px 15px rgba(208, 232, 255, 0.3) !important;
}

select:focus, .code-editor:focus, input:focus {
    border-color: #ff69b4 !important;
    box-shadow: 0 0 0 4px rgba(255, 105, 180, 0.3) !important;
    outline: none;
}

/* 代码框样式 */
.code-editor textarea {
    background: #f8fdff !important;
    font-family: 'Consolas', 'Courier New', monospace !important;
    border-radius: 15px !important;
}

/* 卡片样式 */
.column {
    background: rgba(240, 248, 255, 0.8) !important;
    border-radius: 20px !important;
    padding: 25px !important;
    box-shadow: 0 6px 25px rgba(173, 216, 235, 0.3) !important;
    border: 1px solid #e6f7ff !important;
    transition: all 0.3s ease;
}

.column:hover {
    box-shadow: 0 8px 30px rgba(173, 216, 235, 0.4) !important;
    transform: translateY(-3px);
}

/* 方法选择区域 */
.group {
    background: linear-gradient(135deg, #e3f2fd 0%, #f8bbd0 100%) !important;
    border-radius: 20px !important;
    padding: 20px !important;
    margin-bottom: 25px !important;
    box-shadow: 0 6px 20px rgba(227, 242, 253, 0.4) !important;
    border: 2px solid #c5e3ff !important;
}

.group h3 {
    color: #ff69b4 !important;
    margin-top: 0 !important;
    font-weight: 700 !important;
    text-align: center;
}

/* 单选按钮样式 */
input[type="radio"] {
    accent-color: #ff69b4 !important;
}

/* 标签样式 */
label {
    color: #5a6c87 !important;
    font-weight: 600 !important;
    margin-bottom: 8px !important;
}

/* 装饰性元素 */
.decoration {
    position: absolute;
    z-index: -1;
}

.decoration.circle {
    width: 200px;
    height: 200px;
    border-radius: 50%;
    background: linear-gradient(45deg, rgba(255, 105, 180, 0.2), rgba(135, 206, 235, 0.2));
}

.decoration.triangle {
    width: 0;
    height: 0;
    border-left: 50px solid transparent;
    border-right: 50px solid transparent;
    border-bottom: 100px solid rgba(135, 206, 235, 0.2);
    transform: rotate(25deg);
}

/* 响应式设计 */
@media (max-width: 768px) {
    .container {
        padding: 15px;
    }
    
    h1 {
        font-size: 2rem !important;
    }
    
    .column {
        padding: 15px !important;
    }
}

/* 滚动条样式 */
::-webkit-scrollbar {
    width: 8px;
    height: 8px;
}

::-webkit-scrollbar-track {
    background: rgba(240, 248, 255, 0.5);
    border-radius: 4px;
}

::-webkit-scrollbar-thumb {
    background: linear-gradient(45deg, #ff69b4, #87ceeb);
    border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
    background: linear-gradient(45deg, #ff5ba7, #73b9e5);
}

/* 动画效果 */
@keyframes float {
    0% {
        transform: translateY(0px);
    }
    50% {
        transform: translateY(-10px);
    }
    100% {
        transform: translateY(0px);
    }
}

@keyframes pulse {
    0% {
        transform: scale(1);
    }
    50% {
        transform: scale(1.05);
    }
    100% {
        transform: scale(1);
    }
}

.animate-float {
    animation: float 3s ease-in-out infinite;
}

.animate-pulse {
    animation: pulse 2s ease-in-out infinite;
}
"""

# 创建Gradio界面
with gr.Blocks(title="反向编程工具", css=custom_css) as demo:
    # 添加装饰性元素
    gr.HTML("""
    <div style="position: fixed; top: 5%; left: 3%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, rgba(255, 182, 193, 0.4) 0%, transparent 70%); z-index: -1; animation: float 4s ease-in-out infinite;"></div>
    <div style="position: fixed; bottom: 8%; right: 4%; width: 150px; height: 150px; border-radius: 50%; background: radial-gradient(circle, rgba(173, 216, 230, 0.4) 0%, transparent 70%); z-index: -1; animation: float 5s ease-in-out infinite;"></div>
    <div style="position: fixed; top: 15%; right: 8%; width: 0; height: 0; border-left: 40px solid transparent; border-right: 40px solid transparent; border-bottom: 80px solid rgba(255, 192, 203, 0.3); transform: rotate(25deg); z-index: -1; animation: pulse 3s ease-in-out infinite;"></div>
    <div style="position: fixed; bottom: 20%; left: 8%; width: 0; height: 0; border-left: 60px solid transparent; border-right: 60px solid transparent; border-bottom: 120px solid rgba(135, 206, 250, 0.3); transform: rotate(-15deg); z-index: -1; animation: pulse 4s ease-in-out infinite;"></div>
    """)
    
    gr.Markdown("# 反向编程工具 🎀")
    gr.Markdown("输入您的代码，我会为您添加一些'有趣'的小bug！✨")
    gr.Markdown("⚠请注意，使用llm模型注入时，注入质量取决于模型能力，不稳定因素较高！")

    with gr.Row():
        with gr.Column(scale=1):
            input_code = gr.Code(label="输入代码 ✨", language="python", lines=15)
            
            with gr.Group():
                gr.Markdown("### Bug注入方法设置 ⚙️")
                injection_method = gr.Radio(
                    choices=[("预设方法", "preset"), ("Ollama模型", "ollama")],
                    value="preset",
                    label="选择注入方法 🎯"
                )
                
                with gr.Column(visible=is_ollama_available()) as ollama_options:
                    ollama_model = gr.Dropdown(
                        choices=get_ollama_models() if is_ollama_available() else [],
                        value=get_ollama_models()[0] if is_ollama_available() and get_ollama_models() else None,
                        label="选择Ollama模型 🤖"
                    )
                    refresh_models_btn = gr.Button("刷新模型列表 🔄")
            
            language = gr.Dropdown(
                choices=list(SUPPORTED_LANGUAGES.keys()),
                value="python",
                label="编程语言 💻"
            )
            submit_btn = gr.Button("注入Bug 🐞", elem_classes=["animate-pulse"])
        
        with gr.Column(scale=1):
            output_code = gr.Code(label="注入Bug后的代码 🎃", language="python", lines=15)
    
    # 设置事件处理
    injection_method.change(
        fn=lambda method: gr.update(visible=(method == "ollama")),
        inputs=injection_method,
        outputs=ollama_options
    )
    
    refresh_models_btn.click(
        fn=update_model_dropdown,
        inputs=None,
        outputs=ollama_model
    )
    
    submit_btn.click(
        fn=process_code,
        inputs=[input_code, language, injection_method, ollama_model],
        outputs=output_code
    )

if __name__ == "__main__":
    demo.launch()