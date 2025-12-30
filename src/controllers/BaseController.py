from helpers.config import get_settings, Settings
import os
import random
import string
class BaseController:
    # constructor
    def __init__(self):
        self.app_settings= get_settings()
        self.base_dir = os.path.dirname(os.path.dirname(__file__)) #get the direname of this file, i.e. the dirname of BaseController
        self.files_dir= os.path.join(
            self.base_dir ,
              "assets/files" 
        )

        self.database_dir = os.path.join(
            self.base_dir ,
            "assets/database"
        )

    def generate_random_string(self, length: int = 12):
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length)) #returns random string of digits and chars of length = 12

    def get_database_path(self, db_name: str):
        database_path = os.path.join(
            self.database_dir,
            db_name
        )
        if not os.path.exists(database_path):
            os.makedirs(database_path)
        return database_path