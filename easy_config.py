import os

#OS指令函数
def The_Comm(comm):

    temp_com = os.system(r"%s"%comm)
    if temp_com != 0:
        print(temp_com)

#一键执行Runserver
def The_runserver(ip,port):
    if ip == '' and port == '':
        print('ip,port为空，使用默认IP和端口：192.168.1.108：5678')
        ip = '192.168.1.108'
        port = '5678'
    The_Comm('python managy.py runserver %s：%s'%(ip,port))

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
    print(temp_commd)
    The_Comm(temp_commd)


#uwsgi运行设置
def The_uwsgi_player(def_path):
    the_dirct ={'1':['运行uwsgi!','ini','uwsgi_config2.ini'],'2':['重启uwsgi!','reload','uwsgi.pid'],'3':['停止uwsgi','stop','uwsgi.pid']}
    temp_chioce = The_dirct_outer(the_dirct)
    rec_comm = 'uwsgi --%s %s/uwsgi_Nginx/%s'%(the_dirct['%s'%temp_chioce[0]][1],The_server_check('',''),the_dirct['%s'%temp_chioce[0]][2])
    print(rec_comm)
    The_Comm(rec_comm)


#服务器识别
def The_server_check(One_comm,two_comm):
    Not_cloud = str(The_Comm('pwd'))
    if 'ubuntu' not in Not_cloud:
        print('检测为本地测试服')
        temp_dir = '~/myvirtualenvs/zzuilACG'
    else:
        print('检测为云服务器！')
        temp_dir = '~/zzuilACGN'
    if One_comm == '' and two_comm =='':
        rel_comm = temp_dir
    else:
        rel_comm = '%s %s/%s' % (One_comm,temp_dir,two_comm)

    return rel_comm

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
        com_str = str(input("输入ip[空格]port(选默认，直接回车)：")).split(' ')
        The_runserver(com_str[0],com_str[1])
    elif choice_num[0] == '3':
        The_uwsgi_player('')
    elif choice_num[0] == '4':
        The_CollecNginx_SLL()
if __name__ == '__main__':
    the_dirct = {
        '1':'更新Nginx.conf',
        '2':'运行RunServer测试服',
        '3':'uwsgi运行设置',
        '4':'Nginx_SSL操作',

    }
    The_Choice(the_dirct)
    print('Ojbk!操作完成！')