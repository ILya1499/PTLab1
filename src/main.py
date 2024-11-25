# -*- coding: utf-8 -*-
import argparse
import sys
from CalcRating import CalcRating
from TextDataReader import TextDataReader
from indDataReader import indDataReader


def get_path_from_arguments(args) -> dict:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    parser.add_argument("-i", dest="pathi", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args


def main():
    args = get_path_from_arguments(sys.argv[1:])
    path = args.path
    pathi = args.pathi
    reader = TextDataReader()
    students = reader.read(path)
    print("Students: ", students)
    rating = CalcRating(students).calc()
    print("Rating: ", rating)

    reader = indDataReader()
    students = reader.read(pathi)
    so = CalcRating(students).so()
    print("Student:", so)


if __name__ == "__main__":
    main()
