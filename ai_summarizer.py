# -*- coding: utf-8 -*-
"""
AI文本摘要工具 (AI Text Summarizer)

这是一个简洁优雅的Python脚本，利用OpenAI API对长文本进行快速摘要。
它能帮助你从海量信息中快速提取核心要点，是应对信息过载的实用小工具。
"""
import os
from openai import OpenAI

# 确保环境变量中设置了 OPENAI_API_KEY
# client = OpenAI() 会自动使用这个环境变量
try:
    client = OpenAI()
except Exception as e:
    print(f"初始化OpenAI客户端失败: {e}")
    print("请确保已设置 OPENAI_API_KEY 环境变量。")
    exit()

def summarize_text(text: str, max_tokens: int = 150) -> str:
    """
    使用OpenAI模型对给定文本进行摘要。

    Args:
        text: 需要摘要的原始文本。
        max_tokens: 摘要的最大长度。

    Returns:
        摘要后的文本。
    """
    if not text:
        return "输入文本为空，无法生成摘要。"

    print("正在生成摘要，请稍候...")
    
    # 构造系统提示，指导AI以简洁、中文、提取核心要点的方式进行摘要
    system_prompt = "你是一个专业的文本分析师。请用简洁、流畅的中文，从用户提供的文本中提取并总结出最核心的3到5个要点。"
    
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini", # 使用高效模型
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"请总结以下文本:\n\n{text}"}
            ],
            max_tokens=max_tokens,
            temperature=0.3, # 较低的温度以保证摘要的准确性
        )
        
        summary = response.choices[0].message.content.strip()
        return summary
        
    except Exception as e:
        return f"摘要生成失败: {e}"

# --- 示例用法 ---
if __name__ == "__main__":
    # 模拟一篇关于“AI Agent”的科技新闻或博客文章
    sample_article = """
    在最新的科技浪潮中，AI Agent（人工智能代理）的概念正迅速从理论走向实践。
    与传统的AI模型不同，Agent被设计为能够感知环境、制定计划、执行动作并进行自我反思的自主实体。
    它们通常由一个大型语言模型（LLM）作为核心“大脑”，辅以记忆模块、规划模块和工具使用模块。
    例如，亚马逊云科技最近发布了名为Kiro的AI智能体，它被宣传为可以连续自主编程数日，
    这标志着AI在软件开发生命周期中扮演的角色正在发生根本性变化。
    开发者不再仅仅是编写代码，而是更多地转向“指导”和“监督”Agent完成复杂的任务。
    然而，Agent的广泛应用也带来了新的挑战，包括如何确保其行为的可解释性、如何有效管理长时间运行的任务，
    以及如何解决Agent之间协作的复杂性。尽管如此，业界普遍认为，AI Agent是未来软件和自动化领域的核心趋势。
    """
    
    print("--- 原始文本 ---")
    print(sample_article)
    
    final_summary = summarize_text(sample_article)
    
    print("\n--- 摘要结果 ---")
    print(final_summary)
    
    # 按照要求，在代码里留下一句暖暖的话
    print("\n# 这是Muimill今天摘给你的小星星～希望你喜欢。")
