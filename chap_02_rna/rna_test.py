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
    assert re.search(f"No such file or directory: '{bad}'", out)


# --------------------------------------------------
def test_good_input1() -> None:
    """ Runs on good input """

    out_dir = 'output'
    try:
        if os.path.isdir(out_dir):
            shutil.rmtree(out_dir)

        retval, out = getstatusoutput(f'{RUN} {INPUT1}')
        assert retval == 0
        assert out == 'data/input1.txt -> output/out_input1.txt\n' \
                      'Wrote 1 file with 1 sequence in total to "output" directory.'
        assert os.path.isdir(out_dir)
        out_file = os.path.join(out_dir, 'out_' + 'input1.txt')
        assert os.path.isfile(out_file)
        assert open(out_file).read().rstrip() == 'GAUGGAACUUGACUACGUAAAUU'

    finally:
        if os.path.isdir(out_dir):
            shutil.rmtree(out_dir)


# --------------------------------------------------
def random_filename() -> str:
    """ Generate a random filename """

    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))