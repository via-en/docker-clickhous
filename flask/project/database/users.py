from infi.clickhouse_orm.database import Database
from infi.clickhouse_orm.models import Model
from infi.clickhouse_orm.fields import *
from infi.clickhouse_orm.engines import Memory

import logging.config
import os
from pathlib import Path
import json


class Person(Model):
    id = UInt64Field()
    first_name = StringField()
    last_name = StringField()
    gender = StringField()
    email = StringField()
    birth_date = UInt64Field()

    engine = Memory()


if __name__ == "__main__":

    CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
    logging.config.fileConfig(os.path.join(CURRENT_DIR, '../config', 'logging.conf'))
    logger = logging.getLogger(__name__)
    DIR = 'data'

    dir_for_file = Path.cwd().joinpath(DIR)


    def _sample_data():
        for file in dir_for_file.iterdir():
            with file.open() as jsonfile:
                try:
                    for line in jsonfile:
                        data = json.loads(line)
                        for entry in data['users']:
                            entry['birth_date'] = abs(entry['birth_date'])
                            yield Person(**entry)
                except Exception as err:
                    logger.debug(err)

    database = Database('demo')
    database.create_table(Person)

    for el in _sample_data():
        database.insert([el])