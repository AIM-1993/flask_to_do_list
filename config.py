from flask_sqlalchemy import SQLAlchemy
import pymysql
SQLALCHEMY_DATABASE_URI="sqlite:/// + os.path.join(base_dir, 'flasktodo_db')"
SQLALCHEMY_TRACK_MODIFICATIONS=False
