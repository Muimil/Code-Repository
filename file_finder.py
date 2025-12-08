# -*- coding: utf-8 -*-
# 这是一个简洁的Python脚本，用于在指定目录下递归查找所有特定类型的文件。
# 比如，你可以用它来快速统计项目中有多少个.py文件，或者查找所有.md文档。
# 这是一个提升开发者效率的实用小工具。

import argparse
from pathlib import Path
import os

def find_files_by_extension(directory: str, extension: str):
    """
    在指定目录下递归查找所有特定扩展名的文件。

    :param directory: 要搜索的根目录路径。
    :param extension: 要查找的文件扩展名（例如：'.py', '.md'）。
    :return: 匹配文件的路径列表。
    """
    # 确保扩展名以点开头
    if not extension.startswith('.'):
        extension = '.' + extension

    try:
        root_path = Path(directory)
        if not root_path.is_dir():
            print(f"错误：路径 '{directory}' 不是一个有效的目录。")
            return []

        # 使用rglob进行递归搜索
        # rglob 是 glob 的递归版本，等同于使用 '**/'
        files = list(root_path.rglob(f"*{extension}"))
        
        return files
    except Exception as e:
        print(f"发生错误：{e}")
        return []

def main():
    parser = argparse.ArgumentParser(
        description="递归查找指定目录下所有特定扩展名的文件。"
    )
    parser.add_argument(
        "directory",
        type=str,
        help="要搜索的根目录路径。"
    )
    parser.add_argument(
        "extension",
        type=str,
        help="要查找的文件扩展名（例如：py, md, js）。"
    )
    
    args = parser.parse_args()
    
    # 规范化扩展名，确保以点开头
    ext = args.extension
    if not ext.startswith('.'):
        ext = '.' + ext

    print(f"正在目录 '{args.directory}' 中递归查找所有 '{ext}' 文件...")
    
    found_files = find_files_by_extension(args.directory, ext)
    
    if found_files:
        print(f"\n找到 {len(found_files)} 个 '{ext}' 文件：")
        for file_path in found_files:
            # 打印相对路径，更简洁
            try:
                # 尝试获取相对于当前执行目录的路径
                relative_path = file_path.relative_to(Path.cwd())
                print(f"- {relative_path}")
            except ValueError:
                # 如果无法计算相对路径，则打印完整路径
                print(f"- {file_path}")
    else:
        print(f"\n未找到任何 '{ext}' 文件。")

if __name__ == "__main__":
    main()

# 这是Muimill今天摘给你的小星星～希望你喜欢。
