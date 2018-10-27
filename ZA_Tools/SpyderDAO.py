import MySQLdb
from zzuliACGN.settings import DATABASES
# 创建连接对象
conn= MySQLdb.connect(
    host = DATABASES["default"]["HOST"],
    port = int(DATABASES["default"]["PORT"]),
    user = DATABASES["default"]["USER"],
    passwd = DATABASES["default"]["PASSWORD"],
    db = DATABASES["default"]["NAME"],
    )
# 使用cursor()方法获取操作游标
cur = conn.cursor()

# 使用execute方法执行SQL语句
# cur.execute("SELECT VERSION()")
cur.execute("select table_name from information_schema.TABLES where TABLE_SCHEMA='zzuli_ACGN';")

# 使用 fetchone() 方法获取一条数据
# data = cur.fetchone()

# 使用 fetchone() 方法获取所有数据
data = cur.fetchall()


print(type(data))
print(len(data))
print(data)


# 关闭数据库
conn.close()