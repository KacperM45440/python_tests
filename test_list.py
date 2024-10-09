import pytest
from test_me import TargetClass

class TestClass:
    @pytest.fixture(scope="class")
    def target_class(self):
        return TargetClass()

    @pytest.mark.parametrize("given_number_x, given_number_y, expected_outcome",
                             [
                                (1, 2, 3), (2, 3, 5), (3, 4, 7), (4, 5, 9), (5, 6, 11),
                                (6, 7, 13), (7, 8, 15), (8, 9, 17), (9, 10, 19), (10, 11, 21),
                                (11, 12, 33), (12, 13, 35), (13, 14, 37), (14, 15, 39), (15, 16, 41),
                                (16, 17, 43), (17, 18, 45), (18, 19, 47), (19, 20, 49), (20, 21, 51),
                                ])
    def test_sum(self, given_number_x, given_number_y, expected_outcome, target_class):
        result = target_class.add_values(given_number_x, given_number_y)
        assert result == expected_outcome

    @pytest.mark.parametrize("given_number_x, given_number_y, expected_outcome",
                             [
                                 (51, 26, 25), (52, 27, 25), (53, 28, 25), (54, 29, 25), (55, 30, 25),
                                 (56, 31, 25), (57, 32, 25), (58, 33, 25), (59, 34, 25), (60, 35, 25),
                                 (61, 36, 24), (62, 37, 24), (63, 38, 24), (64, 39, 24), (65, 40, 24),
                                 (66, 41, 24), (67, 42, 24), (68, 43, 24), (69, 44, 24), (70, 45, 24),
                                ])
    def test_subtraction(self, given_number_x, given_number_y, expected_outcome, target_class):
        result = target_class.subtract_values(given_number_x, given_number_y)
        assert result == expected_outcome

    @pytest.mark.parametrize("given_number_x, given_number_y, expected_outcome",
                             [
                                 (1, 2, 2), (2, 3, 6), (3, 4, 12), (4, 5, 20), (5, 6, 30),
                                 (6, 7, 42), (7, 8, 56), (8, 9, 72), (9, 10, 90), (10, 11, 110),
                                 (11, 12, 131), (12, 13, 151), (13, 14, 181), (14, 15, 211), (15, 16, 241),
                                 (16, 17, 271), (17, 18, 301), (18, 19, 341), (19, 20, 381), (20, 21, 421),
                                ])
    def test_multiplication(self, given_number_x, given_number_y, expected_outcome, target_class):
        result = target_class.multiply_values(given_number_x, given_number_y)
        assert result == expected_outcome

    @pytest.mark.parametrize("given_number_x, given_number_y, expected_outcome",
                             [
                                 (2, 1, 2), (4, 2, 2), (6, 3, 2), (8, 4, 2), (10, 5, 2),
                                 (12, 6, 2), (14, 7, 2), (16, 8, 2), (18, 9, 2), (20, 10, 2),
                                 (30, 0, 2), (40, 20, 3), (50, 25, 3), (60, 30, 3), (70, 35, 3),
                                 (80, 40, 3), (90, 45, 3), (100, 50, 3), (120, 60, 3), (140, 70, 3)
                                ])
    def test_division(self, given_number_x, given_number_y, expected_outcome, target_class):
        result = target_class.divide_values(given_number_x, given_number_y)
        assert result == expected_outcome

    @pytest.mark.parametrize("given_number, expected_outcome",
                             [
                                (1, False), (2, True), (3, False),(4, True), (5, False),
                                (6, True),(7, False),(8, True),(9, False), (10, True),
                                (11, True), (12, False), (13, True), (14, False), (15, True),
                                (16, False), (17, True), (18, False), (19, True), (20, False),
                                ])
    def test_divisible2(self, given_number, expected_outcome, target_class):
        result = target_class.divisible_by_two(given_number)
        assert result == expected_outcome
