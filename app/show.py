import os

VERSION = os.getenv('SHOW_VERSION')

if VERSION:
    print(f'Have version: {VERSION}')

from credentials import DB_HOST

print(f'дб хост: {DB_HOST}')
