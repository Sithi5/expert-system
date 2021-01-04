from Resources.Parser.args import ArgsParser
from Resources.Parser.parser import Parser

if __name__ == "__main__":
	args = ArgsParser.args
	parser = Parser(args.file)
