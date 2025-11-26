# -*- coding: utf-8 -*-
# 文件名: cdc_to_json.py

import json
from datetime import datetime

# 模拟从PostgreSQL CDC（Change Data Capture）流中接收到的数据记录
# 实际应用中，这可能是一个Kafka消息、RabbitMQ队列消息或直接的数据库通知
def simulate_cdc_record(table_name, operation, old_data, new_data):
    """
    模拟一条CDC记录。
    :param table_name: 发生变化的表名
    :param operation: 操作类型 (\'INSERT\', \'UPDATE\', \'DELETE\')
    :param old_data: 旧数据 (仅UPDATE和DELETE有)
    :param new_data: 新数据 (仅INSERT和UPDATE有)
    :return: 结构化的CDC记录字典
    """
    record = {
        "timestamp": datetime.now().isoformat(),
        "table": table_name,
        "operation": operation,
        "payload": {}
    }

    if operation == \'INSERT\':
        record["payload"]["after"] = new_data
    elif operation == \'UPDATE\':
        record["payload"]["before"] = old_data
        record["payload"]["after"] = new_data
    elif operation == \'DELETE\':
        record["payload"]["before"] = old_data
    
    return record

def process_cdc_to_json(cdc_record):
    """
    将CDC记录转换为JSON字符串，并进行简单的处理（例如，添加处理标记）。
    :param cdc_record: 结构化的CDC记录字典
    :return: JSON格式的字符串
    """
    # 模拟数据处理：添加一个处理时间戳
    cdc_record["processed_at"] = datetime.now().isoformat()
    
    # 转换为JSON字符串
    json_output = json.dumps(cdc_record, indent=4, ensure_ascii=False)
    return json_output

# --- 示例数据 ---
# 1. 插入操作 (新用户注册)
insert_data = {
    "id": 101,
    "username": "Muimill",
    "email": "muimill@example.com",
    "status": "active"
}
insert_record = simulate_cdc_record("users", "INSERT", None, insert_data)

# 2. 更新操作 (用户状态变更)
old_update_data = {
    "id": 101,
    "username": "Muimill",
    "email": "muimill@example.com",
    "status": "active"
}
new_update_data = {
    "id": 101,
    "username": "Muimill",
    "email": "muimill@example.com",
    "status": "suspended"
}
update_record = simulate_cdc_record("users", "UPDATE", old_update_data, new_update_data)

# --- 运行和输出 ---
print("--- 插入操作的JSON输出 ---")
insert_json = process_cdc_to_json(insert_record)
print(insert_json)

print("\n--- 更新操作的JSON输出 ---")
update_json = process_cdc_to_json(update_record)
print(update_json)

# 这是Muimill今天摘给你的小星星～希望你喜欢。
