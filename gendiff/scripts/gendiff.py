#!/usr/bin/env python3.9.5
# file <gendiff>
import argparse

parser = argparse.ArgumentParser()


parser.add_argument("first_file")
parser.add_argument("second_file")

args = parser.parse_args()

print(args)

def main():
    print(args)


if __name__ == '__main__':
    main()
