# Task 1
# Создать в БД таблицу на 10 или более записей.
# Удалите половину записей.
# А вторую половину измените.

import sqlite3
from random import randint, shuffle
conn = sqlite3.connect('base.db')
cursor = conn.cursor()

# создание таблицы
cursor.execute('''DROP TABLE IF EXISTS task1''')
cursor.execute('''CREATE TABLE IF NOT EXISTS task1(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    col1 INTEGER
    )''')
for i in range(randint(10, 51)):
    cursor.execute(
        '''INSERT INTO task1(col1) VALUES(?)''', (randint(1, 15), ))

# получение количества всех записей
cursor.execute('''SELECT * FROM task1''')
stat1 = cursor.fetchall()

# удаление половины элементов
for i in range(len(stat1)//2):
    cursor.execute('''DELETE FROM task1 WHERE id=?''', (i+1,))

# изменение оставшихся элементов
cursor.execute('''SELECT * FROM task1''')
stat2 = cursor.fetchall()
for i in range(len(stat2)):
    cursor.execute('''UPDATE task1 SET col1 = 1001''')


# Task 2
# Создать две таблицы в одной базе данных.
# Одна таблица будет содержать текстовые данные в единственной колонке
# (не считая id),
# вторая таблица только числовые данные в единственной колонке
# (не считая id).
# В любом месте кода создайте список
# (например sp = [1,2,3,4,10,100,1000, 'one' , 'potato', 'carrot'],
# в котором будут числа и слова. Ну а теперь - что с этим делать:
# 1. В текстовую таблицу закинуть все слова, а в числовую все числа.
# 2. В числовой таблице удалить все строки, где число больше 10.
# 3. В текстовой таблице все строки со словами длиннее 4 символов обновить на фразу 'Overone‘

cursor.execute('''DROP TABLE IF EXISTS task2_text''')
cursor.execute('''DROP TABLE IF EXISTS task2_num''')

cursor.execute('''CREATE TABLE IF NOT EXISTS task2_text(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    col1 TEXT
    )''')
cursor.execute('''CREATE TABLE IF NOT EXISTS task2_num(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    col1 INTEGER
    )''')

# список случайных элементов
t = 'lpuda timstzvd gdjgoou dgv nmwli j yytfwim ktxy bvxyb jfwxer  qindgp paokb vdclukr ' \
    'flv x jfajc vttjswt gywd dp bewy eabkp 11 8 144 4 7 151 6 8 51 31 58 137 4 6 113 1 5 ' \
    '16 73 101 117 156 100 72 102 109 152 41 13 42 99 11 62 145 36'
sp = []
for x in t.split():
    if x.isalpha():
        sp.append(x)
    elif x.isdigit():
        sp.append(int(x))
shuffle(sp)

for x in sp:
    if type(x) == str:
        cursor.execute('''INSERT INTO task2_text(col1) VALUES(?)''', (x, ))
    else:
        cursor.execute('''INSERT INTO task2_num(col1) VALUES(?)''', (x,))

cursor.execute('''DELETE FROM task2_num WHERE col1>10 ''')
cursor.execute('''SELECT * FROM task2_text WHERE col1 LIKE '%_____%' ''')
a = cursor.fetchall()
for i in a:
    cursor.execute('''UPDATE task2_text SET col1='Overone' WHERE id=?''', (i[0],))


# Task 3
# Заполнить таблицу БД названиями песен с указанием их длительности
# (то есть колонка с названием и колонка со временем в секундах)
# Из этой таблицы собрать все записи, с длительностью больше 60 секунд
# и записать их в текстовый файл (название и время)

cursor.execute('''DROP TABLE IF EXISTS task3''')

cursor.execute('''CREATE TABLE IF NOT EXISTS task3(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    len1 INTEGER
    )''')

cursor.execute('''INSERT INTO task3(title, len1) VALUES('How Long', 199)''')
cursor.execute('''INSERT INTO task3(title, len1) VALUES('2 Die 4', 186)''')
cursor.execute('''INSERT INTO task3(title, len1) VALUES("Don't Say Goodbye", 187)''')
cursor.execute('''INSERT INTO task3(title, len1) VALUES('Heroes (we could be)', 209)''')
cursor.execute('''INSERT INTO task3(title, len1) VALUES('Habits (Stay High)', 258)''')
cursor.execute('''INSERT INTO task3(title, len1) VALUES('Cool Girl', 44)''')
cursor.execute('''INSERT INTO task3(title, len1) VALUES('PITCH BLACK', 53)''')

conn.commit()

cursor.execute('''SELECT title, len1 FROM task3 WHERE len1>60''')
spis = cursor.fetchall()

with open('songs.txt', 'w') as f:
    for i in spis:
        print(*i, sep=' - ', file=f)
