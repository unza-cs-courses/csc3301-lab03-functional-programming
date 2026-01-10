#!/usr/bin/env python3
"""
Variant Generator for Lab 3: Functional Programming
Generates unique variants based on student ID for HOF operations.

CSC3301 Programming Language Paradigms
"""
import hashlib
import json
import sys
from pathlib import Path
from typing import Dict, Any, List


def generate_seed(student_id: str) -> int:
    """Generate deterministic seed from student ID."""
    hash_bytes = hashlib.sha256(student_id.encode()).digest()
    return int.from_bytes(hash_bytes[:8], byteorder='big')


class SeededRandom:
    """Simple deterministic random number generator."""

    def __init__(self, seed: int):
        self.state = seed

    def next(self) -> int:
        """Linear congruential generator."""
        self.state = (self.state * 1103515245 + 12345) & 0x7FFFFFFF
        return self.state

    def randint(self, low: int, high: int) -> int:
        """Generate random integer in range [low, high]."""
        return low + (self.next() % (high - low + 1))

    def choice(self, items: list):
        """Choose random item from list."""
        return items[self.next() % len(items)]

    def sample(self, items: list, k: int) -> list:
        """Sample k items from list without replacement."""
        items_copy = items.copy()
        result = []
        for _ in range(min(k, len(items_copy))):
            idx = self.next() % len(items_copy)
            result.append(items_copy.pop(idx))
        return result

    def shuffle(self, items: list) -> list:
        """Return a shuffled copy of the list."""
        items_copy = items.copy()
        for i in range(len(items_copy) - 1, 0, -1):
            j = self.next() % (i + 1)
            items_copy[i], items_copy[j] = items_copy[j], items_copy[i]
        return items_copy


def generate_map_data(rng: SeededRandom) -> Dict[str, Any]:
    """Generate data for my_map tests."""
    # Different base datasets
    base_numbers = list(range(1, 11))
    shuffled = rng.shuffle(base_numbers)
    data_set = shuffled[:rng.randint(4, 7)]

    # Different transformation types
    multipliers = [2, 3, 4, 5]
    multiplier = rng.choice(multipliers)

    addends = [1, 5, 10, -3, 7]
    addend = rng.choice(addends)

    # Select transformation type
    transform_types = ["multiply", "add", "square", "negate"]
    transform_type = rng.choice(transform_types)

    if transform_type == "multiply":
        expected = [x * multiplier for x in data_set]
        transform_desc = f"multiply by {multiplier}"
        transform_lambda = f"lambda x: x * {multiplier}"
    elif transform_type == "add":
        expected = [x + addend for x in data_set]
        transform_desc = f"add {addend}"
        transform_lambda = f"lambda x: x + {addend}"
    elif transform_type == "square":
        expected = [x * x for x in data_set]
        transform_desc = "square"
        transform_lambda = "lambda x: x * x"
    else:  # negate
        expected = [-x for x in data_set]
        transform_desc = "negate"
        transform_lambda = "lambda x: -x"

    return {
        "input_data": data_set,
        "transform_type": transform_type,
        "transform_desc": transform_desc,
        "transform_lambda": transform_lambda,
        "multiplier": multiplier,
        "addend": addend,
        "expected": expected
    }


def generate_filter_data(rng: SeededRandom) -> Dict[str, Any]:
    """Generate data for my_filter tests."""
    # Generate diverse input set
    base = list(range(1, 16))
    data_set = rng.shuffle(base)[:rng.randint(6, 10)]

    # Different predicate types
    predicate_types = ["greater_than", "less_than", "even", "odd", "divisible_by"]
    predicate_type = rng.choice(predicate_types)

    threshold = rng.randint(3, 10)
    divisor = rng.choice([2, 3, 4, 5])

    if predicate_type == "greater_than":
        expected = [x for x in data_set if x > threshold]
        predicate_desc = f"greater than {threshold}"
        predicate_lambda = f"lambda x: x > {threshold}"
    elif predicate_type == "less_than":
        expected = [x for x in data_set if x < threshold]
        predicate_desc = f"less than {threshold}"
        predicate_lambda = f"lambda x: x < {threshold}"
    elif predicate_type == "even":
        expected = [x for x in data_set if x % 2 == 0]
        predicate_desc = "even numbers"
        predicate_lambda = "lambda x: x % 2 == 0"
    elif predicate_type == "odd":
        expected = [x for x in data_set if x % 2 == 1]
        predicate_desc = "odd numbers"
        predicate_lambda = "lambda x: x % 2 == 1"
    else:  # divisible_by
        expected = [x for x in data_set if x % divisor == 0]
        predicate_desc = f"divisible by {divisor}"
        predicate_lambda = f"lambda x: x % {divisor} == 0"

    return {
        "input_data": data_set,
        "predicate_type": predicate_type,
        "predicate_desc": predicate_desc,
        "predicate_lambda": predicate_lambda,
        "threshold": threshold,
        "divisor": divisor,
        "expected": expected
    }


def generate_reduce_data(rng: SeededRandom) -> Dict[str, Any]:
    """Generate data for my_reduce tests."""
    # Generate input set
    base = list(range(1, 10))
    data_set = rng.shuffle(base)[:rng.randint(4, 6)]

    # Different reduce operations
    reduce_types = ["sum", "product", "max", "min", "concat_str"]
    reduce_type = rng.choice(reduce_types)

    if reduce_type == "sum":
        initial = rng.randint(0, 5)
        expected = initial + sum(data_set)
        reduce_desc = "sum"
        reduce_lambda = "lambda acc, x: acc + x"
    elif reduce_type == "product":
        initial = 1
        product = 1
        for x in data_set:
            product *= x
        expected = product
        reduce_desc = "product"
        reduce_lambda = "lambda acc, x: acc * x"
    elif reduce_type == "max":
        initial = data_set[0] if data_set else 0
        expected = max(data_set) if data_set else initial
        reduce_desc = "maximum"
        reduce_lambda = "lambda acc, x: x if x > acc else acc"
    elif reduce_type == "min":
        initial = data_set[0] if data_set else 0
        expected = min(data_set) if data_set else initial
        reduce_desc = "minimum"
        reduce_lambda = "lambda acc, x: x if x < acc else acc"
    else:  # concat as string
        initial = ""
        expected = "".join(str(x) for x in data_set)
        reduce_desc = "concatenation"
        reduce_lambda = "lambda acc, x: acc + str(x)"

    return {
        "input_data": data_set,
        "reduce_type": reduce_type,
        "reduce_desc": reduce_desc,
        "reduce_lambda": reduce_lambda,
        "initial_value": initial,
        "expected": expected
    }


def generate_zip_with_data(rng: SeededRandom) -> Dict[str, Any]:
    """Generate data for my_zip_with tests."""
    # Generate two input sets
    length = rng.randint(4, 6)
    list1 = [rng.randint(1, 10) for _ in range(length)]
    list2 = [rng.randint(1, 10) for _ in range(length)]

    # Different combine operations
    combine_types = ["add", "multiply", "subtract", "pair"]
    combine_type = rng.choice(combine_types)

    if combine_type == "add":
        expected = [a + b for a, b in zip(list1, list2)]
        combine_desc = "add pairs"
        combine_lambda = "lambda a, b: a + b"
    elif combine_type == "multiply":
        expected = [a * b for a, b in zip(list1, list2)]
        combine_desc = "multiply pairs"
        combine_lambda = "lambda a, b: a * b"
    elif combine_type == "subtract":
        expected = [a - b for a, b in zip(list1, list2)]
        combine_desc = "subtract pairs"
        combine_lambda = "lambda a, b: a - b"
    else:  # pair as tuple
        expected = [(a, b) for a, b in zip(list1, list2)]
        combine_desc = "create tuples"
        combine_lambda = "lambda a, b: (a, b)"

    return {
        "list1": list1,
        "list2": list2,
        "combine_type": combine_type,
        "combine_desc": combine_desc,
        "combine_lambda": combine_lambda,
        "expected": expected
    }


def generate_transformation_chain(rng: SeededRandom) -> Dict[str, Any]:
    """Generate a chain of transformations for pipeline testing."""
    # Initial data
    data = [rng.randint(1, 20) for _ in range(rng.randint(5, 8))]

    # Build transformation chain
    chain = []
    result = data.copy()

    # Step 1: Filter
    threshold = rng.randint(5, 12)
    result = [x for x in result if x > threshold]
    chain.append({
        "operation": "filter",
        "description": f"keep values > {threshold}",
        "lambda": f"lambda x: x > {threshold}"
    })

    # Step 2: Map
    multiplier = rng.choice([2, 3])
    result = [x * multiplier for x in result]
    chain.append({
        "operation": "map",
        "description": f"multiply by {multiplier}",
        "lambda": f"lambda x: x * {multiplier}"
    })

    # Step 3: Reduce
    chain.append({
        "operation": "reduce",
        "description": "sum all values",
        "lambda": "lambda acc, x: acc + x",
        "initial": 0
    })
    final_result = sum(result)

    return {
        "initial_data": data,
        "chain": chain,
        "intermediate_after_filter": [x for x in data if x > threshold],
        "intermediate_after_map": result,
        "final_result": final_result,
        "threshold": threshold,
        "multiplier": multiplier
    }


def generate_variant(student_id: str) -> Dict[str, Any]:
    """Generate complete variant configuration for a student."""
    seed = generate_seed(student_id)
    rng = SeededRandom(seed)

    variant = {
        "student_id": student_id,
        "variant_seed": seed,
        "lab_number": 3,
        "lab_title": "Functional Programming and Higher-Order Functions",

        # HOF test data
        "map_test": generate_map_data(rng),
        "filter_test": generate_filter_data(rng),
        "reduce_test": generate_reduce_data(rng),
        "zip_with_test": generate_zip_with_data(rng),

        # Transformation chain for advanced testing
        "transformation_chain": generate_transformation_chain(rng),

        # Additional test values for edge cases
        "empty_list_test": {
            "map_result": [],
            "filter_result": [],
            "reduce_initial": rng.randint(0, 10)
        },

        # Lazy evaluation test values
        "lazy_test": {
            "large_range_limit": rng.randint(3, 5),
            "expected_first_n": list(range(1, rng.randint(3, 5) + 1))
        }
    }

    return variant


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python variant_generator.py <student_id>")
        print("Example: python variant_generator.py jdoe2024")
        sys.exit(1)

    student_id = sys.argv[1]

    # Generate variant
    variant = generate_variant(student_id)

    # Determine output path
    repo_root = Path(__file__).parent.parent
    config_path = repo_root / ".variant_config.json"

    # Write variant configuration
    with open(config_path, 'w') as f:
        json.dump(variant, f, indent=2)

    print(f"Generated variant for student: {student_id}")
    print(f"Variant seed: {variant['variant_seed']}")
    print(f"Configuration saved to: {config_path}")

    # Print summary
    print("\nVariant Summary:")
    print(f"  Map test: {variant['map_test']['transform_desc']} on {variant['map_test']['input_data']}")
    print(f"  Filter test: {variant['filter_test']['predicate_desc']} on {variant['filter_test']['input_data']}")
    print(f"  Reduce test: {variant['reduce_test']['reduce_desc']} on {variant['reduce_test']['input_data']}")
    print(f"  Zip-with test: {variant['zip_with_test']['combine_desc']}")


if __name__ == "__main__":
    main()
