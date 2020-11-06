import os


class EnvironmentVariables:
    @staticmethod
    def set(key_name, value, verbose=False):
        if verbose:
            print("{}={}".format(key_name, value))
        os.environ[key_name] = value
