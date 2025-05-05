FROM python:3.9-slim

WORKDIR /app

# 设置DNS
RUN echo "nameserver 8.8.8.8" > /etc/resolv.conf

# 复制依赖文件并安装
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制应用代码
COPY . .

# 暴露Flask端口
EXPOSE 5000

# 运行应用的命令
CMD ["python", "app.py"] 