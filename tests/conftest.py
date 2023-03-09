"""Custom fixtures for tests."""

import pytest


def get_fake_execute_sql(selects: dict):
    """
    Prepare fake_execute_sql function.

    Args:
        selects: fake sql select results

    Returns:
        function
    """
    def fake_execute_sql(self, sql_type: str, table: str):
        if sql_type == 'select':
            return selects[table]
    return fake_execute_sql


@pytest.fixture()
def fake_kcell_execute_sql():
    """
    Fake exequte_sql function to get Kcell sites for tests.

    Returns:
        function
    """
    selects = {
        'gsm': [
            ('42468SHORJANDIL',),
            ('51002DISTR11H6',),
            ('42828TURKONGRES',),
        ],
        'wcdma': [
            ('42468SHORJANDIL',),
            ('51002DISTR11H6',),
            ('42828TURKONGRES',),
        ],
        'lte': [('ERBS_51002_DISTR11_KB',), ('gRBS_42828_TURKONGRES',)],
        'nr5g': [('gRBS_42828_TURKONGRES',)],
        'iot': [('ERBS_06076_SHEVSHENKO_2KB',)],
    }

    return get_fake_execute_sql(selects)


@pytest.fixture()
def fake_tele2_execute_sql():
    """
    Fake exequte_sql function to get Tele2 sites for tests.

    Returns:
        function
    """
    selects = {
        'gsm': [('AL4099',), ('AL8310',), ('UK9201',)],
        'wcdma': [('AL4099',), ('AL8310',), ('UK7331',)],
        'lte': [('AL4099',), ('AL8310',), ('SE4029',)],
    }
    return get_fake_execute_sql(selects)


@pytest.fixture()
def fake_beeline_execute_sql():
    """
    Fake exequte_sql function to get Beeline sites for tests.

    Returns:
        function
    """
    selects = {
        'gsm': [('KOK_Business_GU21L821BK',), ('KOK_Sadik_GU21L821BK',)],
        'wcdma': [('KOK_Business_GU21L821BK',), ('KAR_Aktailak_UL21BKTZ',)],
        'lte': [('KOK_Business_GU21L821BK',), ('NUR_Zemkom_nL81821GU21BK',)],
    }
    return get_fake_execute_sql(selects)
