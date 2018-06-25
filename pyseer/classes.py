from collections import namedtuple

LMM = namedtuple('LMM', ['kmer', 'pattern',
                         'af', 'prep', 'pvalue',
                         'kbeta', 'bse', 'frac_h2',
                         'max_lineage',
                         'kstrains', 'nkstrains',
                         'notes',
                         'prefilter', 'filter'])

Enet = namedtuple('Enet', ['kmer', 'af', 'kbeta',
                            'max_lineage', 'kstrains',
                            'nkstrains'])

Seer = namedtuple('Seer', ['kmer', 'pattern',
                           'af', 'prep', 'pvalue',
                           'kbeta', 'bse',
                           'intercept', 'betas',
                           'max_lineage',
                           'kstrains', 'nkstrains',
                           'notes',
                           'prefilter', 'filter'])
