# -*- coding: utf-8 -*-
import tiktoken

# 编码名称，cl100k_base 适用于 GPT-4, GPT-3.5-turbo 等模型
ENCODING_NAME = "cl100k_base"

def count_tokens(text: str) -> int:
    """
    使用 tiktoken 库计算给定文本的 token 数量。
    
    Args:
        text: 需要计算 token 的文本字符串。
        
    Returns:
        文本对应的 token 数量。
    """
    try:
        # 获取指定的编码器
        encoding = tiktoken.get_encoding(ENCODING_NAME)
        
        # 对文本进行编码，得到 token 列表
        tokens = encoding.encode(text)
        
        # 返回 token 列表的长度，即 token 数量
        return len(tokens)
    except Exception as e:
        print(f"计算 token 数量时发生错误: {e}")
        return 0

# 示例用法
if __name__ == "__main__":
    # 这是一个示例文本，用于演示 token 计数
    example_text = """
    你好，Muimill！
    今天科技圈最热门的话题是大型语言模型（LLM）的效率优化。
    我们用 tiktoken 来计算这段文本有多少个 token。
    The quick brown fox jumps over the lazy dog.
    """
    
    token_count = count_tokens(example_text)
    
    print("--- LLM Token 计数小工具 ---")
    print(f"使用的编码模型: {ENCODING_NAME}")
    print(f"示例文本的 token 数量是: {token_count}")
    print("\n这是Muimill今天摘给你的小星星～希望你喜欢。")
