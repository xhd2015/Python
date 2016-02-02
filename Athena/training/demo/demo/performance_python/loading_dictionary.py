#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
import optparse
import sys
import time

def fillDict(map, nop, num, guid):
  before = time.time()

  for i in xrange(0, num):
    key = (i, guid)
    if not nop:
      map[key] = ([], {})

  after = time.time()
  elapsed = (after - before)
  if elapsed <= 0:
    divide = 1.0
  else:
    divide = elapsed
  elapsedTime = datetime.timedelta(seconds=int(elapsed))
  print("Inserting %d keys lasted %s (%d 1/s)" % (num, elapsedTime, (num / divide)))
  print("len(map) %d" % (len(map)))


def test0(nop, num):
  print("Inserting into one map")
  map = {}
  fillDict(map, nop, num, "0561c83c-9675-4e6f-bedc-86bcb6acfd71")
  fillDict(map, nop, num, "0561c83c-9675-4e6f-bedc-86bcb6acfd72")
  fillDict(map, nop, num, "0561c83c-9675-4e6f-bedc-86bcb6acfd73")
  print("total %d" % (len(map)))


def test1(nop, num):
  print("Inserting into three maps")
  map1 = {}
  map2 = {}
  map3 = {}
  fillDict(map1, nop, num, "0561c83c-9675-4e6f-bedc-86bcb6acfd71")
  fillDict(map2, nop, num, "0561c83c-9675-4e6f-bedc-86bcb6acfd72")
  fillDict(map3, nop, num, "0561c83c-9675-4e6f-bedc-86bcb6acfd73")
  total = 0
  for map in [map1, map2, map3]:
    total += len(map)
  print("total %d" % (total))



if __name__ == "__main__":
  usage = "USAGE: %prog [options]"
  description="test"
  version="%prog 1.0"

  parser = optparse.OptionParser(usage=usage, version=version, description=description)
  parser.add_option(
    "-t",
    "--testnum",
    action="store",
    dest="testnum",
    help="the number of the test to execute",
    type="int",
    default=1
  )
  parser.add_option(
    "-i",
    "--iterations",
    action="store",
    dest="iterations",
    help="the number of iterations",
    type="int",
    default=1000000
  )
  parser.add_option(
    "-n",
    "--nop",
    action="store_true",
    dest="nop",
    help="don't store in the dictionary only load and parse",
    default=False
  )

  (options, args) = parser.parse_args()

  testmap = {
    0:test0,
    1:test1,
  }

  test = testmap[options.testnum]

  print "\n\nrunning tests with GC DISABLED"
  import gc; gc.disable()
  test(options.nop, options.iterations)
  gc.enable()

  print "\n\nrunning tests with GC ENABLED"
  test(options.nop, options.iterations)
