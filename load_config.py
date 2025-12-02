# load_config.py: 使用PyYAML加载配置文件

import yaml
import os

def load_yaml_config(file_path):
    """
    加载并解析指定的YAML配置文件。
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
        return config
    except FileNotFoundError:
        print(f"错误：配置文件未找到在 {file_path}")
        return None
    except yaml.YAMLError as exc:
        print(f"错误：解析YAML文件时出错: {exc}")
        return None

if __name__ == "__main__":
    # 假设配置文件在当前目录下
    config_file = "config.yaml"
    
    # 检查config.yaml是否存在
    if not os.path.exists(config_file):
        print(f"请确保 {config_file} 文件存在于当前目录。")
    else:
        print(f"正在加载配置文件: {config_file}...")
        config_data = load_yaml_config(config_file)

        if config_data:
            print("\n--- 配置加载成功 ---")
            
            # 打印一些关键配置项以验证
            print(f"数据库主机: {config_data.get('database', {}).get('host')}")
            print(f"日志级别: {config_data.get('logging', {}).get('level')}")
            print(f"是否启用Beta特性: {config_data.get('features', {}).get('enable_beta')}")
            
            # 打印服务器列表中的第一个服务器名称
            servers = config_data.get('servers', [])
            if servers:
                print(f"第一个服务器名称: {servers[0].get('name')}")
            
            print("\n----------------------")

# 这是Muimill今天摘给你的小星星～希望你喜欢。
