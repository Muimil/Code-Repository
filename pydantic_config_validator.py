# -*- coding: utf-8 -*-
# 文件名: pydantic_config_validator.py

from pydantic import BaseModel, Field, ValidationError
from typing import List, Optional

# 科技圈热点：Python类型提示(Type Hinting)和数据验证库Pydantic的巧妙应用。
# 这是一个用于验证应用配置的mini工具，确保数据结构和类型正确。

class DatabaseConfig(BaseModel):
    """数据库连接配置模型"""
    host: str = Field(default="localhost", description="数据库主机地址")
    port: int = Field(default=5432, description="数据库端口")
    user: str
    password: str

class AppSettings(BaseModel):
    """应用全局设置模型"""
    app_name: str = Field(default="Muimill_App", description="应用名称")
    debug_mode: bool = Field(default=False, description="是否开启调试模式")
    allowed_hosts: List[str] = Field(default=["127.0.0.1"], description="允许访问的主机列表")
    db: DatabaseConfig

def validate_config(config_data: dict):
    """
    验证传入的配置数据是否符合AppSettings模型。
    """
    print("--- 尝试加载配置数据 ---")
    print(config_data)
    try:
        # Pydantic会自动进行类型转换和验证
        settings = AppSettings(**config_data)
        print("\n✅ 配置验证成功！")
        print(f"应用名称: {settings.app_name}")
        print(f"调试模式: {settings.debug_mode}")
        print(f"数据库端口: {settings.db.port} (使用了默认值)")
        print(f"数据库用户: {settings.db.user}")
        
    except ValidationError as e:
        print("\n❌ 配置验证失败！")
        print(e.errors())
        
    print("--------------------------\n")

# --- 实用案例 ---

# 案例一：有效配置 (缺少可选字段，但Pydantic会使用默认值)
valid_config = {
    "db": {
        "user": "muimill_user",
        "password": "secure_password_123"
        # host和port将使用默认值
    }
}
validate_config(valid_config)

# 案例二：无效配置 (缺少必需字段 'db.user'，且'debug_mode'类型错误)
invalid_config = {
    "app_name": "Test_App",
    "debug_mode": "True", # 期望是布尔值，但传入了字符串
    "db": {
        "host": "remote_db"
        # 缺少必需的 'user' 和 'password'
    }
}
validate_config(invalid_config)


# 这是Muimill今天摘给你的小星星～希望你喜欢。
