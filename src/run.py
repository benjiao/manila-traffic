#!/usr/bin/env python

import os
import json
import logging
from manilatraffic import ManilaTraffic

FILENAME = 'manilatraffic.json'

if __name__ == '__main__':
    logger = logging.getLogger(__name__)

    # Set Logging Level
    logger.setLevel(logging.DEBUG)

    # Set Log Format
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

    # Create Handler (with own logging level)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)

    # Add handler(s)
    logger.addHandler(ch)

    logger.info("Fetch traffic data...")

    mt = ManilaTraffic(logger=logger)
    traffic_data = mt.fetch()

    if isinstance(traffic_data, dict):
        with open(FILENAME, mode='a') as f:
            f.write(json.dumps(traffic_data))
            f.write(os.linesep)

    print json.dumps(mt.fetch(), indent=4)
