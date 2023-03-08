"""Count sites by technologies."""


def parse_site_id(sitename: str):
    """
    Parse site id from sitename.

    Args:
        sitename: a site name

    Returns:
        str
    """
    return sitename


def count_sites(network_live: object, parse_id=parse_site_id):
    """
    Count sites by Network Live instance.

    Args:
        network_live: NetworkLive instance
        parse_id: function to parse site_id from site name

    Returns:
        dict
    """
    unique_ids = set()
    sites = {}
    for tech in network_live.sql_selects.keys():
        selected_sites = network_live.execute_sql('select', tech)
        site_ids = {parse_id(*row) for row in selected_sites}
        sites[tech] = len(site_ids)
        unique_ids.update(site_ids)
    sites['total'] = len(unique_ids)
    return sites
