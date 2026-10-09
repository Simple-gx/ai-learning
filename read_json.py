import json   # json 模块：负责把 json 格式的文字 <-> Python 字典 互相转

# with 语句：打开文件，用完自动关，不怕忘
with open("data.txt", "r", encoding="utf-8") as f:   # "r"=读模式，encoding 防中文乱码
    text = f.read()        # 把文件里的文字全部读出来，变成一串字符串

data = json.loads(text)    # loads = 把 json 文字"解析"成 Python 字典（和之前 resp.json() 同理）
print("名字：", data["name"])
print("爱好：", data["hobby"])
print("年龄：", data["age"])
print("城市：", data["city"])
