import os

from fastapi_poe import make_app
from modal import Image, Secret, Stub, asgi_app

from nous_hermes_13b import NousHermes13BBot

image = Image.debian_slim().pip_install_from_requirements("requirements.txt")
stub = Stub("nous-hermes-13b-app")


@stub.function(image=image, secret=Secret.from_name("nous-hermes-13b-secret"))
@asgi_app()
def fastapi_app():
    bot = NousHermes13BBot(TOGETHER_API_KEY=os.environ["TOGETHER_API_KEY"])
    app = make_app(bot, api_key=os.environ["POE_API_KEY"])
    return app
