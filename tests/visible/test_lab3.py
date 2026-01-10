"""
Lab 3: Functional Programming - Visible Tests
Tests use variant-specific data when available, with sensible defaults.

CSC3301 Programming Language Paradigms
"""
import pytest
import types
from src.task2_hof import my_map, my_filter, my_reduce, my_zip_with


class TestMyMap:
    """Tests for the my_map higher-order function."""

    def test_my_map_basic(self):
        """Basic test: double each element."""
        result = list(my_map(lambda x: x * 2, iter([1, 2, 3])))
        assert result == [2, 4, 6]

    def test_my_map_is_lazy(self):
        """my_map should return a generator, not a list."""
        result = my_map(lambda x: x, iter([1, 2, 3]))
        assert isinstance(result, types.GeneratorType), "my_map must return a generator"

    def test_my_map_empty(self):
        """my_map on empty iterable should return empty."""
        result = list(my_map(lambda x: x * 2, iter([])))
        assert result == []

    def test_my_map_with_variant(self, map_test_data, lambda_helper):
        """Test my_map with variant-specific data."""
        input_data = map_test_data["input_data"]
        transform = lambda_helper(map_test_data["transform_lambda"])
        expected = map_test_data["expected"]

        result = list(my_map(transform, iter(input_data)))
        assert result == expected, f"Expected {expected}, got {result}"

    def test_my_map_string_transform(self):
        """Test my_map with string transformation."""
        result = list(my_map(lambda x: x.upper(), iter(["a", "b", "c"])))
        assert result == ["A", "B", "C"]


class TestMyFilter:
    """Tests for the my_filter higher-order function."""

    def test_my_filter_basic(self):
        """Basic test: keep elements greater than 2."""
        result = list(my_filter(lambda x: x > 2, iter([1, 2, 3, 4])))
        assert result == [3, 4]

    def test_my_filter_is_lazy(self):
        """my_filter should return a generator, not a list."""
        result = my_filter(lambda x: True, iter([1, 2, 3]))
        assert isinstance(result, types.GeneratorType), "my_filter must return a generator"

    def test_my_filter_empty(self):
        """my_filter on empty iterable should return empty."""
        result = list(my_filter(lambda x: x > 0, iter([])))
        assert result == []

    def test_my_filter_none_match(self):
        """my_filter with no matches should return empty."""
        result = list(my_filter(lambda x: x > 100, iter([1, 2, 3])))
        assert result == []

    def test_my_filter_all_match(self):
        """my_filter where all match should return all."""
        result = list(my_filter(lambda x: x > 0, iter([1, 2, 3])))
        assert result == [1, 2, 3]

    def test_my_filter_with_variant(self, filter_test_data, lambda_helper):
        """Test my_filter with variant-specific data."""
        input_data = filter_test_data["input_data"]
        predicate = lambda_helper(filter_test_data["predicate_lambda"])
        expected = filter_test_data["expected"]

        result = list(my_filter(predicate, iter(input_data)))
        assert result == expected, f"Expected {expected}, got {result}"


class TestMyReduce:
    """Tests for the my_reduce higher-order function."""

    def test_my_reduce_sum(self):
        """Basic test: sum all elements."""
        result = my_reduce(lambda a, x: a + x, iter([1, 2, 3]), 0)
        assert result == 6

    def test_my_reduce_product(self):
        """Test reduce with multiplication."""
        result = my_reduce(lambda a, x: a * x, iter([1, 2, 3, 4]), 1)
        assert result == 24

    def test_my_reduce_empty(self, empty_list_test_data):
        """my_reduce on empty iterable should return initial value."""
        initial = empty_list_test_data["reduce_initial"]
        result = my_reduce(lambda a, x: a + x, iter([]), initial)
        assert result == initial

    def test_my_reduce_single_element(self):
        """my_reduce on single element iterable."""
        result = my_reduce(lambda a, x: a + x, iter([5]), 0)
        assert result == 5

    def test_my_reduce_with_variant(self, reduce_test_data, lambda_helper):
        """Test my_reduce with variant-specific data."""
        input_data = reduce_test_data["input_data"]
        reducer = lambda_helper(reduce_test_data["reduce_lambda"])
        initial = reduce_test_data["initial_value"]
        expected = reduce_test_data["expected"]

        result = my_reduce(reducer, iter(input_data), initial)
        assert result == expected, f"Expected {expected}, got {result}"

    def test_my_reduce_string_concat(self):
        """Test reduce with string concatenation."""
        result = my_reduce(lambda a, x: a + x, iter(["a", "b", "c"]), "")
        assert result == "abc"


class TestMyZipWith:
    """Tests for the my_zip_with higher-order function."""

    def test_my_zip_with_add(self):
        """Basic test: add corresponding elements."""
        result = list(my_zip_with(lambda a, b: a + b, iter([1, 2, 3]), iter([4, 5, 6])))
        assert result == [5, 7, 9]

    def test_my_zip_with_is_lazy(self):
        """my_zip_with should return a generator, not a list."""
        result = my_zip_with(lambda a, b: a + b, iter([1]), iter([2]))
        assert isinstance(result, types.GeneratorType), "my_zip_with must return a generator"

    def test_my_zip_with_empty(self):
        """my_zip_with on empty iterables should return empty."""
        result = list(my_zip_with(lambda a, b: a + b, iter([]), iter([])))
        assert result == []

    def test_my_zip_with_unequal_lengths(self):
        """my_zip_with should stop at shorter iterable."""
        result = list(my_zip_with(lambda a, b: a + b, iter([1, 2, 3, 4]), iter([10, 20])))
        assert result == [11, 22]

    def test_my_zip_with_tuple(self):
        """Test my_zip_with creating tuples."""
        result = list(my_zip_with(lambda a, b: (a, b), iter([1, 2]), iter([3, 4])))
        assert result == [(1, 3), (2, 4)]

    def test_my_zip_with_variant(self, zip_with_test_data, lambda_helper):
        """Test my_zip_with with variant-specific data."""
        list1 = zip_with_test_data["list1"]
        list2 = zip_with_test_data["list2"]
        combiner = lambda_helper(zip_with_test_data["combine_lambda"])
        expected = zip_with_test_data["expected"]

        result = list(my_zip_with(combiner, iter(list1), iter(list2)))
        assert result == expected, f"Expected {expected}, got {result}"


class TestTransformationChain:
    """Tests for chaining HOF operations together."""

    def test_chain_filter_then_map(self, transformation_chain_data, lambda_helper):
        """Test chaining filter and map operations."""
        data = transformation_chain_data["initial_data"]
        threshold = transformation_chain_data["threshold"]
        multiplier = transformation_chain_data["multiplier"]

        # Apply filter then map
        filtered = my_filter(lambda x: x > threshold, iter(data))
        mapped = my_map(lambda x: x * multiplier, filtered)
        result = list(mapped)

        expected = transformation_chain_data["intermediate_after_map"]
        assert result == expected, f"Expected {expected}, got {result}"

    def test_full_chain(self, transformation_chain_data, lambda_helper):
        """Test complete filter -> map -> reduce chain."""
        data = transformation_chain_data["initial_data"]
        threshold = transformation_chain_data["threshold"]
        multiplier = transformation_chain_data["multiplier"]

        # Apply full chain
        filtered = my_filter(lambda x: x > threshold, iter(data))
        mapped = my_map(lambda x: x * multiplier, filtered)
        result = my_reduce(lambda acc, x: acc + x, mapped, 0)

        expected = transformation_chain_data["final_result"]
        assert result == expected, f"Expected {expected}, got {result}"


class TestLazyEvaluation:
    """Tests for lazy evaluation behavior."""

    def test_map_lazy_infinite(self, lazy_test_data):
        """Test that map is truly lazy by using limited consumption."""
        def infinite_counter():
            n = 0
            while True:
                n += 1
                yield n

        limit = lazy_test_data["large_range_limit"]
        gen = my_map(lambda x: x, infinite_counter())

        # Take only first few elements - should not hang
        result = []
        for _ in range(limit):
            result.append(next(gen))

        assert result == list(range(1, limit + 1))

    def test_filter_lazy_infinite(self, lazy_test_data):
        """Test that filter is truly lazy."""
        def infinite_counter():
            n = 0
            while True:
                n += 1
                yield n

        limit = lazy_test_data["large_range_limit"]
        gen = my_filter(lambda x: True, infinite_counter())

        result = []
        for _ in range(limit):
            result.append(next(gen))

        assert result == list(range(1, limit + 1))
