import rumps
import os

class StregsystemApp(object):
    def __init__(self):
        self.config = {
            "app_name" : "StregsystemApp",
            "username" : "TheMindFrom99",
            "update" : "Update Balance",
            "sportscola" : "Buy Sportscola 6 $",
            "coffe" : "Buy Coffee 2 $",
            "success_message" : "Command successfully executed!",
            "error_message" : "Command failed, are you at AAU?"
        }
        self.app = rumps.App(self.config["app_name"])
        self.set_up_menu
        self.update_button = rumps.MenuItem(title=self.config["start"], callback=self.update_balance)
        self.buy_sportscola = rumps.MenuItem(title=self.config["sportscola"], callback=self.buy_sportscola)
        self.app.menu = [self.update_button, self.buy_sportscola]


    def set_up_menu(self):
        self.update_balance()

    def update_balance(self):
        balance = os.popen("sts -u " + self.config["username"] + " -b").read()
        self.app.title = balance + " $"


    def buy_sportscola(self):
        message = os.popen("sts -u " + self.config["username"]).read()
        # if message is good, output success message, else output error message


if __name__ == '__main__':
    app = StregsystemApp()
    app.run()
