from app import create_app
from config import DevConfig

app = create_app()

if __name__ == "__main__":
    app.run()
