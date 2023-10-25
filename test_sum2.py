import pytest
from main import sum2
class SummCheck:
    def test_cum2(self):
        assert sum2(2, 5) > 5, 'Good'

    def test_message(self):
        # assert True, 'Test message'
        assert False, 'Test message'

def test_three():
    pass


import pytest
from main import pos_or_neg
@pytest.mark.parametrize('x', [25, 25.6, 0.00000000000000002])
def test_pon_int(x):
    assert pos_or_neg(x) == 'positive'
@pytest.mark.parametrize('x', [-25, -25.6, -0.00000000000000002])
def test_pon_float(x):
    assert pos_or_neg(x) == 'negative'
@pytest.mark.parametrize('x', [-25, -25.6, -0.00000000000000002])
def test_pon_zero(x):
    assert pos_or_neg(0) == 'zero'


import pytest
from main import pos_or_neg


@pytest.mark.parametrize('x, exp_res', [(25, 'positive'),
                                        (6, 'positive'),
                                        (0.00000000000000002, 'positive'),
                                        (-25, 'negative'),
                                        (-25.6, 'negative'),
                                        (-0.00000000000000002, 'negative'),
                                        (0, 'zero')])
def test_pon(x, exp_res):
    assert pos_or_neg(x) == exp_res

def test_error():
    with pytest.raises(ValueError):
        pos_or_neg('yes')


import pytest
from main import check_even
@pytest.mark.parametrize("number, exp_res", [
    (6, True),
    (7, False),
    (20, True),
    (-5, False),
    (0, True),
    (-4, True)
])
def test_check_even(number, exp_res):
    assert check_even(number) == exp_res


from main import check_quantity
@pytest.mark.parametrize("n, exp_res", [
    (0, 1),
    (123, 3),
    (456789, 6),
    (1000, 4),
    (987654321, 9)
])
def test_check_quantity(n, exp_res):
    assert check_quantity(n) == exp_res


from main import sum_list
@pytest.mark.parametrize("num, exp_res", [
    ([1, 2, 3, 4, 5], 15),
    ([0, 0, 0, 0], 0),
    ([10, -5, 7, 2], 14),
    ([-1, -2, -3, -4, -5], -15),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 45)
])
def test_sum_list(num, exp_res):
    assert sum_list(num) == exp_res










