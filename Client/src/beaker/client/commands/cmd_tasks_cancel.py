# -*- coding: utf-8 -*-


from beaker.client import BeakerCommand
from optparse import OptionValueError


class Cancel_Tasks(BeakerCommand):
    """Cancel Tasks"""
    enabled = True

    def options(self):
        self.parser.add_option(
            "--msg",
            default=None,
            help="Optional message to record as to why you cancelled",
        )

        self.parser.usage = "%%prog %s" % self.normalized_name


    def run(self, *args, **kwargs):
        username = kwargs.pop("username", None)
        password = kwargs.pop("password", None)
        msg = kwargs.pop("msg", None)

        self.set_hub(username, password)
        for task in args:
            print self.hub.taskactions.stop(task, 'cancel', msg)
