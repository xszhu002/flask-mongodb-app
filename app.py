from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import os
import time

app = Flask(__name__)

# MongoDB连接
mongo_host = os.environ.get('MONGO_HOST', 'localhost')
mongo_port = int(os.environ.get('MONGO_PORT', 27017))

# 尝试连接MongoDB，如果失败则使用内存中的数据
try:
    print(f"尝试连接到MongoDB: {mongo_host}:{mongo_port}")
    client = MongoClient(f'mongodb://{mongo_host}:{mongo_port}/', serverSelectionTimeoutMS=2000)
    # 通过执行一个简单的命令来验证连接
    client.admin.command('ping')
    print("MongoDB连接成功！")
    db = client['testdb']
    todos_collection = db['todos']
    use_mongodb = True
except Exception as e:
    print(f"MongoDB连接失败: {e}")
    print("将使用内存中的数据来代替MongoDB")
    use_mongodb = False
    # 在内存中存储待办事项
    memory_todos = []

@app.route('/')
def index():
    if use_mongodb:
        all_todos = list(todos_collection.find())
    else:
        all_todos = memory_todos
    return render_template('index.html', todos=all_todos)

@app.route('/add', methods=['POST'])
def add_todo():
    todo = request.form.get('todo')
    if todo:
        if use_mongodb:
            todos_collection.insert_one({'task': todo, 'done': False})
        else:
            # 为内存中的待办事项创建一个简单的ID
            todo_id = str(int(time.time() * 1000))
            memory_todos.append({'_id': todo_id, 'task': todo, 'done': False})
    return redirect(url_for('index'))

@app.route('/delete/<id>')
def delete_todo(id):
    if use_mongodb:
        from bson.objectid import ObjectId
        todos_collection.delete_one({'_id': ObjectId(id)})
    else:
        # 从内存中删除待办事项
        for i, todo in enumerate(memory_todos):
            if todo['_id'] == id:
                memory_todos.pop(i)
                break
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True) 