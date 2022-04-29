import itertools
import logging


logger = logging.getLogger("django")


class PrimaryReplicaRouter:

    def __init__(self, *args, **kwargs):
        from django.conf import settings
        self.databases = tuple(settings.DATABASES.keys())
        self.pool = itertools.cycle(self.databases)
        logger.debug("Database routing: %s", self.databases)

    def db_for_read(self, model, **hints):
        choice = next(self.pool)
        logger.debug("Read in database routed to: %s", choice)
        return choice

    def db_for_write(self, model, **hints):
        logger.debug("Write in database routed to: default")
        return "default"

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return True
