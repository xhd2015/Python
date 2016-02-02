"""Some nosetests for the 'functions' module."""

from nose.tools import assert_equal, assert_raises

import numpy

from functions import Channel, ChannelClosedError


def test_calibrate():
    c = Channel()
    param = 99
    c.calibrate(param)
    assert_equal(c.status, param)

def test_write_str():
    c = Channel()
    result = c.write('ABC')
    expected = 65 + 66 + 67
    assert_equal(result, expected)

def test_write_array():
    c = Channel()
    data = numpy.array([1, 2, 3], dtype=numpy.uint8)
    result = c.write(data)
    expected = data.sum()
    assert_equal(result, expected)

def test_write_list():
    c = Channel()
    data = [1, 2, 3]
    result = c.write(data)
    expected = sum(data)
    assert_equal(result, expected)

def test_channel_closed1():
    c = Channel()
    c.close()
    assert_raises(ChannelClosedError, c.calibrate, 99)

def test_channel_closed2():
    c = Channel()
    c.close()
    assert_raises(ChannelClosedError, lambda: c.status)
