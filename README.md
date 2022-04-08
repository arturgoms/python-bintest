# Bintest

Bintest is a extension for `unitest`, it will provide a way to run a command and assert the output.

## Installation

``` shell
pip install bintest
```

### Usage

1. Create a file in your project: testcase.py for example
``` python
from bintest import bintest
import unittest


class MyTestCase(unittest.TestCase, bintest.BinTest):
    __test__ = True

    def setUp(self):
        self.set_env(
            env="./output",  # temp dir
            input="./tests_case.yml",  # yml file
        )

    # This works
    def test_simple_cat(self):
        output, err = self.run_bin(name="SimpleCAT")
        # two ways of test, this both will do exactly the same
        self.assertEqual(output, "test\n")
        # this one is more auto because is reading from the yml
        self.assertOutput(name="SimpleCAT", output=output)

    # This Fails
    def test_simple_cat_fail(self):
        output, err = self.run_bin(name="SimpleCATFail")
        # this one will fail
        self.assertOutput(name="SimpleCATFail", output=output)


if __name__ == "__main__":
    unittest.main()
```

2. Create the config file: tests_case.yml

``` yaml
---

# Example test file
# required: bin, output
# everything in the middle will be passing as paramters to the binary: only the values

SimpleCAT:
  bin: /bin/cat
  path: /Users/artur.gomes/projects/pybintest/examples/test.txt
  output: "test\n"

SimpleCATFail:
  bin: /bin/cat
  path: /Users/artur.gomes/projects/pybintest/examples/test.txt
  output: "not test\n"
```

In this case we are testing the cat command, using a file test.txt as argument and expecting the output

3. Create the test.txt file

``` sh
test
```


4. Then run:

``` shell
python3 -m unittest discover  -vvv
```

5. Unittest will find yout test and run it for you.

``` shell
test_simple_cat (testcase.MyTestCase) ... ok
test_simple_cat_fail (testcase.MyTestCase) ... FAIL

======================================================================
FAIL: test_simple_cat_fail (testcase.MyTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/artur.gomes/projects/test_bintest/testcase.py", line 26, in test_simple_cat_fail
    self.assertOutput(name="SimpleCATFail", output=output)
  File "/Users/artur.gomes/Library/Caches/pypoetry/virtualenvs/test-bintest-LukI1uz2-py3.9/lib/python3.9/site-packages/bintest/bintest.py", line 34, in assertOutput
    raise self.failureException(msg)
AssertionError: Error: not test
 != test


----------------------------------------------------------------------
Ran 2 tests in 0.011s

FAILED (failures=1)
```

## Contribution

If this helps you consider help me to improve.
