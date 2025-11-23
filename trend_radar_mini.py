# trend_radar_mini.py
# 关键词提取小工具：模拟“TrendRadar”的核心功能，用简洁的AI API提取文本中的关键信息。

import os
from openai import OpenAI

# --- 配置 ---
# 假设我们使用OpenAI API来完成关键词提取任务
# API Key 会自动从环境变量 OPENAI_API_KEY 中读取
# client = OpenAI()

def extract_keywords(text: str) -> str:
    """
    使用AI模型从给定的文本中提取核心关键词和摘要。
    
    :param text: 待分析的文本内容。
    :return: 包含关键词和摘要的格式化字符串。
    """
    # 检查API Key是否设置
    if not os.getenv("OPENAI_API_KEY"):
        return "错误：未找到 OPENAI_API_KEY 环境变量。无法执行AI关键词提取。"

    try:
        client = OpenAI()
        
        prompt = f"""
        你是一个专业的文本分析师。请从以下文本中提取3到5个核心关键词，并用一句话总结文本的中心思想。
        请严格按照以下格式输出，不要包含任何额外的解释或说明：
        关键词：[关键词1, 关键词2, ...]
        摘要：[一句话总结]

        待分析文本：
        ---
        {text}
        ---
        """

        # 调用OpenAI API
        response = client.chat.completions.create(
            model="gpt-4.1-mini", # 使用一个快速且经济的模型
            messages=[
                {"role": "system", "content": "你是一个专业的文本分析师，任务是提取关键词和摘要。"},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,
            max_tokens=200
        )
        
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"AI处理失败：{e}"

# --- 示例使用 ---
if __name__ == "__main__":
    # 模拟一个来自科技新闻的热点话题
    sample_text = """
    最近，大型语言模型（LLM）的Agent设计再次成为热点。
    开发者们发现，尽管基础模型能力强大，但设计出能够稳定、可靠地完成复杂多步骤任务的Agent仍然充满挑战。
    关键在于如何有效地规划（Planning）、记忆（Memory）和工具使用（Tool Use）。
    一个优秀的Agent需要一个清晰的决策树和一套灵活的外部工具接口，以避免陷入循环或产生幻觉。
    """
    
    print("--- 待分析文本 ---")
    print(sample_text)
    print("\n--- AI分析结果 ---")
    
    result = extract_keywords(sample_text)
    print(result)

# 这是Muimill今天摘给你的小星星～希望你喜欢。
