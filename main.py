# Преамбула
#%matplotlib inline

import requests
from bs4 import BeautifulSoup as Bs
import smtplib
import time
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

# класс с методами по проверке текущей ситуации
class Currency:

    # переменная для текущих данных
    currentData = None
    # переменная для данных из файла предназначенная для сравнения
    fileData = None

    # геттер для текущих данных
    def get_currData(self):
        return self.currentData

    # геттер для всех данных из файла
    def get_fileData(self):
        f = open('data.txt', 'r')
        temp = f.readlines()
        f.close()
        return temp

    # геттер для последних данных из файла
    def get_fileLastData(self):
        f = open('data.txt', 'r')
        temp = f.readlines()[-1]
        f.close()
        return temp.split()

    # геттер для предпоследних данных из файла
    def get_filePreLastData(self):
        f = open('data.txt', 'r')
        temp = f.readlines()[-2]
        f.close()
        return temp.split()

    # конструктор класса (даже не знаю почему и зачем именно такой)
    def __init__(self, justInCase):
        self.justInCase = justInCase

    # метод, предназначенный для парсинга веб-страницы, для получения определенных данных
    def get_currency(self):
        # ссылка на сайт
        # currency_url = '''https://стопкоронавирус.рф'''
        currency_url = '''https://стопкоронавирус.рф/information/'''

        # user-agent для совершения запроса как пользователь, а не как бот (для обхода капч (предназначенно самой
        # библеотекой requests))
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/80.0.3987.149 Safari/537.36'
        }

        # переменная для html-кода всех веб страницы
        full_page = requests.get(currency_url, headers=headers)
        # парсим веб страницу
        soup = Bs(full_page.content, 'html.parser')

        # производим поиск, выцеживаем интересующие нас данные (актуально только для текущего сайта, и на момент
        # разработки и на ближайшее время)
        # currentData = soup.find_all('div', {'class': 'cv-countdown__item-value'}, 'span')
        currentData = soup.find_all('cv-stats-virus__item-additional-number') 

        # возвращаем текущие данные
        return currentData

    # метод для отправки электронного письма
    def send_mail(self, text):

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        # указываем уникальный пароль веб приложения
        server.login('lesh77906@gmail.com', 'pcfatrhicdocqken')
        # тема письма
        subject = 'Coronavirus Currency Alert'
        # текст письма, его мы получаем в виде аргумента метода при вызове
        body = text
        message = f'Subject: {subject}\n\n{body}'

        server.sendmail(
            'admin@itproger.com',
            'dln.wlkmn@gmail.com',
            message
        )

        # загатовка для быстрого ввода какого-либо второго мейла для демонстрации отправки писем
        # server.sendmail(
        #     'admin@itproger.com',
        #     '@mail.ru',
        #     message
        # )

        print("\nthe email has been sent")
        server.quit()

    # метод для проверки данных
    def check_data(self):
        # переменная для данных из файла предназначенна для сравнения
        fileData = self.get_fileLastData()
        # инициализируем классовуд переменную при помощи метода "интернет запроса"
        self.currentData = self.get_currency()

        # сравнивание с данными из файла
        if (float(fileData[0]) < float(remove_gaps(self.currentData[1].text)) and
                float(fileData[2]) <= float(remove_gaps(self.currentData[3].text)) and
                float(fileData[3]) <= float(remove_gaps(self.currentData[4].text))):
            # в том случае если данные изменились (то есть увеличились, уменьшиться они просто напросто не могли)
            f = open('data.txt','a')
            f.write("\n")
            tempCount = 0
            for i in self.currentData:
                if tempCount != 0:
                    f.write(remove_gaps(str(i.text)) + " ")
                tempCount += 1
            f.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            f.close()
            print("data has been updated...\n")
            time.sleep(3)
        else:
            # пишем что данные не изменились
            self.currentData = None
            print("we all gonna die...\n")
            time.sleep(2)
            print("kidding, nothing new\n")
            time.sleep(2)

# функция удаления пробелов, обозначающих размерность в цифрах (прим.: 2 378 (2 тысячи 378))
def remove_gaps(str):
    return str.replace(' ', '')

# функция меню, позволяющая удобно управлять программой
def menu():
    print("Menu\n"
          "1) Make checking request\n"
          "2) Show last results\n"
          "3) Send mail\n"
          "4) Print all Data\n"
          "5) Exit")
    choice = input(">>> ")
    return choice

# главная функция
def main():
    # начало прогарммы, инициализация объекта класса
    situation = Currency(1)

    # меню-цикл
    while True:
        # выбираем пункт меню
        choice = float(menu())
        if choice == 1:
            # проверка на наличие новых данных
            situation.check_data()
        elif choice == 2:
            # печать самой актуальной информации из файла
            fileData = situation.get_fileLastData()
            preFileData = situation.get_filePreLastData()
            print(f'\033[33mCases\033[0m: {fileData[0]} (+{fileData[1]} for the past day), '
                  f'\n\033[31mDeath\033[25m\033[0m: {fileData[3]} (+{int(fileData[3]) - int(preFileData[3])} from last check), '
                  f'\n\033[36mRecovered\033[0m: {fileData[2]} (+{int(fileData[2]) - int(preFileData[2])} from last check) '
                  f'\n[\033[35mactual on {fileData[4]} {fileData[5]}\033[0m]' )
            input("press Enter...\n")
        elif choice == 3:
            # отправка письма на почту, уведомляющее что положение дел изменилось
            preFileData = situation.get_filePreLastData()
            if situation.currentData != None:
                situation.send_mail(f'The situation with coronavirus in Russia has changed!\n'
                               f'Here is the most up-to-date (on {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}) data:\n'
                               f'Cases: {remove_gaps(situation.currentData[1].text)} (+{remove_gaps(situation.currentData[2].text)} for the past day)\n'
                               f'Recovered: {remove_gaps(situation.currentData[3].text)} (+{int(remove_gaps(situation.currentData[3].text)) - int(preFileData[2])} from last check)\n'
                               f'Death: {remove_gaps(situation.currentData[4].text)} (+{int(remove_gaps(situation.currentData[4].text)) - int(preFileData[3])} from last check) \n'
                               f'---\n'
                               f'(spamm)')

                input("press Enter...\n")

            else:
                # если проверенные данные совпадают с последними из файла, тогда попадаем сюда
                print("there is nothing new to send!...")
                input("press Enter...\n")
        elif choice == 4:
            # печать всех данных из файла наэкран консоли
            print("%9s%9s%10s%9s%14s%12s" % ("Cases", "Increase", "Recovered", "Death", "Date", "Time"))
            list = situation.get_fileData()
            count = 0
            for i in list:
                if count != 0:
                    st = str(i)
                    splited = st.split()
                    print("%9s%9s%10s%9s%14s%12s" % (splited[0], splited[1], splited[2], splited[3], splited[4], splited[5]))
                count += 1
            input("press Enter...\n")

        elif choice == 5:
            # завершение
            print("bye bye\n")
            break
        elif choice == 6:
            fig = plt.figure()
            # графики
            list = situation.get_fileData()
            list.pop(0)
            increase = []
            dates = []
            for i in list:
                increase.append(i.split()[0])
                dates.append(i.split()[3])
            plt.bar(dates, increase)
            plt.title('Simple bar chart')
            plt.grid(True)

            # cr = plt.contour(dates, increase)
            # plt.colorbar(cr)
            # plt.title('Simple contour plot')

            plt.show()




        else:
            print("choise right menu option...\n")

    input("press Enter to close app...")
    # конец главной функции

# вызов главной функции
if __name__ == "__main__":
    main()