# from config import engine

from old.app.controller import factory, db
from old import app

factory.Register_Config()
db.create_all()
if __name__ == '__main__':
    app.run('0.0.0.0', 3000)