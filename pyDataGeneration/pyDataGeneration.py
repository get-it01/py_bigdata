import flask

from flask import Flask, jsonify

# 创建 Flask 应用实例
app = Flask(__name__)

# 定义一个函数




# 定义一个路由，当访问根路径时触发该函数
@app.route('/get_json', methods=['GET'])
def get_json_data():
    # 产生一万条保险的保单数据




    # 定义要发送的 JSON 数据
    data = {
        "message": "这是一个来自 Flask 接口的 JSON 响应",
        "status": "成功",
        "code": 200
    }
    # 使用 jsonify 函数将 Python 字典转换为 JSON 响应
    return jsonify(data)

if __name__ == '__main__':
    # 启动 flask, ip单独设置
    # app.run('0.0.0.0', 123123)
    app.run(host='localhost', port=1233)
