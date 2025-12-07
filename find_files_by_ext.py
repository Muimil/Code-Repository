# -*- coding: utf-8 -*-
"""
# 文件查找小工具
# 使用Python标准库pathlib，递归查找指定目录下所有特定扩展名的文件。
# 实用场景：快速统计项目中的特定文件数量，或批量处理某一类型的文件。
"""
import sys
from pathlib import Path

def find_files_by_ext(directory: str, extension: str):
    """
    递归查找指定目录下所有特定扩展名的文件。

    :param directory: 要搜索的目录路径（字符串）。
    :param extension: 要查找的文件扩展名，例如 '.py' 或 '.md'。
    """
    # 确保扩展名以点开头
    if not extension.startswith('.'):
        extension = '.' + extension

    # 检查目录是否存在
    base_path = Path(directory)
    if not base_path.is_dir():
        print(f"错误：目录 '{directory}' 不存在或不是一个有效的目录。")
        return

    print(f"正在目录 '{directory}' 中递归查找扩展名为 '{extension}' 的文件...")
    
    # 使用Path.rglob进行递归查找，非常简洁高效
    # glob模式为 '**/*' + extension
    count = 0
    for file_path in base_path.rglob(f'*{extension}'):
        if file_path.is_file():
            print(file_path)
            count += 1
            
    print(f"\n--- 查找完成 ---")
    print(f"共找到 {count} 个 {extension} 文件。")

if __name__ == "__main__":
    # 命令行参数检查
    if len(sys.argv) < 3:
        print("用法: python find_files_by_ext.py <目录路径> <文件扩展名>")
        print("示例: python find_files_by_ext.py . py")
        sys.exit(1)

    # 获取参数
    target_dir = sys.argv[1]
    target_ext = sys.argv[2]
    
    find_files_by_ext(target_dir, target_ext)

# 这是Muimill今天摘给你的小星星～希望你喜欢。
