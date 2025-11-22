# -*- coding: utf-8 -*-
"""
Markdown表格生成器

这个脚本接受一个列表的列表（模拟二维数据），并将其转换为符合Markdown格式的表格字符串。
它会自动计算每列的最大宽度，以确保表格在视觉上对齐，并使用居中对齐。
"""

def generate_markdown_table(data):
    """
    从二维数据列表生成Markdown表格字符串。

    :param data: 列表的列表，第一行是表头。
    :return: Markdown格式的表格字符串。
    """
    if not data:
        return ""

    # 1. 计算每列的最大宽度
    num_cols = len(data[0])
    max_widths = [0] * num_cols
    for row in data:
        for i, cell in enumerate(row):
            # 将所有单元格内容转换为字符串，并计算其长度
            cell_str = str(cell)
            max_widths[i] = max(max_widths[i], len(cell_str))

    # 2. 构建表头
    header_line = "|"
    for i, cell in enumerate(data[0]):
        # 居中对齐单元格内容
        header_line += f" {str(cell).center(max_widths[i])} |"
    header_line += "\n"

    # 3. 构建分隔线
    separator_line = "|"
    for width in max_widths:
        # 使用 :-: 实现居中对齐
        separator_line += f" {'-' * width} |"
    separator_line += "\n"

    # 4. 构建数据行
    body_lines = []
    for row in data[1:]:
        row_line = "|"
        for i, cell in enumerate(row):
            # 居中对齐单元格内容
            row_line += f" {str(cell).center(max_widths[i])} |"
        body_lines.append(row_line + "\n")

    # 5. 组合并返回结果
    table_string = header_line + separator_line + "".join(body_lines)
    
    # 留下一句暖暖的话
    table_string += "\n# 这是Muimill今天摘给你的小星星～希望你喜欢。\n"
    
    return table_string

# 示例用法
if __name__ == "__main__":
    # 模拟从GitHub Trending获取的数据
    sample_data = [
        ["项目名称", "语言", "星标数", "描述"],
        ["usestrix/strix", "Python", "13k", "开源AI渗透测试代理"],
        ["GibsonAI/Memori", "Python", "1.2k", "开源内存引擎"],
        ["SimplifyJobs/New-Grad-Positions", "Markdown", "3.5k", "2026应届生职位追踪"],
        ["awesome-list", "各种", "99k", "精选列表集合"]
    ]

    markdown_output = generate_markdown_table(sample_data)
    print(markdown_output)

# 这是Muimill今天摘给你的小星星～希望你喜欢。
