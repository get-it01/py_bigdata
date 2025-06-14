import requests
import pandas as pd
import logging

def setup_logger():
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        handlers=[logging.StreamHandler()])
setup_logger()



# 定义 Flask 接口的 URL
api_url = 'http://127.0.0.1:1233/stut_info'
area_api_url = 'http://127.0.0.1:1233/area_info'
def analyze_api_data(api_url=api_url):
    try:
        # 发送 GET 请求到 Flask 接口
        response = requests.get(api_url)
        
        # Analyze the status code, if it's not 200, output an error message
        # if response.status_code != 200:
        #     print(f'Error: Received status code {response.status_code}, expected 200.')
        #     return 0
        # else:
        #     print(f'Success: Received status code {response.status_code}.')
        # 解析 JSON 数据
        json_data = response.json()
        
        # 根据返回的数据类型创建 DataFrame
        if isinstance(json_data, list):
            # 如果是 JSON 数组
            df = pd.DataFrame(json_data)
        elif isinstance(json_data, dict):
            # 如果是 JSON 字典
            df = pd.DataFrame([json_data])
        else:
            print('不支持的数据类型，期望 JSON 数组或字典。')
            return
        
        # 进行简单的数据分析
        print('数据基本信息：')
        df.info()
        
        # 显示数据集行数和列数
        rows, columns = df.shape
        if rows > 0:
            # 显示数据集前几行
            print('数据前几行：')
            print(df.head().to_csv(sep='\t', na_rep='nan'))
            
            # 显示数值列的统计信息
            if df.select_dtypes(include=['number']).shape[1] > 0:
                print('数值列统计信息：')
                print(df.select_dtypes(include=['number']).describe().to_csv(sep='\t', na_rep='nan'))
            else:
                print('数据集中没有数值列。')
        else:
            print('数据集中没有数据。')

    except requests.RequestException as e:
        print(f'请求发生错误: {e}')
    except ValueError as e:
        print(f'JSON 解析错误: {e}')

if  __name__ == '__main__':
    analyze_api_data(area_api_url)