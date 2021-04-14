#! /usr/bin/env python3

import argparse
import hashlib
import os
import sys


BUFFER_SIZE = 3145728  # 3MB


def get_hash(type_of_hash, filename):

    try:
        hash_obj = hashlib.new(type_of_hash)
    except ValueError:
        sys.exit("Not supported or invalid HASH type.")

    print("\n[*] Calculating HASH value...")

    with open(filename, 'rb') as f:
        while True:
            data = f.read(BUFFER_SIZE)
            if not data:
                break
            hash_obj.update(data)

    return hash_obj.hexdigest()


def get_arguments():
    parser = argparse.ArgumentParser(prog="Verify Hash",
                                     usage="%(prog)s [options]\n\t[-f | --file] [location|name]_of_file\n\t[-t | "
                                           "--type] type_of_hash",
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     description=""">>> | Verify Hash v1.0 by Hack Hunt | <<<
    ---------------------------------""")

    parser._optionals.title = "Optional Argument"

    parser.add_argument('-v', '--verify-hash',
                        dest='hash',
                        metavar='',
                        help='Specify the HASH to check with')

    required_arguments = parser.add_argument_group("Required Arguments")
    required_arguments.add_argument('-f', '--file',
                                    dest='name',
                                    metavar="",
                                    help="Specify the name and location of the file",
                                    required=True)

    required_arguments.add_argument('-t', '--type',
                                    dest='type',
                                    metavar='',
                                    help='Specify the HASH type, (SHA256/MD5)',
                                    required=True)

    args = parser.parse_args()
    check_input(args.name)
    return args


def check_input(file_path):

    if not os.path.isfile(file_path):
        sys.exit("Invalid location of the file!")


def main():

    args = get_arguments()

    try:
        type_of_hash = args.type
        file_name = args.name
        hash_of_file = args.hash

        check_input(file_name)

        calc_hash = get_hash(type_of_hash, file_name)
        print("\n{0}: {1}".format(type_of_hash.upper(), calc_hash))

        if hash_of_file is not None:
            if calc_hash == hash_of_file:
                print("[+] File is safe to use!")
            else:
                print("[-] File is not safe to use!")

    except KeyboardInterrupt:
        print("\n[+] Exiting...")
        sys.exit(0)

    except BaseException as e:
        print("\n[-] Error: {0}".format(e))
        sys.exit(1)


##############################################
if __name__ == '__main__':
    main()
