import sys
import datetime
import time

from src.dictionaries.simplest_set_dictionary import SimplestSetDictionary
from src.dictionaries.simplest_array_dictionary import SimplestArrayDictionary
from src.text_file_tokenizers.text_file_simplest_tokenizer import TextFileSimplestTokenizer


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

    '-i'  [dic_filename] : specifies an input dictionary, which will be imported
        before target files analysis, and new tokens will be added to this
        dictionary.

    '-I'  [dic_filename] : the same behaviour as -i, but output filename is
        specified the same as [dic_filename].

    '-o'  [out_filename] : specifies filename for output file. If file do not exist,
        it will be created, otherwise existing file will be rewritten. If out_filename
        is not specified, [default_dir]/[timestamp].txt used instead.

    '-a'  forces program to use array (list) as data structure

    '-t'  forces program to print traces

        Commands are used to get some data about program. Commands line argument of
        command starts with "--", and can be only one CLA for call.

    '--help'  prints help

    """

    # TODO check type asserts

    __target = []
    __output = ""
    __input = ""
    __printTraces = False
    __useArray = False

    __arg_flags = "iIo"
    __nonarg_flags = "at"

    __DEFAULT_OUTPUT_DIRECTORY = "data"

    __REUSAGE_ASSERT_STATEMENT = "This version of CLIMain do not support" \
                                 "multiple call during one execution"

    @staticmethod
    def main():
        assert not CLIMain.__target, CLIMain.__REUSAGE_ASSERT_STATEMENT
        assert not CLIMain.__output, CLIMain.__REUSAGE_ASSERT_STATEMENT
        assert not CLIMain.__input, CLIMain.__REUSAGE_ASSERT_STATEMENT
        assert not CLIMain.__printTraces, CLIMain.__REUSAGE_ASSERT_STATEMENT
        assert not CLIMain.__useArray, CLIMain.__REUSAGE_ASSERT_STATEMENT

        if len(sys.argv) < 2:
            print(sys.argv[0] + ": usage: " + sys.argv[0] + " [-a|-t] "
                                                            "[-i dic_filename] "
                                                            "[-I dic_filename] "
                                                            "[-o out_filename] "
                                                            "[arguments]")
            print(sys.argv[0] + ": use " + sys.argv[0] + " --help")
            return
        if not CLIMain.__handle_command(sys.argv):
            return
        i = 1
        while i < len(sys.argv):
            if sys.argv[i][0] == '-':
                i = CLIMain.__handle_flag(sys.argv, i)
                if not i:
                    return
            else:
                CLIMain.__target.append(sys.argv[i])
            i += 1
        if not CLIMain.__target:
            print(sys.argv[0] + ": target files not specified")
            return
        if not CLIMain.__output:
            CLIMain.__output = CLIMain.__DEFAULT_OUTPUT_DIRECTORY + "/" \
                 + datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H-%M-%S.txt')
        if CLIMain.__printTraces:
            print(sys.argv[0] + ": running with traces ON")
            print(sys.argv[0] + ": data structure used: " + ("array" if CLIMain.__useArray
                                                             else "set"))
            print(sys.argv[0] + ": import dictionary: "
                  + ("not specified"
                     if not CLIMain.__input else CLIMain.__input))
            print(sys.argv[0] + ": target files: " + str(CLIMain.__target))
            print(sys.argv[0] + ": output file name: " + CLIMain.__output)
        CLIMain.__do_task()

    @staticmethod
    def __do_task():
        # noinspection PyBroadException
        try:
            if CLIMain.__printTraces:
                if CLIMain.__input:
                    print(sys.argv[0] + ": importing dictionary \"" + CLIMain.__input + "\"...")
                else:
                    print(sys.argv[0] + ": creating dictionary...")
            dictionary = (SimplestArrayDictionary(
                CLIMain.__input) if CLIMain.__useArray else SimplestSetDictionary(
                CLIMain.__input))
            if CLIMain.__printTraces:
                if CLIMain.__input:
                    print(sys.argv[0] + ": importing dictionary: OK")
                else:
                    print(sys.argv[0] + ": creating dictionary: OK")
        except FileNotFoundError:
            print(sys.argv[0] + ": input file \"" + CLIMain.__input + "\" not found")
            return
        except Exception:
            print(sys.argv[0] + ": unknown error while reading input file")
            return
        for filename in CLIMain.__target:
            # noinspection PyBroadException
            try:
                if CLIMain.__printTraces:
                    print(sys.argv[0] + ": reading and adding \"" + filename + "\"...")
                    # TODO simplify using add_words
                tfst = TextFileSimplestTokenizer(filename)
                for word in tfst.token_generator:
                    dictionary.add_word(word)
                if CLIMain.__printTraces:
                    print(sys.argv[0] + ": reading and adding \"" + filename + "\": OK")
            except FileNotFoundError:
                print(sys.argv[0] + ": target file \"" + filename + "\" not found")
                return
            except Exception:
                print(
                    sys.argv[0] + ": unknown error while reading target file \"" + filename + "\"")
                return
        # noinspection PyBroadException
        try:
            if CLIMain.__printTraces:
                print(sys.argv[0] + ": writing new dictionary to \"" + CLIMain.__output + "\"...")
            dictionary.export_dictionary(CLIMain.__output)
            if CLIMain.__printTraces:
                print(sys.argv[0] + ": writing new dictionary: OK")
        except Exception:
            print(sys.argv[0] + ": unknown error exporting files")
            return
        print(sys.argv[0] + ": success")

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
    def __handle_flag(argv, i):
        if len(argv[i]) > 2:
            for flag in argv[i][1:]:
                if flag in CLIMain.__arg_flags:
                    print(argv[0] + ": usage of arg flag with any other if forbidden")
                    return False
                if flag == 'a':
                    CLIMain.__useArray = True
                elif flag == 't':
                    CLIMain.__printTraces = True
                else:
                    print(argv[0] + ": wrong flag used, use --help")
                    return False
        else:
            if argv[i][1] == 'i':
                if (len(argv) == i + 1) or (argv[i + 1][0] == '-'):
                    print(argv[0] + ": argument for flag -i not specified")
                    return False
                i += 1
                if CLIMain.__input:
                    print(argv[0] + ": input dictionary specification duplicates")
                    return False
                CLIMain.__input = argv[i]
            elif argv[i][1] == 'I':
                if (len(argv) == i + 1) or (argv[i + 1][0] == '-'):
                    print(argv[0] + ": argument for flag -I not specified")
                    return False
                i += 1
                if CLIMain.__input:
                    print(argv[0] + ": input dictionary specification duplicates")
                    return False
                if CLIMain.__output:
                    print(argv[0] + ": output filename specification duplicates")
                    return False
                CLIMain.__input = argv[i]
                CLIMain.__output = argv[i]
            elif argv[i][1] == 'o':
                if (len(argv) == i + 1) or (argv[i + 1][0] == '-'):
                    print(argv[0] + ": argument for flag -o not specified")
                    return False
                i += 1
                if CLIMain.__output:
                    print(argv[0] + ": output filename specification duplicates")
                    return False
                CLIMain.__output = argv[i]
            elif argv[i][1] == 'a':
                CLIMain.__useArray = True
            elif argv[i][1] == 't':
                CLIMain.__printTraces = True
            else:
                print(argv[0] + ": wrong flag used, use --help")
                return False
        return i

    __HELP_MESSAGE = "\nFlag is a command line argument which starts with '-' There " \
                     "are two types of flags: one, that require arguments, and one " \
                     "which not (called non-arg flags). Non-arg flags can be grouped " \
                     "in one string (like '-nmlf', for ex.). Therefore, it is forbidden" \
                     " to have arg flag grouped with any other flag.\n\n" \
                     "Arguments without flag are taken as target files.\n\n" \
                     "\t-i [dic_filename] : specifies an input dictionary, which will be " \
                     "imported before target files analysis, and new tokens will be added" \
                     " to this dictionary.\n\n" \
                     "\t-I [dic_filename] : the same behaviour as -i, but output filename is" \
                     " specified the same as [dic_filename].\n\n" \
                     "\t-o  [out_filename] : specifies filename for output file. If file do not" \
                     " exist it will be created, otherwise existing file will be rewritten." \
                     "If out_filename is not specified, [default_dir]/[timestamp].txt used " \
                     "instead.\n\n" \
                     "\t-a  forces program to use array (list) as data structure\n\n" \
                     "\t-t  forces program to print traces\n\n" \
                     "Commands are used to get some data about program. Commands line argument" \
                     " ofcommand starts with \"--\", and can be only one CLA for call.\n\n" \
                     "\t--help  prints help\n"
