from fastapi import FastAPI

app = FastAPI()                 # 创建一个接口应用，相当于开了一个能接单的服务台

@app.get("/")                   # 路由：别人用 GET 访问根路径 "/" 时，触发下面这个函数
def read_root():
    return {"message": "Hello World"}   # 返回字典，FastAPI 自动帮你转成 json 回出去
