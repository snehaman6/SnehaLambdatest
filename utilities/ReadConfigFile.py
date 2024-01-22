import configparser

config = configparser.RawConfigParser()

config.read("G:\\SnehaLambdatest\\Configiration\\Config.ini")

class ReadConfig():
    @staticmethod
    def getUsername():
        username = config.get('login name', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('login id', 'password')
        return password
