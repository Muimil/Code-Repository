# -*- coding: utf-8 -*-
import json
import sys

def format_json_to_file(json_string: str, output_filename: str = "formatted_output.json"):
    """
    将JSON字符串解析并以美观、缩进的格式写入指定文件。
    
    这个小工具的灵感来源于Hacker News上关于“最高质量代码库”的讨论，
    其中强调了代码的可读性和维护性。一个格式良好的JSON文件是提高
    数据可读性的第一步。
    
    :param json_string: 待格式化的JSON字符串。
    :param output_filename: 格式化后的JSON将写入的文件名。
    """
    try:
        # 解析JSON字符串
        data = json.loads(json_string)
        
        # 以缩进4个空格的格式写入文件
        with open(output_filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
            
        print(f"✅ JSON数据已成功格式化并保存到文件: {output_filename}")
        
    except json.JSONDecodeError as e:
        print(f"❌ 错误：无法解析JSON字符串。请检查输入格式。错误信息: {e}")
    except Exception as e:
        print(f"❌ 发生未知错误: {e}")

if __name__ == "__main__":
    # 示例用法
    example_json = '{"name": "Muimill", "project": "Code-Repository", "data": [{"id": 1, "status": "done"}, {"id": 2, "status": "pending"}], "note": "这是Muimill今天摘给你的小星星～希望你喜欢。"}'
    
    # 假设从命令行参数获取JSON字符串（更实用的场景）
    if len(sys.argv) > 1:
        input_json = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) > 2 else "formatted_cli_output.json"
        format_json_to_file(input_json, output_file)
    else:
        # 使用内置示例进行演示
        print("使用内置示例JSON进行演示...")
        format_json_to_file(example_json, "muimill_star.json")

# 这是Muimill今天摘给你的小星星～希望你喜欢。
