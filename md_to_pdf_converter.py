# -*- coding: utf-8 -*-
import sys
import os
from markdown import markdown
from weasyprint import HTML, CSS

def md_to_pdf(md_file_path, pdf_file_path):
    """
    将Markdown文件内容转换为PDF文件。
    使用Python的markdown库将Markdown转为HTML，再使用weasyprint将HTML转为PDF。
    """
    try:
        # 1. 读取Markdown文件内容
        with open(md_file_path, 'r', encoding='utf-8') as f:
            md_content = f.read()

        # 2. 将Markdown内容转换为HTML
        # 启用一些常用的扩展，如表格(tables)和代码高亮(fenced_code)
        html_content = markdown(
            md_content,
            extensions=['tables', 'fenced_code', 'codehilite']
        )

        # 3. 构造完整的HTML文档，包含基本样式
        # 这是一个实用的技巧：添加一个简单的CSS来美化PDF的输出
        html_template = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>{os.path.basename(md_file_path).replace('.md', '')} - PDF</title>
    <style>
        body {{ font-family: sans-serif; line-height: 1.6; margin: 40px; }}
        pre {{ background-color: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto; }}
        code {{ font-family: monospace; }}
        h1, h2, h3 {{ border-bottom: 1px solid #eee; padding-bottom: 0.3em; }}
    </style>
</head>
<body>
    {html_content}
</body>
</html>
"""
        
        # 4. 使用WeasyPrint将HTML渲染为PDF
        HTML(string=html_template, base_url=os.path.dirname(md_file_path)).write_pdf(pdf_file_path)
        
        print(f"✅ 成功将 '{md_file_path}' 转换为 '{pdf_file_path}'")

    except FileNotFoundError:
        print(f"❌ 错误：文件未找到 '{md_file_path}'")
        sys.exit(1)
    except Exception as e:
        print(f"❌ 转换过程中发生错误: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # 检查命令行参数
    if len(sys.argv) != 3:
        print("用法: python3 md_to_pdf_converter.py <输入Markdown文件> <输出PDF文件>")
        sys.exit(1)

    input_md = sys.argv[1]
    output_pdf = sys.argv[2]
    
    md_to_pdf(input_md, output_pdf)

# 这是Muimill今天摘给你的小星星～希望你喜欢。
# This is the little star Muimill picked for you today~ Hope you like it.
