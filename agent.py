from telethon import TelegramClient, events, sync
import time
import datetime
import re
import schedule
import random

api_id = 1009331
api_hash = "ecaae8b20d23e51145562db3ba8de0a0"
client = TelegramClient('session_name', api_id, api_hash)

client.start()

while True:
    try:
        def check_feel():
            client.send_message(-325042930, "Моя жаба")
            time.sleep(0.5)
            myfrog = client.get_messages(-325042930)
            print(myfrog[0].message)
            if re.search("Нуждается", myfrog[0].message.split("\n")[4]):
                client.send_message(-325042930, "Мой инвентарь")
                time.sleep(1)
                inv = client.get_messages(-325042930)
                if re.search("0", inv[0].message.split("\n")[2]):
                    client.send_message(-325042930, "Жаба инфо")
                    time.sleep(1)
                    info = client.get_messages(-325042930)
                    if re.search("можно покормить", info[0].message.split("\n")[0]) and not re.search("через", info[0].message.split("\n")[0]):
                        if int(myfrog[0].message.split("\n")[5].split(": ")[1]) >= 1500:
                            client.send_message(-325042930, "Откормить жабу")
                        else:
                            client.send_message(-325042930, "Покормить жабу")
                    client.send_message(-325042930, "Моя жаба")
                    time.sleep(1)
                    myfrog = client.get_messages(-325042930)
                    if int(myfrog[0].message.split("\n")[5].split(": ")[1]) >= 1500 and re.search("Нуждается", myfrog[0].message.split("\n")[4]):
                        client.send_message(-325042930, "Ребят, ни у кого нет аптечки?")
                        time.sleep(60)
                        client.send_message(-325042930, "Мой инвентарь")
                        time.sleep(1)
                        inv = client.get_messages(-325042930)
                        if re.search("0", inv[0].message.split("\n")[2]):
                            client.send_message(-325042930, "@sedukh, в течение 60 секунд можно отменить покупку аптечки")
                            time.sleep(60)
                            client.send_message(-325042930, "Приобрести аптечку")
                            client.send_message(-325042930, "Реанимировать жабу")
                        else:
                            client.send_message(-325042930, "Спасибо")
                            client.send_message(-325042930, "Реанимировать жабу")
                    else:
                        client.send_message(-325042930, "Ребят, ни у кого нет аптечки?")
                        time.sleep(60)
                        client.send_message(-325042930, "Мой инвентарь")
                        time.sleep(1)
                        inv = client.get_messages(-325042930)
                        if not re.search("0", inv[0].message.split("\n")[2]):
                            client.send_message(-325042930, "Спасибо")
                            client.send_message(-325042930, "Реанимировать жабу")
                else:
                    client.send_message(-325042930, "Жаба инфо")
                    time.sleep(1)
                    info = client.get_messages(-325042930)
                    if re.search("можно покормить", info[0].message.split("\n")[0]) and not re.search("через", info[0].message.split("\n")[0]):
                        if int(myfrog[0].message.split("\n")[5].split(": ")[1]) >= 1500:
                            client.send_message(-325042930, "Откормить жабу")
                        else:
                            client.send_message(-325042930, "Покормить жабу")
                    else:
                        client.send_message(-325042930, "Реанимировать жабу")
        def deeds():
            if (datetime.datetime.now().hour > 9 and datetime.datetime.now().hour < 20) and random.randint(0, 100) + (datetime.datetime.now().hour / 2) > 60:
                client.send_message(-325042930, "Начать клановую войну")
            client.send_message(-325042930, "Жаба инфо")
            time.sleep(1)
            info = client.get_messages(-325042930)
            client.send_message(-325042930, "Моя жаба")
            time.sleep(1)
            myfrog = client.get_messages(-325042930)
            if re.search("Можно забрать жабу", info[0].message.split("\n")[2]):
                client.send_message(-325042930, "Завершить работу")
                time.sleep(0.5)
                worksuc = client.get_messages(-325042930)
                if re.search("КАПЕЦ", worksuc[0].message):
                    check_feel()
            client.send_message(-325042930, "Жаба инфо")
            time.sleep(1)
            info = client.get_messages(-325042930)
            if not re.search("Забрать жабу можно", info[0].message.split("\n")[2]):
                print(myfrog[0])
                if int(myfrog[0].message.split("\n")[5].split(": ")[1]) >= 1700:
                    client.send_message(-325042930, "Отправиться в золотое подземелье")
                elif int(myfrog[0].message.split("\n")[5].split(": ")[1]) >= 1200:
                    client.send_message(-325042930, "@sedukh, можно отправиться в серебряное подземелье")
                elif int(myfrog[0].message.split("\n")[5].split(": ")[1]) >= 700:
                    client.send_message(-325042930, "@sedukh, можно отправиться в бронзовое подземелье")

        def food():
            client.send_message(-325042930, "Жаба инфо")
            time.sleep(1)
            info = client.get_messages(-325042930)
            client.send_message(-325042930, "Моя жаба")
            time.sleep(1)
            myfrog = client.get_messages(-325042930)
            if re.search("можно \w\wкормить", info[0].message.split("\n")[0]) and not re.search("через", info[0].message.split("\n")[0]):
                if int(myfrog[0].message.split("\n")[5].split(": ")[1]) >= 1500:
                    client.send_message(-325042930, "Откормить жабу")
                else:
                    client.send_message(-325042930, "Покормить жабу")

        def work():
            client.send_message(-325042930, "Жаба инфо")
            time.sleep(1)
            info = client.get_messages(-325042930)
            if re.search("Жабу можно отправить", info[0].message.split("\n")[2]):
                client.send_message(-325042930, "Отправить жабу на работу")
        schedule.every(360).minutes.do(work)
        schedule.every(240).minutes.do(food)
        schedule.every(120).minutes.do(deeds)
        schedule.every(121).minutes.do(check_feel)
        while True:
            schedule.run_pending()
            time.sleep(60)
    except IndexError:
        print("error")
