#!/usr/bin/env python3.9.5
# file <gendiff>
import argparse
#from gendiff.gendiff1 import generate_diff

parser = argparse.ArgumentParser(description='Generate diff')

parser.add_argument("first_file")
parser.add_argument("second_file")

#parser.add_arguments("-f", "--format", help='set format of output')
parser.add_argument('-f', '--format', help='set format of output')
args = parser.parse_args()

print(args)

def main():
    print(args)
#    diff = generate_diff()
#    print(diff)


if __name__ == '__main__':
    main()
