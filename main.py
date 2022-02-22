import rumps
import os


class StregsystemApp(object):
    def __init__(self):
        self.config = {
            "app_name": "StregsystemApp",
            "username": "alex",
            "update": "Update Balance",
            "sportscola": "Buy Sportscola 6 $",
            "coffee": "Buy Coffee 2 $",
            "success_message": "Command successfully executed!",
            "error_message": "Command failed, are you at AAU?"
        }
        self.app = rumps.App(self.config["app_name"])
        self.set_up_menu()
        self.update_button = rumps.MenuItem(title=self.config["update"], callback=self.update_balance)
        self.buy_sportscola = rumps.MenuItem(title=self.config["sportscola"], callback=self.buy_sportscola)
        self.buy_coffee = rumps.MenuItem(title=self.config["coffee"], callback=self.buy_coffee)
        self.app.menu = [self.update_button, self.buy_sportscola, self.buy_coffee]

    def set_up_menu(self):
        self.app.title = os.popen("python3 ~/sts -u " + self.config["username"] + " -b").read().split("\n")[1] + " $"

    def update_balance(self):
        message = os.popen("python3 ~/sts -u " + self.config["username"] + " -b").read()
        if message == "Noget gik galt 403":
            rumps.notification(title=self.config["app_name"], subtitle=self.config["error_message"], message="")
        else:
            self.app.title = message.split()[1] + " $"

    def buy_sportscola(self):
        message = os.popen("sts -u " + self.config["username"] + " -i 1891").read()


    def buy_coffee(self):
        var = 2
        print("HELLO")
        # buys coffee

    def run(self):
        self.app.run()


if __name__ == '__main__':
    app = StregsystemApp()
    app.run()
