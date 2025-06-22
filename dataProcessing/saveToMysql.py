
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

def connect_to_mysql_and_execute(dataFrame,table_name = 'test' , sql = None):
    # MySQL 数据库配置
    db_config = {
        'drivername': 'mysql+pymysql',  # 使用 pymysql 作为驱动
        'username': 'root',    # 替换为你的 MySQL 用户名
        'password': 'mysql',    # 替换为你的 MySQL 密码
        'host': 'localhost',            # 数据库主机地址
        'port': 3306,                   # 数据库端口
        'database': 'dbtest'     # 要连接的数据库名称
    }

    try:
        # 构建数据库连接 URL
        db_url = URL.create(
            drivername=db_config['drivername'],
            username=db_config['username'],
            password=db_config['password'],
            host=db_config['host'],
            port=db_config['port'],
            database=db_config['database']
        )

        # 创建 SQLAlchemy 引擎
        engine = create_engine(db_url)
        if sql:
            engine.execute(sql)
        else:
            pd_to_db(engine,dataFrame,table_name)
        # 连接数据库
        # with engine.connect() as connection:
        #     print("成功连接到 MySQL 数据库")
            
            # 在这里可以执行 SQL 操作，例如：
            # result = connection.execute("SELECT * FROM your_table")
            # for row in result:
            #     print(row)
        return True
    except Exception as e:
        print("连接或操作数据库时发生错误: ", e)
        return False
    finally:
        engine.dispose()    



def pd_to_db(engine,df,table_name):

        # 使用 pandas 的 to_sql 方法写入数据库
    df.to_sql(name=table_name, con=engine, if_exists='append', index=True)
    print(f"数据已成功写入表 {table_name}")



# 示例用法（可选）
if __name__ == "__main__":
    # 示例 DataFrame
    data = {
        'id': [1, 2, 3],
        'name': ['Alice', 'Bob', 'Charlie']
    }
    df = pd.DataFrame(data)
    
    connect_to_mysql_and_execute(df)