"""Count sites by operators, vendors and regions."""

from sites_count.counter.kcell import count_kcell_sites
from sites_count.counter.tele2 import count_tele2_sites


def count_sites_total():
    """
    Count total sites number by technologies.

    Returns:
        dict
    """
    sites = {}
    operator_functions = [
        count_kcell_sites,
        count_tele2_sites,
    ]
    for func in operator_functions:
        operator_sites = func()
        for tech, sites_count in operator_sites:
            sites[tech] = sites.setdefault(tech, 0) + sites_count
    return sites
