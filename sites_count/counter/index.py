"""Count sites by operators, vendors and regions."""

from sites_count.counter import kcell, tele2_beeline


def count_sites_total():
    """
    Count total sites number by technologies and operators.

    Returns:
        dict
    """
    sites = {}
    sites_by_operators = {
        'kcell': kcell.count_kcell_sites(),
        'tele2': tele2_beeline.count_tele2_bee_sites('tele2'),
        'beeline': tele2_beeline.count_tele2_bee_sites('beeline'),
    }
    for operator, operator_sites in sites_by_operators.items():
        for tech, sites_count in operator_sites.items():
            sites[f'{operator}_{tech}'] = sites_count
            sites[tech] = sites.setdefault(tech, 0) + sites_count
    return sites
