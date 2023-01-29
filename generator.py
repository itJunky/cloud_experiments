#!/usr/bin/env python
import os
import random
import copy
import string
from datetime import datetime
from db import *
from rmq_sender import send_to_mq

from sqlalchemy.orm import sessionmaker, scoped_session
session = scoped_session(sessionmaker(bind=engine))

data = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(16))
msg = Generator(msg=data,
                date=datetime.now())
# Object deleted after commit to DB
output = copy.deepcopy(msg)
# TODO Need to log every try
session.add(msg)
session.commit()

send_to_mq(message=f'{str(output.id)} - {str(output.msg)}: {str(output.date)}')

