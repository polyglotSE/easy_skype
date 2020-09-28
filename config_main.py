import argparse

def getUserCread():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("-u", "--username", help='Take skype username(needed first time)')
    arg_parser.add_argument("-p", "--password", help='Take skype password(needed first time)')
    arg_parser.add_argument("--default_path", help='Put path where to save downloaded files')
    arg_parser.add_argument("-c", "--contact", help="Put Skype Id whose chat's files you wanna download")
    args = arg_parser.parse_args()

    try:
        config = open('.sk_usr_config', 'r')
        username = config.readline()
        password = config.readline()
        path = config.readline()
        return username, password, path, args.contact
    except FileNotFoundError:
        if args.username is None:
            username = input('Enter Skype username : ')
            password = input('Enter Skype password : ')
            def_path = input('Enter download path : ')
            cred = username, password, def_path, args.contact
            write_cred_into_file(cred)
            return cred
        elif args.password is None:
            password = input('Enter Skype password : ')
            def_path = input('Enter download path : ')
            cred = args.username, password, def_path, args.contact
            write_cred_into_file(cred)
            return cred
        elif args.default_path is None:
            def_path = input('Enter download path : ')
            cred = args.username, args.password, def_path, args.contact
            write_cred_into_file(cred)
            return cred
        else:
            cred = args.username, args.password, args.default_path
            write_cred_into_file(cred)
            return args.username, args.password, args.default_path, args.contact


def write_cred_into_file(cred):
    config = open('.sk_usr_config', 'w')
    config.writelines(cred[0] + '\n')
    config.write(cred[1] + '\n')
    config.write(cred[2])
