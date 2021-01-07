from expert_system import main
from pathlib import Path


def test_simple_1():
	assert "B resolved as True" == main(open(Path(__file__ + "/../" + "files/test_simple_1").absolute()), False)


def test_simple_2():
	assert "B resolved as True" == main(open(Path(__file__ + "/../" + "files/test_simple_2").absolute()), False)


def test_simple_3():
	assert "B resolved as True" == main(open(Path(__file__ + "/../" + "files/test_simple_3").absolute()), False)


def test_simple_4():
	assert "B resolved as True" == main(open(Path(__file__ + "/../" + "files/test_simple_4").absolute()), False)


def test_simple_5():
	assert "B resolved as True" == main(open(Path(__file__ + "/../" + "files/test_simple_5").absolute()), False)
