from skpy import Skype
import config_main as conf
import downloader as dw
from rich.console import Console
from rich.table import Column, Table

console = Console()
sk = None

def get_msg_list(skypr_id):
    file_dict = {}
    ch = sk.contacts[skypr_id].chat
    msgs = sk.chats[ch.id].getMsgs()
    print('getting chat sucess')
    i = 1
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column('ID')
    table.add_column('DateTime')
    table.add_column('File Name')
    for msg in msgs:
        if 'RichText/Media_GenericFile' == msg.type:
            table.add_row(str(i), msg.time.strftime("%d-%b-%Y %I:%M %p"), str(msg.file.name))
            file_dict[i] = msg.file.name, "{0}/views/original".format(msg.file.urlAsm)
            i = i + 1
    console.print("Files List : ", style="bold red")
    console.print(table)
    return file_dict


cred = conf.getUserCread()

if cred[0] is not None and cred[3] is not None:
    sk = Skype(cred[0], cred[1], "tokenFile")
    file_dict = get_msg_list(cred[3])
    while True:
        user_input = input('n/id/quit >> ')
        if user_input.isnumeric():
            index = int(user_input)
            if 1 <= index <= len(file_dict):
                file_tuple = file_dict[index]
                dw.download_file(file_tuple[0], file_tuple[1],
                                 "skype_token {0}".format(sk.conn.tokens["skype"]), cred[2])
            else:
                print('Please Enter valid Id')
        else:
            if user_input == 'quit':
                break
            elif user_input == 'n':
                file_dict = get_msg_list(cred[3])
            else:
                print('Please Enter Valid Option')

elif cred[0] is not None and cred[3] is None:
    sk = Skype(cred[0], cred[1], "tokenFile")
    contact = sk.contacts
    contact_dict = {}
    i = 1
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column('ID')
    table.add_column('Name')
    for c in contact:
        table.add_row(str(i), str(c.name))
        contact_dict[i] = c.id
        i = i + 1
    console.print("Contact List : ", style="bold red")
    console.print(table)
    print('Please type contactId and press Enter')
    contact_id = int(input())
    file_dict = get_msg_list(contact_dict[contact_id])
    while True:
        user_input = input('n/{id}/quit >> ')
        if user_input.isnumeric():
            index = int(user_input)
            if 1 <= index <= len(file_dict):
                file_tuple = file_dict[index]
                dw.download_file(file_tuple[0], file_tuple[1],
                                 "skype_token {0}".format(sk.conn.tokens["skype"]), cred[2])
            else:
                print('Please Enter valid Id')
        else:
            if user_input == 'quit':
                break
            elif user_input == 'n':
                file_dict = get_msg_list(contact_dict[contact_id])
            else:
                print('Please Enter Valid Option')