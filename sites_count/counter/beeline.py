"""Count Tele2 sites."""

from sites_count.counter.counter import count_sites
from sites_count.sql import NetworkLive

gsm_select = """
    SELECT DISTINCT sitename
    FROM gsmcells2
    WHERE sitename IS NOT NULL AND operator = 'Beeline'
"""

wcdma_select = """
    SELECT DISTINCT sitename
    FROM wcdmacells2
    WHERE sitename IS NOT NULL AND operator = 'Beeline'
"""

lte_select = """
    SELECT DISTINCT sitename
    FROM ltecells2
    WHERE sitename IS NOT NULL AND subnetwork = 'Beeline'
"""


def count_beeline_sites():
    """
    Count Beeline sites.

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
