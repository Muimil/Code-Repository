_# -*- coding: utf-8 -*-
# 这是Muimill今天摘给你的小星星～希望你喜欢。

import duckdb
import os

# --------------------------------------------------------------------------------
# 实用技巧：DuckDB 数据静止加密 (Data-at-Rest Encryption)
# --------------------------------------------------------------------------------
# DuckDB 是一个高性能的进程内分析型数据库。
# 它的一个强大功能是支持数据静止加密，确保数据库文件在磁盘上是加密的，
# 即使文件被盗，数据也无法被读取。
# --------------------------------------------------------------------------------

DB_FILE = "encrypted_muimill.duckdb"
ENCRYPTION_KEY = "MuimillLovesCoding123" # 替换为你的强密码

def create_and_encrypt_db():
    """
    创建并加密一个DuckDB数据库文件。
    """
    print(f"1. 尝试创建并连接到加密数据库: {DB_FILE}")
    try:
        # 连接到数据库并设置加密密钥
        con = duckdb.connect(database=DB_FILE, read_only=False)
        con.execute(f"PRAGMA key='{ENCRYPTION_KEY}'")

        # 创建一个简单的表
        con.execute("CREATE TABLE stars (id INTEGER, name VARCHAR, magnitude DOUBLE)")

        # 插入数据
        data = [
            (1, 'Polaris', 1.98),
            (2, 'Sirius', -1.46),
            (3, 'Vega', 0.03)
        ]
        con.executemany("INSERT INTO stars VALUES (?, ?, ?)", data)

        print("   - 数据库创建成功，数据已插入。")
        con.close()
        print("   - 数据库连接已关闭。")

    except Exception as e:
        print(f"   - 错误: {e}")

def read_encrypted_db():
    """
    尝试使用正确的密钥读取加密数据库。
    """
    print("\n2. 尝试使用正确的密钥读取数据库...")
    try:
        con = duckdb.connect(database=DB_FILE, read_only=True)
        con.execute(f"PRAGMA key='{ENCRYPTION_KEY}'")
        result = con.execute("SELECT * FROM stars WHERE magnitude < 0").fetchall()
        print("   - 读取成功！负星等恒星:")
        for row in result:
            print(f"     {row}")
        con.close()
    except Exception as e:
        print(f"   - 错误: {e}")

def read_without_key():
    """
    尝试不使用密钥读取加密数据库（预期失败）。
    """
    print("\n3. 尝试不使用密钥读取数据库（预期失败）...")
    try:
        con = duckdb.connect(database=DB_FILE, read_only=True)
        con.execute("SELECT * FROM stars").fetchall()
        print("   - 错误：意外地读取成功了！(这不应该发生)")
        con.close()
    except duckdb.IOException as e:
        print(f"   - 预期错误发生：{e}")
        print("   - 数据库文件已被有效加密。")
    except Exception as e:
        print(f"   - 发生其他错误: {e}")

def cleanup():
    """
    清理创建的数据库文件。
    """
    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)
        print(f"\n4. 清理完成，文件 {DB_FILE} 已删除。")

if __name__ == "__main__":
    # 确保DuckDB已安装
    try:
        import duckdb
    except ImportError:
        print("DuckDB 库未安装。请运行 'pip3 install duckdb'。")
        exit()

    cleanup() # 确保开始前没有旧文件
    create_and_encrypt_db()
    read_encrypted_db()
    read_without_key()
    cleanup() # 再次清理
_
