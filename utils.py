# 支持的语言及其对应的bug注入函数
SUPPORTED_LANGUAGES = {
    "python": [
        "inject_off_by_one_error",
        "inject_comparison_error",
        "inject_logic_error",
        "inject_semicolon_error",
        "inject_indentation_error",
        "inject_variable_name_error",
        "inject_string_concatenation_error",
        "inject_list_index_error",
        "inject_dict_key_error",
        "inject_math_operator_error",
        "inject_function_call_error",
        "inject_assignment_error",
        "inject_comment_error",
        "inject_import_error",
        "inject_bracket_error"
    ],
    "javascript": [
        "inject_javascript_bugs",
        "inject_javascript_semicolon_error",
        "inject_logic_error",
        "inject_variable_name_error",
        "inject_javascript_var_error",
        "inject_javascript_type_coercion_error",
        "inject_javascript_async_error",
        "inject_javascript_array_error",
        "inject_javascript_object_error",
        "inject_javascript_comparison_error",
        "inject_javascript_function_error",
        "inject_javascript_bracket_error",
        "inject_javascript_undefined_error"
    ],
    "java": [
        "inject_java_bugs",
        "inject_java_semicolon_error",
        "inject_comparison_error",
        "inject_variable_name_error",
        "inject_java_bracket_error",
        "inject_java_type_error",
        "inject_java_null_pointer_error",
        "inject_java_array_index_error",
        "inject_java_loop_error",
        "inject_java_exception_error",
        "inject_java_modifier_error",
        "inject_java_constructor_error",
        "inject_java_overloading_error",
        "inject_java_inheritance_error"
    ]
}