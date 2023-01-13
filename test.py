import speech_recognition as sr
import webbrowser as wb
r = sr.Recognizer()

def listen():
    text = ''
    with sr.Microphone() as source:
        print('Я вас слушаю: ')
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            text = (r.recognize_google(audio, Language='ru-RU')).lower()
        except:
            pass
        print(f'Вы сказали: {text}')
        return(text)

def exe(task):
    mas = ['попугай', 'папуг', 'папугай', 'попуг', 'бот']
    keys = ('найди', 'найти', 'найди в интрнете', 'ищи')
    for i in mas:
        task = task.replace(i, '')
        task = task.replace('  ', ' ')
    task = task.strip()

    for i in keys:
        if i in task:
            zaproc = task.replace(i, '')
            zaproc = zaproc.strip()
            task = 'найди'

    if task == 'найди':
        wb.open(f'https://www.google.com/search?q={zaproc}&oq=%{zaproc}%81&aqs=chrome..69i57j69i59j35i39j46i512j0i512l6.1422j0j1&sourceid=chrome&ie=UTF-8')

while True:
    exe(listen())


