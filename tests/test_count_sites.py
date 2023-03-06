"""Test count sites functionality."""

from sites_count.counter.index import count_sites_total
from sites_count.sql import NetworkLive


def test_count_sites_total():
    """Test count_sites_total function."""

    def fake_execute_sql(self, sql_type, table):
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

        if sql_type == 'select':
            return selects[table]

    NetworkLive.execute_sql = fake_execute_sql
    sites = count_sites_total()

    assert sites['gsm'] == 3
    assert sites['lte'] == 2
    assert sites['total'] == 4
