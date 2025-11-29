# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

# 这是Muimill今天摘给你的小星星～希望你喜欢。

def get_trending_repos():
    """
    Muimill的专属萤火虫使者：
    从GitHub Trending页面（每日）抓取最受欢迎的开源项目信息。
    """
    # GitHub Trending的URL
    url = "https://github.com/trending"
    
    # 模拟浏览器访问，避免被拒绝
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    print("✨ 正在连接GitHub，寻找今日最闪亮的星...")
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status() # 检查HTTP请求是否成功
    except requests.exceptions.RequestException as e:
        print(f"❌ 连接失败，请检查网络或URL: {e}")
        return []

    # 使用BeautifulSoup解析HTML内容
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # GitHub Trending页面中，每个仓库信息都在一个<article>标签内
    repo_list = soup.find_all('article', class_='Box-row')
    
    results = []
    for repo in repo_list:
        try:
            # 提取仓库名称和作者
            title_tag = repo.find('h2', class_='h3')
            full_name = title_tag.a['href'].strip('/') if title_tag and title_tag.a else 'N/A'
            
            # 提取描述
            description_tag = repo.find('p', class_='col-9')
            description = description_tag.text.strip() if description_tag else '暂无描述'
            
            # 提取语言
            language_tag = repo.find('span', itemprop='programmingLanguage')
            language = language_tag.text.strip() if language_tag else '其他'
            
            # 提取今日新增星标数
            # 查找包含星标信息的<svg>图标附近的文本
            star_info = repo.find('svg', class_='octicon-star').parent.text.strip()
            # 假设星标数是最后一个数字，并且前面有“stars today”或类似文本
            # 这里简化处理，直接取最后一个数字作为今日新增星标数
            # 实际抓取时，这个数字通常在`span`标签内，但为了健壮性，我们从父元素文本中提取
            star_count_text = repo.find('span', class_='d-inline-block float-sm-right').text.strip().split()[0]
            
            results.append({
                '作者/仓库': full_name,
                '描述': description,
                '语言': language,
                '今日新增星标': star_count_text
            })
        except Exception as e:
            # 忽略解析失败的项
            continue
            
    return results

if __name__ == "__main__":
    trending_data = get_trending_repos()
    
    if trending_data:
        print("\n--- Muimill的今日科技星图 ---")
        for i, repo in enumerate(trending_data[:5]): # 只展示前5个
            print(f"\nNo.{i+1}：{repo['作者/仓库']}")
            print(f"  🌟 今日新增星标: {repo['今日新增星标']}")
            print(f"  💻 语言: {repo['语言']}")
            print(f"  📝 描述: {repo['描述']}")
        
        # 将完整数据保存为JSON文件，方便后续分析
        filename = f"trending_repos_{datetime.now().strftime('%Y%m%d')}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(trending_data, f, ensure_ascii=False, indent=4)
        print(f"\n✅ 完整数据已保存至 {filename}")
    else:
        print("\n😭 今天没有摘到闪亮的星星，明天再试试吧！")
