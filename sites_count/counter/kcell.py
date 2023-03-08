"""Count Kcell sites."""

import re

from sites_count.counter.counter import count_sites
from sites_count.sql import NetworkLive

gsm_select = """
    SELECT DISTINCT sitename
    FROM gsmcells2
    WHERE sitename IS NOT NULL AND operator = 'Kcell'
"""

wcdma_select = """
    SELECT DISTINCT sitename
    FROM wcdmacells2
    WHERE sitename IS NOT NULL AND operator = 'Kcell'
"""

lte_select = """
    SELECT DISTINCT sitename
    FROM ltecells2
    WHERE sitename IS NOT NULL AND subnetwork LIKE 'LTE_%'
"""

nr5g_select = """
    SELECT DISTINCT sitename
    FROM nrcells
    WHERE sitename IS NOT NULL
"""

iot_select = """
    SELECT DISTINCT sitename
    FROM iotcells
    WHERE sitename IS NOT NULL
"""


def parse_kcell_site_id(sitename):
    """
    Parse site id from site name.

    Args:
        sitename (str): a name of site

    Returns:
        str: a site id - 5 digits
    """
    site_id_obj = re.search(r'\d{5}', sitename)
    return site_id_obj.group()


def count_kcell_sites():
    """
    Count Kcell sites by technologies and total quantity.

    Returns:
        dict
    """
    sql_selects = {
        'gsm': gsm_select,
        'wcdma': wcdma_select,
        'lte': lte_select,
        'nr5g': nr5g_select,
        'iot': iot_select,
    }
    network_live = NetworkLive(sql_selects)
    return count_sites(network_live, parse_kcell_site_id)
