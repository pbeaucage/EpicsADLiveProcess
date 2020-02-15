


class CollateDaemon(threading.Thread):
    def __init__(self,app,reduction_queue,**kwargs):
        app.logger.info('Creating CollateDaemon thread')

        threading.Thread.__init__(self,name='CollateDaemon',daemon=True)
        self._stop = False
        self._app = app

        self.reduction_queue = reduction_queue

        self.detector = AreaDetectorLive(**kwargs)

    def terminate(self):
        self._app.logger.info('Terminating CollateDaemon thread')
        self._stop = True

    def run(self):
        while not self._stop:
            tempval = self.detector.queuehandler()
            if tempval is not None:
                self.reduction_queue.put(tempval)
            time.sleep(0.1)
        self._app.logger.info('CollateDaemon runloop exiting')
