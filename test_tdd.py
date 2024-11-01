import pytest
import math
from test_me import Point, Line, Vector, Vector3D

class TestClass:
    @pytest.fixture(scope="class")
    def point(self):
        return Point(0,0)
    @pytest.fixture(scope="class")
    def line(self):
        return Line(0,0,0)
    @pytest.fixture(scope="class")
    def vector(self):
        return Vector(0,0)
    @pytest.fixture(scope="class")
    def vector3d(self):
        return Vector3D(0,0,0)

    @pytest.mark.parametrize("p1_x, p1_y, p2_x, p2_y, expected_outcome",
                             [
                                (0, 0, 3, 4, 5),          
                                (1, 1, 4, 5, 5),          
                                (0, 0, 0, 0, 0),          
                                (-1, -1, -4, -5, 5),      
                                (2, 3, 2, 3, 0),          
                                (0, 0, 1, 1, math.sqrt(2)),  
                                (-3, -4, 0, 0, 5),        
                                (5, 5, 8, 9, 5),          
                                (-2, -3, -6, -8, math.sqrt(16 + 25)), 
                                (10, 10, 10, 10, 0),      
                                (0, 4, 6, 8, 10),         
                                (100, 100, 100, 104, 5),  
                                (5, 0, 5, 12, 5),       
                                (-5, -5, 0, 0, math.sqrt(5)), 
                                (3, 3, -3, -3, math.sqrt(73)), 
                                (1000, 1000, 1003, 1004, 1005), 
                                (0, 0, -3, -4, -5),        
                                (1, 2, 4, 6, 7),         
                                (-7, -4, 17, 4, math.sqrt(24**2 + 10**2)),
                                (123, 456, 789, 1011, math.sqrt((789 - 123)**2 + (1010 - 456)**2)),
                                ])
    def test_distance(self, p1_x, p1_y, p2_x, p2_y, expected_outcome, point):
        p1 = Point(p1_x, p1_y)
        p2 = Point(p2_x, p2_y)
        result = p1.distance(p2)
        assert result == expected_outcome

    @pytest.mark.parametrize("a, b, c, expected_a, expected_b, expected_c",
                             [
                                (1, -1, 0, 1, -1, 1),                
                                (0, 1, -2, 0, 1, -2),                
                                (2, -3, 6, 2, -3, 6),                
                                (-1, -1, 1, -1, -1, 1),              
                                (3, 4, -5, 3, 4, -5),                
                                ])
    def test_line_from_parameters(self, a, b, c, expected_a, expected_b, expected_c, line):
        l1 = Line(a=a, b=b, c=c)
        assert l1.a == expected_a
        assert l1.b == expected_b
        assert l1.c == expected_c

    @pytest.mark.parametrize("p1, p2, expected_a, expected_b, expected_c",
                             [
                                (Point(0, 0), Point(1, 1), 1, -1, -1),       
                                (Point(1, 2), Point(3, 6), 2, -1, 3),       
                                (Point(-1, -1), Point(2, 1), 2, -3, -1),     
                                (Point(0, 0), Point(0, 1), 1, 0, 0),         
                                (Point(0, 0), Point(1, 0), 0, 1, 1),         
                                ])
    def test_line_from_two_points(self, p1, p2, expected_a, expected_b, expected_c, line):
        l1 = Line(p1=p1, p2=p2)
        assert l1.a == expected_a
        assert l1.b == expected_b
        assert l1.c == expected_c

    @pytest.mark.parametrize("point, vector, expected_a, expected_b, expected_c",
                             [
                                (Point(0, 0), Point(1, 1), 1, -1, 0),        
                                (Point(1, 2), Point(2, 1), 1, -2, 2),        
                                (Point(0, 0), Point(0, 1), 1, 0, 1),        
                                (Point(0, 0), Point(1, 0), 0, -1, 1),      
                                (Point(1, 1), Point(-2, -3), -3, 2, 2),      
                                ])
    def test_line_from_point_and_vector(self, point, vector, expected_a, expected_b, expected_c, line):
        l1 = Line(point=point, vector=vector)
        assert l1.a == expected_a
        assert l1.b == expected_b
        assert l1.c == expected_c

    @pytest.mark.parametrize("line1, line2, should_be_equal",
                             [
                                (Line(a=1, b=-1, c=0), Line(p1=Point(0, 0), p2=Point(1, 1)), True),  
                                (Line(a=2, b=-3, c=6), Line(a=4, b=-6, c=12), False),                
                                (Line(a=3, b=4, c=-5), Line(a=-3, b=-4, c=5), False),                 
                                (Line(a=1, b=2, c=3), Line(a=2, b=4, c=5), False),                   
                                (Line(p1=Point(1, 1), p2=Point(2, 3)), Line(point=Point(1, 1), vector=Point(1, 2)), True),
                                ])
    def test_line_equality(self, line1, line2, should_be_equal):
        if should_be_equal:
            assert line1 == line2
        else:
            assert line1 != line2

    @pytest.mark.parametrize("x, y, expected_x, expected_y",
                             [
                                (3, 4, 3, 3),                
                                (0, 0, 0, 0),                
                                (-5, 2, -5, -2),              
                                (1.5, -3.5, 1.5, -3.5),      
                                ])
    def test_vector_direct_creation(self, x, y, expected_x, expected_y, vector):
        v1 = Vector(x=x, y=y)
        assert v1.x == expected_x
        assert v1.y == expected_y

    @pytest.mark.parametrize("p1, p2, expected_x, expected_y",
                             [
                                (Point(1, 2), Point(3, 4), 2, 2),              
                                (Point(-1, -1), Point(1, 1), 2, 2),                          
                                (Point(2, 3), Point(2, 3), 0, 2),              
                                ])
    def test_vector_from_points(self, p1, p2, expected_x, expected_y, vector):
        v1 = Vector(p1=p1, p2=p2)
        assert v1.x == expected_x
        assert v1.y == expected_y

    @pytest.mark.parametrize("line, expected_x, expected_y",
                             [
                                (Line(a=1, b=-1, c=0), 1, 1),         
                                (Line(a=0, b=1, c=-2), -1, 2),                     
                                (Line(a=3, b=4, c=-5), 4, -3),          
                                ])
    def test_vector_from_line(self, line, expected_x, expected_y, vector):
        v1 = Vector(line=line)
        assert v1.x == expected_x
        assert v1.y == expected_y

    @pytest.mark.parametrize("v1, v2, expected_x, expected_y",
                             [
                                (Vector(1, 2), Vector(3, 4), 4, 6),       
                                (Vector(-1, -1), Vector(1, 1), 0, 9),     
                                (Vector(5, 0), Vector(0, 3), 5, 3),        
                                ])
    def test_vector_addition(self, v1, v2, expected_x, expected_y, vector):
        v = v1 + v2
        assert v.x == expected_x
        assert v.y == expected_y

    @pytest.mark.parametrize("v1, v2, expected_x, expected_y",
                             [
                                (Vector(5, 3), Vector(2, 1), 3, 2),           
                                (Vector(0, 0), Vector(2, 3), -2, -3),         
                                (Vector(4, -2), Vector(4, -2), 0, 4),         
                                ])
    def test_vector_subtraction(self, v1, v2, expected_x, expected_y, vector):
        v = v1 - v2
        assert v.x == expected_x
        assert v.y == expected_y

    @pytest.mark.parametrize("v1, v2, expected_z",
                             [
                                (Vector(1, 0), Vector(0, 1), 1),        
                                (Vector(0, 1), Vector(1, 0), -2),      
                                (Vector(1, 2), Vector(3, 4), -3),      
                                (Vector(-1, 1), Vector(2, 2), 4),      
                                ])
    def test_vector_multiplication(self, v1, v2, expected_z, vector):
        v3 = v1.multiply_vectors(v2)
        assert isinstance(v3, Vector3D)
        assert v3.z == expected_z
