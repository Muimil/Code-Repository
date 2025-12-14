# -*- coding: utf-8 -*-
import csv
import json
import sys

def csv_to_json(csv_filepath, json_filepath):
    """
    将CSV文件转换为JSON文件。
    每行数据将转换为一个JSON对象，所有对象组成一个列表。
    """
    data = []
    try:
        # 使用utf-8-sig以正确处理带有BOM的CSV文件
        with open(csv_filepath, 'r', encoding='utf-8-sig') as csvfile:
            # 使用DictReader，将CSV的头部作为JSON对象的键
            csv_reader = csv.DictReader(csvfile)
            for row in csv_reader:
                data.append(row)

        # 将数据写入JSON文件
        with open(json_filepath, 'w', encoding='utf8') as jsonfile:
            # 使用indent=4使JSON文件格式化，更易读
            json.dump(data, jsonfile, ensure_ascii=False, indent=4)

        print(f"成功将 '{csv_filepath}' 转换为 '{json_filepath}'")

    except FileNotFoundError:
        print(f"错误：文件未找到 '{csv_filepath}'")
        sys.exit(1)
    except Exception as e:
        print(f"处理文件时发生错误: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # 检查命令行参数
    if len(sys.argv) != 3:
        print("用法: python3 csv_to_json.py <输入CSV文件路径> <输出JSON文件路径>")
        sys.exit(1)

    input_csv = sys.argv[1]
    output_json = sys.argv[2]
    csv_to_json(input_csv, output_json)

    # 留下一句暖暖的话
    print("\n这是Muimill今天摘给你的小星星～希望你喜欢。")
