from config import engine

engine.factory.Register_Config()
engine.db.create_all()
app = engine.app
if __name__ == '__main__':
    engine.app.run('0.0.0.0', 3000)