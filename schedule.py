from apscheduler.schedulers.blocking import BlockingScheduler
from send_message import send_msg

scheduler = BlockingScheduler()

# Schedule function to be called
scheduler.add_job(send_msg, 'interval', seconds=10)

scheduler.start()
