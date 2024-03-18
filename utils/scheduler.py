from apscheduler.schedulers.asyncio import AsyncIOScheduler
from handlers.goals_work import send_summary, send_goals, send_messages


scheduler = AsyncIOScheduler()
scheduler.add_job(send_summary, 'cron', hour = 3, minute = 15, timezone = 'Europe/Moscow')
scheduler.add_job(send_goals, 'cron', hour = 3, minute = 25, timezone = 'Europe/Moscow')
scheduler.add_job(send_messages, 'cron', hour = 9, minute = 0, timezone = 'Europe/Moscow')
scheduler.add_job(send_messages, 'cron', hour = 15, minute = 15, timezone = 'Europe/Moscow')
scheduler.add_job(send_messages, 'cron', hour = 20, minute = 15, timezone = 'Europe/Moscow')