"""Count Tele2 sites."""

from sites_count.counter.counter import count_sites
from sites_count.sql import NetworkLive

gsm_select = """
    SELECT DISTINCT sitename
    FROM gsmcells2
    WHERE sitename IS NOT NULL AND operator = 'Tele2'
"""

wcdma_select = """
    SELECT DISTINCT sitename
    FROM wcdmacells2
    WHERE sitename IS NOT NULL AND operator = 'Tele2'
"""

lte_select = """
    SELECT DISTINCT sitename
    FROM ltecells2
    WHERE sitename IS NOT NULL AND subnetwork = 'Tele2'
"""


def count_tele2_sites():
    """
    Count Tele2 sites.

    Returns:
        dict
    """
    sql_selects = {
        'gsm': gsm_select,
        'wcdma': wcdma_select,
        'lte': lte_select,
    }
    network_live = NetworkLive(sql_selects)
    return count_sites(network_live)
