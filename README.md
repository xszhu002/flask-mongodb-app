# Flask MongoDB Docker 应用

一个简单的使用Flask和MongoDB的待办事项应用，通过Docker容器化部署。

## 功能特点

- 创建和删除待办事项
- 使用MongoDB存储数据
- 完全容器化的应用部署
- 包含错误处理逻辑，当MongoDB不可用时使用内存存储

## 技术栈

- **后端**: Flask (Python 3.9)
- **数据库**: MongoDB 7.0
- **容器化**: Docker & Docker Compose

## 开始使用

### 使用Docker Compose

```bash
docker-compose up -d
```

### 访问应用

应用将在以下地址可用:
```
http://localhost:5000
```

## 环境变量

应用支持以下环境变量:

- `MONGO_HOST`: MongoDB主机名 (默认: "localhost")
- `MONGO_PORT`: MongoDB端口 (默认: 27017)

## 构建Docker镜像

```bash
docker build -t flask-mongodb-app .
```

## 许可证

MIT 