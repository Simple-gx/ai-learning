import requests
from my_key import API_KEY          # 密钥从 Day3 那个 my_key.py 拿，不写死

URL = "https://open.bigmodel.cn/api/paas/v4/chat/completions"

history = []   # 历史消息列表：每轮对话都往里塞，这就是"记忆"

print("=== 多轮对话（输入 exit 退出）===")
while True:                              # 死循环，一直聊直到输入 exit
    user_input = input("你：")           # 等你在终端打字
    if user_input == "exit":
        break                            # 输入 exit 就跳出循环
    history.append({"role": "user", "content": user_input})  # 把你说的话加进历史
    data = {
        "model": "glm-4-flash",
        "messages": history,             # 关键：把整个历史发给模型，它才"看得到"前面聊的
        "temperature": 0.7
    }
    headers = {"Authorization": "Bearer " + API_KEY, "Content-Type": "application/json"}
    resp = requests.post(URL, json=data, headers=headers, timeout=10)
    answer = resp.json()["choices"][0]["message"]["content"]
    print("模型：", answer)
    history.append({"role": "assistant", "content": answer})   # 把模型回答也加进历史

print("这次对话共攒了", len(history), "条消息")
