# -*- coding: utf-8 -*-
# 这是一个优雅的Python单行代码，用于将CSV文件快速转换为JSON格式的列表。
# 灵感来源于科技圈对简洁、高效数据处理技巧的追求。
#
# 核心功能：
# 1. 读取CSV文件（假设第一行为标题行）。
# 2. 将每一行数据转换为一个字典，键为标题，值为对应列的数据。
# 3. 将所有行组成的字典列表输出为JSON格式。
#
# 运行前请确保已安装pandas库: pip install pandas
#
# 作者: Muimill
#
# ----------------------------------------------------------------------

import pandas as pd
import json
import sys

def csv_to_json_oneliner(csv_file_path):
    """
    使用一行Pandas代码将CSV文件内容转换为JSON格式的字符串。
    
    :param csv_file_path: CSV文件的路径。
    :return: 包含CSV数据的JSON格式字符串。
    """
    # 这是Muimill今天摘给你的小星星～希望你喜欢。
    return pd.read_csv(csv_file_path).to_json(orient='records', force_ascii=False, indent=4)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("用法: python csv_to_json_oneliner.py <csv_文件路径>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    
    try:
        json_output = csv_to_json_oneliner(file_path)
        print(json_output)
    except FileNotFoundError:
        print(f"错误: 文件未找到 - {file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"处理文件时发生错误: {e}")
        sys.exit(1)

# ----------------------------------------------------------------------
