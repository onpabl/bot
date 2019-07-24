# -*- coding: utf-8 -*-
from command_class import command_list



def get_answer(data,token,vk):
    message = "Прости, не понимаю тебя. Напиши 'помощь', чтобы узнать мои команды"
    body = data['body'].lower()
    for c in command_list:
       if body in c.keys:
           message = c.process(data,token,vk)
    return message


def create_answer(data, token,vk):
    user_id = data['user_id']
    message= get_answer(data,token,vk)
    vk.messages.send(
        message=message,
        random_id=0,
        peer_id=user_id,
        )
    return 'ok'
