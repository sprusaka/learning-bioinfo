# Counting DNA nucleotides
https://rosalind.info/problems/dna/

## Input and output
`dna.py` will accept a single positional argument which can be either a string or a file containing a string.
The program will print a "usage" statement for `-h` or `--help`flags:


```
$ ./dna.py -h
usage: dna.py [-h] str

-- Counting DNA nucleotides

positional arguments:
  str         A string of nucleotides in a file or via command line

optional arguments:
  -h, --help  show this help message and exit

```

The program will output a text file with base names in the first column and base counts in the second column.
The file will be written to a pre-created `output` directory.

```
$ ./dna.py ATGC
Counting is done!
'output.txt' is in the directory out :)
A: 1 (25%)
C: 1 (25%)
G: 1 (25%)
T: 1 (25%)
$ cat output/output.txt 
A       1
C       1
G       1
T       1
```
The program can only read and output one file at each run.

## Tests
`count()` function in `dna.py` is tested with `count_test()`:

`$ pytest dna.py`


## Things learnt
* Writing a simple unit test for the `count()` function which is placed in the source code.
* Using `argparse` module to define and validate arguments and to generate documentation.
* Using a file as an input.


**To do:**

* Create a complete set of tests for `dna.py` in a separate directory.
* Create a `Makefile` to run all the tests.