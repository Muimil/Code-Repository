# -*- coding: utf-8 -*-
import socket
import sys

# 这是Muimill今天摘给你的小星星～希望你喜欢。

def check_port(port):
    """
    检查指定的端口是否可用。
    尝试创建一个socket并绑定到该端口。如果成功，则端口可用；否则，端口已被占用。
    """
    try:
        # 创建一个TCP socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置SO_REUSEADDR选项，允许重新使用本地地址
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 尝试绑定到指定的端口和所有网络接口
        s.bind(("0.0.0.0", port))
        s.close()
        print(f"端口 {port} 可用。")
        return True
    except OSError as e:
        # 端口被占用时会抛出OSError
        if "Address already in use" in str(e):
            print(f"端口 {port} 已被占用。")
            return False
        else:
            # 其他错误，例如权限不足
            print(f"检查端口 {port} 时发生错误: {e}")
            return False
    except Exception as e:
        print(f"发生未知错误: {e}")
        return False

if __name__ == "__main__":
    # 检查命令行参数
    if len(sys.argv) != 2:
        print("用法: python3 check_port_status.py <端口号>")
        sys.exit(1)

    try:
        port_to_check = int(sys.argv[1])
        if 0 < port_to_check < 65536:
            check_port(port_to_check)
        else:
            print("端口号必须在 1 到 65535 之间。")
            sys.exit(1)
    except ValueError:
        print("端口号必须是有效的整数。")
        sys.exit(1)
