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
