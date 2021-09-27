import os

from app import create_app

port = int(os.getenv('PORT', '5000'))
messages_app = create_app()
messages_app.run(port=port)
