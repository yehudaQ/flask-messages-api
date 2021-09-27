from app import create_app

if __name__ == '__main__':
    messages_app = create_app()
    messages_app.run()
