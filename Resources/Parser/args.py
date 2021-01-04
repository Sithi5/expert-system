import argparse


class ArgsParser:
	parser = argparse.ArgumentParser(description="Expert System")
	parser.add_argument("file", type=argparse.FileType('r'), help="The file containing rules")
	parser.add_argument("-vb", "--verbose", action='store_true', help="Enable verbose")
	args = parser.parse_args()
