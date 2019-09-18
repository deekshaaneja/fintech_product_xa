from flask import Flask
try:
    import init_mysql_schema
except Exception as e:
    print("msyql connection exception", e)
    
from app_grab_and_save import grab_and_save_blueprint
from app_last import last_blueprint

application = Flask(__name__)
application.register_blueprint(grab_and_save_blueprint)
application.register_blueprint(last_blueprint)

if __name__ == '__main__':
    application.run(host='0.0.0.0',port=9000)