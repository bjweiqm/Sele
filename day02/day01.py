#! /usr/bin/env python
#encoding:utf-8





#第一节作业；登录      密码错误三次   锁死
import getpass


def user_input(): #从文件中读取用户信息
    with file('log.txt', 'r+') as f:
        return f.readlines()

def resolve_list():#把从文件中读取的用户信息转换成 字典
    user_list = {}
    li = user_input()
    for l in li:
        data = l.strip()
        name = data.split(';')
        user_list[name[0]] = {'pwd':name[1],'id':int(name[2])}
    return user_list

def huanyuan(dic): #用户信息改变后，写入文件
    user = []
    for i in dic:
        li = ';'.join([i,dic[i]['pwd'],str(dic[i]['id'])+'\n'])
        user.append(li)

    with file('log.txt', 'w') as f:
        for li in user:
            f.write(li)

def is_user(): #判断用户名与密码是否正确
    li =  resolve_list()
    flag = True
    while flag:
        name = raw_input('username:')
        pwd = getpass.getpass('password:')

        if name not in li.keys():
            print 'naem error'
            continue
        else:
            if li[name]['id'] > 3:
                print 'lock'
                flag = False
            else:
                if pwd  == li[name]['pwd']:
                    print 'login ok'
                    break
                else:
                    li[name]['id'] += 1
                    huanyuan(li)




if __name__ == '__main__':
    is_user()
