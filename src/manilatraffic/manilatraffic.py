import requests


class ManilaTraffic:
    API_URL = 'http://mmda.ewoklabs.net/v1/traffic'

    def __init__(self, logger=None):
        self.logger = logger

    def fetch(self):
        try:
            r = requests.get(self.API_URL)
            status = r.status_code

            self.logger.info('HTTP Status: %s', status)

            if status == 200:
                return r.json()
            else:
                raise Exception("Non 200 status code!")

        except:
            self.logger.exception("Having trouble connecting to to the server")
            return False
