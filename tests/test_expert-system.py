import pytest

from pathlib import Path

from expert_system import main
from Resources.Parser.exceptions import InputError

# def test_subject():
#     assert "B resolved as True" == main(
#         open(Path(__file__ + "/../" + "files/test_subject").absolute()), False
#     )


# def test_simple_1():
#     assert "B resolved as True" == main(
#         open(Path(__file__ + "/../" + "files/test_simple_1").absolute()), False
#     )


# def test_simple_2():
#     assert "B resolved as True" == main(
#         open(Path(__file__ + "/../" + "files/test_simple_2").absolute()), False
#     )


# def test_simple_3():
#     assert "B resolved as True" == main(
#         open(Path(__file__ + "/../" + "files/test_simple_3").absolute()), False
#     )


# def test_simple_4():
#     assert "B resolved as True" == main(
#         open(Path(__file__ + "/../" + "files/test_simple_4").absolute()), False
#     )


# def test_simple_5():
#     assert "B resolved as True" == main(
#         open(Path(__file__ + "/../" + "files/test_simple_5").absolute()), False
#     )


# def test_simple_bonus_1():
#     assert "B resolved as True" == main(
#         open(Path(__file__ + "/../" + "files/tests_bonus/test_simple_bonus_1").absolute()), False
#     )


# def test_hard_bonus_1():
#     assert "B resolved as True" == main(
#         open(Path(__file__ + "/../" + "files/tests_bonus/test_hard_bonus_1").absolute()), False
#     )


# def test_example_tree():
#     assert "B resolved as True" == main(
#         open(Path(__file__ + "/../" + "files/test_example_tree").absolute()), False
#     )


# Test False here


def test_false_too_much_or_or_xor_operators():
    with pytest.raises(InputError) as e:
        main(
            open(
                Path(
                    __file__ + "/../" + "files/tests_false/test_false_too_much_xor_operators"
                ).absolute()
            ),
            False,
        )
    assert e.value.message == "Only one 'XOR' or 'OR' operator are allowed in result."
    with pytest.raises(InputError) as e:
        main(
            open(
                Path(
                    __file__ + "/../" + "files/tests_false/test_false_too_much_or_operators"
                ).absolute()
            ),
            False,
        )
    assert e.value.message == "Only one 'XOR' or 'OR' operator are allowed in result."
    with pytest.raises(InputError) as e:
        main(
            open(
                Path(
                    __file__ + "/../" + "files/tests_false/test_false_too_much_or_or_xor_operators"
                ).absolute()
            ),
            False,
        )
    assert e.value.message == "Only one 'XOR' or 'OR' operator are allowed in result."


# def test_false():
#     with pytest.raises(InputError) as e:
#         main(
#             open(
#                 Path(__file__ + "/../" + "files/tests_false/test_false_letter_is_lower").absolute()
#             ),
#             False,
#         )
#     assert e.value.message == "Only one 'XOR' or 'OR' operator are allowed in result."
