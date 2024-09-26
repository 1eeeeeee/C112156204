import json

# 預設匯率
exchange_rates = {
    'USD': 0.032,  # 美元
    'EUR': 0.027,  # 歐元
    'JPY': 3.5     # 日圓
}

# 將字典轉換成JSON格式
exchange_rates_json = json.dumps(exchange_rates, indent=4)

# 將JSON格式的匯率寫入一個新的JSON文件
with open('exchange_rates.json', 'w') as json_file:
    json_file.write(exchange_rates_json)

print("匯率已成功轉換並寫入exchange_rates.json文件")