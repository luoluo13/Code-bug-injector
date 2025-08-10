import random
import re
from utils import SUPPORTED_LANGUAGES

def inject_bugs(code, language="python"):
    """
    根据指定的语言为代码注入bug
    """
    # 定义所有可能的bug注入函数
    bug_functions = {
        # Python相关函数
        'inject_off_by_one_error': inject_off_by_one_error,
        'inject_comparison_error': inject_comparison_error,
        'inject_logic_error': inject_logic_error,
        'inject_semicolon_error': inject_semicolon_error,
        'inject_indentation_error': inject_indentation_error,
        'inject_variable_name_error': inject_variable_name_error,
        'inject_string_concatenation_error': inject_string_concatenation_error,
        'inject_list_index_error': inject_list_index_error,
        'inject_dict_key_error': inject_dict_key_error,
        'inject_math_operator_error': inject_math_operator_error,
        'inject_function_call_error': inject_function_call_error,
        'inject_assignment_error': inject_assignment_error,
        'inject_comment_error': inject_comment_error,
        'inject_import_error': inject_import_error,
        'inject_bracket_error': inject_bracket_error,
        
        # JavaScript相关函数
        'inject_javascript_bugs': inject_javascript_bugs,
        'inject_javascript_semicolon_error': inject_javascript_semicolon_error,
        'inject_javascript_var_error': inject_javascript_var_error,
        'inject_javascript_type_coercion_error': inject_javascript_type_coercion_error,
        'inject_javascript_async_error': inject_javascript_async_error,
        'inject_javascript_array_error': inject_javascript_array_error,
        'inject_javascript_object_error': inject_javascript_object_error,
        'inject_javascript_comparison_error': inject_javascript_comparison_error,
        'inject_javascript_function_error': inject_javascript_function_error,
        'inject_javascript_bracket_error': inject_javascript_bracket_error,
        'inject_javascript_undefined_error': inject_javascript_undefined_error,
        
        # Java相关函数
        'inject_java_bugs': inject_java_bugs,
        'inject_java_semicolon_error': inject_java_semicolon_error,
        'inject_java_bracket_error': inject_java_bracket_error,
        'inject_java_type_error': inject_java_type_error,
        'inject_java_null_pointer_error': inject_java_null_pointer_error,
        'inject_java_array_index_error': inject_java_array_index_error,
        'inject_java_loop_error': inject_java_loop_error,
        'inject_java_exception_error': inject_java_exception_error,
        'inject_java_modifier_error': inject_java_modifier_error,
        'inject_java_constructor_error': inject_java_constructor_error,
        'inject_java_overloading_error': inject_java_overloading_error,
        'inject_java_inheritance_error': inject_java_inheritance_error
    }
    
    # 获取语言特定的bug注入函数名称
    if language in SUPPORTED_LANGUAGES:
        bug_function_names = SUPPORTED_LANGUAGES[language]
    else:
        # 默认使用Python的bug注入
        bug_function_names = SUPPORTED_LANGUAGES["python"]
    
    # 随机选择要注入的bug数量 (增加到最多5个)
    bug_count = random.randint(2, 5)
    
    # 应用bug注入函数
    buggy_code = code
    for _ in range(bug_count):
        func_name = random.choice(bug_function_names)
        if func_name in bug_functions:
            bug_func = bug_functions[func_name]
            buggy_code = bug_func(buggy_code)
    
    return buggy_code

# Python特定的bug注入函数
def inject_off_by_one_error(code):
    """注入差一错误"""
    lines = code.split('\n')
    new_lines = []
    for line in lines:
        # 查找循环结构
        if re.search(r'range\s*\(', line) and 'for' in line:
            # 将 range(n) 替换为 range(n+1) 或 range(n-1)
            if random.choice([True, False]):
                line = re.sub(r'range\s*\(([^)]+)\)', r'range(\1+1)', line)
            else:
                line = re.sub(r'range\s*\(([^)]+)\)', r'range(\1-1)', line)
        new_lines.append(line)
    return '\n'.join(new_lines)

def inject_comparison_error(code):
    """注入比较运算符错误"""
    # 使用正则表达式避免重复替换
    code = re.sub(r'(?<![\!<\>])==(?!>)', '=', code)  # 将相等比较替换为赋值
    code = re.sub(r'(?<!\!)!=(?!=)', '==', code)  # 将不等比较替换为相等比较
    code = re.sub(r'<=(?!=)', '<', code)  # 将小于等于替换为小于
    code = re.sub(r'>=(?!=)', '>', code)  # 将大于等于替换为大于
    return code

def inject_logic_error(code):
    """注入逻辑运算符错误"""
    # 避免重复替换
    code = code.replace(' and ', ' or ')
    code = code.replace(' or ', ' and ')
    return code

def inject_semicolon_error(code):
    """注入分号错误（在Python中添加不必要的分号）"""
    lines = code.split('\n')
    new_lines = []
    for line in lines:
        # 在一些行末添加分号
        if line.strip() and random.random() < 0.3 and not line.strip().endswith(':') and not line.strip().endswith('\\'):
            if not line.rstrip().endswith(';'):
                line = line.rstrip() + ';'
        new_lines.append(line)
    return '\n'.join(new_lines)

def inject_indentation_error(code):
    """注入缩进错误"""
    lines = code.split('\n')
    new_lines = []
    for i, line in enumerate(lines):
        # 随机修改某些行的缩进
        if line.strip() and random.random() < 0.2 and not line.startswith('#'):
            stripped = line.lstrip()
            current_indent = len(line) - len(stripped)
            if current_indent > 0:
                # 修改缩进
                if current_indent >= 4 and random.choice([True, False]):
                    # 减少缩进
                    line = ' ' * (current_indent - 1) + stripped
                else:
                    # 增加缩进
                    line = ' ' * (current_indent + 1) + stripped
        new_lines.append(line)
    return '\n'.join(new_lines)

def inject_variable_name_error(code):
    """注入变量名错误"""
    # 将一些变量名稍作修改
    code = re.sub(r'\b(count)\b', 'counter', code, count=1)
    code = re.sub(r'\b(data)\b', 'datas', code, count=1)
    code = re.sub(r'\b(items)\b', 'item', code, count=1)
    code = re.sub(r'\b(result)\b', 'results', code, count=1)
    code = re.sub(r'\b(value)\b', 'values', code, count=1)
    return code

def inject_string_concatenation_error(code):
    """注入字符串连接错误"""
    # 将 + 替换为 , 在print语句中
    code = re.sub(r'print\s*\(([^)]+)\s*\+\s*([^)]+)\)', r'print(\1, \2)', code)
    return code

def inject_list_index_error(code):
    """注入列表索引错误"""
    # 在列表访问中添加错误的索引
    code = re.sub(r'(\w+)\[(\d+)\]', lambda m: f'{m.group(1)}[{int(m.group(2))+1}]' if random.random() < 0.3 else m.group(0), code)
    return code

def inject_dict_key_error(code):
    """注入字典键错误"""
    # 修改字典键名
    code = re.sub(r'"([^"]+)"\s*:', lambda m: f'"{m.group(1)}_" :' if random.random() < 0.3 else m.group(0), code)
    code = re.sub(r"'([^']+)'\\s*:", lambda m: f"'{m.group(1)}_' :" if random.random() < 0.3 else m.group(0), code)
    return code

def inject_math_operator_error(code):
    """注入数学运算符错误"""
    # 将 * 替换为 /，+ 替换为 -
    code = code.replace(' * ', ' / ')
    code = code.replace(' + ', ' - ')
    return code

def inject_function_call_error(code):
    """注入函数调用错误"""
    # 移除函数参数
    code = re.sub(r'(\w+)\s*\([^)]*\)', lambda m: f'{m.group(1)}()' if random.random() < 0.2 else m.group(0), code)
    return code

def inject_assignment_error(code):
    """注入赋值错误"""
    # 将 == 替换为 =
    code = re.sub(r'(\w+)\s*==', r'\1 =', code)
    return code

def inject_comment_error(code):
    """注入注释错误"""
    # 将注释内容复制到代码行
    lines = code.split('\n')
    new_lines = []
    for line in lines:
        if line.strip().startswith('#') and random.random() < 0.3:
            comment_content = line.strip()[1:].strip()
            new_lines.append(line)
            new_lines.append(comment_content)  # 将注释内容作为代码添加
        else:
            new_lines.append(line)
    return '\n'.join(new_lines)

def inject_import_error(code):
    """注入导入错误"""
    # 修改导入语句
    code = re.sub(r'import (\w+)', lambda m: f'import {m.group(1)} as {m.group(1)}_' if random.random() < 0.3 else m.group(0), code)
    return code

def inject_bracket_error(code):
    """注入括号错误"""
    # 随机添加或移除括号
    if random.random() < 0.3:
        code = code.replace('(', '((', 1)
    if random.random() < 0.3:
        code = code.replace('))', ')', 1)
    return code

# JavaScript特定的bug注入函数
def inject_javascript_bugs(code):
    """JavaScript特定的bug注入"""
    # 将 === 替换为 ==
    code = code.replace('===', '==')
    # 将 let/const 替换为 var
    code = code.replace('let ', 'var ')
    code = code.replace('const ', 'var ')
    # 将 != 替换为 !==
    code = code.replace('!=', '!==')
    return code

def inject_javascript_semicolon_error(code):
    """JavaScript中移除分号"""
    lines = code.split('\n')
    new_lines = []
    for line in lines:
        if line.strip() and random.random() < 0.5 and line.strip().endswith(';'):
            line = line.rstrip(';')
        new_lines.append(line)
    return '\n'.join(new_lines)

def inject_javascript_var_error(code):
    """JavaScript变量声明错误"""
    # 将var替换为let或const
    code = code.replace('var ', 'let ' if random.random() < 0.5 else 'const ')
    return code

def inject_javascript_type_coercion_error(code):
    """JavaScript类型强制转换错误"""
    # 将 == 替换为 ===
    code = code.replace('==', '===')
    return code

def inject_javascript_async_error(code):
    """JavaScript异步错误"""
    # 移除async关键字
    code = code.replace('async ', '')
    return code

def inject_javascript_array_error(code):
    """JavaScript数组错误"""
    # 将push替换为pop
    code = code.replace('.push(', '.pop(')
    return code

def inject_javascript_object_error(code):
    """JavaScript对象错误"""
    # 将点号访问替换为括号访问
    code = re.sub(r'\.(\w+)', r"['\1']", code)
    return code

def inject_javascript_comparison_error(code):
    """JavaScript比较错误"""
    # 将 < 替换为 <=
    code = code.replace(' < ', ' <= ')
    return code

def inject_javascript_function_error(code):
    """JavaScript函数错误"""
    # 移除return语句
    code = re.sub(r'\s*return [^;]+;', '', code)
    return code

def inject_javascript_bracket_error(code):
    """JavaScript括号错误"""
    # 随机添加或移除大括号
    if random.random() < 0.3:
        code = code.replace('{', '{{', 1)
    return code

def inject_javascript_undefined_error(code):
    """JavaScript未定义错误"""
    # 将undefined替换为null
    code = code.replace('undefined', 'null')
    return code

# Java特定的bug注入函数
def inject_java_bugs(code):
    """Java特定的bug注入"""
    # 将 == 替换为 = 在条件语句中（简单处理）
    code = re.sub(r'if\s*\(\s*([^=]+)\s*==\s*([^\)]+)\s*\)', r'if(\1=\2)', code)
    return code

def inject_java_semicolon_error(code):
    """Java中移除分号"""
    lines = code.split('\n')
    new_lines = []
    for line in lines:
        if line.strip() and random.random() < 0.3 and line.strip().endswith(';') and 'for(' not in line:
            line = line.rstrip(';')
        new_lines.append(line)
    return '\n'.join(new_lines)

def inject_java_bracket_error(code):
    """Java括号错误"""
    # 随机添加或移除大括号
    if random.random() < 0.3:
        code = code.replace('{', '{{', 1)
    return code

def inject_java_type_error(code):
    """Java类型错误"""
    # 将int替换为String
    code = code.replace('int ', 'String ')
    return code

def inject_java_null_pointer_error(code):
    """Java空指针错误"""
    # 在对象使用前移除初始化
    code = re.sub(r'(\w+)\s+(\w+)\s*=\s*new\s+', r'\1 \2 = ', code)
    return code

def inject_java_array_index_error(code):
    """Java数组索引错误"""
    # 在数组访问中添加错误的索引
    code = re.sub(r'(\w+)\[(\d+)\]', lambda m: f'{m.group(1)}[{int(m.group(2))+1}]' if random.random() < 0.3 else m.group(0), code)
    return code

def inject_java_loop_error(code):
    """Java循环错误"""
    # 将 < 替换为 <=
    code = code.replace('; i < ', '; i <= ')
    return code

def inject_java_exception_error(code):
    """Java异常处理错误"""
    # 移除try-catch块
    code = re.sub(r'try\s*\{([^}]+)\}\s*catch\s*\([^)]+\)\s*\{[^}]+\}', r'\1', code, flags=re.DOTALL)
    return code

def inject_java_modifier_error(code):
    """Java修饰符错误"""
    # 移除public修饰符
    code = code.replace('public ', '')
    return code

def inject_java_constructor_error(code):
    """Java构造函数错误"""
    # 修改构造函数名
    code = re.sub(r'public\s+(\w+)\s*\(', r'public \1_(', code)
    return code

def inject_java_overloading_error(code):
    """Java重载错误"""
    # 移除方法参数
    code = re.sub(r'(\w+)\s*\([^)]*\)', lambda m: f'{m.group(1)}()' if random.random() < 0.3 else m.group(0), code)
    return code

def inject_java_inheritance_error(code):
    """Java继承错误"""
    # 移除extends关键字
    code = re.sub(r'class\s+(\w+)\s+extends\s+(\w+)', r'class \1', code)
    return code