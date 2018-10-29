import MySQLdb,sys,time
from zzuliACGN.settings import DATABASES

connect_dict = {
    "host":DATABASES["default"]["HOST"],
    "port":int(DATABASES["default"]["PORT"]),
    "user":DATABASES["default"]["USER"],
    "passwd":DATABASES["default"]["PASSWORD"],
    "db":DATABASES["default"]["NAME"],
}

# 需要插入的数据

insert_dict = {
    'novel_id':'',
    'novel_name':'',
    'novel_intro':'',
    'novel_headerImage':'',
    'novel_worksNum':'',
    'novel_saveTime':'',
    'novel_updateTime':'',
    'novel_types_id':'',
    'novel_writer_id':'',
}

# 创建连接对象
def connect(connect_dict):
    try:
        # 创建连接对象
        conn = MySQLdb.connect(
            # host=connect_dict["HOST"],
            # port=connect_dict["PORT"],
            # user=connect_dict["USER"],
            # passwd=connect_dict["PASSWORD"],
            # db=connect_dict["NAME"],
            host=DATABASES["default"]["HOST"],
            port= int(DATABASES["default"]["PORT"]),
            user= DATABASES["default"]["USER"],
            passwd= DATABASES["default"]["PASSWORD"],
            db= DATABASES["default"]["NAME"],
        )
        return conn
    except Exception as e:
        print("FTP登陆失败，请检查主机号、用户名、密码是否正确:%s"%e)
        sys.exit(0)

# 关闭数据库
def mysql_close(connect):
    connect.close()

# 查询数据库版本
def mysql_version(connect):
    cur = connect.cursor()
    cur.execute("SELECT VERSION()")
    # 使用 fetchone() 方法获取一条数据
    data = cur.fetchone()
    print(data)


# 查询数据库中所有表名
def tables(connect, db_name='zzuli_ACGN'):
    """

    :param connect: 连接对象
    :param db_name: 数据库名
    :return: 返回嵌套的元组
    """

    try:
        # 使用cursor()方法获取操作游标
        cur = connect.cursor()
        # 使用execute方法执行SQL语句
        cur.execute("select table_name from information_schema.TABLES where TABLE_SCHEMA=%s;" % (db_name))
        # 使用 fetchone() 方法获取所有数据
        data = cur.fetchall()
        for i in data:
            print(i[0])
        return data
    except Exception as e:
        print("查询数据库中所有表名发生错误:%s"%e)

# 查询指定数据库中指定表的所有字段名column_name
def column_name(connect,db_name = 'zzuli_ACGN',table_name = 'ZA_Novel_novel_info'):
    """

    :param connect: 连接对象
    :param db_name: 数据库名
    :param table_name: 表名
    :return: 返回嵌套的元组
    """

    try:
        # 使用cursor()方法获取操作游标
        cur = connect.cursor()
        cur.execute(
            "select column_name from information_schema.columns where table_schema=%s and table_name=%s;"%(db_name,table_name)
        )
        data = cur.fetchall()
        for i in data:
            print(i[0])
        return data
    except Exception as e:
        print("查询指定数据库中指定表的所有字段名时发生错误:%s"%e)

# 插入数据
def insert_into(connect,table_name,data):
    # 使用cursor()方法获取操作游标
    cursor = connect.cursor()
    mykeys = ",".join(data.keys())
    myvalues = ",".join(['%s']*len(data))
    sql = "INSERT INTO{table}({keys) VALUES ({values})".format(table=table_name,keys=mykeys,values=myvalues)
    try:
        if cursor.execute(sql,tuple(data.values())):
            print("中出成功！")
            connect.commit()
    except Exception as e:
        print("插入数据时发生错误:%s"%e)
        connect.rollback()

# 批量插入executemany
def insert_by_many(connect,table_name,data):
    # 使用cursor()方法获取操作游标
    cursor = connect.cursor()
    mykeys = ",".join(data.keys())
    myvalues = ",".join(['%s'] * len(data))
    sql = "INSERT INTO{table}({keys) VALUES ({values})".format(table=table_name, keys=mykeys, values=myvalues)
    try:
        if cursor.executemany(sql, tuple(data.values())):
            print("批量中出成功！")
    except Exception as e:
        print("批量插入executemany 时发生错误:%s" % e)
        connect.rollback()

# 数据提交
def sql_commit(connect):
    connect.commit()

# 更新数据
def sql_update(connect,table_name,data):
    # 使用cursor()方法获取操作游标
    cursor = connect.cursor()
    mykeys = ",".join(data.keys())
    myvalues = ",".join(['%s'] * len(data))
    sql = "INSERT INTO{table}({keys) VALUES ({values}) ON DUPLICATE KEY UPDATE".format(table=table_name, keys=mykeys, values=myvalues)
    myUpdate = ",".join([" {key} = %s".format(key=key) for key in data])
    sql += myUpdate
    try:
        if cursor.executemany(sql, tuple(data.values())):
            print("批量中出成功！")
    except Exception as e:
        print("更新数据时发生错误:%s"%e)

print(connect_dict)
time.sleep(100)
conn = connect(connect_dict)
cur = conn.cursor()
table = "students"

# try:
#     # 使用cursor()方法获取操作游标
#     cursor = connect.cursor()
#     return data
# except Exception as e:
#     print("插入数据 时发生错误:%s"%e)
conn.close()