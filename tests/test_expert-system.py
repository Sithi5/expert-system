from expert_system import main_test
from pathlib import Path


def test_correction_1():
    assert "A is True\nF is True\nK is True\nP is True" == main_test(
        open(Path(__file__ + "/../" + "files/correction/test_correction_1").absolute()), False
    )


def test_correction_2():
    assert "A is True\nF is True\nK is False\nP is True" == main_test(
        open(Path(__file__ + "/../" + "files/correction/test_correction_2").absolute()), False
    )


def test_correction_3():
    assert "A is False" == main_test(
        open(Path(__file__ + "/../" + "files/correction/test_correction_3").absolute()), False
    )


def test_correction_4():
    assert "A is True" == main_test(
        open(Path(__file__ + "/../" + "files/correction/test_correction_4").absolute()), False
    )


def test_correction_5():
    assert "A is True" == main_test(
        open(Path(__file__ + "/../" + "files/correction/test_correction_5").absolute()), False
    )


def test_correction_6():
    assert "A is True" == main_test(
        open(Path(__file__ + "/../" + "files/correction/test_correction_6").absolute()), False
    )


def test_correction_7():
    assert "A is False" == main_test(
        open(Path(__file__ + "/../" + "files/correction/test_correction_7").absolute()), False
    )


def test_correction_8():
    assert "A is True" == main_test(
        open(Path(__file__ + "/../" + "files/correction/test_correction_8").absolute()), False
    )


def test_correction_9():
    assert "A is True" == main_test(
        open(Path(__file__ + "/../" + "files/correction/test_correction_9").absolute()), False
    )


def test_correction_10():
    assert "A is True" == main_test(
        open(Path(__file__ + "/../" + "files/correction/test_correction_10").absolute()), False
    )


def test_correction_11():
    assert "A is False" == main_test(
        open(Path(__file__ + "/../" + "files/correction/test_correction_11").absolute()), False
    )


def test_correction_12():
    assert "A is False" == main_test(
        open(Path(__file__ + "/../" + "files/correction/test_correction_12").absolute()), False
    )


def test_correction_13():
    assert "A is False" == main_test(
        open(Path(__file__ + "/../" + "files/correction/test_correction_13").absolute()), False
    )


def test_correction_14():
    assert "A is True" == main_test(
        open(Path(__file__ + "/../" + "files/correction/test_correction_14").absolute()), False
    )


def test_correction_15():
    assert "A is True" == main_test(
        open(Path(__file__ + "/../" + "files/correction/test_correction_15").absolute()), False
    )


def test_correction_16():
    assert "A is True" == main_test(
        open(Path(__file__ + "/../" + "files/correction/test_correction_16").absolute()), False
    )


def test_correction_17():
    assert "E is False" == main_test(
        open(Path(__file__ + "/../" + "files/correction/test_correction_17").absolute()), False
    )


def test_correction_18():
    assert "E is True" == main_test(
        open(Path(__file__ + "/../" + "files/correction/test_correction_18").absolute()), False
    )


def test_correction_19():
    assert "E is False" == main_test(
        open(Path(__file__ + "/../" + "files/correction/test_correction_19").absolute()), False
    )


def test_correction_20():
    assert "E is False" == main_test(
        open(Path(__file__ + "/../" + "files/correction/test_correction_20").absolute()), False
    )


def test_correction_21():
    assert "E is True" == main_test(
        open(Path(__file__ + "/../" + "files/correction/test_correction_21").absolute()), False
    )


def test_correction_22():
    assert "E is True" == main_test(
        open(Path(__file__ + "/../" + "files/correction/test_correction_22").absolute()), False
    )


def test_correction_23():
    assert "E is False" == main_test(
        open(Path(__file__ + "/../" + "files/correction/test_correction_23").absolute()), False
    )


def test_correction_24():
    assert "E is False" == main_test(
        open(Path(__file__ + "/../" + "files/correction/test_correction_24").absolute()), False
    )


def test_correction_25():
    assert "E is False" == main_test(
        open(Path(__file__ + "/../" + "files/correction/test_correction_25").absolute()), False
    )


def test_correction_26():
    assert "E is True" == main_test(
        open(Path(__file__ + "/../" + "files/correction/test_correction_26").absolute()), False
    )


def test_correction_27():
    assert "E is True" == main_test(
        open(Path(__file__ + "/../" + "files/correction/test_correction_27").absolute()), False
    )


def test_error_1():
    assert "Error" in main_test(
        open(Path(__file__ + "/../" + "files/error/test_error_1").absolute()), False
    )


def test_error_2():
    assert "Error" in main_test(
        open(Path(__file__ + "/../" + "files/error/test_error_2").absolute()), False
    )


def test_error_3():
    assert "Error" in main_test(
        open(Path(__file__ + "/../" + "files/error/test_error_3").absolute()), False
    )


def test_error_4():
    assert "Error" in main_test(
        open(Path(__file__ + "/../" + "files/error/test_error_4").absolute()), False
    )


def test_error_5():
    assert "Error" in main_test(
        open(Path(__file__ + "/../" + "files/error/test_error_5").absolute()), False
    )


def test_error_6():
    assert "Error" in main_test(
        open(Path(__file__ + "/../" + "files/error/test_error_6").absolute()), False
    )


def test_error_7():
    assert "Error" in main_test(
        open(Path(__file__ + "/../" + "files/error/test_error_7").absolute()), False
    )


def test_error_8():
    assert "Error" in main_test(
        open(Path(__file__ + "/../" + "files/error/test_error_8").absolute()), False
    )


def test_error_9():
    assert "Error" in main_test(
        open(Path(__file__ + "/../" + "files/error/test_error_9").absolute()), False
    )


def test_error_10():
    assert "Error" in main_test(
        open(Path(__file__ + "/../" + "files/error/test_error_10").absolute()), False
    )


def test_error_11():
    assert "Error" in main_test(
        open(Path(__file__ + "/../" + "files/error/test_error_11").absolute()), False
    )


def test_error_12():
    assert "Error" in main_test(
        open(Path(__file__ + "/../" + "files/error/test_error_12").absolute()), False
    )


def test_error_13():
    assert "Error" in main_test(
        open(Path(__file__ + "/../" + "files/error/test_error_13").absolute()), False
    )


def test_error_14():
    assert "Error" in main_test(
        open(Path(__file__ + "/../" + "files/error/test_error_14").absolute()), False
    )


def test_error_15():
    assert "Error" in main_test(
        open(Path(__file__ + "/../" + "files/error/test_error_15").absolute()), False
    )


def test_error_16():
    assert "Error" in main_test(
        open(Path(__file__ + "/../" + "files/error/test_error_16").absolute()), False
    )


def test_error_17():
    assert "Error" in main_test(
        open(Path(__file__ + "/../" + "files/error/test_error_17").absolute()), False
    )


def test_error_18():
    assert "Error" in main_test(
        open(Path(__file__ + "/../" + "files/error/test_error_18").absolute()), False
    )


def test_error_19():
    assert "Error" in main_test(
        open(Path(__file__ + "/../" + "files/error/test_error_19").absolute()), False
    )


def test_error_20():
    assert "Error" in main_test(
        open(Path(__file__ + "/../" + "files/error/test_error_20").absolute()), False
    )


def test_error_21():
    assert "Error" in main_test(
        open(Path(__file__ + "/../" + "files/error/test_error_21").absolute()), False
    )


def test_error_22():
    assert "Error" in main_test(
        open(Path(__file__ + "/../" + "files/error/test_error_22").absolute()), False
    )


def test_error_23():
    assert "Error" in main_test(
        open(Path(__file__ + "/../" + "files/error/test_error_23").absolute()), False
    )


def test_error_24():
    assert "Error" in main_test(
        open(Path(__file__ + "/../" + "files/error/test_error_24").absolute()), False
    )


def test_error_25():
    assert "Error" in main_test(
        open(Path(__file__ + "/../" + "files/error/test_error_25").absolute()), False
    )


def test_error_26():
    assert "Error" in main_test(
        open(Path(__file__ + "/../" + "files/error/test_error_26").absolute()), False
    )


def test_error_27():
    assert "Error" in main_test(
        open(Path(__file__ + "/../" + "files/error/test_error_27").absolute()), False
    )


def test_error_28():
    assert "Error" in main_test(
        open(Path(__file__ + "/../" + "files/error/test_error_28").absolute()), False
    )


def test_error_29():
    assert "Error" in main_test(
        open(Path(__file__ + "/../" + "files/error/test_error_29").absolute()), False
    )


def test_error_30():
    assert "Error" in main_test(
        open(Path(__file__ + "/../" + "files/error/test_error_30").absolute()), False
    )


def test_error_31():
    assert "Error" in main_test(
        open(Path(__file__ + "/../" + "files/error/test_error_31").absolute()), False
    )


def test_error_32():
    assert "Error" in main_test(
        open(Path(__file__ + "/../" + "files/error/test_error_32").absolute()), False
    )


def test_error_33():
    assert "Error" in main_test(
        open(Path(__file__ + "/../" + "files/error/test_error_33").absolute()), False
    )


def test_simple_1():
    assert "B is True" == main_test(
        open(Path(__file__ + "/../" + "files/simple/test_simple_1").absolute()), False
    )


def test_simple_2():
    assert "A is True" == main_test(
        open(Path(__file__ + "/../" + "files/simple/test_simple_2").absolute()), False
    )


def test_simple_3():
    assert "B is True" == main_test(
        open(Path(__file__ + "/../" + "files/simple/test_simple_3").absolute()), False
    )


def test_simple_4():
    assert "B is True" == main_test(
        open(Path(__file__ + "/../" + "files/simple/test_simple_4").absolute()), False
    )


def test_simple_5():
    assert "B is True" == main_test(
        open(Path(__file__ + "/../" + "files/simple/test_simple_5").absolute()), False
    )


def test_simple_6():
    assert "B is False" == main_test(
        open(Path(__file__ + "/../" + "files/simple/test_simple_6").absolute()), False
    )


def test_simple_7():
    assert "B is True" == main_test(
        open(Path(__file__ + "/../" + "files/simple/test_simple_7").absolute()), False
    )


def test_hard_1():
    assert "C is True\nE is True\nG is True\nI is True\nK is True\nM is True" == main_test(
        open(Path(__file__ + "/../" + "files/hard/test_hard_1").absolute()), False
    )


def test_hard_2():
    assert "C is True" == main_test(
        open(Path(__file__ + "/../" + "files/hard/test_hard_2").absolute()), False
    )


def test_hard_3():
    assert "K is True" == main_test(
        open(Path(__file__ + "/../" + "files/hard/test_hard_3").absolute()), False
    )


def test_hard_4():
    assert "A is True\nB is True\nC is Undetermined" == main_test(
        open(Path(__file__ + "/../" + "files/hard/test_hard_4").absolute()), False
    )


def test_hard_5():
    assert "B is True" == main_test(
        open(Path(__file__ + "/../" + "files/hard/test_hard_5").absolute()), False
    )


def test_hard_6():
    assert "D is False" == main_test(
        open(Path(__file__ + "/../" + "files/hard/test_hard_6").absolute()), False
    )


def test_hard_7():
    assert "C is False" == main_test(
        open(Path(__file__ + "/../" + "files/hard/test_hard_7").absolute()), False
    )


def test_hard_8():
    assert "A is False" == main_test(
        open(Path(__file__ + "/../" + "files/hard/test_hard_8").absolute()), False
    )


def test_hard_9():
    assert "A is True" == main_test(
        open(Path(__file__ + "/../" + "files/hard/test_hard_9").absolute()), False
    )


def test_hard_10():
    assert "A is True" == main_test(
        open(Path(__file__ + "/../" + "files/hard/test_hard_10").absolute()), False
    )


def test_hard_11():
    assert "A is True" == main_test(
        open(Path(__file__ + "/../" + "files/hard/test_hard_11").absolute()), False
    )


def test_hard_12():
    assert "E is False" == main_test(
        open(Path(__file__ + "/../" + "files/hard/test_hard_12").absolute()), False
    )


def test_hard_13():
    assert "E is True" == main_test(
        open(Path(__file__ + "/../" + "files/hard/test_hard_13").absolute()), False
    )


def test_hard_14():
    assert "E is False" == main_test(
        open(Path(__file__ + "/../" + "files/hard/test_hard_14").absolute()), False
    )


def test_hard_15():
    assert "E is False" == main_test(
        open(Path(__file__ + "/../" + "files/hard/test_hard_15").absolute()), False
    )


def test_hard_16():
    assert "E is True" == main_test(
        open(Path(__file__ + "/../" + "files/hard/test_hard_16").absolute()), False
    )


def test_hard_17():
    assert "E is False" == main_test(
        open(Path(__file__ + "/../" + "files/hard/test_hard_17").absolute()), False
    )


def test_hard_18():
    assert "E is False" == main_test(
        open(Path(__file__ + "/../" + "files/hard/test_hard_18").absolute()), False
    )


def test_hard_19():
    assert "E is False" == main_test(
        open(Path(__file__ + "/../" + "files/hard/test_hard_19").absolute()), False
    )


def test_hard_20():
    assert "E is True" == main_test(
        open(Path(__file__ + "/../" + "files/hard/test_hard_20").absolute()), False
    )


def test_hard_21():
    assert "E is True" == main_test(
        open(Path(__file__ + "/../" + "files/hard/test_hard_21").absolute()), False
    )


def test_hard_22():
    assert "E is True" == main_test(
        open(Path(__file__ + "/../" + "files/hard/test_hard_22").absolute()), False
    )


def test_hard_23():
    assert "E is True" == main_test(
        open(Path(__file__ + "/../" + "files/hard/test_hard_23").absolute()), False
    )


def test_hard_24():
    assert "E is False" == main_test(
        open(Path(__file__ + "/../" + "files/hard/test_hard_24").absolute()), False
    )


def test_hard_25():
    assert "E is Undetermined" == main_test(
        open(Path(__file__ + "/../" + "files/hard/test_hard_25").absolute()), False
    )


def test_hard_26():
    assert "E is False" == main_test(
        open(Path(__file__ + "/../" + "files/hard/test_hard_26").absolute()), False
    )


def test_bonus_simple_1():
    assert "G is Undetermined" in main_test(
        open(Path(__file__ + "/../" + "files/tests_bonus/test_simple_1").absolute()), False
    )


def test_bonus_hard_1():
    assert "C is Undetermined" in main_test(
        open(Path(__file__ + "/../" + "files/tests_bonus/test_hard_1").absolute()), False
    )


def test_bonus_hard_2():
    assert "C is Undetermined" in main_test(
        open(Path(__file__ + "/../" + "files/tests_bonus/test_hard_2").absolute()), False
    )


def test_bonus_hard_3():
    assert "E is Undetermined" in main_test(
        open(Path(__file__ + "/../" + "files/tests_bonus/test_hard_3").absolute()), False
    )


def test_bonus_hard_4():
    assert "G is Undetermined" in main_test(
        open(Path(__file__ + "/../" + "files/tests_bonus/test_hard_4").absolute()), False
    )


def test_bonus_ultra_hard_1():
    assert "A is True\nB is False\nC is Undetermined\nH is True" in main_test(
        open(Path(__file__ + "/../" + "files/tests_bonus/test_ultra_hard_1").absolute()), False
    )


def test_bonus_ultra_hard_2():
    assert "A is True\nB is True\nC is Undetermined\nH is True" in main_test(
        open(Path(__file__ + "/../" + "files/tests_bonus/test_ultra_hard_2").absolute()), False
    )

