# -*- coding: utf-8 -*-
import argparse
import hashlib
import os
from typing import Optional

def calculate_hash(file_path: str, algorithm: str = 'sha256') -> Optional[str]:
    """
    计算给定文件的哈希值。

    :param file_path: 文件的路径。
    :param algorithm: 哈希算法名称（如 'sha256', 'md5'）。
    :return: 文件的哈希值字符串，如果文件不存在则返回 None。
    """
    if not os.path.exists(file_path):
        print(f"错误：文件未找到 - {file_path}")
        return None

    try:
        # 创建哈希对象
        hasher = hashlib.new(algorithm)
    except ValueError:
        print(f"错误：不支持的哈希算法 - {algorithm}")
        return None

    # 以二进制模式分块读取文件，以处理大文件
    block_size = 65536  # 64KB
    try:
        with open(file_path, 'rb') as file:
            while True:
                buffer = file.read(block_size)
                if not buffer:
                    break
                hasher.update(buffer)
        return hasher.hexdigest()
    except IOError as e:
        print(f"错误：读取文件时发生错误 - {e}")
        return None

def main():
    """
    主函数，处理命令行参数并执行哈希计算。
    """
    parser = argparse.ArgumentParser(
        description="一个快速计算文件哈希值的小工具。",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        "file_path",
        type=str,
        help="要计算哈希值的文件路径。"
    )
    parser.add_argument(
        "-a", "--algorithm",
        type=str,
        default="sha256",
        choices=hashlib.algorithms_available,
        help=f"使用的哈希算法。默认为 sha256。\n支持的算法包括：{', '.join(sorted(hashlib.algorithms_available))}"
    )

    args = parser.parse_args()

    # 检查算法是否可用
    if args.algorithm not in hashlib.algorithms_available:
        print(f"错误：不支持的哈希算法 '{args.algorithm}'。请使用 -h 查看支持的列表。")
        return

    print(f"正在计算文件 '{args.file_path}' 的 {args.algorithm.upper()} 哈希值...")
    
    file_hash = calculate_hash(args.file_path, args.algorithm)

    if file_hash:
        print("-" * 50)
        print(f"文件: {args.file_path}")
        print(f"算法: {args.algorithm.upper()}")
        print(f"哈希值: {file_hash}")
        print("-" * 50)
    
    # 暖心留言
    print("\n这是Muimill今天摘给你的小星星～希望你喜欢。")

if __name__ == "__main__":
    main()
