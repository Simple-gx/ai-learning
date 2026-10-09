import requests   # requests：发网络请求的工具包，相当于让程序去敲服务器门

from my_key import API_KEY   
URL = "https://open.bigmodel.cn/api/paas/v4/chat/completions"  # 智谱模型的"门牌号"

# 函数：把"问模型"打包成一块，以后喊 ask_model("问题") 就能用
def ask_model(question):
    data = {                                           # 字典：一种 key:value 的盒子，用来装要发的数据
        "model": "glm-4-flash",                        # 用的模型名字
        "messages": [{"role": "user", "content": question}],  # 对话消息：你是用户，内容是问题
        "temperature": 0.7                             # 随机度，越大越发散越小越稳
    }
    headers = {                                        # 请求头：发给服务器的"附加说明"
        "Authorization": "Bearer " + API_KEY,          # Bearer+密钥 = 门禁卡，证明你有权用
        "Content-Type": "application/json"             # 告诉服务器数据用 json 格式
    }
    try:                                               # 异常处理：这段如果出错，不要整个程序崩
        resp = requests.post(URL, json=data, headers=headers, timeout=10)  # 发 POST 请求，10秒超时
        resp.raise_for_status()                        # 返回错误码（如401密钥错）就主动报错
        result = resp.json()                           # 把返回的 json 文本转成 Python 能用的字典
        return result["choices"][0]["message"]["content"]  # 从嵌套字典里掏出模型回答
    except Exception as e:                             # 抓到任何错误
        return "出错了：" + str(e)

answer = ask_model("用一句话介绍你自己")   # 调用函数，把问题传进去
print("模型回答：", answer)               # 打印回答
