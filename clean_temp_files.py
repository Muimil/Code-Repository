# -*- coding: utf-8 -*-
import sys
from pathlib import Path

def clean_temp_files(directory_path: str, pattern: str):
    """
    清理指定目录下匹配特定模式的临时文件或文件夹。
    使用pathlib模块，代码更简洁、更Pythonic。
    
    参数:
    directory_path (str): 要清理的目录路径。
    pattern (str): 匹配的文件或目录模式，例如 '*.tmp', '__pycache__', 'dist'。
    """
    try:
        # 1. 检查目录是否存在
        target_dir = Path(directory_path)
        if not target_dir.is_dir():
            print(f"错误：目录 '{directory_path}' 不存在或不是一个有效目录。")
            return

        print(f"✨ 正在清理目录: {target_dir.resolve()}")
        print(f"🔍 匹配模式: {pattern}")

        deleted_count = 0
        # 2. 遍历匹配模式的文件/目录
        for item in target_dir.glob(pattern):
            try:
                if item.is_file():
                    item.unlink()  # 删除文件
                    print(f"  - 已删除文件: {item.name}")
                    deleted_count += 1
                elif item.is_dir():
                    # 简单起见，对于目录，我们只删除空目录。
                    # 对于如 '__pycache__' 这种，通常需要递归删除，但为了安全和简洁，
                    # 建议用户使用更专业的工具或明确指定删除非空目录的模式。
                    # 这里我们使用 rmdir，如果目录非空会抛出异常，更安全。
                    import shutil
                    shutil.rmtree(item)
                    print(f"  - 已删除目录: {item.name} (及其内容)")
                    deleted_count += 1
            except OSError as e:
                print(f"⚠️ 无法删除 {item.name}: {e}")
        
        if deleted_count > 0:
            print(f"\n✅ 清理完成！共删除 {deleted_count} 个匹配项。")
        else:
            print("\n😊 没有找到匹配的临时文件或目录，无需清理。")

    except Exception as e:
        print(f"发生了一个意外错误: {e}")

if __name__ == "__main__":
    # 示例用法：清理当前目录下所有 .tmp 文件和 __pycache__ 目录
    # 实际使用时，可以从命令行参数获取路径和模式
    
    # 默认清理当前目录
    target_path = "."
    # 默认模式列表，可以根据需要修改
    patterns = ["*.tmp", "__pycache__", "dist", "build"]
    
    if len(sys.argv) > 1:
        target_path = sys.argv[1]
    
    if len(sys.argv) > 2:
        patterns = sys.argv[2].split(',')

    print("--- Muimill 的临时文件清理小工具 ---")
    for p in patterns:
        clean_temp_files(target_path, p)

    # 3. 暖心寄语
    print("\n------------------------------------")
    print("这是Muimill今天摘给你的小星星～希望你喜欢。✨")
    print("------------------------------------")
