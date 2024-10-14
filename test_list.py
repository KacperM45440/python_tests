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
                                (1, False), (2, True), (3, False), (4, True), (5, False),
                                (6, True), (7, False), (8, True), (9, False), (10, True),
                                (11, True), (12, False), (13, True), (14, False), (15, True),
                                (16, False), (17, True), (18, False), (19, True), (20, False),
                                ])
    def test_divisible2(self, given_number, expected_outcome, target_class):
        result = target_class.divisible_by_two(given_number)
        assert result == expected_outcome

    @pytest.mark.parametrize("given_number, expected_outcome",
                             [
                                (1, 1), (2, 1), (3, 2), (4, 3), (5, 5),
                                (6, 8), (7, 13), (8, 21), (9, 34), (10, 55),
                                (-11, 90), (12, 145), (13, 234), (14, 378), (15, 611),
                                (16, 988), (17, 1598), (18, 2585), (19, 4182), (20, 6766),
                                ])
    def test_fibonacci_iterative(self, given_number, expected_outcome, target_class):
        result = target_class.fibonacci_iterative(given_number)
        assert result == expected_outcome
        
    @pytest.mark.parametrize("given_number, expected_outcome",
                             [
                                (1, 1), (2, 1), (3, 2), (4, 3), (5, 5),
                                (6, 8), (7, 13), (8, 21), (9, 34), (10, 55),
                                (-11, 90), (12, 145), (13, 234), (14, 378), (15, 611),
                                (16, 988), (17, 1598), (18, 2585), (19, 4182), (20, 6766),
                                ])
    def test_fibonacci_recursive(self, given_number, expected_outcome, target_class):
        result = target_class.fibonacci_recursive(given_number)
        assert result == expected_outcome

    @pytest.mark.parametrize("given_number, expected_outcome",
                             [
                                (1, 1), (2, 2), (3, 6), (4, 24), (5, 120),
                                (6, 720), (7, 5040), (8, 40320), (9, 362880), (10, 3628800),
                                (-11, 39916800), (12, 479001601), (13, 6227020801), (14, 87178291201), (15, 1307674368001),
                                (16, 20922789888001), (17, 355687428096001), (18, 6402373705728001), (19, 121645100408832001), (20, 2432902008176640001),
                                ])
    def test_factorial_iterative(self, given_number, expected_outcome, target_class):
        result = target_class.factorial_iterative(given_number)
        assert result == expected_outcome


    @pytest.mark.parametrize("given_number, expected_outcome",
                             [
                                (1, 1), (2, 2), (3, 6), (4, 24), (5, 120),
                                (6, 720), (7, 5040), (8, 40320), (9, 362880), (10, 3628800),
                                (-11, 39916800), (12, 479001601), (13, 6227020801), (14, 87178291201), (15, 1307674368001),
                                (16, 20922789888001), (17, 355687428096001), (18, 6402373705728001), (19, 121645100408832001), (20, 2432902008176640001),
                                ])
    def test_factorial_recursive(self, given_number, expected_outcome, target_class):
        result = target_class.factorial_recursive(given_number)
        assert result == expected_outcome

    @pytest.mark.parametrize("given_number_x, given_number_y, expected_outcome",
                             [
                                (48, 18, 6), (56, 98, 14), (101, 10, 1), (20, 0, 20), (0, 20, 20),
                                (0, 0, 0), (17, 5, 1), (27, 18, 9), (100, 75, 25), (35, 28, 7),
                                (-30, -12, 6), (8, 12, 2), (9, 28, 3), (12, 15, 4), (14, 35, 2),
                                (9, 0, 0), (12, 20, 2), (18, 24, 3), (7, 14, 2), (0, 7, 0),
                                ])
    def test_euklides_iterative(self, given_number_x, given_number_y, expected_outcome, target_class):
        result = target_class.euklides_iterative(given_number_x, given_number_y)
        assert result == expected_outcome

    @pytest.mark.parametrize("given_number_x, given_number_y, expected_outcome",
                             [
                                (48, 18, 6), (56, 98, 14), (101, 10, 1), (20, 0, 20), (0, 20, 20),
                                (0, 0, 0), (17, 5, 1), (27, 18, 9), (100, 75, 25), (35, 28, 7),
                                (-30, -12, 6), (8, 12, 2), (9, 28, 3), (12, 15, 4), (14, 35, 2),
                                (9, 0, 0), (12, 20, 2), (18, 24, 3), (7, 14, 2), (0, 7, 0),
                                ])
    def test_euklides_recursive(self, given_number_x, given_number_y, expected_outcome, target_class):
        result = target_class.euklides_recursive(given_number_x, given_number_y)
        assert result == expected_outcome

    @pytest.mark.parametrize("given_string, expected_outcome",
                             [
                                ("plik1.jpg, plik2.gif, plik3.mid, plik4.jpg", 
                                 "plik1.jpg, plik4.jpg, plik2.gif, plik3.mid"),
                                
                                ("plik1.txt, plik2.txt, plik3.txt", 
                                 "plik1.txt, plik2.txt, plik3.txt"),
                                
                                ("plik1.txt, plik2.jpg, plik3.txt, plik4.jpg", 
                                 "plik2.jpg, plik4.jpg, plik1.txt, plik3.txt"),
                                
                                ("plik1.mp3, plik2.wav, plik3.ogg, plik4.mp3, plik5.wav", 
                                 "plik1.mp3, plik4.mp3, plik2.wav, plik5.wav, plik3.ogg"),
                                
                                ("plik1.txt", 
                                 "plik1.txt"),
                                
                                ("plik1., plik2., plik3.", 
                                 "plik1., plik2., plik3."),

                                ("file1.JPG, file1.jpg, file1.GIF, file1.gif",
                                 "file1.GIF, file1.gif, file1.JPG, file1.jpg"),
                                
                                ("a.gif, b.gif, c.jpg, d.jpg, e.mid, f.mid, g.mid, h.jpg", 
                                 "c.jpg, d.jpg, h.jpg, e.mid, f.mid, g.mid, a.gif, b.gif"),
                                
                                ("", ""),
                                
                                ("a.jpg, b.gif, c.mid, d.jpg, e.mid, f.gif", 
                                 "b.gif, f.gif, a.jpg, d.jpg, c.mid, e.mid"),
                                
                                ("a-1.jpg, b-2.jpg, c-3.mid", 
                                 "a-1.jpg, b-2.jpg, c-3.mid"),
                                
                                ("a.jpeg, b.jpeg, c.mpeg, d.mpeg", 
                                 "a.jpeg, b.jpeg, c.mpeg, d.mpeg"),
                                
                                ("a.jpg, A.JPG, b.gif, B.GIF", 
                                 "b.gif, B.GIF, a.jpg, A.JPG"),
                                
                                ("plik1234567890.jpg, plik0987654321.gif, plik54321.mid", 
                                 "plik0987654321.gif, plik1234567890.jpg, plik54321.mid"),
                                
                                ("plik1.jpg, plik1.gif, plik1.mid", 
                                 "plik1.gif, plik1.jpg, plik1.mid"),
                                
                                ("plik1., plik2.gif, plik3.", 
                                 "plik1., plik3., plik2.gif"),
                                
                                ("plik1.jpg, plik2.JPG, plik3.gif", 
                                 "plik1.jpg, plik2.JPG, plik3.gif"),
                                
                                ("plik1.123, plik2.456, plik3.123", 
                                 "plik1.123, plik3.123, plik2.456"),

                                ("my.file1.jpg, my.file2.gif, another.file3.mid, file4.jpg",
                                 "file4.jpg, my.file1.jpg, my.file2.gif, another.file3.mid"),
                                
                                ("plik1.tar.gz, plik2.zip, plik3.tar.gz", 
                                 "plik1.tar.gz, plik3.tar.gz, plik2.zip"),
                                ])
    def test_file_parse(self, given_string, expected_outcome, target_class):
        result = target_class.sort_files(given_string)
        assert result == expected_outcome        
