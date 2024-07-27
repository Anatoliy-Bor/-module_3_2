import re
def domain(a):       # создаем функцию с одним аргементом для проверки домена и символа @
    list_domain = ['.com', '.ru', '.net', '@']          # создаёмсписок доменов
    d = a.find('@')                                     # проверяем нааличие символа @ встроке
    result = re.findall(r'.\S+(\W\w+)', a)      # при помощи регулярных выражений получаем домен
    if d != -1:                     # если @ присутствует встроке то спомощь цикла проверяем наличие домена
        for i in list_domain:       # сли и @ и домены проверены, функция возвращает 1 , иначе 0 и принтует
            if result[0] != i:
                continue
            if result[0] == i:
                return 1
        else:
            print('В адрессе : ', a , ' Неправильный домен' , result[0])
            return 0
    else:
        print('В адрессе ', a, ' отсутствует символа @ ')
        return 0

def send_email(message, recipient, sender="university.help@gmail.com"): # получает аргументы по запросу
    a = domain(recipient) # вызываем проверку адресса
    b = domain(sender)

    if a + b != 2:  # если проверка прошла удачно , то продолжаем далее по условию
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print(f" Письмо успешно отправлено с адреса {sender} на адрес {recipient} .")
    else:
        print(f" НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес{recipient} .")


# send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
# send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender ='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
#send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')