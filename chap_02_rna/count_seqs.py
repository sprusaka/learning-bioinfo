#!/usr/bin/env python3
"""
Purpose: Calculating lengths of input sequences
"""

import argparse
from typing import NamedTuple, List, TextIO
import os
from statistics import mean


class Args(NamedTuple):
    """ Command-line arguments """
    file: List[TextIO]
    out_dir: str


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='-- Calculating sequence length',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input sequence file(s)',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('rt'))

    parser.add_argument('-o',
                        '--out_dir',
                        help='Output directory',
                        metavar='DIR',
                        type=str,
                        default='output')

    args = parser.parse_args()

    return Args(file=args.file, out_dir=args.out_dir)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()

    if not os.path.isdir(args.out_dir):
        os.makedirs(args.out_dir)

    seq_lengths = []
    for filehandle in args.file:
        out_file = os.path.join(args.out_dir,
                                'seq_' + os.path.basename(filehandle.name))
        with open(out_file, 'wt') as out_filehandle:
            for dna in filehandle:
                length = len(dna)
                seq_lengths.append(length)
                out_filehandle.write(str(length))
        print(filehandle.name, '->', out_file)

    if len(seq_lengths) == 1:
        print(f'Input file contains 1 sequence'
              f'of {seq_lengths[0]} base pairs.')
    else:
        print(f'The average length of all processed sequences '
              f'is {mean(seq_lengths)} base pairs.\n'
              f'The longest sequence is {max(seq_lengths)} '
              f'and the shortest sequence is {min(seq_lengths)}.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
