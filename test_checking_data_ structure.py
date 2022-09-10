import pytest

from functions import get_area


def test_check_input_data_int_in_get_area():
    res = get_area(2, 7)
    assert res == 14, "The area is not determined correctly"


def test_check_input_data_str_in_get_area():
    with pytest.raises(TypeError) as ex_context:
        get_area("2", 15)
    assert ex_context.value.args[0] == "The input data must be of type int or float"


def test_check_input_data_float_in_get_area():
    res = get_area(2.0, 0.5)
    assert res == 1.0, "The area is not determined correctly"


def test_check_input_negative_data_in_get_area():
    with pytest.raises(TypeError) as ex_context:
        get_area(-2, 15.7)
    assert ex_context.value.args[0] == "The input data must be greater then zero"
    with pytest.raises(TypeError) as ex_context:
        get_area(2, -15.7)
    assert ex_context.value.args[0] == "The input data must be greater then zero"


def test_check_input_data_at_zero_in_get_area():
    assert get_area(0, 0) == 0, "The area is not zero"
    assert get_area(1, 0.0) == 0, "The area is not zero"
    assert get_area(0, 1.0) == 0, "The area is not zero"


@pytest.mark.parametrize('x, y, result', [(0, 0, 0), (1, 14, 14), (0.5, 14.1, 7.05), (31, 0.5, 15.5)])
def test_param_check_input_data_in_get_area(x, y, result):
    assert get_area(x, y) == result, "The area is not determined correctly"

