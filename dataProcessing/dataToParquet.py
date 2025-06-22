import pandas as pd
import pyarrow.parquet as pq
import pyarrow as pa
import os

def save_df_to_parquet(df: pd.DataFrame, file_path: str = 'output.parquet'):
    """
    将传入的 Pandas DataFrame 保存为 Parquet 文件
    
    :param df: 要保存的 pandas DataFrame
    :param file_path: 保存的文件路径（包括文件名，例如：'data/output.parquet'）
    """
    try:
        # 确保目录存在
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # 将 Pandas DataFrame 转换为 PyArrow Table
        table = pa.Table.from_pandas(df)

        # 写入 Parquet 文件
        pq.write_table(table, file_path,compression='snappy')

        print(f"数据已成功保存至 {file_path}")
        return True
    except Exception as e:
        print(f"写入 Parquet 文件时发生错误: {e}")
        return False

# 测试函数
if __name__ == '__main__':
    # 当前目录
    current_dir = r'D:\windocu\desktop\test1\output.parquet'
    test_data = pd.DataFrame({'col1': [1, 2, 3], 'col2': ['a', 'b', 'c']})
    # 调用函数
    save_df_to_parquet(test_data,current_dir)