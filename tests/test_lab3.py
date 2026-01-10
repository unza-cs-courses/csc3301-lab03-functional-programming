import pytest
from src.task2_hof import my_map, my_filter, my_reduce

class TestHOF:
    def test_my_map(self):
        result = list(my_map(lambda x: x * 2, iter([1, 2, 3])))
        assert result == [2, 4, 6]
    
    def test_my_filter(self):
        result = list(my_filter(lambda x: x > 2, iter([1, 2, 3, 4])))
        assert result == [3, 4]
    
    def test_my_reduce(self):
        result = my_reduce(lambda a, x: a + x, iter([1, 2, 3]), 0)
        assert result == 6
    
    def test_my_map_is_lazy(self):
        """my_map should return a generator, not a list."""
        import types
        result = my_map(lambda x: x, iter([1, 2, 3]))
        assert isinstance(result, types.GeneratorType)
