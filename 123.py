import requests
import itchat
KEY = 'xxxxxxxxxxxxxxxxxxxxx' #图灵机器人的KEY

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
@itchat.msg_register(itchat.content.TEXT)

def tuling_reply(msg):
    
    reply = get_reply(msg['Text'])
    return reply 

itchat.auto_login(hotReload=True)
itchat.run()