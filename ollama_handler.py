import json
import requests
import re

def is_ollama_available():
    """
    检查Ollama服务是否可用
    """
    try:
        response = requests.get("http://localhost:11434/api/tags", timeout=5)
        return response.status_code == 200
    except:
        return False

def get_ollama_models():
    """
    获取Ollama可用的模型列表
    """
    try:
        response = requests.get("http://localhost:11434/api/tags")
        if response.status_code == 200:
            models = response.json().get("models", [])
            return [model["name"] for model in models]
    except:
        pass
    return []

def inject_bugs_with_ollama(code, language, model_name):
    """
    使用Ollama模型为代码注入bug
    """
    prompt = _create_bug_injection_prompt(code, language)
    
    payload = {
        "model": model_name,
        "prompt": prompt,
        "stream": False
    }
    
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json=payload,
            timeout=60
        )
        
        if response.status_code == 200:
            result = response.json()
            buggy_code = result.get("response", "")
            # 尝试从响应中提取代码部分
            extracted_code = _extract_code_from_response(buggy_code)
            return extracted_code if extracted_code else buggy_code
        else:
            return f"Ollama服务错误: {response.status_code}"
    except Exception as e:
        return f"连接Ollama服务时出错: {str(e)}"

def _create_bug_injection_prompt(code, language):
    """
    创建用于bug注入的提示词
    """
    language_name = {"python": "Python", "javascript": "JavaScript", "java": "Java"}.get(language, language)
    
    prompt = f"""
你是一个专业的程序员，但今天你要扮演一个"反向编程助手"来整蛊用户。你的任务不是修复代码中的bug，而是巧妙地在一段没有明显错误的{language_name}代码中添加一些有趣的小bug。

请遵循以下原则：
1. 必须添加BUG，并确保添加的bug是微妙的，会让代码无法按原有逻辑运行，有时候无法运行，或者运行时出错。
2. 保持代码的基本结构和功能不变。
3. 可以添加的bug类型包括但不限于：
   - 语法错误（如缺少分号、括号、花括号）
   - 拼写错误（如将变量名、关键字、函数名称的拼写故意写错几个字母）
   - 逻辑错误（如条件判断错误）
   - 边界条件错误（如差一错误）
   - 运算符错误（如使用=代替==）
   - 循环控制错误
   - 变量名拼写错误
   - 数据类型使用错误
   - 函数调用错误
   - 数组索引错误
   - 函数参数错误
4. 特别注意：至少注入2个不同类型的bug！不要添加过于简单无聊的bug。
5. 只返回注入后的代码，不要添加任何解释或其他文本，也不要使用markdown格式。

原始{language_name}代码如下：
{code}

请返回添加了bug的代码：
"""
    return prompt

def _extract_code_from_response(response):
    """
    从模型响应中提取代码部分
    """
    # 尝试提取代码块
    code_block_pattern = r"```(?:[a-zA-Z]*)\n(.*?)\n```"
    match = re.search(code_block_pattern, response, re.DOTALL)
    if match:
        return match.group(1)
    
    # 如果没有代码块，返回整个响应
    return response