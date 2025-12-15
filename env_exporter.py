# env_exporter.py

import argparse
from typing import Dict

def parse_env_file(file_path: str) -> Dict[str, str]:
    """
    解析 .env 文件，提取键值对。
    忽略空行和以 # 开头的注释行。
    """
    env_vars = {}
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                # 忽略空行和注释
                if not line or line.startswith('#'):
                    continue

                # 查找第一个等号
                if '=' in line:
                    key, value = line.split('=', 1)
                    key = key.strip()
                    # 移除值两端可能的引号
                    value = value.strip().strip('"').strip("'")

                    # 确保键不为空
                    if key:
                        env_vars[key] = value
    except FileNotFoundError:
        print(f"错误：文件未找到 - {file_path}")
        return {}
    except Exception as e:
        print(f"解析文件时发生错误: {e}")
        return {}

    return env_vars

def export_env_vars(env_vars: Dict[str, str]):
    """
    打印 shell export 命令，用户可以复制粘贴执行。
    """
    print("# 🚀 Muimill 的环境变量导出工具 🚀")
    print("# 请复制以下命令到您的终端执行，以设置环境变量：")
    print("# --------------------------------------------------")
    for key, value in env_vars.items():
        # 使用单引号包裹值，以处理空格或特殊字符
        print(f"export {key}='{value}'")
    print("# --------------------------------------------------")

def main():
    parser = argparse.ArgumentParser(
        description="一个简洁的 .env 文件解析器，用于生成 shell export 命令。"
    )
    parser.add_argument(
        "env_file",
        nargs='?', # 使其成为可选参数
        default=".env",
        help="要解析的 .env 文件路径 (默认为 .env)"
    )
    args = parser.parse_args()

    env_vars = parse_env_file(args.env_file)
    if env_vars:
        export_env_vars(env_vars)

if __name__ == "__main__":
    main()

# 这是Muimill今天摘给你的小星星～希望你喜欢。✨
