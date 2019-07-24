# -*- coding: utf-8 -*-
import command_class

def hello(body,token,vk):
    message = 'Привет! Я бот-ЕГЭ(информатика). Помогу тебе в тренировке заданий. Напиши номер задания, который хочешь закрепить'
    return message

def create():
    hello_c = command_class.Command()
    hello_c.keys = [u'привет',u'здравствуй',u'ку',u'хай',u'дарова', u'hi',u'здрасте', u'здравствуйте']
    hello_c.description =u'Приветствие'
    hello_c.process = hello
    command_class.command_list.append(hello_c)
    return
