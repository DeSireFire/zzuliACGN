import os,time
#OS指令函数
def The_Comm(comm):

    # temp_com = os.system(r"%s"%comm)
    temp_com = os.popen(r"%s"%comm).read()
    return temp_com

#一键执行Runserver
def The_runserver():
    print('ip,port为空，使用默认IP和端口：192.168.1.108：5678')
    ip = '192.168.1.108'
    port = '5678'
    temp_path = The_server_check('python', 'manage.py runserver')
    print(The_Comm('%s %s:%s' % (temp_path, ip, port)))




#一键执行更新Nginx_Config
def The_CollecNginx_Config(def_path):
    if def_path == '':
        print('def_path为空，使用默认路径来执行！')
        def_path = 'uwsgi_Nginx/nginx.conf /etc/nginx/nginx.conf'
    one_comm = 'sudo cp'
    The_Comm(The_server_check(one_comm,def_path))

#一键执行Nginx_SSL操作
def The_CollecNginx_SLL():
    the_dirct = {'1': ['提取SSL到项目', 'sudo cp -r /etc/nginx/ssl/', ''],
                 '2': ['从项目更新SSL', 'sudo cp -r', 'ssl/ /etc/nginx/'],
                 '3': ['备份SSL文件', 'sudo cp -r /etc/nginx/ssl/', 'ssl/ssl_back/'],
                 '9': ['查找SSL文件是否存在', 'ls', '/etc/nginx/ssl/']
                 }
    temp_chioce = The_dirct_outer(the_dirct)
    if temp_chioce[0] in '123':
        temp_commd = The_server_check(the_dirct[temp_chioce[0]][1],the_dirct[temp_chioce[0]][2])
    else:
        temp_commd = '%s %s'%(the_dirct[temp_chioce[0]][1],the_dirct[temp_chioce[0]][2])
    print(The_Comm(temp_commd))

#一键执行Nginx运行操作
def The_CollecNginx_player():
    the_dirct = {'1': ['运行Nginx', 'sudo /usr/sbin/nginx',],
                 '2': ['停止Nginx', 'sudo /usr/sbin/nginx -s stop',],
                 '3': ['重启Nginx', 'sudo /usr/sbin/nginx -s reload',],
                 '9': ['查看Nginx日志', 'cat /var/log/nginx/access.log']
                 }
    temp_chioce = The_dirct_outer(the_dirct)
    temp_commd = the_dirct[temp_chioce[0]][1]
    print(The_Comm(temp_commd))

#uwsgi运行设置
def The_uwsgi_player(def_path):
    the_dirct ={
        '1':['运行uwsgi!','ini','uwsgi_config.ini'],
        '2':['重启uwsgi!','reload','uwsgi.pid'],
        '3':['停止uwsgi','stop','uwsgi.pid'],
        '4':['查看uwsgi状态','ps -aux | grep uwsgi'],
        '5':['强行终止uwsgi','kill all uwsgi'],
        '6':['查看uwsgi日志','cat uwsgi_Nginx/uwsgi.log'],
        '7':['查看uwsgi文件列表','ls uwsgi_Nginx/'],
        '8':['运行测试test','ini','uwsgi_config_test.ini'],
        '9':['关闭测试test','stop','uwsgi.pid'],
    }
    temp_chioce = The_dirct_outer(the_dirct)
    if temp_chioce[0] in '12378':
        rec_comm = 'uwsgi --%s %s/uwsgi_Nginx/%s'%(the_dirct['%s'%temp_chioce[0]][1],The_server_check('',''),the_dirct['%s'%temp_chioce[0]][2])
        print(rec_comm)
        The_Comm(rec_comm)
    elif temp_chioce[0] in 6:
        The_logReader(the_dirct[temp_chioce[0]][1])
    else:
        print(The_Comm(the_dirct[temp_chioce[0]][1]))

#Django指令
def The_DjangoCommod():
    print('注意该脚本必须与manage.py放于同目录')
    the_dirct = {
        '1': ['创建app', 'django-admin startproject ',],
        '2': ['一键migrations', 'python manage.py makemigrations',],
        '3': ['一键migrate', 'python manage.py migrate',],
                 }
    temp_chioce = The_dirct_outer(the_dirct)
    if temp_chioce[0] in '1':
        print('操作 = %s'%temp_chioce[0])
        com_str = str(input("请输入需要的参数(无，直接回车)："))
        temp_comm = '%s%s'%(the_dirct[temp_chioce[0]][1],com_str)
        print('执行：%s'%temp_comm)
    else:
        print('操作 = %s' % the_dirct[temp_chioce[0]][1])
        temp_comm = the_dirct[temp_chioce[0]][1]

    # The_Comm(temp_comm)

#一键收集静态文件
def The_collectstatic():
    com_str = ['sudo chmod -R 777 /var/www/','python manage.py collectstatic','sudo chmod -R 740 /var/www/']
    for i in com_str:
        The_Comm(i)

def test():
    com_str = str(input("def_path(选默认，直接回车)："))
    a = The_Comm(com_str)
    print(type(a))
    print(a)

#服务器识别
def The_server_check(One_comm,two_comm):
    Not_cloud = str(The_Comm('pwd'))
    if 'ruanqing' in Not_cloud:
        print('检测为本地测试服')
        temp_dir = '~/myvirtualenvs/zzuliACGN'
    else:
        print('检测为云服务器！')
        temp_dir = '~/zzuliACGN'

    if One_comm == '' and two_comm =='':
        rel_comm = temp_dir
    else:
        rel_comm = '%s %s/%s' % (One_comm,temp_dir,two_comm)

    return rel_comm

#日志刷新器
def The_logReader(log_path):
    pass
    while True:
        temp_comm = 'cat %s'%(log_path)
        The_Comm(temp_comm)
        time.sleep(50)

#选项遍历器
def The_dirct_outer(temp_dirct):
    for key in sorted(temp_dirct.items()):
        print('%s:%s' % (key[0], key[1]))
    com_list = str(input("OS指令(例如：1)：")).split(' ')
    return com_list

#选择函数
def The_Choice(the_dirct):
    choice_num=The_dirct_outer(the_dirct)
    if choice_num[0] == '1':
        com_str = str(input("def_path(选默认，直接回车)："))
        The_CollecNginx_Config('')
    elif choice_num[0] == '2':
        The_runserver()
    elif choice_num[0] == '3':
        The_uwsgi_player('')
    elif choice_num[0] == '4':
        The_CollecNginx_SLL()
    elif choice_num[0] == '5':
        The_CollecNginx_player()
    elif choice_num[0] == '6':
        The_collectstatic()
    elif choice_num[0] == '7':
        The_DjangoCommod()

if __name__ == '__main__':
    the_dirct = {
        '1':'更新Nginx.conf',
        '2':'运行RunServer测试服',
        '3':'uwsgi运行设置',
        '4':'Nginx_SSL操作',
        '5':'Nginx运行操作',
        '6':'部署静态文件',
        '7':'Django指令',

    }
    The_Choice(the_dirct)
    print('Ojbk!操作完成！')