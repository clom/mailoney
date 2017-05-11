import ConfigParser
import os

config = ConfigParser.ConfigParser()

DATABASE = 'Database'

def write_config():
    if not os.path.isfile('../settings.conf'):
        config.add_section(DATABASE)
        config.set(DATABASE, 'type', 'mysql')
        config.set(DATABASE, 'host', 'localhost')
        config.set(DATABASE, 'port', 3389)
        config.set(DATABASE, 'db_name', 'mailoney')
        config.set(DATABASE, 'db_user', 'mailoney')
        config.set(DATABASE, 'db_password', 'secret')


        with open('../settings.conf', 'w') as f:
            config.write(f)

def read_config_database():
    config.read('../settings.conf')

    type  = config.get(DATABASE, 'type')
    db_user     = config.get(DATABASE, 'db_user')
    db_password = config.get(DATABASE, 'db_password')
    host        = config.get(DATABASE, 'host')
    port        = config.get(DATABASE, 'port')
    db_name     = config.get(DATABASE, "db_name")

    database = {'type': type,
                'db_user': db_user,
                'db_password': db_password,
                'host': host,
                'port': port,
                'db_name': db_name
                }

    return database