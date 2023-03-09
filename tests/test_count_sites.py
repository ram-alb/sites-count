"""Test count sites by technologies."""

from sites_count.counter import kcell, tele2_beeline
from sites_count.counter.index import count_sites_total


def fake_count_kcell_sites():
    """
    Fake count_kcell_sites used only for tests.

    Returns:
        dict
    """
    return {
        'gsm': 3,
        'wcdma': 3,
        'lte': 2,
        'nr5g': 1,
        'iot': 1,
        'total': 4,
    }


def fake_count_tele2_bee_sites(operator: str):
    """
    Fake count_tele2_bee_sites used only for tests.

    Args:
        operator: a name of operator

    Returns:
        dict
    """
    if operator == 'tele2':
        return {
            'gsm': 3,
            'wcdma': 3,
            'lte': 3,
            'total': 5,
        }
    elif operator == 'beeline':
        return {
            'gsm': 2,
            'wcdma': 2,
            'lte': 2,
            'total': 4,
        }


def test_count_sites_total():
    """Test count_sites_total function."""
    kcell.count_kcell_sites = fake_count_kcell_sites
    tele2_beeline.count_tele2_bee_sites = fake_count_tele2_bee_sites

    sites = count_sites_total()
    assert sites['kcell_gsm'] == 3
    assert sites['tele2_lte'] == 3
    assert sites['beeline_total'] == 4
    assert sites['wcdma'] == 8
    assert sites['total'] == 13
