# Copyright 2018 Marco Galardini and John Lees

'''Save a model from pyseer output'''


def get_options():
    import argparse

    description = 'Save model from pyseer output'
    parser = argparse.ArgumentParser(description=description)

    parser.add_argument('table',
                        help='Pyseer output')
    parser.add_argument('output',
                        help='Model prefix')

    parser.add_argument('--p-cutoff',
                        type=float,
                        default=1,
                        help='Cutoff on lrt-pvalue for inclusion')
    parser.add_argument('--continuous',
                        action='store_true',
                        default=False,
                        help='Model is for a continuous phenotype'
                             ' [default is binary]')

    return parser.parse_args()


def main():
    options = get_options()

    import pickle
    import pandas as pd

    pyseer_out = pd.read_table(options.table,
                      usecols=['variant','af','lrt-pvalue','beta'])

    pred_model = {}
    for row in pyseer_out.itertuples():
        if row[3] > options.p_cutoff:
            pred_model[row.variant] = (row.af, row.beta)

    with open(options.output + '_model.pkl', 'wb') as pickle_file:
        pickle.dump([pred_model, options.continuous], pickle_file)


if __name__ == "__main__":
    main()
