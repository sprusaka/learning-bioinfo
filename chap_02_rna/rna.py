#!/usr/bin/env python3
"""
Purpose: Transcribing DNA into RNA
Rosalind ID: RNA
"""

import argparse
from typing import NamedTuple, List, TextIO
import os


class Args(NamedTuple):
    """ Command-line arguments """
    file: List[TextIO]
    out_dir: str


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='-- Transcribing DNA into RNA',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input DNA file(s)',
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

    # -- Create output directory if it doesn't exist
    if not os.path.isdir(args.out_dir):
        os.makedirs(args.out_dir)

    # -- Transcribe DNA and write output in 'out' directory
    n_files, n_seqs = 0, 0
    for filehandle in args.file:
        # - count files
        n_files += 1
        # - name the output files
        out_file = os.path.join(args.out_dir,
                                'out_' + os.path.basename(filehandle.name))

        # - open an output file in the output directory
        with open(out_file, 'wt') as out_filehandle:
            # - write the transcribed seq to output file
            for dna in filehandle:
                # - update the number of seqs transcribed
                n_seqs += 1
                # - update the number of files transcribed
                out_filehandle.write(dna.replace('T', 'U'))
        # - print as output files get written
        print(filehandle.name, '->', out_file)

    # -- Print out a message
    print(f'Wrote {n_files} file{"" if n_files == 1 else "s"} '
          f'with {n_seqs} sequence{"" if n_seqs == 1 else "s"} in total '
          f'to "{args.out_dir}" directory.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
