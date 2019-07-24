# -*- coding: utf-8 -*-
import command_class
#import get_task
def info(data,token,vk):
    message =''
    for c in command_class.command_list[::2]:
       message = message + u'\n"' + c.keys[0] + u'". Описание: ' + c.description
    return message


def create():
    inf = command_class.Command()
    inf.keys = [u'help', u'помощь', u'помоги']
    inf.description = u'Помогу'
    inf.process = info
    command_class.command_list.append(inf)
