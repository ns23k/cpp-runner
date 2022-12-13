import argparse
import os

parser = argparse.ArgumentParser()

parser.add_argument("files")

parse = parser.parse_args()

os.system(f"g++ {parse.files} && .\\a.exe")
