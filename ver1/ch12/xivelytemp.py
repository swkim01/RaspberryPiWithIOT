#!/usr/bin/env python

import os
import xively
import subprocess
import time, datetime
import requests
import Adafruit_DHT

FEED_ID="<FEED ID>"
API_KEY="<API KEY>"
DEBUG = True
sensor = Adafruit_DHT.DHT22
pin = 18

def read_temp():
  if DEBUG:
    print "reading temp"
  humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
  return temperature

# initialize api client
api = xively.XivelyAPIClient(API_KEY)

# function to return a datastream object.
# this either creates a new datastream, or returns an existing one
def get_datastream(feed):
  try:
    datastream = feed.datastreams.get("sensor1")
    if DEBUG:
      print "Found existing datastream"
    return datastream
  except:
    if DEBUG:
      print "Creating new datastream"
    datastream = feed.datastreams.create("sensor1", tags="temperature_01")
    return datastream

feed = api.feeds.get(FEED_ID)
datastream = get_datastream(feed)
datastream.max_value = None
datastream.min_value = None
while True:
    temp = read_temp()
    if DEBUG:
      print "Updating Xively feed with value: %{0:0.1f}s*C".format(temp)
    datastream.current_value = temp
    datastream.at = datetime.datetime.utcnow()
    try:
      datastream.update()
    except requests.HTTPError as e:
      print "HTTPError({0}): {1}".format(e.errno, e.strerror)
    time.sleep(10)
