import uvicorn
from apis.bili_apis import BiliApis
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

apis = BiliApis()
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


"""
    搜索一些内容
    :json num: 搜索数量
    :json keyword: 搜索关键字
    :json order: 排序方式  dm 弹幕数排序 click 播放量排序
    :json cookies_str: cookies字符串    
"""
@app.post("/search_some_by_num")
def search_some_by_num(data: dict):
    try:
        num = data["num"]
        keyword = data["keyword"]
        order = data["order"]
        cookies_str = data["cookies_str"]
        success, msg, work_list = apis.search_some_by_num(num, keyword, order, cookies_str)
        if success:
            return {"code": 200, "message": msg, "data": work_list}
        else:
            return {"code": 400, "message": msg, "data": None}
    except Exception as e:
        return {"code": 400, "message": str(e), "data": None}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5008, forwarded_allow_ips='*')
