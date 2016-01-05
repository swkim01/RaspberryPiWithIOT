#!/usr/bin/env python

import os
import xively
import subprocess
import time, datetime
import requests


FEED_ID = os.environ["FEED_ID"]
API_KEY = os.environ["API_KEY"]
DEBUG = os.environ["DEBUG"] or False

api = xively.XivelyAPIClient(API_KEY)

def read_loadavg():
  if DEBUG:
    print "reading load average"
  return subprocess.check_output(["awk '{print $1}' /proc/loadavg"], shell=True)

def get_datastream(feed):
  try:
    datastream = feed.datastreams.get("load_avg")
    if DEBUG:
      print "Found existing datastream"
    return datastream
  except:
    if DEBUG:
      print "Creating new datastream"
    datastream = feed.datastreams.create("load_avg", tags="load_01")
    return datastream

def run():
  print "Starting Xively tutorial script"
  feed = api.feeds.get(FEED_ID)
  datastream = get_datastream(feed)
  datastream.max_value = None
  datastream.min_value = None
  while True:
    load_avg = read_loadavg()

    if DEBUG:
      print "Updating Xively feed with value: %s" % load_avg
    datastream.current_value = load_avg
    datastream.at = datetime.datetime.utcnow()
    try:
      datastream.update()
    except requests.HTTPError as e:
      print "HTTPError({0}): {1}".format(e.errno, e.strerror)
    time.sleep(10)

run()
