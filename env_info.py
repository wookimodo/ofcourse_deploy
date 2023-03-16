from pathlib import Path

SECRET_KEY = 'django-insecure-qxxuc+cqy8zt)*4sn+stz=mq%vk^es^j5e&5ph28x-m!2bmxre'

DEBUG = True

ALLOWED_HOSTS = ['18.204.15.215']

BASE_DIR = Path(__file__).resolve().parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql', # mysql 엔진 설정
#         'NAME': 'ofcourse', # 데이터베이스 이름
#         'USER': 'kokonenne', # 데이터베이스 연결시 사용할 유저 이름(개발자 계정)
#         'PASSWORD': 'zhzhsosso', # 유저 패스워드      
#         'HOST': 'ofcourse.cdnhswpc3uak.ap-northeast-2.rds.amazonaws.com', 
#         'PORT': '3306',
#         'OPTIONS':{
#             'init_command' : "SET sql_mode='STRICT_TRANS_TABLES'"
#         }
#     }
# }