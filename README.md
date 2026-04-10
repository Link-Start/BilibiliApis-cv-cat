# Bilibili Platform API

基于 FastAPI 封装的 Bilibili 搜索接口服务，支持按关键词、排序方式批量获取视频信息。

## 技术栈

- **Python 3.12** + **FastAPI** + **Uvicorn**
- **PyExecJS** + **Node.js** — 在 Python 中执行 JS 代码，用于生成 Bilibili WBI 签名参数

## 快速开始

### Docker 运行（推荐）

```bash
# 构建镜像
docker build -t bilibili-platform .

# 启动容器
docker run -d -p 5008:5008 --name bilibili-platform bilibili-platform
```

### 本地运行

```bash
# 安装依赖（需要 Python 3.12+ 和 Node.js 20+）
pip install -r requirements.txt

# 启动服务
python App.py
```

服务启动后访问 http://localhost:5008/docs 查看交互式 API 文档。

## API 说明

### POST `/search_some_by_num`

按数量批量搜索 Bilibili 视频。

**请求体**

| 字段         | 类型   | 必填 | 说明                                      |
|------------|------|----|-----------------------------------------|
| keyword    | str  | 是  | 搜索关键词                                   |
| num        | int  | 是  | 期望返回的视频数量                               |
| order      | str  | 是  | 排序方式：`dm`（弹幕数）/ `click`（播放量）           |
| cookies_str | str  | 是  | Bilibili 登录 Cookie 字符串（格式见下方说明）        |

**cookies_str 格式**

从浏览器开发者工具中复制 Bilibili 请求头中的 Cookie 字段值，格式为：

```
SESSDATA=xxx; bili_jct=xxx; DedeUserID=xxx; ...
```

**请求示例**

```bash
curl -X POST http://localhost:5008/search_some_by_num \
  -H "Content-Type: application/json" \
  -d '{
    "keyword": "编程教学",
    "num": 20,
    "order": "click",
    "cookies_str": "SESSDATA=xxx; bili_jct=xxx; DedeUserID=xxx"
  }'
```

**响应示例**

```json
{
  "code": 200,
  "message": "成功",
  "data": [
    {
      "aid": 123456789,
      "bvid": "BVxxxxxxxx",
      "title": "视频标题",
      "author": "UP主名称",
      "play": 100000,
      "video_review": 5000,
      ...
    }
  ]
}
```

**响应字段**

| 字段      | 说明              |
|---------|-----------------|
| code    | 200 成功，400 失败   |
| message | 结果描述            |
| data    | 视频列表，失败时为 null |

## 项目结构

```
.
├── App.py              # FastAPI 应用入口
├── apis/
│   └── bili_apis.py    # Bilibili API 封装
├── utils/
│   └── bili_utils.py   # 工具函数（签名、请求头、Cookie 解析）
├── static/
│   └── bili.js         # WBI 签名所需 JS 代码
├── requirements.txt
├── Dockerfile
└── .dockerignore
```

## 注意事项

- 需要有效的 Bilibili 登录 Cookie，Cookie 过期后需重新获取
- 搜索结果依赖 Bilibili 接口，受其频率限制和反爬策略影响
- 仅供学习和研究使用，请遵守 Bilibili 用户协议
