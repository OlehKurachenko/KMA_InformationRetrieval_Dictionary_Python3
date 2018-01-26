import sys


class CLIMain:
    """
    Class used to handle CLI for KMA_IR program.

    CLI:
        Flag is a command line argument which starts with '-'.
        There are two types of flags: one, that require arguments, and one
        which not (called non-arg flags). Non-arg flags can be grouped in one
        string (like '-nmlf', for ex.). Therefore, it is forbidden to have arg
        flag grouped with any other flag.

        Arguments without flag are taken as target files.

    -i  [dic_filename] : specifies an input dictionary, which will be imported
        before target files analysis, and new tokens will be added to this
        dictionary.

    -I  [dic_filename] : the same behaviour as -i, but output filename is
        specified the same as [dic_filename].

    -o  [out_filename] : specifies filename for output file. If file do not exist,
        it will be created, otherwise existing file will be rewritten.

    -a  forces program to use array (list) as data structure

    -t  forces program to print traces

        Commands are used to get some data about program. Commands line argument of
        command starts with "--", and can be only one CLA for call.

    --help  prints help

        TODO finish doc
    """

    __target = []
    __output = ""
    __input = []
    __printTraces = False

    __REUSAGE_ASSERT_STATEMENT = "This version of CLIMain do not support" \
                                 "multiple call during one execution"

    @staticmethod
    def __handle_flag(flags, i):
        print(flags)
        # TODO write
        return i

    @staticmethod
    def __handle_command(argv):
        print(argv)
        # TODO write
        return True

    @staticmethod
    def main():
        assert not CLIMain.__target, CLIMain.__REUSAGE_ASSERT_STATEMENT
        assert not CLIMain.__output, CLIMain.__REUSAGE_ASSERT_STATEMENT
        assert not CLIMain.__input, CLIMain.__REUSAGE_ASSERT_STATEMENT
        assert not CLIMain.__printTraces, CLIMain.__REUSAGE_ASSERT_STATEMENT

        if len(sys.argv) < 2:
            print(sys.argv[0] + ": usage: " + sys.argv[0] + " [-a|-t] "
                                                            "[-i dic_filename] "
                                                            "[-I dic_filename] "
                                                            "[-o out_filename] "
                                                            "[arguments]")
            print(sys.argv[0] + ": use " + sys.argv[0] + " --help")
        # TODO check "--" - type flags
        i = 1
        while i < len(sys.argv):
            if sys.argv[i][0] == '-':
                i = CLIMain.__handle_flag(sys.argv, i)
            else:
                CLIMain.__target.append(sys.argv[i])
            i += 1
