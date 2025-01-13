class Application:
    def __init__(self, app_name, app_link, icon_link, description, id=None):
        self.id = id
        self.app_name = app_name
        self.app_link = app_link
        self.icon_link = icon_link
        self.description = description
