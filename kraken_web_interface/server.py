import os
import uvicorn

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kraken_web_interface.settings')

application = get_asgi_application()

if __name__ == '__main__':
    uvicorn.run("server:application", host="0.0.0.0", port=5000)
