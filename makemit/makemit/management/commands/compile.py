import os
import sys
import subprocess
import signal
import time
from optparse import make_option

from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('-w',
            help="spawn a watch command",
            action="store_true",
            dest="watch"
            ),
        )
    def handle(self, *args, **options):
        watch = False
        if options['watch']:
            watch = True
        params = ['', '-w'][watch]
        stylus = subprocess.Popen('../node_modules/.bin/stylus %s makemit/static/stylesheets/*.styl -o makemit/static/stylesheets/' % params,
        	shell=True, preexec_fn=os.setsid)

        def signal_handler(sig, fname):
        	os.killpg(stylus.pid, signal.SIGTERM)
        	sys.exit(0)
        signal.signal(signal.SIGINT, signal_handler)

        if watch:
            time.sleep(1)
            signal.pause()
        else:
            try:
                os.waitpid(-1, 0)
                os.waitpid(-1, 0)
            except OSError:
                pass