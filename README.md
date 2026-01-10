# Lab 3: Functional Programming and Higher-Order Functions

**CSC3301 Programming Language Paradigms**
**Points:** 100

## Overview

This lab focuses on implementing fundamental higher-order functions (HOFs) from scratch. You will build your own versions of `map`, `filter`, `reduce`, and `zip_with` without using Python's built-in implementations.

## Learning Objectives

- Understand how higher-order functions work internally
- Implement lazy evaluation using Python generators
- Practice functional programming patterns
- Learn to compose functions for data transformation pipelines

## Tasks

### Task 1: Implement `my_map` (25 points)
Apply a transformation function to each element of an iterable.
- Must return a generator (lazy evaluation)
- Cannot use built-in `map()`

### Task 2: Implement `my_filter` (25 points)
Keep only elements that satisfy a predicate function.
- Must return a generator (lazy evaluation)
- Cannot use built-in `filter()`

### Task 3: Implement `my_reduce` (25 points)
Reduce an iterable to a single value using an accumulator function.
- Must process elements left-to-right
- Cannot use `functools.reduce()`

### Task 4: Implement `my_zip_with` (25 points)
Combine two iterables element-wise using a combining function.
- Must return a generator (lazy evaluation)
- Should stop when the shorter iterable is exhausted

## Getting Started

1. Open `src/task2_hof.py`
2. Implement each function according to its docstring
3. Run tests to verify your implementation

## Running Tests

```bash
# Run visible tests
pytest tests/visible/ -v

# Run with detailed output
pytest tests/visible/ -v --tb=long
```

## File Structure

```
.
├── src/
│   └── task2_hof.py          # Your implementation goes here
├── tests/
│   └── visible/
│       ├── conftest.py       # Test fixtures and configuration
│       └── test_lab3.py      # Visible test cases
├── scripts/
│   ├── variant_generator.py  # Generates student-specific variants
│   └── generate_assignment.py # Creates personalized assignment
├── .github/
│   └── workflows/
│       ├── autograding.yml   # Runs tests on push
│       └── generate-variant.yml # Generates variant on repo creation
├── ASSIGNMENT_TEMPLATE.md    # Template for personalized assignment
├── ASSIGNMENT.md             # Your personalized assignment (generated)
└── README.md                 # This file
```

---

## Variant System Documentation

This assignment uses a **variant-based system** to generate unique test values for each student. This ensures academic integrity while maintaining consistent learning objectives.

### How It Works

1. **Automatic Generation**: When your repository is created via GitHub Classroom, a GitHub Action automatically generates your unique variant based on your GitHub username.

2. **Deterministic Variants**: The variant is generated using a hash of your student ID, ensuring:
   - Each student gets unique test values
   - The same student always gets the same variant
   - Instructors can reproduce any student's variant

3. **Personalized Assignment**: After variant generation, `ASSIGNMENT.md` is created with your specific test values.

### Variant Components

Your variant includes personalized values for:

| Component | Description |
|-----------|-------------|
| **Map Test** | Unique input data and transformation |
| **Filter Test** | Unique input data and predicate condition |
| **Reduce Test** | Unique input data and reduction operation |
| **Zip-With Test** | Unique input lists and combining operation |
| **Transformation Chain** | Complete filter-map-reduce pipeline test |

### Configuration Files

- **`.variant_config.json`**: Contains your complete variant configuration (generated automatically)
- **`ASSIGNMENT.md`**: Your personalized assignment with specific values (generated automatically)

### Manual Variant Generation

If you need to regenerate your variant (instructors only):

```bash
# Generate variant for a specific student
python scripts/variant_generator.py <student_id>

# Generate personalized assignment
python scripts/generate_assignment.py
```

### Test Fixtures

Tests use pytest fixtures that automatically load your variant configuration:

```python
def test_my_map_with_variant(self, map_test_data, lambda_helper):
    """Test uses variant-specific data."""
    input_data = map_test_data["input_data"]
    transform = lambda_helper(map_test_data["transform_lambda"])
    expected = map_test_data["expected"]

    result = list(my_map(transform, iter(input_data)))
    assert result == expected
```

If no variant configuration exists, sensible defaults are used.

---

## Submission Guidelines

1. Implement all functions in `src/task2_hof.py`
2. Ensure all visible tests pass locally
3. Push your changes to trigger the autograder
4. Check GitHub Actions for your score

## Tips

- Use `yield` to create lazy generators
- Test with the basic examples first, then check variant-specific tests
- Remember: functions should work with any iterable, not just lists
- Edge cases matter: empty iterables, single elements, etc.

## Academic Integrity

Each student receives unique test values. Your implementation must work correctly with YOUR specific values. Copying code that works for another student's values will not pass your tests.
