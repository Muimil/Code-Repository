# -*- coding: utf-8 -*-
# 这是Muimill今天摘给你的小星星～希望你喜欢。✨

"""
实用技巧：使用 Pydantic 和 Rich 库进行配置验证和美化输出

这个脚本演示了如何使用 Pydantic 来定义和验证结构化的配置数据，
并使用 Rich 库将验证结果和配置内容以美观、彩色的格式输出到命令行。
这对于任何需要读取和验证配置文件的项目都非常实用。
"""

import json
from pydantic import BaseModel, Field, ValidationError
from rich.console import Console
from rich.panel import Panel
from rich.pretty import pprint

# 1. 定义配置模型 (Pydantic BaseModel)
# 假设我们有一个项目配置，包含数据库连接信息和一些通用设置
class DatabaseConfig(BaseModel):
    """数据库连接配置模型"""
    host: str = Field(..., description="数据库主机地址")
    port: int = Field(5432, description="数据库端口")
    user: str = Field(..., description="数据库用户名")
    password: str = Field(..., description="数据库密码")

class ProjectConfig(BaseModel):
    """项目主配置模型"""
    project_name: str = Field(..., description="项目名称")
    version: str = Field("1.0.0", description="项目版本号")
    debug_mode: bool = Field(False, description="是否开启调试模式")
    database: DatabaseConfig = Field(..., description="数据库配置")

# 2. 模拟读取配置文件
CONFIG_FILE_PATH = "config.json"

def load_config(file_path: str) -> dict:
    """从JSON文件加载配置数据"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

# 3. 验证和输出
def validate_and_display_config():
    """验证配置并使用 Rich 输出结果"""
    console = Console()
    raw_config = load_config(CONFIG_FILE_PATH)

    if not raw_config:
        console.print(Panel("[bold red]错误：[/bold red] 无法加载配置文件或文件为空。", title="[bold yellow]配置验证结果[/bold yellow]", border_style="red"))
        return

    try:
        # 使用 Pydantic 模型验证原始数据
        validated_config = ProjectConfig(**raw_config)

        # 验证成功，使用 Rich 打印美观的成功信息和配置详情
        console.print(Panel(
            f"[bold green]配置验证成功！[/bold green] 项目名称: [cyan]{validated_config.project_name}[/cyan]",
            title="[bold yellow]配置验证结果[/bold yellow]",
            border_style="green"
        ))
        
        console.print("\n[bold magenta]--- 验证后的配置详情 ---[/bold magenta]")
        # 使用 Rich 的 pprint 打印结构化数据，自动美化
        pprint(validated_config.model_dump(), console=console)

    except ValidationError as e:
        # 验证失败，使用 Rich 打印错误信息
        console.print(Panel(
            f"[bold red]配置验证失败！[/bold red] 请检查 {CONFIG_FILE_PATH} 文件中的错误。",
            title="[bold yellow]配置验证结果[/bold yellow]",
            border_style="red"
        ))
        console.print("\n[bold red]--- 详细错误信息 ---[/bold red]")
        # 打印 Pydantic 提供的详细错误报告
        pprint(e.errors(), console=console)

if __name__ == "__main__":
    validate_and_display_config()
