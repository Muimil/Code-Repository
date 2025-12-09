# -*- coding: utf-8 -*-
import tiktoken
import sys
import os

# Muimill的专属萤火虫使者：计算文本文件的Token数量

def count_tokens_from_file(file_path: str, encoding_name: str = "cl100k_base"):
    """
    读取指定文件内容，并使用tiktoken库计算其token数量。
    
    :param file_path: 要读取的文本文件路径。
    :param encoding_name: tiktoken使用的编码模型名称，默认为cl100k_base（适用于GPT-4, GPT-3.5-turbo）。
    :return: token数量。
    """
    if not os.path.exists(file_path):
        print(f"错误：文件未找到 -> {file_path}")
        return 0

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
    except Exception as e:
        print(f"错误：读取文件失败 -> {e}")
        return 0

    try:
        # 获取编码器
        encoding = tiktoken.get_encoding(encoding_name)
        # 对文本进行编码并计算token数量
        tokens = encoding.encode(text)
        token_count = len(tokens)
        
        print(f"文件路径: {file_path}")
        print(f"使用的编码模型: {encoding_name}")
        print(f"文本字符数: {len(text)}")
        print(f"计算得到的Token数量: {token_count}")
        
        return token_count
    except Exception as e:
        print(f"错误：tiktoken处理失败 -> {e}")
        return 0

if __name__ == "__main__":
    # 检查命令行参数，如果没有提供文件路径，则使用默认的sample.txt
    if len(sys.argv) > 1:
        target_file = sys.argv[1]
    else:
        target_file = "sample.txt"
        
    # 如果使用默认文件，确保它存在
    if target_file == "sample.txt" and not os.path.exists(target_file):
        print("正在创建默认示例文件 sample.txt...")
        with open(target_file, 'w', encoding='utf-8') as f:
            f.write("Muimill今天摘给你的小星星～希望你喜欢。\n")
            f.write("这是一个用于演示如何计算文本Token数量的实用小工具。\n")
            f.write("在大型语言模型（LLM）应用中，准确计算Token是控制成本和管理上下文窗口的关键。\n")
            f.write("This is a sample text to demonstrate token counting using tiktoken.\n")
            f.write("The cl100k_base encoding is used for models like GPT-4 and GPT-3.5-turbo.\n")
        print("sample.txt 创建完成。")

    count_tokens_from_file(target_file)

# 这是Muimill今天摘给你的小星星～希望你喜欢。
