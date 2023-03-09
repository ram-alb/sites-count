"""Count sites by operators, vendors and regions."""

from sites_count.counter import beeline, kcell, tele2


def count_sites_total():
    """
    Count total sites number by technologies.

    Returns:
        dict
    """
    sites = {}
    operator_functions = {
        'kcell': kcell.count_kcell_sites,
        'tele2': tele2.count_tele2_sites,
        'beeline': beeline.count_beeline_sites,
    }
    for operator, func in operator_functions.items():
        operator_sites = func()
        for tech, sites_count in operator_sites.items():
            sites[f'{operator}_{tech}'] = sites_count
            sites[tech] = sites.setdefault(tech, 0) + sites_count
    return sites
