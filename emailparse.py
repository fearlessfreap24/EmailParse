from email.parser import BytesParser, Parser
from email.policy import default
import argparse as arg


if __name__ == "__main__":

    parse = arg.ArgumentParser(description='A test script to parse email headers')
    parse.add_argument('-f', '--file', help='File to be read', required=True)
    args = vars(parse.parse_args())

    print("before if")
    if args['file'] == "" or args['file'] is None:
        print("Input file not detected\n")
        exit(1)
    else:
        print("in else")
        with open(args['file'], 'rb') as fp:
            headers = BytesParser(policy=default).parse(fp)

        for part in headers:
            print("{}: {}".format(part, headers[part]))
            # if part == "Received":
            #     print("{}: {}".format(part, headers[part]))
        print("finished else")
