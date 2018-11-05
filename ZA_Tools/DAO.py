import MySQLdb,sys,datetime
from zzuliACGN.settings import DATABASES

connect_dict = {
    "host":DATABASES["default"]["HOST"],
    "port":int(DATABASES["default"]["PORT"]),
    "user":DATABASES["default"]["USER"],
    "passwd":DATABASES["default"]["PASSWORD"],
    "db":DATABASES["default"]["NAME"],
}


# 创建连接对象
def connect(connect_dict):
    """

    :param connect_dict: 传入连接数据库的必要信息
    :return: 返回连接对象
    """
    try:
        # 创建连接对象
        conn = MySQLdb.connect(
            host=connect_dict["host"],
            port=connect_dict["port"],
            user=connect_dict["user"],
            passwd=connect_dict["passwd"],
            db=connect_dict["db"],
            # host=DATABASES["default"]["HOST"],
            # # port= int(DATABASES["default"]["PORT"]),
            # user= DATABASES["default"]["USER"],
            # passwd= DATABASES["default"]["PASSWORD"],
            # db= DATABASES["default"]["NAME"],
        )
        conn.set_character_set('utf8')
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
def tables_list(connect, db_name='zzuli_ACGN'):
    """

    :param connect: 连接对象
    :param db_name: 数据库名
    :return: 返回嵌套的元组
    """

    try:
        # 使用cursor()方法获取操作游标
        cur = connect.cursor()
        # 使用execute方法执行SQL语句
        cur.execute("SELECT TABLE_NAME,TABLE_ROWS FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA='%s';" % (db_name))
        # 使用 fetchone() 方法获取所有数据
        data = cur.fetchall()
        for i in data:
            print(i[0])
        return data
    except Exception as e:
        print("查询数据库中所有表名 时发生错误:%s"%e)

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
            "select column_name from information_schema.columns where table_schema='%s' and table_name='%s';"%(db_name,table_name)

        )
        data = cur.fetchall()
        for i in data:
            print(i[0])
        return data
    except Exception as e:
        print("查询指定数据库中指定表的所有字段名 时发生错误:%s"%e)

# 插入数据
def insert_into(connect,table_name,data):
    """

    :param connect: 连接对象
    :param table_name: 表名
    :param data: 要插入的数据，传入字典
    :return:
    """
    # 使用cursor()方法获取操作游标
    cursor = connect.cursor()
    print(data.keys())
    mykeys = ",".join(data.keys())
    myvalues = ",".join(['%s']*len(data))
    sql = "INSERT INTO {table}({keys}) VALUES ({values})".format(table=table_name,keys=mykeys,values=myvalues)
    print(sql)

    try:
        if cursor.execute(sql,tuple(data.values())):
            print("中出成功！")
            connect.commit()
    except Exception as e:
        print("插入数据 时发生错误:%s"%e)
        connect.rollback()

# 批量插入executemany
def insert_by_many(connect,table_name,data):
    # 使用cursor()方法获取操作游标
    cursor = connect.cursor()
    mykeys = ",".join([x[0] for x in column_name(connect,table_name = table_name)[1:]])
    myvalues = ",".join(['%s'] * len([x[0] for x in column_name(connect,table_name = table_name)[1:]]))
    sql = "INSERT INTO {table} ({keys}) VALUES({values})".format(table=table_name, keys=mykeys, values=myvalues)

    try:
        if cursor.executemany(sql, data):
            print("批量中出成功！")
            connect.commit()
    except Exception as e:
        print("批量插入executemany 时发生错误:%s" % e)
        connect.rollback()


# 忽略以存在数据插入
def insert_IGNORE(connect, table_name, data):
    """

    :param connect: 连接对象
    :param table_name: 表名
    :param data: 要插入的数据，传入字典
    :return:
    """
    # 使用cursor()方法获取操作游标
    cursor = connect.cursor()
    mykeys = ",".join(data.keys())
    myvalues = ",".join(['%s'] * len(data))
    sql = "INSERT IGNORE INTO {table}({keys}) VALUES ({values})".format(table=table_name, keys=mykeys, values=myvalues)
    try:
        if cursor.execute(sql, tuple(data.values())):
            print("忽略中出成功！")
            connect.commit()
    except Exception as e:
        print("忽略以存在数据插入 时发生错误:%s" % e)
        connect.rollback()

# 替换方式数据插入
def replace_INTO(connect, table_name, data):
    """

    :param connect: 连接对象
    :param table_name: 表名
    :param data: 要插入的数据，传入字典
    :return:
    """
    # 使用cursor()方法获取操作游标
    cursor = connect.cursor()
    mykeys = ",".join(data.keys())
    myvalues = ",".join(['%s'] * len(data))
    sql = "REPLACE  INTO {table}({keys}) VALUES ({values})".format(table=table_name, keys=mykeys, values=myvalues)
    # sql = "INSERT IGNORE INTO {table}({keys}) VALUES ({values})".format(table=table_name, keys=mykeys, values=myvalues)
    try:
        if cursor.execute(sql, tuple(data.values())):
            print("替换插入成功！")
            connect.commit()
    except Exception as e:
        print("忽略以存在数据插入 时发生错误:%s" % e)
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
    myUpdate = ",".join([" {key} = %s".format(key=key) for key in data])
    sql = "INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE".format(table=table_name, keys=mykeys, values=myvalues)
    sql += myUpdate

    try:
        if cursor.execute(sql, tuple(data.values())*2):
            print("更新成功！")
            connect.commit()
    except Exception as e:
        print("更新数据 时发生错误:%s"%e)

# 删除数据
def delete(connect,table_name,conditon):
    """

    :param connect: 连接对象
    :param table_name: 表名
    :param conditon: 删除条件多样，直接将其当作字符串来床底，以实现删除操作（例如：“age > 20"）
    :return:
    """
    # 使用cursor()方法获取操作游标
    cursor = connect.cursor()
    sql = "DELETE FROM {table} WHERE {conditon}".format(table=table_name,conditon=conditon)
    print(sql)
    try:
        cursor.execute(sql)
        connect.commit()
    except Exception as e:
        print("插入数据 时发生错误:%s"%e)

# 查询数据
def demand(connect,table_name,conditon):
    # 使用cursor()方法获取操作游标
    cursor = connect.cursor()
    sql = "SELECT * FROM {table} WHERE {conditon}".format(table=table_name,conditon=conditon)
    try:
        cursor.execute(sql)
        print("查询到数量: %s 条"%(cursor.rowcount))
        row = cursor.fetchone()
        while row:
            print("row:",row)
            row = cursor.fetchone()
    except Exception as e:
        print("查询数据 时发生错误:%s"%e)

# 删除表数据并重置ID
def Refresh_ID(connect,table_name):
    """

    :param connect: 连接对象
    :param table_name: 表名
    :return:
    """
    # 使用cursor()方法获取操作游标
    cursor = connect.cursor()
    sql1 = "DELETE FROM {table}".format(table=table_name)
    sql2 = "ALTER TABLE {table} AUTO_INCREMENT = 1;".format(table=table_name)
    try:
        cursor.execute(sql1)
        cursor.execute(sql2)
        connect.commit()
    except Exception as e:
        print("删除表数据并重置ID 时发生错误:%s"%e)

# 测试用主函数
def main():
    # 建立连接
    db = connect(connect_dict)
    try:
        # 需要插入的数据

        insert_dict = {
            # 'novel_id': '1',
            # 'novel_name': 'test',
            # 'novel_intro': 'test',
            # 'novel_headerImage': 'test',
            # 'novel_worksNum': '233',
            # 'novel_saveTime': datetime.date.today(),
            # 'novel_updateTime': datetime.date.today(),
            # 'novel_types_id': '1',
            # 'novel_writer_id': '1',
            "id":6,
            "Type_title":"test666",
            "isDelete":"0",

        }
        tables_list(db)
        print("*"*50)
        column_name(db,table_name="ZA_Novel_type")
        print("*" * 50)
        # 单条插入
        # insert_into(db, "ZA_Novel_type", insert_dict)
        print("*" * 50)
        # 批量插入
        newlist = []
        typelist = ["玄幻","奇幻","武侠","仙侠","都市","现实","军事","历史","游戏","体育","科幻","灵异","女生","轻小说",]
        for i in typelist:
            temp = (i,0)
            newlist.append(temp)
        print(newlist)
        insert_by_many(db,"ZA_Novel_type",newlist)
        print("*" * 50)
        # 忽略以存在数据插入
        # insert_IGNORE(db,"ZA_Novel_type", insert_dict)
        print("*" * 50)
        # 以替换数据插入
        # replace_INTO(db,"ZA_Novel_type", insert_dict)
        print("*" * 50)
        # 数据更新
        # insert_dict = {
        #     "id": 7,
        #     "Type_title":"test666",
        #     "isDelete":"0",
        # }
        # sql_update(db,"ZA_Novel_type", insert_dict)
        # print("*" * 50)
        # # 数据删除
        # conditon = "Type_title  = 'test'"
        # # conditon = "REGEXP '^test';"
        # delete(db,"ZA_Novel_type", conditon)
        # print("*" * 50)
        # # 查询数据
        # conditon = "Type_title REGEXP '^test'"
        # demand(db,"ZA_Novel_type", conditon)
        print("*" * 50)
        # # 删除表数据并重置ID
        # Refresh_ID(db, "ZA_Novel_type")

    except Exception as e:
        print("总函数 时发生错误:%s"%e)
    finally:
        db.close()

if __name__ == '__main__':
    main()


# try:
#     # 使用cursor()方法获取操作游标
#     cursor = connect.cursor()
#     cursor.execute()
# except Exception as e:
#     print("插入数据 时发生错误:%s"%e)
