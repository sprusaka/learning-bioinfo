# Transcribing DNA into RNA
https://rosalind.info/problems/rna/

## rna.py
### Input and output
`rna.py` will accept a single positional argument which can be a file or multiple files which contain one or more sequences of DNA.
It will also accept an optional argument to name an output directory.
The program then outputs transcribed DNA sequences in the output directory.
The program will print a "usage" statement for `-h` or `--help`flags:


```
$ ./rna.py -h
usage: rna.py [-h] [-o DIR] FILE [FILE ...]

-- Transcribing DNA into RNA

positional arguments:
  FILE                  Input DNA file(s)

optional arguments:
  -h, --help            show this help message and exit
  -o DIR, --out_dir DIR
                        Output directory (default: output)
```


### Tests
`rna_test.py `contains tests for `rna.py`. The test can be run using the Makefile:

```
$ make test
make[1]: Entering directory '/home/my/projects/learning-bioinfo/chap_02_rna'
pytest -xv && flake8 rna.py
================================================================= test session starts ==================================
platform linux -- Python 3.8.10, pytest-6.2.5, py-1.11.0, pluggy-1.0.0 -- /home/my/projects/biofx_python/venv/bin/python
cachedir: .pytest_cache
rootdir: /home/my/projects/learning-bioinfo/chap_02_rna
plugins: mypy-0.8.1, flake8-1.0.7, pylint-0.18.0
collected 7 items                                                                                                                                                                                                                       

rna_test.py::test_exists PASSED                                                                                   [ 14%]
rna_test.py::test_usage PASSED                                                                                    [ 28%]
rna_test.py::test_no_args PASSED                                                                                  [ 42%]
rna_test.py::test_bad_file PASSED                                                                                 [ 57%]
rna_test.py::test_good_input1 PASSED                                                                              [ 71%]
rna_test.py::test_good_input2 PASSED                                                                              [ 85%]
rna_test.py::test_good_multiple_inputs PASSED                                                                     [100%]

================================================================== 7 passed in 0.69s ===================================
```
## count_seqs.py
This script was written as a part of an exercise at the end of Chapter 2 in Mastering Python for Bioinformatics.

Inputs and outputs are the same as in `rna.py`, but the output is sequences length rather than transcribed RNA.

```
$ cat output/seq_input2.txt 
21
19
```
### To do:
Test suite still needs to be written for this script.
## Things learnt
* Defined an optional parameter for the command-line interface.
* Defined a list as a required positional argument to allow for multiple inputs.
* Opened, wrote to, iterated through, and closed files to handle input and output. 
* Created an output directory as part of the output.
* Created a separate script (`rna_test.py`) to test the source code.