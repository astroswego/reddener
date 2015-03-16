from argparse import ArgumentParser, FileType
from numpy import loadtxt, savetxt
from sys import stdin, stdout

import util

def get_args():
    parser = ArgumentParser(prog="reddener")

    parser.add_argument("-i", "--input", type=FileType("r"),
        default=stdin.buffer,
        help="Input table.")
    parser.add_argument("-f", "--format", type=str,
        default="%.8f",
        help="Output format specifier")

    args = parser.parse_args()

    return args

def main():
    args = get_args()

    data = loadtxt(args.input, dtype=float)

    color_excess  = data[1:,0 ]
    band_constant = data[0 ,1:]
    A_0           = data[1:,1:]

    corrected_A_0 = correct(A_0,
                            color_excess=color_excess,
                            band_constant=band_constant)

    savetxt(stdout.buffer, corrected_A_0, fmt=args.format)

    return 0

def correct(X, *, color_excess, band_constant):
    rows, cols = X.shape
    color_excess = util.colvec(color_excess)
    correction = band_constant * util.repeat_column(color_excess, cols)

    return X-correction

if __name__ == "__main__":
    exit(main())
