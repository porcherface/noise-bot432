# getter.py

class configClass:
    def __init__(self,u, t1, t2, t3):
        self.APP_ID       = t1
        self.APP_SECRET   = t2
        self.ACCESS_TOKEN = t3
        self.username = u
    def __str__(self):
        return self.APP_ID+": "+self.ACCESS_TOKEN +" from "+self.username

def get_config(username):

    APP_ID       = "Your ID"
    APP_SECRET   = "Your SECRET"
    ACCESS_TOKEN = "Your Token"    
    return configClass(username, APP_ID, APP_SECRET, ACCESS_TOKEN)
