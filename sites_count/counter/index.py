"""Count sites by operators, vendors and regions."""

from sites_count.counter.kcell import count_kcell_sites


def count_sites_total():
    """
    Count sites by operators, vendors and regions.

    Returns:
        dict
    """
    return count_kcell_sites()
