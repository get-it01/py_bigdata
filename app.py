from dataProcessing.dataReceive import analyze_api_data,area_api_url,user_api_url,sign_api_url
from dataProcessing.dataToParquet import save_df_to_parquet
from dataProcessing.saveToMysql import connect_to_mysql_and_execute
from msgPush.emailPush import send_email_notification
from pyDataGeneration.pyDataGeneration import area_info,user_info,sign_info,setup_logger
setup_logger() #作用: 设置日志


# 启动flask服务器
import threading
from flask import Flask
from pyDataGeneration.pyDataGeneration import app  # 直接导入已定义好的 Flask app 实例
user_data_dir = r'D:\windocu\desktop\test1\user_data_dir'
sign_data_dir = r'D:\windocu\desktop\test1\sign_data_dir'
area_data_dir = r'D:\windocu\desktop\test1\area_data_dir'
def run_flask():
    app.run(host='0.0.0.0', port=1233, threaded=True)

if __name__ == '__main__':
    # 启动 Flask 服务在子线程中运行
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True  # 主线程结束时自动关闭子线程
    flask_thread.start()

    print("Flask 已启动，现在可以继续执行其他任务...")
    for i in range(10):
        print(f"当前循环次数：{i}")
        res_df = analyze_api_data(user_api_url,num=i)
        save_df_to_parquet(res_df,user_data_dir+user_api_url.split('/')[-1]+str(i)+'.parquet')
        connect_to_mysql_and_execute(res_df,f'{user_api_url.split('/')[-1]}')

        res_df = analyze_api_data(sign_api_url,num=i)
        save_df_to_parquet(res_df,sign_data_dir+sign_api_url.split('/')[-1]+str(i)+'.parquet')
        connect_to_mysql_and_execute(res_df,f'{sign_api_url.split('/')[-1]}')

    res_df = analyze_api_data(area_api_url)
    save_df_to_parquet(res_df,area_data_dir+area_api_url.split('/')[-1]+str(i)+'.parquet')
    connect_to_mysql_and_execute(res_df,f'{area_api_url.split('/')[-1]}')

    # 在这里你可以调用其他函数，比如数据分析、写入 Parquet 等
    # analyze_api_data(...)
    # save_df_to_parquet(...)