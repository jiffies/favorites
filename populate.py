#-*- coding:utf-8 _*-
from favorites.models import *
import datetime

User = [
        {'id':1,'username':'jiffies','password':'jiffies','join_at':datetime.date.today()},
        {'id':2,'username':'lcq','password':'lcq','join_at':datetime.date.today()},
        {'id':3,'username':'lcy','password':'lcy','join_at':datetime.date.today()},
        {'id':4,'username':'yxj','password':'yxj','join_at':datetime.date.today()},
        {'id':5,'username':'lsm','password':'lsm','join_at':datetime.date.today()},
]

Folder = [
        {'id':1,'folder_name':'python'},
        {'id':2,'folder_name':'github'},
        {'id':3,'folder_name':'足球'},
        {'id':4,'folder_name':'机器学习'},
        {'id':5,'folder_name':'购物'},
        {'id':6,'folder_name':'linux'},
        {'id':7,'folder_name':'美女'},
]

User_Folder = [
        {'id':1,'user':1,'folder':1},        
        {'id':2,'user':1,'folder':2},        
        {'id':3,'user':1,'folder':4},        
        {'id':4,'user':1,'folder':6},        
        {'id':5,'user':1,'folder':3},        
        {'id':6,'user':2,'folder':1},        
        {'id':7,'user':2,'folder':2},        
        {'id':8,'user':2,'folder':3},        
        {'id':9,'user':2,'folder':4},        
        {'id':10,'user':2,'folder':5},        
        {'id':11,'user':2,'folder':6},        
        {'id':12,'user':3,'folder':3},        
        {'id':13,'user':3,'folder':7},        
        {'id':14,'user':4,'folder':5},        
        {'id':15,'user':4,'folder':1},        
        {'id':16,'user':4,'folder':2},        
]

Webpage = [
        {'id':1,'url':'baidu.com'},
        {'id':2,'url':'google.com'},
        {'id':3,'url':'code4awesome.com'},
        {'id':4,'url':'facebook.com'},
        {'id':5,'url':'twitter.com'},
        {'id':6,'url':'weibo.com'},
        {'id':7,'url':'taobao.com'},
        {'id':8,'url':'12306.com'},
]

User_Webpage = [
        {'id':1,'user':1,'webpage':1},        
        {'id':2,'user':1,'webpage':2},        
        {'id':3,'user':1,'webpage':3},        
        {'id':4,'user':1,'webpage':4},        
        {'id':5,'user':2,'webpage':3},        
        {'id':6,'user':2,'webpage':4},        
        {'id':7,'user':2,'webpage':5},        
        {'id':8,'user':4,'webpage':6},        
        {'id':9,'user':4,'webpage':7},        
        {'id':10,'user':4,'webpage':3},        
        {'id':11,'user':4,'webpage':8},        
]

UserFolder_UserWebpage = [
        {'userfolder':1,'userwebpage':1},        
        {'userfolder':1,'userwebpage':2},        
        {'userfolder':1,'userwebpage':3},        
        {'userfolder':2,'userwebpage':2},        
        {'userfolder':2,'userwebpage':4},        
]
