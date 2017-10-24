"""
Plots with jitter.
"""

import sys
import argparse
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def main(source_fn):
    print("Working on file: ", source_fn)
    df = pd.read_csv(source_fn, sep='\t')
    df["hapfreq"] = df["hapfreq"]*200
    print(df)

    sns.set_style("whitegrid")

    #ax = sns.stripplot(y="distocon", data=df, jitter=True, size=df["hapfreq"])

    ax = sns.violinplot(y="distocon", data=df, inner = None, color=".8")
    #ax = sns.stripplot(y="distocon", data=df, jitter=True)
    ax = sns.swarmplot(y="distocon", data=df) # size=df["hapfreq"]
    plt.show()


if __name__ == "__main__":
    if not sys.version_info >= (3,2):
        print("Please run using python version >= 3.2\nNow exiting")
        sys.exit()

    parser = argparse.ArgumentParser(description='Python script to glycosylate a protein. Input is a pdb file, output '
                                                 'is a glycosylated pdb file.')
    parser.add_argument('-source_csv_file', '--source_csv_file', type=str,
                        help='The source csv file to plot data from.', required=True)

    args = parser.parse_args()

    in_file = args.source_csv_file

    main(in_file)
