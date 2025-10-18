from aiogram import Router
from handler import start, about_us,ariza_qoldiring,kontaktlar


def setup_message_router():
    router = Router()
    router.include_router(start.router)
    router.include_router(about_us.router)
    router.include_router(ariza_qoldiring.router)
    router.include_router(kontaktlar.router)
    return router