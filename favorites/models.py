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
    def userfolders(self):
        query = (User_Folder
                .select()
                .join(User)
                .where(User.id == self.id))
        return query
                
    @property
    def userwebpages(self):
        query = (User_Webpage
                .select()
                .join(User)
                .where(User.id == self.id))
        return query

    def add_folder(self,folder):
        return User_Folder.create(user=self, folder=folder)

    def add_webpage(self,webpage):
        return User_Webpage.create(user=self, webpage=webpage)

class Folder(flask_db.Model):
    id = PrimaryKeyField()
    folder_name = CharField(unique=True)




#Folder,Webpage is a common property.User_Folder and UserFolder_Webpage like a proxy for real world use.
class User_Folder(flask_db.Model):
    id = PrimaryKeyField()
    user = ForeignKeyField(User)
    folder = ForeignKeyField(Folder)
    parent = ForeignKeyField('self',null=True,related_name='subfolders')

    @property
    def userfolder_webpages(self):
        query = (UserFolder_Webpage
                .select()
                .where((UserFolder_Webpage.userfolder == self)))
        return query

    def add_webpage(self,userwebpage):
        webpage = userwebpage.webpage
        return UserFolder_Webpage.create(userfolder=self,
                webpage=webpage)

class Webpage(flask_db.Model):
    id = PrimaryKeyField()
    url = CharField(unique=True)
    abstract = TextField()



class User_Webpage(flask_db.Model):
    id = PrimaryKeyField()
    user = ForeignKeyField(User)
    webpage = ForeignKeyField(Webpage)


#only someone's webpage could add in someone's folder,someone must be the same person.
class UserFolder_Webpage(flask_db.Model):
    userfolder = ForeignKeyField(User_Folder)
    webpage = ForeignKeyField(Webpage)



