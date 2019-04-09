import time

import pymongo
import requests


def scrape_asset_manager():
    """Scrape data from the BigCo asset manager site"""
    pass


def pull_excavator_stats():
    """Pull from the GET excavator_stats endpoint"""
    pass


def pull_can_data():
    """Pull from the GET can_stream endpoint"""
    pass

while True:
    scrape_asset_manager()
    pull_excavator_stats()
    pull_can_data()
    time.sleep(30)
