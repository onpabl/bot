
from flask import Flask, request
import vk_api
import messHand
import sys
sys.path.insert(0, "mysite/commands")
import hello
import get_task
import info
from command_class import command_list

t = '7fbca9caed7f0de5b6d7962419bb7283e95e7d203613f6bdb203143c25994837e8553938cf187d7890829'
confirmation_code = '56725373'

hello.create()
get_task.create()
info.create()

app = Flask(__name__)
vk_session = vk_api.VkApi(token=t)
vk = vk_session.get_api()
@app.route('/', methods=['POST'])
def processing():
    data = request.get_json(force=True, silent=True)
    if 'type' not in data.keys():
        return 'not vk'
    if data['type'] == 'confirmation':
        return '56725373'
    elif data['type'] == 'message_new':
        messHand.create_answer(data['object'], t,vk)
        return 'ok'
