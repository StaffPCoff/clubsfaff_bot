import telepot, time, subprocess

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if (content_type == 'text'):
        command = msg['text']
        print ('Got command: %s' % command)

        if  '/0' in command:#В кавычках команда которую мы будем писать в телеграмм. 
                            #Можно и слова и по русски но начинать нужно именно с косой палочки
            p = subprocess.Popen(cmd0, shell=True)#А тут собственно выполняется команда которую
                            #мы задали для переменной "cmd0"
            bot.sendMessage(chat_id, "Комп не уйдёт в спящий режим")#А это ответ бота в чат.

        if  '/1' in command:
            p = subprocess.Popen(cmd1, shell=True)
            bot.sendMessage(chat_id, "Комп уйдёт в спящий режим через одну минуту простоя")

        if  '/off pc' in command:
            p = subprocess.Popen(shut, shell=True)
            bot.sendMessage(chat_id, "Выключаю комп")

        if  '/p' in command:
            p = subprocess.Popen(soundpc, shell=True)
            bot.sendMessage(chat_id, "Звук на столе")

        if  '/t' in command:
            p = subprocess.Popen(soundtv, shell=True)
            bot.sendMessage(chat_id, "Звук на телике")


bot = telepot.Bot('856784301:AAEaH0fKdlw3hXx4ioMaMP3-uQ8o40KfzbA')#Вместо иксов пишем ваш токен
cmd0 = 'Powercfg -setactive 54d30300-0b17-44ab-af1d-88d83b5cd0f2'
cmd1 = 'Powercfg -setactive 94c20331-c628-4ac0-9c31-6d8369cae53a'
shut = 'shutdown -s'
soundpc = 'C:\SSD_v3.exe\SSD.exe 7777hidden'
soundtv = 'C:\SSD_v3.exe\SSD.exe 7771hidden'

bot.message_loop(handle)

while 1:
    time.sleep(20)
