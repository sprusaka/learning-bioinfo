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

The program will output a text file in the `output` directory with base names in the first column and base counts in the second column.

```
$ ./dna.py ATGC
Counting is done!
Output "output.txt" is in the output/ directory :)
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


**To do:**

* Create a complete set of tests for `dna.py` in a separate directory.
* Create a `Makefile` to run all the tests.