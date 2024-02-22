import firebase_admin
import os
from werkzeug.security import check_password_hash, generate_password_hash
from firebase_admin import db, credentials

cred = credentials.Certificate(os.getenv('FIREBASE_CRED_PATH'))
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://solution-challenge-d36ce-default-rtdb.europe-west1.firebasedatabase.app/'
})

class User:
    def __init__(self, **kwargs):
        self.details = kwargs


    def add(self):
        """Adds User to the database"""
        self['password'] = generate_password_hash(self['password'])
        ref = db.reference('User')
        ref.update({
            self["id"]: self.details
        })


    def delete(self):
        """NOT TESTED"""
        """Deletes User From the database"""
        ref = db.reference('User')
        ref.update({
            self["id"]: {}
        })


    def update(self, **kwargs):
        """Updates User info"""
        ref = db.reference(f'User/{self["id"]}')
        ref.update(kwargs)

    def __getitem__(self, attribute):
        if attribute in self.details:
            return self.details[attribute]
        else:
            return None
        

    def __setitem__(self, attribute, value):
        if attribute in self.details:
            self.details[attribute] = value
        else:
            raise IndexError('Attribute Not Found')        
        
    def auth(self, password):
        return check_password_hash(self["password"], password)

    def add_file(self, file):
        ref = db.reference(f'User/{self["id"]}')
        reports = {}

        try:
            reports = ref.get()["reports"]
        except: pass


        reports.update({
            file.file_name: {
                "data": file.file_data
            }
        })

        self.update(**{
            "reports": reports
            })

    @staticmethod
    def get(id):
        ref = db.reference(f'User/{id}')
        return User(**ref.get()) if ref.get() is not None else None


class Question:
    def __init__(self, num) -> None:
        self.num = num
        
    def increment(self):
        ref = db.reference(f'Data/')
        numbers = ref.get()
        ref.update({numbers[self.num]: numbers[self.num] + 1})


class File:
    def __init__(self, file_data, file_name):
        self.file_data = file_data
        self.file_name = file_name
