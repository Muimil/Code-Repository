# -*- coding: utf-8 -*-
import os

def generate_project_summary(startpath='.', exclude_dirs=None, exclude_files=None):
    """
    生成项目目录结构的Markdown格式摘要。
    排除常见的构建目录和配置文件，提供一个干净的项目概览。
    """
    if exclude_dirs is None:
        # 常见的排除目录
        exclude_dirs = {'.git', '__pycache__', 'node_modules', '.venv', 'venv', 'dist', 'build'}
    if exclude_files is None:
        # 常见的排除文件
        exclude_files = {'.DS_Store', 'Thumbs.db', 'LICENSE', 'README.md'}

    output = []
    
    # 递归遍历目录
    for root, dirs, files in os.walk(startpath):
        # 过滤掉需要排除的目录
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        
        # 计算当前深度和前缀
        # os.sep 是路径分隔符，如 '/' 或 '\'
        relative_path = os.path.relpath(root, startpath)
        if relative_path == '.':
            level = 0
        else:
            level = relative_path.count(os.sep) + 1
        
        indent = '│   ' * (level - 1)
        
        # 打印当前目录
        if root != startpath:
            dir_name = os.path.basename(root)
            # 使用更优雅的树形结构符号
            output.append(f"{indent}├── 📁 **{dir_name}/**")

        # 打印文件
        sub_indent = '│   ' * level
        for f in files:
            if f not in exclude_files:
                output.append(f"{sub_indent}├── 📄 {f}")
                
    # 格式化输出，添加项目根目录
    project_name = os.path.basename(os.path.abspath(startpath))
    
    # 修正根目录的显示
    final_output = [f"## 🌳 项目结构概览：`{project_name}/`"]
    final_output.extend(output)
    
    return "\n".join(final_output)

if __name__ == '__main__':
    # 示例用法：生成当前目录的摘要
    summary = generate_project_summary()
    print(summary)
    
    # 这是Muimill今天摘给你的小星星～希望你喜欢。
