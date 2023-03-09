"""Count Tele2 and Beeline sites."""

from sites_count.counter.counter import count_sites
from sites_count.sql import NetworkLive

tele2_gsm_select = """
    SELECT DISTINCT sitename
    FROM gsmcells2
    WHERE sitename IS NOT NULL AND operator = 'Tele2'
"""

tele2_wcdma_select = """
    SELECT DISTINCT sitename
    FROM wcdmacells2
    WHERE sitename IS NOT NULL AND operator = 'Tele2'
"""

tele2_lte_select = """
    SELECT DISTINCT sitename
    FROM ltecells2
    WHERE sitename IS NOT NULL AND subnetwork = 'Tele2'
"""

beeline_gsm_select = """
    SELECT DISTINCT sitename
    FROM gsmcells2
    WHERE sitename IS NOT NULL AND operator = 'Beeline'
"""

beeline_wcdma_select = """
    SELECT DISTINCT sitename
    FROM wcdmacells2
    WHERE sitename IS NOT NULL AND operator = 'Beeline'
"""

beeline_lte_select = """
    SELECT DISTINCT sitename
    FROM ltecells2
    WHERE sitename IS NOT NULL AND subnetwork = 'Beeline'
"""


def count_tele2_bee_sites(operator: str):
    """
    Count Tele2 and Beeline sites.

    Args:
        operator: an operator name

    Returns:
        dict
    """
    tele2_sql_selects = {
        'gsm': tele2_gsm_select,
        'wcdma': tele2_wcdma_select,
        'lte': tele2_lte_select,
    }
    beeline_sql_selects = {
        'gsm': beeline_gsm_select,
        'wcdma': beeline_wcdma_select,
        'lte': beeline_lte_select,
    }
    if operator == 'tele2':
        network_live = NetworkLive(tele2_sql_selects)
    elif operator == 'beeline':
        network_live = NetworkLive(beeline_sql_selects)
    return count_sites(network_live)
