#
import itchat
import requests
import pymysql


KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxx'

conn = pymysql.connect(host='数据库的IP', port=3306, user='数据库账户', passwd='数据库密码', db='数据库的表', charset='utf8')
cursor = conn.cursor()
@itchat.msg_register(itchat.content.TEXT)
def wechat_reply(msg):
    UserName = msg['FromUserName']
    Insert_sql = """INSERT INTO wechat_reply(wechat_friend,friend_state) VALUES ('%s',1)"""  % (UserName)

    Select_sql = "SELECT * FROM wechat_reply WHERE wechat_friend = '%s'" % (UserName)

    Update_sql = "UPDATE wechat_reply SET friend_state = 0 WHERE wechat_friend = '%s'" % (UserName)

    if msg['Text'] == 'TD' or msg['Text'] == 'td':
        cursor.execute(Update_sql)
        conn.commit()
        return '自动回复已关闭，也可以把它再打开，输入启动即可'

    if msg['Text'] == '启动':
        cursor.execute("UPDATE wechat_reply SET friend_state = 1 WHERE wechat_friend = '%s'" % (UserName))
        conn.commit()
        return '自动回复已开启'

    try:
        cursor.execute(Select_sql)
        results = cursor.fetchone()
        if results[2] is 1:
            talk = get_reply(msg['Text'])
            return talk
    except:
        if results == None:
            cursor.execute(Insert_sql)
            conn.commit()
            return '您好我有事不在,我是3号,有什么事情可以先告我。如果不需要回复TD即可'

def get_reply(msg):
    URL = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'   : KEY,
        'info'  : msg,
        'userid': 'xxx',
    }
    try:
        r = requests.post(URL, data=data).json()
        return r.get('text')
    except:
        return

def main():
    wechat_reply()
    itchat.auto_login(hotReload=False)                                                                                                                                       
    itchat.run()
if __name__ == '__main__':
    main()
    

