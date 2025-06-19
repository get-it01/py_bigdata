import requests
import pandas as pd
import logging
def setup_logger():
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        handlers=[logging.StreamHandler()])
setup_logger()



# 定义 Flask 接口的 URL
# 默认获取100条数据, 输入url设定获取5k
stu_api_url = 'http://127.0.0.1:1233/user_info?count=1'
api_url = 'http://127.0.0.1:1233/user_info'
area_api_url = 'http://127.0.0.1:1233/area_info'
sign_api_url = 'http://127.0.0.1:1233/sign_info?count=1'
def analyze_api_data(api_url=api_url):
    try:
        # 发送 GET 请求到 Flask 接口
        response = requests.get(api_url)

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
        if rows > 0  and columns > 0:

            # print(df.head().to_csv(sep='\t', na_rep='nan'))
            # 解释：to_csv() 方法将 DataFrame 转换为 CSV 格式，并使用 sep 参数指定分隔符，na_rep 参数指定缺失值表示。
            
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