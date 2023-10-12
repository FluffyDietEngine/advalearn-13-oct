from logging import getLogger, ERROR
from logging.handlers import SMTPHandler
from logging import Formatter

from decouple import config

logger = getLogger("mailer-test")


mailer = SMTPHandler(
    mailhost=("smtp.gmail.com", 587),
    fromaddr=config("SENDER_EMAIL"),
    toaddrs=[config("RECEIVER_EMAIL")],
    secure=(),
    subject="Error message from AdvaLearn",
    credentials=(config("SENDER_EMAIL"), config("APP_PASSWORD"))
)
log_format = Formatter("%(asctime)s | %(appName)s | %(funcName)s | %(filename)s | %(message)s", defaults={"appName": "LogTest"})
mailer.setFormatter(log_format)
logger.addHandler(mailer)

logger.setLevel(ERROR)
