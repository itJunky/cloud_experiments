import os
import random
import string
from datetime import datetime
from db import *

from sqlalchemy.orm import sessionmaker, scoped_session
session = scoped_session(sessionmaker(bind=engine))

data = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(16))
msg = Generator(msg=data,
                date=datetime.now())
session.add(msg)
session.commit()

print(msg.id)

