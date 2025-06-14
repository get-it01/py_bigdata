import json
import random
import logging
import time
import datetime
# from requests import Response
from flask import Flask, jsonify , request , Response

# 创建 Flask 应用实例
app = Flask(__name__)

def setup_logger():
    # 设置日志输出到文件，编码为 UTF-8，追加模式
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(levelname)s: %(message)s',
        handlers=[
            logging.StreamHandler(),  # 控制台输出
            logging.FileHandler('app.log', encoding='utf-8')  # 文件输出
        ]
    )
setup_logger()
# 定义城市映射表
city_mapping = {
    0: "北京",
    1: "上海",
    2: "南京",
    3: "杭州"
}

# 修改city获取函数
def get_city(i):
    return city_mapping.get(i % len(city_mapping), "未知")

# 定义个路由并fj访问该路由时，会返回一个 JSON 响应
@app.route('/area_info', methods=['GET'])
def area_info():
    try:
        data = [
            {
                "id": i,
                "city": get_city(i),
                "num": random.randint(0, 10)
            } for i in range(1, 5)
        ]
        return jsonify(data)
    except Exception as e:
        app.logger.error(f"Error in /area_info: {str(e)}")
        return jsonify({"code": 500, "message": "Internal Server Error"}), 500

# 定义一个路由，当访问根路径时触发该函数,并需要传入参数
@app.route('/stut_info', methods=['GET'])
def get_json_data():
    try:
        # 获取查询参数并限制最大值
        count = request.args.get('count', default=100, type=int)
        count = min(count, 1000)  # 防止过大请求

        data = [
            {
                "id": i,
                "name": f"用户{i}",
                'age': random.randint(7, 25),
                "gender": "男" if i % 2 == 0 else "女",
                "address": f"地址{i}",
                # 城市制造数据倾斜场景
                "city": "北京" if i % 9 == 0 else "上海" if i % 9 == 1 else "上海" if i % 9 == 2 else "上海" if i % 9 == 3 else "上海" if i % 9 == 4 else "上海" if i % 9 == 5 else "上海" if i % 9 == 6 else "上海" if i % 9 == 7 else "上海" if i % 8 == 0 else "南京",
                "yw_score": random.randint(0, 100),
                "sx_score": random.randint(0, 100),
                "yy_score": random.randint(0, 100),
                "time": datetime.datetime.now() - datetime.timedelta(days=random.randint(0, 1000)),
                
            } for i in range(1, count + 1)
        ]

        # def generate(data_list):
        #     yield "["
        #     count = len(data_list)
        #     for i, item in enumerate(data_list):
        #         yield json.dumps(item, ensure_ascii=False) + ("," if i < count - 1 else "]")

        # return Response(generate(data), mimetype='application/json')
        return jsonify(data)
    except Exception as e:
        app.logger.error(f"Error in /stut_info: {str(e)}")
        return jsonify({"code": 500, "message": "Internal Server Error"}), 500

if __name__ == '__main__':
    app.run(host='localhost', port=1233, threaded=True)
