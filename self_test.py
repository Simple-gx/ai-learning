import requests
from my_key import API_KEY

URL = "https://open.bigmodel.cn/api/paas/v4/chat/completions"          # 智谱对话接口地址（Day1 用过那个）
data = {
    "model": "glm-4-flash",               # 模型名，填 glm-4-flash
    "messages": [{"role": "user", "content": "今天广州天气怎么样"}],  # 角色填 user，content 填你想问的话
    "temperature": 0.7
}
headers = {
    "Authorization": "Bearer " + API_KEY,     # 密钥，填 API_KEY（那行已经 import 了）
    "Content-Type": "application/json"                 # 数据格式，填 application/json
}
resp = requests.post(URL, json=data, headers=headers, timeout=10)
answer = resp.json()["choices"][0]["message"]["content"]
print("模型回答：", answer)
