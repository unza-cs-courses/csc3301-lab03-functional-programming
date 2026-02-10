"""
Lab 3: Functional Programming and Higher-Order Functions
CSC3301 Programming Language Paradigms

This module organizes functional programming concepts across three tasks:
- Task 1 (task1_basics): First-class functions, lambdas, closures
- Task 2 (task2_hof): Higher-order functions (map, filter, reduce)
- Task 3 (task3_advanced): Currying, partial application, lazy evaluation, memoization
"""

# Import from Task 1: Basic Functional Programming
from .task1_basics import (
    apply_twice,
    create_multiplier,
    create_adder,
    make_counter,
    make_multiplier_with_limit,
    make_operation,
    compose_simple,
    apply_in_sequence,
)

# Import from Task 2: Higher-Order Functions
from .task2_hof import (
    my_map,
    my_filter,
    my_reduce,
    my_zip_with,
    compose,
)

# Import from Task 3: Advanced Functional Programming
from .task3_advanced import (
    curry,
    partial,
    lazy_range,
    take,
    pipe,
    memoize,
    fibonacci,
    Pipeline,
    repeatedly,
    until,
)

__all__ = [
    # Task 1
    "apply_twice",
    "create_multiplier",
    "create_adder",
    "make_counter",
    "make_multiplier_with_limit",
    "make_operation",
    "compose_simple",
    "apply_in_sequence",
    # Task 2
    "my_map",
    "my_filter",
    "my_reduce",
    "my_zip_with",
    "compose",
    # Task 3
    "curry",
    "partial",
    "lazy_range",
    "take",
    "pipe",
    "memoize",
    "fibonacci",
    "Pipeline",
    "repeatedly",
    "until",
]
