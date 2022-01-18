#!/usr/bin/env python3
"""
Purpose: Counting DNA nucleotides
Rosalind ID: DNA
"""

import argparse
from typing import NamedTuple, Tuple, Dict
import os


class Args(NamedTuple):
    """ Command-line arguments """
    dna: str


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='-- Counting DNA nucleotides',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('dna',
                        metavar='str',
                        help='A string of nucleotides as a raw string or file')

    args = parser.parse_args()

    # -- Add an option to upload a file
    # - check if file is an existing file
    if os.path.isfile(args.dna):
        # - read file
        # - remove whitespace
        args.dna = open(args.dna).read().rstrip()

    return Args(args.dna)


# --------------------------------------------------
def main():
    """ Execute all functions in the module """

    # -- Get args.dna which is our DNA string
    args = get_args()

    # -- Run the count function to get base counts
    count_a, count_c, count_g, count_t = count(args.dna)

    # -- Make a dict out of base names and base counts
    bases_dict = make_dict(count_a, count_c, count_g, count_t)

    # -- Output .txt file with base names in col1 and base counts in col2
    output(bases_dict)

    # -- Print message
    print("Counting is done!\n"
          "'output.txt' is in the directory out :)")
    message(count_a, count_c, count_g, count_t, bases_dict)


# --------------------------------------------------
def count(dna: str) -> Tuple[int, int, int, int]:
    """ Count the nucleotides """

    # - convert all characters to uppercase
    dna = dna.upper()

    # - count the four bases
    count_a = dna.count('A')
    count_c = dna.count('C')
    count_g = dna.count('G')
    count_t = dna.count('T')

    return count_a, count_c, count_g, count_t


# --------------------------------------------------
def test_count() -> None:
    """ Test count() function """

    # empty string returns zeros
    assert count('') == (0, 0, 0, 0)
    # characters other than ACGT return zeros
    assert count('1234QWERY') == (0, 0, 0, 0)
    # counts all four bases
    assert count('ACGT') == (1, 1, 1, 1)
    # counts bases in the correct order
    assert count('ACCGGGTTTT') == (1, 2, 3, 4)
    # counts lowercase bases
    assert count('acgt') == (1, 1, 1, 1)


# --------------------------------------------------
def make_dict(count_a: int,
              count_c: int,
              count_g: int,
              count_t: int) -> Dict[str, int]:
    """ Make a dictionary with base names as keys and base counts as values """

    bases_dict = {'A': count_a, 'C': count_c, 'G': count_g, 'T': count_t}

    return bases_dict


# --------------------------------------------------
def output(bases_dict: Dict[str, int]) -> None:
    """ Output into a text file """

    with open('output/output.txt', 'w') as file:
        for key, value in bases_dict.items():
            file.write(f'{key}\t{value}\n')


# --------------------------------------------------
def message(count_a: int,
            count_c: int,
            count_g: int,
            count_t: int,
            bases_dict: Dict[str, int]) -> None:
    """ Get % content for each base and print it """

    # -- Count the number of all bases
    n_all_bases = count_a + count_c + count_g + count_t

    # -- Update the dictionary with % content
    for base, base_count in bases_dict.items():
        bases_dict[base] = round(base_count / n_all_bases * 100)

    # -- Print base counts and their % content
    print(f"A: {count_a} ({bases_dict['A']}%)\n"
          f"C: {count_c} ({bases_dict['C']}%)\n"
          f"G: {count_g} ({bases_dict['G']}%)\n"
          f"T: {count_t} ({bases_dict['T']}%)")


# --------------------------------------------------
if __name__ == '__main__':
    main()
