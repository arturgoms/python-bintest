import yaml
from scripttest import TestFileEnvironment


class BinTest(object):
    def __init__(self):  # noqa
        self.input = None
        self.file_loaded = None
        self.env = None
        super(BinTest, self).__init__()

    def set_env(self, env, input):
        self.failureException = AssertionError
        self.env = TestFileEnvironment(env)
        self.input = input
        with open(self.input) as file:
            self.file_loaded = yaml.safe_load(file)

    def run_bin(self, name, use_names=False):
        binary = self.file_loaded[name]["bin"]
        args = []
        if len(self.file_loaded[name].values()) > 2:
            args = list(self.file_loaded[name].values())[1:-1]
        runned = self.env.run(binary, *args)
        return runned.stdout, runned.stderr

    def assertOutput(self, name, output, msg=None):
        if not self.file_loaded[name]["output"] == output:
            msg = (
                msg
                if msg is not None
                else f'Error: {self.file_loaded[name]["output"] } != {output}'
            )
            raise self.failureException(msg)
