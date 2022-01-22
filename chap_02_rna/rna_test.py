""" Tests for rna.py """

from subprocess import getstatusoutput
import platform
import os.path
import re
import string
import random
import shutil

PRG = './rna.py'
RUN = f'python {PRG}' if platform.system() == 'Windows' else PRG
INPUT1 = 'data/input1.txt'
INPUT2 = 'data/input2.txt'
INPUT3 = 'data/input3.txt'


# --------------------------------------------------
def test_exists() -> None:
    """ Program exists """

    assert os.path.isfile(PRG)


# --------------------------------------------------
def test_usage() -> None:
    """ Usage statement exists """

    for flag in ['-h', '--help']:
        retval, out = getstatusoutput(f'{RUN} {flag}')
        assert retval == 0
        assert out.lower().startswith('usage:')


# --------------------------------------------------
def test_no_args() -> None:
    """ Dies on no args """

    retval, out = getstatusoutput(RUN)
    assert retval != 0
    assert out.lower().startswith('usage:')


# --------------------------------------------------
def test_bad_file() -> None:
    """ Die on missing input """

    bad = random_filename()
    retval, out = getstatusoutput(f'{RUN} {bad}')
    assert retval != 0
    assert re.match('usage:', out, re.IGNORECASE)
    assert re.search(f'No such file or directory: \'{bad}\'', out)


# --------------------------------------------------
def test_good_input1() -> None:
    """ Runs on good input1 with default output directory name """

    # - state default output directory name
    out_dir = 'output'
    try:
        # - if output directory "output" exists
        if os.path.isdir(out_dir):
            # - remove it and its contents
            shutil.rmtree(out_dir)

        # - run the source code with input1.txt
        retval, out = getstatusoutput(f'{RUN} {INPUT1}')
        # - check the programme runs without errors
        assert retval == 0
        # - check the output to the console
        assert out == ('data/input1.txt -> output/out_input1.txt\n'
                       'Wrote 1 file with 1 sequence in total to "output" directory.')
        # - check that "output" directory is created
        assert os.path.isdir(out_dir)
        out_file = os.path.join(out_dir, 'out_' + 'input1.txt')
        # - check that expected output file is created
        assert os.path.isfile(out_file)
        # - check that the output file is correct
        assert open(out_file).read().rstrip() == 'GAUGGAACUUGACUACGUAAAUU'

    # - remove the output directory
    finally:
        if os.path.isdir(out_dir):
            shutil.rmtree(out_dir)


# --------------------------------------------------
def test_good_input2() -> None:
    """ Runs on good input2 with an output directory name
     different from the default """

    # - state directory name
    out_dir = random_filename()
    try:
        # - if output directory output exists
        if os.path.isdir(out_dir):
            # - remove it and its contents
            shutil.rmtree(out_dir)

        # - run the source code with input2.txt
        retval, out = getstatusoutput(f'{RUN} {INPUT2} -o {out_dir}')
        # - check the programme runs without errors
        assert retval == 0
        # - check the output to the console
        assert out == (f'data/input2.txt -> {out_dir}/out_input2.txt\n'
                       f'Wrote 1 file with 2 sequences in total to "{out_dir}" directory.')
        # - check that the output directory is created
        assert os.path.isdir(out_dir)
        out_file = os.path.join(out_dir, 'out_' + 'input2.txt')
        # - check that expected output file is created
        assert os.path.isfile(out_file)
        # - check that the output file is correct
        assert open(out_file).read().rstrip() == ('UUAGCCCAGACUAGGACUUU\n'
                                                  'AACUAGUCAAAGUACACC')

    # - remove the output directory
    finally:
        if os.path.isdir(out_dir):
            shutil.rmtree(out_dir)


# --------------------------------------------------
def test_good_multiple_inputs():
    """ Runs on good inputs from multiple files"""

    out_dir = random_filename()
    try:
        if os.path.isdir(out_dir):
            shutil.rmtree(out_dir)

        retval, out = getstatusoutput(
            f'{RUN} --out_dir {out_dir} {INPUT1} {INPUT2} {INPUT3}')
        assert retval == 0
        assert out == (f'data/input1.txt -> {out_dir}/out_input1.txt\n'
                       f'data/input2.txt -> {out_dir}/out_input2.txt\n'
                       f'data/input3.txt -> {out_dir}/out_input3.txt\n'
                       f'Wrote 3 files with 5 sequences in total to "{out_dir}" directory.')
        assert os.path.isdir(out_dir)
        out_file1 = os.path.join(out_dir, 'out_' + 'input1.txt')
        out_file2 = os.path.join(out_dir, 'out_' + 'input2.txt')
        out_file3 = os.path.join(out_dir, 'out_' + 'input3.txt')
        assert os.path.isfile(out_file1)
        assert os.path.isfile(out_file2)
        assert os.path.isfile(out_file3)
        assert open(out_file1).read().rstrip() == 'GAUGGAACUUGACUACGUAAAUU'
        assert open(out_file2).read().rstrip() == ('UUAGCCCAGACUAGGACUUU\n'
                                                   'AACUAGUCAAAGUACACC')
        assert open(out_file3).read().rstrip() == output3().rstrip()

    finally:
        if os.path.isdir(out_dir):
            shutil.rmtree(out_dir)


# --------------------------------------------------
def random_filename() -> str:
    """ Generate a random filename """

    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))


# --------------------------------------------------
def output3() -> str:
    """ Output for 3rd input """

    return '\n'.join([('CUUAGGUCAGUGGUCUCUAAACUUUCGGUUCUGUCGUCUUCAUAGGCAAA'
                       'UUUUUGAACCGGCAGACAAGCUAAUCCCUGUGCGGUUAGCUCAAGCAACA'
                       'GAAUGUCCGAUCUUUGAACUUCCUAACGAACCGAACCUACUAUAAUUACA'
                       'UACGAAUAAUGUAUGGGCUAGCGUUGGCUCAUCAUCAAGUCUGCGGUGAA'
                       'AUGGGAACAUAUUCGCAUUGCAUAUAGGGCGUAUCUGACGAUCGAUUCGA'
                       'GUUGGCUAGUCGUACCAAAUGAUUAUGGGCUGGAGGGCCAAUGUAUACGU'
                       'CAGCCAGGCUAAACCACUGGACCGCUUGCAAUCCAUAGGAAGUAAAAUUA'
                       'CCCUUUUUAAACUCUCUAAGAUGUGGCGUCUCGUUCUUAAGGAGUAAUGA'
                       'GACUGUGACAACAUUGGCAAGCACAGCCUCAGUAUAGCUACAGCACCGGU'
                       'GCUAAUAGUAAAUGCAAACACCGUUUCAAGAGCCGAGCCUUUUUUUAAUG'
                       'CAAGGUGACUUCAGAGGGAGUAAAUCGUGGCCGGGGACUGUCCAGAGCAA'
                       'UGCAUUCCCGAGUGCGGGUACCCGUGGUGUGAGAGGAAUCGAUUUCGCGU'
                       'GUGAUACCAUUAAUGGUCCUGUACUACUGUCAGUCAGCUUGAUUUGAAGU'
                       'CGGCCGACAAGGUUGGUACAUAAUGGGCUUACUGGGAGCUUAGGUUAGCC'
                       'UCUGGAAAACUUUAGAAUUUAUAUGGGUGUUUCUGUGUUCGUACAGGCCC'
                       'CAGUCGGGCCAUCGUUGUUGAGCAUAGACCGGUGUAACCUUAAUUAUUCA'
                       'CAGGCCAAUCCCCGUAUACGCAUCUGAAAGGCACACCGCCUAUUACCAAU'
                       'UUGCGCUUCCUUACAUAGGAGGACCUGUUAUCGUCUUCUCAAUCGCUGAG'
                       'UUACCUUAAAACUAGGAUC'),
                      ('ACCGAGUAAAAGGCGACGGUUCGUUUCCGAACCUAUUUGCUCUUAUUUCU'
                       'ACGGGCUGCUAGUGUUGUAGGCUGCAAAACCUACGUAGUCCCAUCUAUCA'
                       'UGCUCGACCCUACGAGGCUAAUGUCUUGUCAGAGGCCCGUCAUGUGCCAC'
                       'GUACAUACACCAAUGUAUACCGCUCUAGCGGUUUGGUGUAGUAGGACUUG'
                       'UGUAUGCACGCUACAGCGAACAACGUUGAUCCCUAACUGAAGUCGGGCUC'
                       'CGCAGGCCUACUCACGCCGUUUCUAUAGGUUGAGCCGCAUCAAACAUUGG'
                       'GUUGAGUCUCGAGUAUAGAGGAAGGCUCUGGUGGCAGGCGCGACGUUGAU'
                       'CGGGAGGAGUAUGGAUGGUGAUCAAUCCCCGUGCCAAUCGCGAGUACUAC'
                       'AGGAGGAGGGGGCGGCUCUGUUCAAUCAUCACCCGUUCCAUCACACGGGC'
                       'AGCACAGUUGACCUCCCGAGCCGUCUCACGGACCUAGUGGCAACAGGUGU'
                       'AUUGAAGCGCCGGGAAUAGUCAUACCCGUGGGCUUGAUUGAGAGACCGAA'
                       'AUUCCGACCGCCAAAACUGCUGAUAUCGUACGCCUUACUACAAAACAAAU'
                       'GACGUCACUACCGGCCAGGGACAAGCUUAUUAAUUAAGUAGGAACCCUAU'
                       'ACCUUGCACAUCCUAAAUCUAGCAGCGGGUCCAGGAUUGGUUCCAGUCCA'
                       'ACGCGCGAUGCGCGUCAAGCUAGGCGAAUGACCACGGUCGAAACACCACU'
                       'UAUGUGACCCACCUUGGCCAACUCUCCCGAUUCUCCUCGCUACUAUCUUG'
                       'AAGGUCACUGAGAAUAUCCCUUAUGGGUCGCAUACGGAGACAGCCGCAGG'
                       'AGCCUUAACGGAGAAUACGCCAAUACUAUGUUCUGGGUCGGUGGGUGUAA'
                       'UGCGAUGCAAUCCGAUCGUGCGAACGUUCCCUUUGAUGACUAUAGGGUCU'
                       'AGUGAUCGUACAUGUGC')])
