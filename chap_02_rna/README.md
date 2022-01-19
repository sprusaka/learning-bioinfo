# Transcribing DNA into RNA
https://rosalind.info/problems/rna/
## Input and output
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


## Tests
`rna_test.py `contains tests for `rna.py`. The test can be run using the Makefile:


```
$ make test
pytest -xv
=========================================== test session starts ========================================================
platform linux -- Python 3.8.10, pytest-6.2.5, py-1.11.0, pluggy-1.0.0 -- /home/my/projects/biofx_python/venv/bin/python
cachedir: .pytest_cache
rootdir: /home/my/projects/learning-bioinfo/chap_02_rna
plugins: mypy-0.8.1, flake8-1.0.7, pylint-0.18.0
collected 5 items                                                                                                                                                                                                                       

rna_test.py::test_exists PASSED                                                            [ 20%]
rna_test.py::test_usage PASSED                                                             [ 40%]
rna_test.py::test_no_args PASSED                                                           [ 60%]
rna_test.py::test_bad_file PASSED                                                          [ 80%]
rna_test.py::test_good_input1 PASSED                                                       [100%]

============================================ 5 passed in 0.78s =========================================================
```

**To do:**
* Finish the set of tests to go through on all files in "data" directory (so far only `input1.txt` is used).
* Write up things learnt this chapter.