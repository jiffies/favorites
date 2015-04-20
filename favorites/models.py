import datetime
from peewee import *
from playhouse.flask_utils import FlaskDB

flask_db = FlaskDB()
database = flask_db.database

class User(flask_db.Model):
    id = PrimaryKeyField()
    username = CharField(unique=True,index=True)
    password = CharField()
    join_at = DateField()

    @property
    def folders(self):
        query = (Folder
                .select()
                .join(User_Folder)
                .join(User)
                .where(User.id == self.id))
        query.execute()
        for folder in query:
            folder.user = self
        return query
                
    @property
    def webpages(self):
        query = (Webpage
                .select()
                .join(User_Webpage)
                .join(User)
                .where(User.id == self.id))
        query.execute()
        for webpages in query:
            webpages.user = self
        return query

    def add_folder(self,folder):
        User_Folder.create(user=self, folder=folder)

    def add_webpage(self,webpage):
        User_Webpage.create(user=self, webpage=webpage)

class Folder(flask_db.Model):
    id = PrimaryKeyField()
    folder_name = CharField(unique=True)

    @property
    def webpages(self):
        query = (Webpage
                .select()
                .join(UserFolder_Webpage)
                .join(User_Folder)
                .where((User_Folder.folder == self) & (User_Folder.user == self.user)))
        return query
                                    

    @property
    def userfolder(self):
        query = (User_Folder
                .select()
                .where((User_Folder.user == self.user) &
                    (User_Folder.folder == self)))
        query.execute()
        return query

    def add_webpage(self,webpage):
        UserFolder_Webpage.create(userfolder=self.userfolder,
                webpage=webpage)

    
class User_Folder(flask_db.Model):
    id = PrimaryKeyField()
    user = ForeignKeyField(User)
    folder = ForeignKeyField(Folder)

class Webpage(flask_db.Model):
    id = PrimaryKeyField()
    url = CharField(unique=True)
    abstract = TextField()

    @property
    def userwebpage(self):
        query = (User_Webpage
                .select()
                .where(User_Webpage.user == self.user &
                    User_Webpage.webpage == self))
        query.execute()
        return query


class User_Webpage(flask_db.Model):
    id = PrimaryKeyField()
    user = ForeignKeyField(User)
    webpage = ForeignKeyField(Webpage)


#only someone's webpage could add in someone's folder,someone must be the same person.
class UserFolder_Webpage(flask_db.Model):
    userfolder = ForeignKeyField(User_Folder)
    webpage = ForeignKeyField(Webpage)



