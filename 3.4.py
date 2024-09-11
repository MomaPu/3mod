import os
import json

def autor(login):
    if login in data:  # Проверяем, есть ли пользователь с таким логином
        print('Логин есть в системе')
        password = input("Введите пароль: ")  # Если есть - авторизуем
        if data[login] == password:  # Проверяем, совпадает ли пароль
            print('Авторизация прошла успешно')
        else: 
            print('Пароль неверный')
    else:
        print('Логина нету в системе, зарегистрируйтесь')
        password = input('Введите пароль: ')
        data[login] = password  # Регистрация
        with open("data.json", "w") as write_file: 
            json.dump(data, write_file) 
        print("Пользователь успешно зарегистрирован.")


if os.path.exists("data.json"):  # Проверка наличия файла с данными
    with open("data.json", "r") as read_file:
        try:
            data = json.load(read_file)
        except json.JSONDecodeError:  # Исключаем ошибку
            data = {}  # Если она случилась создаем новую базу
else:
    data = {}

login = input('Введите логин: ')
autor(login)