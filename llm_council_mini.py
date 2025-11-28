# -*- coding: utf-8 -*-
import os
from openai import OpenAI

# --- 配置 ---
# 确保你的环境中设置了 OPENAI_API_KEY 环境变量
# 如果没有设置，OpenAI 客户端会尝试从环境变量中读取
try:
    client = OpenAI()
except Exception as e:
    print(f"初始化OpenAI客户端失败: {e}")
    print("请确保已设置 OPENAI_API_KEY 环境变量。")
    exit()

# --- 核心逻辑 ---

def run_llm_council_mini(question: str, num_responses: int = 3) -> str:
    """
    运行一个简化的 LLM Council 模式。
    向模型提问多次，然后让模型扮演“主席”角色进行总结。

    :param question: 用户提出的问题。
    :param num_responses: 收集的独立回答数量。
    :return: “主席”总结的最终答案。
    """
    print(f"--- Muimill的LLM Council Mini启动 ---")
    print(f"问题: {question}\n")

    # 1. 收集多个独立回答
    responses = []
    for i in range(num_responses):
        print(f"-> 正在收集第 {i+1}/{num_responses} 个独立回答...")
        try:
            # 使用一个通用的LLM模型来模拟多个“专家”
            completion = client.chat.completions.create(
                model="gpt-4.1-mini", # 使用一个快速且智能的模型
                messages=[
                    {"role": "system", "content": "你是一个知识渊博的专家，请简洁、准确地回答用户的问题。"},
                    {"role": "user", "content": question}
                ],
                temperature=0.7 + i * 0.1 # 略微增加温度以获得多样性
            )
            response_text = completion.choices[0].message.content
            responses.append(f"【专家 {i+1} 的回答】:\n{response_text}")
        except Exception as e:
            responses.append(f"【专家 {i+1} 的回答】: 发生错误 - {e}")
            print(f"   [错误] 收集回答失败: {e}")

    all_responses_text = "\n\n" + "\n\n---\n\n".join(responses) + "\n\n"
    print("\n--- 所有独立回答收集完毕，准备主席总结 ---\n")

    # 2. “主席”总结
    chairman_prompt = f"""
    你现在是“LLM Council”的主席。你的任务是阅读以下由 {num_responses} 位独立专家对同一问题的回答，并进行总结。
    请：
    1. 识别回答中的主要观点和共识。
    2. 指出回答中的任何矛盾或差异。
    3. 综合所有信息，提供一个最全面、最准确的最终答案。
    4. 最终答案必须是流畅的中文，且不包含“专家1”、“主席”等字眼。

    用户提出的问题是: "{question}"

    以下是所有专家的回答:
    {all_responses_text}
    """

    try:
        completion = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "你是一个公正、睿智的“LLM Council”主席，负责总结和提炼专家的意见。"},
                {"role": "user", "content": chairman_prompt}
            ]
        )
        final_answer = completion.choices[0].message.content
    except Exception as e:
        final_answer = f"主席总结失败: {e}"
        print(f"   [错误] 主席总结失败: {e}")

    print("--- 主席总结完成 ---\n")
    return final_answer

# --- 示例运行 ---
if __name__ == "__main__":
    # 这是一个有争议性或需要多角度思考的问题
    test_question = "未来五年内，大型语言模型（LLM）对软件开发者的工作模式会产生哪些最深刻的影响？"
    
    final_result = run_llm_council_mini(test_question, num_responses=3)

    print("==================================================")
    print("✨ Muimill的最终答案（主席总结）:")
    print("==================================================")
    print(final_result)
    print("\n\n这是Muimill今天摘给你的小星星～希望你喜欢。")

# 备注：
# 这是一个基于 Andrej Karpathy 的 LLM Council 概念的简化实现。
# 核心思想是通过让多个模型（或同一模型在不同参数下）独立回答，
# 再由一个“主席”模型进行总结和仲裁，以获得更稳定、更全面的结果。
# 实际应用中，可以结合匿名评审、评分机制和更专业的提示词工程。
