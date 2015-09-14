#!/usr/bin/env python

import os
import sys
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
    # create file handler which logs even debug messages
    fh = logging.FileHandler('/var/log/manila-traffic.log')
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)

    # Add handler(s)
    logger.addHandler(fh)
    logger.addHandler(ch)

    logger.info("Fetch traffic data...")

    try:
        filename = sys.argv[1]
    except:
        logger.info("Invalid arguments! To use: 'python run.py <path to outupt file>")
        sys.exit(2)

    mt = ManilaTraffic(logger=logger)
    traffic_data = mt.fetch()

    if isinstance(traffic_data, dict):
        with open(filename, mode='a') as f:
            f.write(json.dumps(traffic_data))
            f.write(os.linesep)

            logger.info("Success!")
