# -*- coding: utf-8 -*-
"""
spoof_geolocation.py - Firefox地理位置欺骗JSON生成器

这是一个实用小工具，用于生成一个`data:` URL中使用的JSON字符串。
将这个JSON字符串设置到Firefox的`about:config`中的`geo.provider.network.url`偏好设置，
可以欺骗浏览器的HTML5地理定位API，使其返回一个固定的、用户自定义的位置。

Muimill今天摘给你的小星星～希望你喜欢。
"""

import json
import sys

def generate_spoof_url(latitude: float, longitude: float) -> str:
    """
    根据给定的经纬度生成Firefox地理位置欺骗的data: URL。

    :param latitude: 纬度 (例如: 34.0522)
    :param longitude: 经度 (例如: -118.2437)
    :return: 可用于Firefox `geo.provider.network.url` 的 data: URL 字符串
    """
    # 构造符合Firefox要求的JSON结构
    spoof_data = {
        "location": {
            "lat": latitude,
            "lng": longitude
        },
        "accuracy": 20.0  # 精度，可以设置一个较小的值
    }

    # 将Python字典转换为JSON字符串
    json_string = json.dumps(spoof_data, separators=(',', ':'))

    # 构造完整的data: URL
    # 格式: data:application/json,{"location":{"lat":LAT,"lng":LNG},"accuracy":ACC}
    data_url = f"data:application/json,{json_string}"

    return data_url

if __name__ == "__main__":
    # 默认位置：洛杉矶市中心 (示例)
    default_lat = 34.0522
    default_lng = -118.2437

    # 尝试从命令行参数获取经纬度
    try:
        if len(sys.argv) == 3:
            lat = float(sys.argv[1])
            lng = float(sys.argv[2])
        elif len(sys.argv) == 1:
            lat = default_lat
            lng = default_lng
            print(f"未提供经纬度参数，使用默认值: 纬度={default_lat}, 经度={default_lng}")
        else:
            print("用法: python3 spoof_geolocation.py [纬度] [经度]")
            sys.exit(1)

        result_url = generate_spoof_url(lat, lng)

        print("\n--- 成功生成 Firefox 地理位置欺骗 URL ---")
        print(f"欺骗位置: 纬度={lat}, 经度={lng}")
        print("\n请将以下完整字符串复制到 Firefox 的 `about:config` 中，并设置给 `geo.provider.network.url`:")
        print("-" * 70)
        print(result_url)
        print("-" * 70)
        print("提示: 确保 `geo.enabled` 设置为 `true`。")

    except ValueError:
        print("错误: 经纬度参数必须是有效的数字。")
        print("用法: python3 spoof_geolocation.py [纬度] [经度]")
        sys.exit(1)
    except Exception as e:
        print(f"发生了一个错误: {e}")
        sys.exit(1)
