class MobilePhone:

    def __init__(self, manufacturer:str, screen_size:int, num_cores:int, apps:list, status:bool):
        self.manufacturer = manufacturer
        self.screen_size = screen_size
        self.num_cores = num_cores
        self.apps = []
        self.status = status

    def power_on(self):
        self.status = True
        print("Telf encendido")


    def power_off(self):
        self.status = False
        print("Telf apagado")

    def install_app(self, app):
        if app not in self.apps:
            self.apps.append(app)

    def uninstall_app(self, app):
        if app in self.apps:
            self.apps.remove(app)


movil = MobilePhone('Pepephone', 30, 3, [], False)
movil.power_on
movil.power_off
