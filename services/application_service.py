from repositories.application_repo import ApplicationRepository
from database.models import Application  # Adicione essa linha

class ApplicationService:
    def __init__(self):
        self.repo = ApplicationRepository()

    def get_all_applications(self):
        return self.repo.get_all()

    def add_application(self, app_name, app_link, icon_link, description):
        # Você pode adicionar validações aqui
        application = Application(app_name, app_link, icon_link, description)
        self.repo.add(application)

    def delete_application(self, app_id):
        self.repo.delete(app_id)
