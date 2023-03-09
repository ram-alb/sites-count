"""Test functions which count sites by operators."""

from sites_count.counter.kcell import count_kcell_sites
from sites_count.counter.tele2_beeline import count_tele2_bee_sites
from sites_count.sql import NetworkLive


def test_count_kcell_sites(fake_kcell_execute_sql):
    """
    Test count_kcell_sites function.

    Args:
        fake_kcell_execute_sql: fixture function
    """
    NetworkLive.execute_sql = fake_kcell_execute_sql
    sites = count_kcell_sites()

    assert sites['gsm'] == 3
    assert sites['lte'] == 2
    assert sites['total'] == 4


def test_count_tele2_sites(fake_tele2_execute_sql):
    """
    Test count_tele2_sites function.

    Args:
        fake_tele2_execute_sql: fixture function
    """
    NetworkLive.execute_sql = fake_tele2_execute_sql
    sites = count_tele2_bee_sites('tele2')

    assert sites['gsm'] == 3
    assert sites['wcdma'] == 3
    assert sites['lte'] == 3
    assert sites['total'] == 5


def test_count_beeline_sites(fake_beeline_execute_sql):
    """Test count_tele2_sites function.

    Args:
        fake_beeline_execute_sql: fixture function
    """
    NetworkLive.execute_sql = fake_beeline_execute_sql
    sites = count_tele2_bee_sites('beeline')

    assert sites['gsm'] == 2
    assert sites['wcdma'] == 2
    assert sites['lte'] == 2
    assert sites['total'] == 4
