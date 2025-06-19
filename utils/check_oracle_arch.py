import cx_Oracle
import platform

print(f'Python Architecture: {platform.architecture()}')
try:
    print(f'Oracle Client Version: {cx_Oracle.clientversion()}')
    print('✅ 当前使用的是 64 位 Oracle Instant Client')
except Exception as e:
    print('❌ 无法加载 Oracle Client 或使用的是 32 位版本')
    print(e)