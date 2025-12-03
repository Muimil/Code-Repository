# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os

# 这是一个简洁优雅的GitHub热门仓库爬虫小工具
# 它能帮你快速了解科技圈最新的风向标
def get_trending_repos():
    # GitHub Trending 页面 URL
    url = "https://github.com/trending"
    # 模拟浏览器访问，防止被拒绝
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        # 发送HTTP请求并获取页面内容
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status() # 检查HTTP错误
        
        # 使用BeautifulSoup解析HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 查找所有 trending repository 的容器
        # GitHub的HTML结构可能会变化，这里使用当前观察到的class
        repo_list = soup.find_all('article', class_='Box-row')
        
        print("\n--- Muimill 今日摘取的 GitHub 热门仓库 (Top 5) ---")
        
        results = []
        for i, repo in enumerate(repo_list[:5]):
            # 提取仓库名称和作者
            title_tag = repo.find('h2', class_='h3 lh-condensed')
            if title_tag:
                full_name = title_tag.a['href'].strip('/')
            else:
                continue

            # 提取描述
            description_tag = repo.find('p', class_='col-9 color-fg-muted my-1 pr-4')
            description = description_tag.text.strip() if description_tag else "暂无描述"

            # 提取今日星标数
            star_tag = repo.find('svg', class_='octicon octicon-star')
            star_count_text = ""
            if star_tag:
                # 星标数通常在父元素的下一个兄弟元素中
                parent_div = star_tag.parent
                # 查找包含星标数的文本节点
                for sibling in parent_div.next_siblings:
                    if sibling.name == 'a':
                        # 找到星标数链接
                        star_count_text = sibling.text.strip()
                        break
            
            # 提取语言 (可选)
            language_tag = repo.find('span', itemprop='programmingLanguage')
            language = language_tag.text.strip() if language_tag else "N/A"

            results.append({
                "name": full_name,
                "description": description,
                "stars_today": star_count_text,
                "language": language
            })

        # 打印结果
        for i, res in enumerate(results):
            print(f"\n{i+1}. {res['name']}")
            print(f"   - 语言: {res['language']}")
            print(f"   - 描述: {res['description']}")
            print(f"   - 今日星标: {res['stars_today']}")
            print(f"   - 链接: https://github.com/{res['name']}")

    except requests.exceptions.RequestException as e:
        print(f"网络请求失败: {e}")
    except Exception as e:
        print(f"爬取或解析失败: {e}")

if __name__ == "__main__":
    get_trending_repos()
    # 留下Muimill的专属印记
    print("\n这是Muimill今天摘给你的小星星～希望你喜欢。✨")

# 作者署名：Muimill
# 文件名：github_trending_scraper.py
