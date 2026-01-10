"""
Pytest fixtures for Lab 3: Functional Programming
Loads variant configuration with sensible defaults for testing.

CSC3301 Programming Language Paradigms
"""
import json
import pytest
from pathlib import Path


def load_variant_config() -> dict:
    """Load variant configuration from .variant_config.json or return defaults."""
    repo_root = Path(__file__).parent.parent.parent
    config_path = repo_root / ".variant_config.json"

    if config_path.exists():
        with open(config_path) as f:
            return json.load(f)

    # Return default configuration for testing without variant
    return get_default_config()


def get_default_config() -> dict:
    """Return default configuration for standalone testing."""
    return {
        "student_id": "default_student",
        "variant_seed": 0,
        "lab_number": 3,
        "lab_title": "Functional Programming and Higher-Order Functions",

        "map_test": {
            "input_data": [1, 2, 3, 4, 5],
            "transform_type": "multiply",
            "transform_desc": "multiply by 2",
            "transform_lambda": "lambda x: x * 2",
            "multiplier": 2,
            "addend": 0,
            "expected": [2, 4, 6, 8, 10]
        },

        "filter_test": {
            "input_data": [1, 2, 3, 4, 5, 6, 7, 8],
            "predicate_type": "greater_than",
            "predicate_desc": "greater than 4",
            "predicate_lambda": "lambda x: x > 4",
            "threshold": 4,
            "divisor": 2,
            "expected": [5, 6, 7, 8]
        },

        "reduce_test": {
            "input_data": [1, 2, 3, 4],
            "reduce_type": "sum",
            "reduce_desc": "sum",
            "reduce_lambda": "lambda acc, x: acc + x",
            "initial_value": 0,
            "expected": 10
        },

        "zip_with_test": {
            "list1": [1, 2, 3, 4],
            "list2": [5, 6, 7, 8],
            "combine_type": "add",
            "combine_desc": "add pairs",
            "combine_lambda": "lambda a, b: a + b",
            "expected": [6, 8, 10, 12]
        },

        "transformation_chain": {
            "initial_data": [3, 7, 12, 5, 15, 8],
            "chain": [
                {"operation": "filter", "description": "keep values > 6", "lambda": "lambda x: x > 6"},
                {"operation": "map", "description": "multiply by 2", "lambda": "lambda x: x * 2"},
                {"operation": "reduce", "description": "sum all values", "lambda": "lambda acc, x: acc + x", "initial": 0}
            ],
            "intermediate_after_filter": [7, 12, 15, 8],
            "intermediate_after_map": [14, 24, 30, 16],
            "final_result": 84,
            "threshold": 6,
            "multiplier": 2
        },

        "empty_list_test": {
            "map_result": [],
            "filter_result": [],
            "reduce_initial": 0
        },

        "lazy_test": {
            "large_range_limit": 3,
            "expected_first_n": [1, 2, 3]
        }
    }


# Global variant configuration - loaded once
_variant_config = None


def get_variant() -> dict:
    """Get cached variant configuration."""
    global _variant_config
    if _variant_config is None:
        _variant_config = load_variant_config()
    return _variant_config


@pytest.fixture
def variant_config():
    """Fixture providing the complete variant configuration."""
    return get_variant()


@pytest.fixture
def map_test_data(variant_config):
    """Fixture providing map test data from variant."""
    return variant_config["map_test"]


@pytest.fixture
def filter_test_data(variant_config):
    """Fixture providing filter test data from variant."""
    return variant_config["filter_test"]


@pytest.fixture
def reduce_test_data(variant_config):
    """Fixture providing reduce test data from variant."""
    return variant_config["reduce_test"]


@pytest.fixture
def zip_with_test_data(variant_config):
    """Fixture providing zip_with test data from variant."""
    return variant_config["zip_with_test"]


@pytest.fixture
def transformation_chain_data(variant_config):
    """Fixture providing transformation chain test data."""
    return variant_config["transformation_chain"]


@pytest.fixture
def empty_list_test_data(variant_config):
    """Fixture providing empty list test configuration."""
    return variant_config["empty_list_test"]


@pytest.fixture
def lazy_test_data(variant_config):
    """Fixture providing lazy evaluation test configuration."""
    return variant_config["lazy_test"]


@pytest.fixture
def student_id(variant_config):
    """Fixture providing the student ID."""
    return variant_config["student_id"]


# Helper functions for tests
def create_lambda_from_string(lambda_str: str):
    """
    Safely evaluate a lambda string.
    Only allows simple lambda expressions for security.
    """
    # Validate the string starts with "lambda"
    if not lambda_str.strip().startswith("lambda"):
        raise ValueError("Invalid lambda expression")

    # Basic validation - no dangerous operations
    dangerous = ["import", "exec", "eval", "open", "__", "globals", "locals"]
    for d in dangerous:
        if d in lambda_str:
            raise ValueError(f"Potentially dangerous operation: {d}")

    return eval(lambda_str)


@pytest.fixture
def lambda_helper():
    """Fixture providing lambda creation helper."""
    return create_lambda_from_string
