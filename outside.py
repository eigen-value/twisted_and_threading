import threading
import time

from twisted.internet import threads


class ServiceUsingThreadingAndDeferred():
    def __init__(self):
        pass

    def start(self):
        print "3rd party API service starting..."
        self.run_as_thread()

    def run_as_thread(self, *args, **kwargs):
        t = threading.Thread(target=self.run_forever, args=args, kwargs=kwargs)
        t.daemon = True
        t.start()

    def run_forever(self):
        while 1:
            print "Doing something remote..."
            time.sleep(1)
            now = time.time()
            if 1 > now % 5 >= 0:
                self.defer_activity()

    def defer_activity(self):
        threads.deferToThread(self._activity)

    def _activity(self):
        print "Deferring Happily"