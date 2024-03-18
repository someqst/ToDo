from aiogram import Router



def routs_reg() -> Router:
    from handlers import start, goals_work
    router = Router()
    router.include_routers(
        start.router,
        goals_work.router
        )
    return router