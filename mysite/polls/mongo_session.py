import pymongo
import logging
import urllib
import pprint
from typing import Dict


import polls.mongo_settings as settings


class DjangoMongoClient(object):

    def __init__(self, settings=settings, database=None):
        """
        Object to work with MongoDB
        :param settings:
        """
        self._settings = settings
        self.database = self._settings.DATABASE

        # Initializing logging
        logging.basicConfig(format=self._settings.LOG_FORMAT, level=self._settings.LOG_LEVEL)
        self._log = logging.getLogger(__name__)
        self._log.debug('logging initialized')

        # Create client session
        self._username = urllib.parse.quote_plus(self._settings.MONGO_USER)
        self._password = urllib.parse.quote_plus(self._settings.MONGO_PASS)
        self._uri = f"mongodb://{self._username}:{self._password}@{self._settings.MONGO_HOST}:{self._settings.MONGO_PORT}"

        try:
            self.client = pymongo.MongoClient(self._uri)
            self._log.info('Connection to MongoDB successful')
        except Exception as connection_error:
            self._log.exception(connection_error)

        self.db = self.client[self.database]
        self.admin_db = self.client["admin"]

        self.users = self.db.users

    def print_databases(self):
        pprint.pprint(self.client.list_database_names())

    def print_collections(self):
        pprint.pprint(self.db.list_collection_names())

    def get_db_stats(self):
        pprint.pprint(self.db.command('dbstats'))

    def get_server_status(self):
        pprint.pprint(self.db.command('serverStatus'))

    def insert_document_record(self, doc_dict: Dict, collection: str) -> None:
        """

        :param doc_dict: dict of key, values to insert into database
        :param collection str:
        :return:
        """

        col = self.db[collection]

        try:
            col.insert_one(doc_dict).inserted_id
            self._log.info(f"record in {self.database} db has been inserted")
        except Exception as error:
            self._log.exception(error)

    def update_item(self, search_dict: Dict, doc_dict: Dict, collection: str) -> None:
        """

        :param search_dict: dict of key, values to search the database
        :param doc_dict: dict of key, values to update in database
        :param collection str:
        :return:
        """

        col = self.db[collection]

        try:
            doc = col.find_one(search_dict)

            if doc:
                new_values = {"$set": doc_dict}
                col.update_one(search_dict, new_values)
                self._log.info(f"updated values in {col}")

        except Exception as missing_item:
            raise ValueError('incorrect search dict')

    def query_document(self, key: str, value: str, collection: str):

        try:
            col = self.db[collection]
            query = {key: value}
            doc = col.find_one(query)
            return doc

        except Exception as error:
            raise ValueError('incorrect key, value')

    def query_documents(self, collection: str):

        try:
            col = self.db[collection]

            query = col.find()

            return query

        except Exception as e:
            raise ValueError('no query data')

    def delete_document(self, search_dict: Dict, collection: str):

        """

        :param search_dict: dict of key, values to search the database
        :param collection str:
        :return:
        """

        col = self.db[collection]

        try:
            print(search_dict)
            doc = col.find_one(search_dict)
            print(doc)

            if doc:
                col.delete_one(search_dict)
                self._log.info(f"deleted values in {col}")

        except Exception as missing_item:
            raise ValueError('incorrect search dict')



