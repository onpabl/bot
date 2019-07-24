# -*- coding: utf-8 -*-
import command_class

task_list = [u'1',u'2',u'3',u'4',u'5',u'6',u'7',u'8',u'9',u'10',u'11',u'12',u'13',u'14',u'15',u'16',u'17',u'18',u'19',u'20',u'21',u'22',u'23',u'24',u'25',u'26',u'27']

def get(data,token,vk):
    text = data['body']
    #user_id = data['user_id']
    if text in task_list:
        message = u'Вот ссылка с папкой этого задания, там ты найдешь все, что сейчас есть\n ' + pages[text]

    else:
        message = u'Напиши номер задания, который хочешь закрепить'
    return message

def create():
    get_c = command_class.Command()
    get_c.keys = [u'1',u'2',u'3',u'4',u'5',u'6',u'7',u'8',u'9',u'10',u'11',u'12',u'13',u'14',u'15',u'16',u'17',u'18',u'19',u'20',u'21',u'22',u'23',u'24',u'25',u'26',u'27']
    get_c.description = u'Пришли любую цифру - получишь всё, что по нему есть'
    get_c.process = get
    command_class.command_list.append(get_c)


pages = {
    '1' : 'https://drive.google.com/open?id=1BLUgeltvTnYFI2JFEzNkkujgXLrx2lCS',
    '2' : 'https://drive.google.com/open?id=1P394uepqIp243wC5Tbg70swz2KFlP3x4',
    '3' : 'https://drive.google.com/open?id=1ZJyHmNRY2LybNCTknSTLqEns7HOzmIeg',
    '4' : 'https://drive.google.com/open?id=1RW9-_DHU8v5rhQFIP8K_j5gB70_4AF4f',
    '5' : 'https://drive.google.com/open?id=1Owmju42Fjwb7rPhQiCIEzNF7NqTnDQrf',
    '6' : 'https://drive.google.com/open?id=1eu6AE_k31Vk43oSjavwfsggC7mKRbX7f',
    '7' : 'https://drive.google.com/open?id=1KFT-sOa2Ywow680DBIFNvJzIc7GFXCB4',
    '8' : 'https://drive.google.com/open?id=1tXbR3b8MG4Oj3izLum3GwF6nojKXs4Wx',
    '9' : 'https://drive.google.com/open?id=1zED6jX268jP9v8AmK0WnITu_bspfP_PT',
    '10' : 'https://drive.google.com/open?id=1-loJKAZ-RQRiC_GQfVkO6KRGNSsDV8ne',
    '11' : 'https://drive.google.com/open?id=174hxtDxC73cyeXOu4pHZT5BqD6OHzzWQ',
    '12' : 'https://drive.google.com/open?id=16gneQKARYyDuui4Fbifm0xPU6-DzNCUq',
    '13' : 'https://drive.google.com/open?id=1Xt35dbUJ_B4BC8qCd6qztKLZb825yGZy',
    '14' : 'https://drive.google.com/open?id=1CtklG-aHlQzFxEceRLViEzliPHj_s7na',
    '15' : 'https://drive.google.com/open?id=1VmvCsKOT-ZoF_4Eou64PZIrxcGHcDTvi',
    '16' : 'https://drive.google.com/open?id=1Jwhfzh9IAHy8jFy-r4NW_fs3Q1VkHb4J',
    '17' : 'https://drive.google.com/open?id=1iHM5len5tusVbe0aJwCUOQywbwm7qaZO',
    '18' : 'https://drive.google.com/open?id=1n_6DlV4wsEdUQSE_OJg6RRYWBGdnw2NX',
    '19' : 'https://drive.google.com/open?id=1kxU60WfRsW0LOSyt6KRJDM2b_7zfQOd4',
    '20' : 'https://drive.google.com/open?id=11D-vLbxZbLWPBzRzuxmaDppqOppF6sJv',
    '21' : 'https://drive.google.com/open?id=1LLy_bpApPmFN5w049tdvcdMM5pQ71NOn',
    '22' : 'https://drive.google.com/open?id=1yfq-2Pnt8BqwSr6t0ydr3MTvLHBzg4gC',
    '23' : 'https://drive.google.com/open?id=1f9LjXQJNkdV0HAjcg-wV3fuhJf7n1X7w',
    '24' : 'https://drive.google.com/open?id=1X5IyK3kLeCQUgVg6jMVbs3j1rL5TwhQb',
    '25' : 'https://drive.google.com/open?id=1Lp2YRxPMkiDini89lEMIEGWDVVQQBVCt',
    '26' : 'https://drive.google.com/open?id=1Js6WRtjnRJkcdahGr6hPMO40Wtf6riXr',
    '27' : 'https://drive.google.com/open?id=1e_reWE_dfIQuRLryj6wdoVOyJcdmzPDJ'
    }
