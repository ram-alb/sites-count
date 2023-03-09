"""Test count sites functionality."""

from sites_count.counter import kcell
from sites_count.counter import tele2
from sites_count.counter import beeline
from sites_count.counter.index import count_sites_total


def fake_count_kcell_sites():
    return {
       'gsm': 3,
       'wcdma': 3,
       'lte': 2,
       'nr5g': 1,
       'iot': 1,
       'total': 4,
    }


def fake_count_tele2_sites():
    return {
       'gsm': 3,
       'wcdma': 3,
       'lte': 3,
       'total': 5,
    }


def fake_count_beeline_sites():
    return {
       'gsm': 2,
       'wcdma': 2,
       'lte': 2,
       'total': 4,
    }

def test_count_sites_total():
    kcell.count_kcell_sites = fake_count_kcell_sites
    tele2.count_tele2_sites = fake_count_tele2_sites
    beeline.count_beeline_sites = fake_count_beeline_sites

    sites = count_sites_total()
    assert sites['kcell_gsm'] == 3
