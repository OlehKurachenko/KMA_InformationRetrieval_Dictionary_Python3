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
        for cla in argv[1:]:
            if cla[:2] == "--":
                if len(argv) == 2:
                    if argv[1] == "--help":
                        print(CLIMain.__HELP_MESSAGE)
                    else:
                        print(argv[0] + ": wrong command entered, try --help")
                else:
                    print(argv[0] + ": usage of command with any other command line "
                                    "argument is forbidden")
                return False
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
        if not CLIMain.__handle_command(sys.argv):
            return
        i = 1
        while i < len(sys.argv):
            if sys.argv[i][0] == '-':
                i = CLIMain.__handle_flag(sys.argv, i)
            else:
                CLIMain.__target.append(sys.argv[i])
            i += 1

    __HELP_MESSAGE = "Flag is a command line argument which starts with '-' There " \
                     "are two types of flags: one, that require arguments, and one " \
                     "which not (called non-arg flags). Non-arg flags can be grouped " \
                     "in one string (like '-nmlf', for ex.). Therefore, it is forbidden" \
                     " to have arg flag grouped with any other flag.\n\n" \
                     "Arguments without flag are taken as target files.\n\n" \
                     "-i [dic_filename] : specifies an input dictionary, which will be " \
                     "imported before target files analysis, and new tokens will be added" \
                     " to this dictionary.\n\n" \
                     "-I [dic_filename] : the same behaviour as -i, but output filename is" \
                     " specified the same as [dic_filename].\n\n" \
                     "-o  [out_filename] : specifies filename for output file. If file do not" \
                     " exist it will be created, otherwise existing file will be rewritten.\n\n" \
                     "-a  forces program to use array (list) as data structure\n\n" \
                     "-t  forces program to print traces\n\n" \
                     "Commands are used to get some data about program. Commands line argument" \
                     " ofcommand starts with \"--\", and can be only one CLA for call.\n\n" \
                     "--help  prints help\n"
