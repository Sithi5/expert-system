from expert_system import main
from pathlib import Path


def test_simple_1():
	assert "B is True" == main(open(Path(__file__ + "/../" + "files/test_simple_1").absolute()), False)


def test_simple_2():
	assert "B is True" == main(open(Path(__file__ + "/../" + "files/test_simple_2").absolute()), False)


def test_simple_3():
	assert "B is True" == main(open(Path(__file__ + "/../" + "files/test_simple_3").absolute()), False)


def test_simple_4():
	assert "B is True" == main(open(Path(__file__ + "/../" + "files/test_simple_4").absolute()), False)


def test_simple_5():
	assert "B is True" == main(open(Path(__file__ + "/../" + "files/test_simple_5").absolute()), False)


def test_correction_1():
	assert "A is True\nF is True\nK is True\nP is True" == main(open(Path(__file__ + "/../" + "files/test_correction_1").absolute()), False)


def test_correction_2():
	assert "A is True\nF is True\nK is False\nP is True" == main(open(Path(__file__ + "/../" + "files/test_correction_2").absolute()), False)


def test_correction_3():
	assert "A is False" == main(open(Path(__file__ + "/../" + "files/test_correction_3").absolute()), False)


def test_correction_4():
	assert "A is True" == main(open(Path(__file__ + "/../" + "files/test_correction_4").absolute()), False)


def test_correction_5():
	assert "A is True" == main(open(Path(__file__ + "/../" + "files/test_correction_5").absolute()), False)


def test_correction_6():
	assert "A is True" == main(open(Path(__file__ + "/../" + "files/test_correction_6").absolute()), False)


def test_correction_7():
	assert "A is False" == main(open(Path(__file__ + "/../" + "files/test_correction_7").absolute()), False)


def test_correction_8():
	assert "A is True" == main(open(Path(__file__ + "/../" + "files/test_correction_8").absolute()), False)


def test_correction_9():
	assert "A is True" == main(open(Path(__file__ + "/../" + "files/test_correction_9").absolute()), False)


def test_correction_10():
	assert "A is True" == main(open(Path(__file__ + "/../" + "files/test_correction_10").absolute()), False)


def test_correction_11():
	assert "A is False" == main(open(Path(__file__ + "/../" + "files/test_correction_11").absolute()), False)


def test_correction_12():
	assert "A is False" == main(open(Path(__file__ + "/../" + "files/test_correction_12").absolute()), False)


def test_correction_13():
	assert "A is False" == main(open(Path(__file__ + "/../" + "files/test_correction_13").absolute()), False)


def test_correction_14():
	assert "A is True" == main(open(Path(__file__ + "/../" + "files/test_correction_14").absolute()), False)


def test_correction_15():
	assert "A is True" == main(open(Path(__file__ + "/../" + "files/test_correction_15").absolute()), False)


def test_correction_16():
	assert "A is True" == main(open(Path(__file__ + "/../" + "files/test_correction_16").absolute()), False)


def test_correction_17():
	assert "E is False" == main(open(Path(__file__ + "/../" + "files/test_correction_17").absolute()), False)


def test_correction_18():
	assert "E is True" == main(open(Path(__file__ + "/../" + "files/test_correction_18").absolute()), False)


def test_correction_19():
	assert "E is False" == main(open(Path(__file__ + "/../" + "files/test_correction_19").absolute()), False)


def test_correction_20():
	assert "E is False" == main(open(Path(__file__ + "/../" + "files/test_correction_20").absolute()), False)


def test_correction_21():
	assert "E is True" == main(open(Path(__file__ + "/../" + "files/test_correction_21").absolute()), False)


def test_correction_22():
	assert "E is True" == main(open(Path(__file__ + "/../" + "files/test_correction_22").absolute()), False)


def test_correction_23():
	assert "E is False" == main(open(Path(__file__ + "/../" + "files/test_correction_23").absolute()), False)


def test_correction_24():
	assert "E is False" == main(open(Path(__file__ + "/../" + "files/test_correction_24").absolute()), False)


def test_correction_25():
	assert "E is False" == main(open(Path(__file__ + "/../" + "files/test_correction_25").absolute()), False)


def test_correction_26():
	assert "E is True" == main(open(Path(__file__ + "/../" + "files/test_correction_26").absolute()), False)


def test_correction_27():
	assert "E is True" == main(open(Path(__file__ + "/../" + "files/test_correction_27").absolute()), False)
