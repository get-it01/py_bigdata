
import pandas as pd
from sqlalchemy import create_engine
import cx_Oracle


# 数据库配置
db_config = {
    'user': 'scott',
    'password': '123456',
    'host': '127.0.0.1',
    'port': 1521,
    'service_name': 'orcl'
}
def save_df_to_oracle(df, table_name, db_config=db_config):
    """
    将 Pandas DataFrame 写入 Oracle 数据库
    
    :param df: 要写入的 DataFrame
    :param table_name: 目标表名
    :param db_config: 包含数据库连接信息的字典
    """
    # 构建 Oracle 连接字符串
    dsn = cx_Oracle.makedsn(db_config['host'], db_config['port'], service_name=db_config['service_name'])
    connection_string = f'oracle+cx_oracle://{db_config["user"]}:{db_config["password"]}@{dsn}'
    
    # 创建引擎
    engine = create_engine(connection_string, echo=False)
    
    try:
        # 使用 pandas 的 to_sql 方法写入数据库
        df.to_sql(name=table_name, con=engine, if_exists='replace', index=False)
        print(f"数据已成功写入表 {table_name}")
    except Exception as e:
        print(f"写入数据时发生错误: {e}")
    finally:
        engine.dispose()#释放连接

# 示例用法（可选）
if __name__ == "__main__":
    # 示例 DataFrame
    data = {
        'id': [1, 2, 3],
        'name': ['Alice', 'Bob', 'Charlie']
    }
    df = pd.DataFrame(data)
    
    
    
    # 调用函数写入 Oracle
    save_df_to_oracle(df, 'test_table', db_config)