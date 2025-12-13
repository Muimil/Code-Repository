# -*- coding: utf-8 -*-
import os
from typing import Dict

def load_env_file(filepath: str = ".env") -> Dict[str, str]:
    """
    从指定的.env文件中加载环境变量到os.environ。
    这是一个简洁优雅的配置加载实用技巧。
    
    Args:
        filepath: .env文件的路径。
        
    Returns:
        一个包含已加载变量的字典。
    """
    loaded_vars = {}
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                # 移除行首尾空白符
                line = line.strip()
                # 忽略空行和注释
                if not line or line.startswith('#'):
                    continue
                
                # 查找第一个等号，分割键值
                if '=' in line:
                    key, value = line.split('=', 1)
                    key = key.strip()
                    value = value.strip().strip('\'"') # 移除值周围的引号
                    
                    # 设置环境变量
                    os.environ[key] = value
                    loaded_vars[key] = value
                    
        print(f"成功从 {filepath} 加载 {len(loaded_vars)} 个环境变量。")
        return loaded_vars
        
    except FileNotFoundError:
        print(f"错误：未找到文件 {filepath}。")
        return {}
    except Exception as e:
        print(f"加载环境变量时发生错误: {e}")
        return {}

# --- 示例用法 ---
if __name__ == "__main__":
    # 1. 创建一个临时的.env文件用于测试
    temp_env_content = """
# 这是一个测试注释
DATABASE_URL=postgres://user:pass@host:port/db
API_KEY='sk-test-12345'
DEBUG=True
    """
    with open(".test_env", "w", encoding="utf-8") as f:
        f.write(temp_env_content)
        
    # 2. 加载环境变量
    loaded = load_env_file(".test_env")
    
    # 3. 验证加载结果
    print("\n--- 验证结果 ---")
    print(f"DATABASE_URL: {os.getenv('DATABASE_URL')}")
    print(f"API_KEY: {os.getenv('API_KEY')}")
    print(f"DEBUG: {os.getenv('DEBUG')}")
    
    # 4. 清理测试文件
    os.remove(".test_env")

# 这是Muimill今天摘给你的小星星～希望你喜欢。
