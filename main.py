from data_manager import DBManager
from core.models import User
from menu.models import generate_menu_from_dict
from menu.utils import get_input
from core.models import User, Message
import datetime

db_config = {'dbname':'Farzad3','host':'127.0.0.1','port':'5432',
            'password':'8890333','user':'Farzad3'}
manager = DBManager({'db_config':db_config})

user_inf = []

def create_message():
    message_txt = input('Enter message: ')
    from_user = ...
    to_user = input('Enter user id you want to send to: ')
    subject = input('Enter Subject: ')
    time = datetime.datetime.now()
    message = Message(message_txt,from_user,
                      to_user,time, subject)
    m = DBManager({'db_config':db_config})
    m.create(m)

def inbox():
    manager = DBManager({'db_config':db_config})
    result = manager.read_all(user_inf._id, Message)
    for item in result:
        if item[3] == user_inf._id:
            print(item[1])

def sent_box():
    manager = DBManager({'db_config':db_config})
    result = manager.read_all(user_inf._id, Message)
    for item in result:
        if item[2] == user_inf._id:
            print(item[1])


main_menu_dict = {
    'name':'Messenger',
    'children':[
        {
            'name':'Create message',
            'action': Create_message,
        },
        {
            'name':'Inbox',
            'action': Inbox,
        },
        {
            'name':'Outbox',
            'action': Sent_box,
        },
]}

root_menu = generate_menu_from_dict(main_menu_dict, parent=None)

def main():
    username = get_input("Username: ")
    password = get_input("Password: ")
    try:
        user = User.login(username, password)
    except AssertionError:
        print("Manager user is not set")
        exit()

    if user:
        print("Welcome manager...\n")
        user_inf.append(user)
        root_menu()
    else:
        print("invalid username or password")

main()
