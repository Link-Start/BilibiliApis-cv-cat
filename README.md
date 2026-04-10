<div align="center">
    <a href="https://www.python.org/">
        <img src="https://img.shields.io/badge/python-3.12%2B-blue" alt="Python 3.12+">
    </a>
    <a href="https://nodejs.org/zh-cn/">
        <img src="https://img.shields.io/badge/nodejs-20%2B-green" alt="NodeJS 20+">
    </a>
    <a href="https://fastapi.tiangolo.com/">
        <img src="https://img.shields.io/badge/FastAPI-0.115%2B-009688" alt="FastAPI">
    </a>
</div>

# 🎬 Bilibili Platform

**✨ 专业的 B站 视频数据采集解决方案，支持按关键词批量搜索视频信息**

当你需要让 AI Agent 感知 B站内容生态——自动采集视频热度、分析弹幕趋势、驱动内容运营策略——第一道墙往往不是模型能力，而是**平台数据获取能力的缺失**。

本项目做的事很简单：把这道墙拆掉。

**⚠️ 严禁用于爬取用户隐私、违规商业用途！本项目仅供学习与技术研究使用，后果自负。**

## 🌟 功能特性

- ✅ **视频搜索采集**
  - 按关键词批量搜索视频
  - 支持按播放量 / 弹幕数排序
  - 自动翻页，按需获取指定数量结果
- 🔐 **WBI 签名自动计算**
  - 内嵌 JS 运行时，自动生成 `w_rid` 签名参数
  - 适配 B站最新 WBI 鉴权接口
- 🚀 **高性能服务**
  - 基于 FastAPI + Uvicorn 异步服务
  - 支持 Docker 一键部署

## 🛠️ 快速开始

### ⛳ 运行环境

- Python 3.12+
- Node.js 20+


### 🎯 本地安装

```bash
pip install -r requirements.txt
```

### 🚀 运行项目

```bash
python App.py
```

服务启动后访问 http://localhost:5008/docs 查看交互式 API 文档。

### 🎨 Cookie 配置

在浏览器中打开 [www.bilibili.com](https://www.bilibili.com)，**登录账号**后按 `F12` 打开开发者工具，点击「网络」→ 找任意一个接口请求 → 复制请求头中的 `Cookie` 字段值。

> ⚠️ 注意：必须登录后获取的 Cookie 才有效，未登录的 Cookie 无法正常请求搜索接口。

将获取到的 Cookie 字符串作为 `cookies_str` 参数传入接口，格式如下：

```
SESSDATA=xxx; bili_jct=xxx; DedeUserID=xxx; ...
```

## 📡 接口说明

### POST `/search_some_by_num`

按数量批量搜索 B站 视频。

**请求参数**

| 字段          | 类型  | 必填 | 说明                                  |
|-------------|-----|----|-------------------------------------|
| keyword     | str | 是  | 搜索关键词                               |
| num         | int | 是  | 期望返回的视频数量                           |
| order       | str | 是  | 排序方式：`dm`（弹幕数）/ `click`（播放量）       |
| cookies_str | str | 是  | B站登录 Cookie 字符串                     |

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
      "video_review": 5000
    }
  ]
}
```

## 🍥 日志

| 日期       | 说明                            |
|----------|---------------------------------|
| 26/04/10 | 项目初始化，完成视频搜索 API 封装            |

## 🧸 额外说明

1. 感谢 star⭐ 和 follow📰！不时更新
2. 有问题欢迎通过 Issue 反馈
3. 仅供学习和技术研究，请遵守 [B站用户服务协议](https://www.bilibili.com/blackboard/agreement.html)
