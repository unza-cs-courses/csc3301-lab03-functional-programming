# Lab 3: Functional Programming and Higher-Order Functions

**CSC3301 Programming Language Paradigms**
**Student ID:** {{STUDENT_ID}}
**Points:** 100

---

## Overview

In this lab, you will implement fundamental higher-order functions from scratch. These functions are the building blocks of functional programming and are used extensively in modern programming languages.

**Important:** You must implement these functions WITHOUT using Python's built-in `map()`, `filter()`, or `functools.reduce()`. The goal is to understand how these functions work internally.

---

## Your Personalized Test Values

Your implementation will be tested with the following student-specific values:

### Map Test
- **Input data:** `{{MAP_INPUT_DATA}}`
- **Transformation:** {{MAP_TRANSFORM_DESC}}
- **Expected output:** `{{MAP_EXPECTED}}`

### Filter Test
- **Input data:** `{{FILTER_INPUT_DATA}}`
- **Predicate:** {{FILTER_PREDICATE_DESC}}
- **Expected output:** `{{FILTER_EXPECTED}}`

### Reduce Test
- **Input data:** `{{REDUCE_INPUT_DATA}}`
- **Operation:** {{REDUCE_DESC}}
- **Initial value:** `{{REDUCE_INITIAL}}`
- **Expected output:** `{{REDUCE_EXPECTED}}`

### Zip-With Test
- **List 1:** `{{ZIP_LIST1}}`
- **List 2:** `{{ZIP_LIST2}}`
- **Operation:** {{ZIP_COMBINE_DESC}}
- **Expected output:** `{{ZIP_EXPECTED}}`

---

## Tasks

### Task 1: Implement `my_map` (25 points)

Implement a function that applies a transformation to each element of an iterable.

```python
def my_map(func: Callable[[T], U], iterable: Iterator[T]) -> Iterator[U]:
    """Apply func to each element. Must return a generator."""
    pass
```

**Requirements:**
- Must return a generator (lazy evaluation)
- Must work with any iterable
- Do NOT use the built-in `map()` function

**Example:**
```python
result = list(my_map(lambda x: x * 2, iter([1, 2, 3])))
# result: [2, 4, 6]
```

---

### Task 2: Implement `my_filter` (25 points)

Implement a function that keeps only elements that satisfy a predicate.

```python
def my_filter(predicate: Callable[[T], bool], iterable: Iterator[T]) -> Iterator[T]:
    """Keep elements where predicate is True. Must return a generator."""
    pass
```

**Requirements:**
- Must return a generator (lazy evaluation)
- Must work with any iterable
- Do NOT use the built-in `filter()` function

**Example:**
```python
result = list(my_filter(lambda x: x % 2 == 0, iter([1, 2, 3, 4])))
# result: [2, 4]
```

---

### Task 3: Implement `my_reduce` (25 points)

Implement a function that reduces an iterable to a single value.

```python
def my_reduce(func: Callable[[U, T], U], iterable: Iterator[T], initial: U) -> U:
    """Reduce iterable to single value using func."""
    pass
```

**Requirements:**
- Must process elements left-to-right
- Must use the initial value as the starting accumulator
- Do NOT use `functools.reduce()`

**Example:**
```python
result = my_reduce(lambda acc, x: acc + x, iter([1, 2, 3, 4]), 0)
# result: 10
```

---

### Task 4: Implement `my_zip_with` (25 points)

Implement a function that combines two iterables element-wise using a function.

```python
def my_zip_with(func: Callable[[T, U], Any], iter1: Iterator[T], iter2: Iterator[U]) -> Iterator[Any]:
    """Combine two iterables element-wise using func."""
    pass
```

**Requirements:**
- Must return a generator (lazy evaluation)
- Should stop when the shorter iterable is exhausted
- Do NOT use the built-in `zip()` function in your implementation logic (hint: use iteration)

**Example:**
```python
result = list(my_zip_with(lambda a, b: a + b, iter([1, 2, 3]), iter([4, 5, 6])))
# result: [5, 7, 9]
```

---

## Transformation Chain Challenge (Bonus Understanding)

Your variant includes a transformation chain test. Understanding how to compose these operations is key:

**Initial data:** `{{CHAIN_INITIAL_DATA}}`

**Chain:**
1. Filter: {{CHAIN_FILTER_DESC}}
2. Map: {{CHAIN_MAP_DESC}}
3. Reduce: {{CHAIN_REDUCE_DESC}}

**Final result:** `{{CHAIN_FINAL_RESULT}}`

---

## Testing Your Implementation

Run the visible tests to check your implementation:

```bash
pytest tests/visible/ -v
```

Your code will also be tested against hidden test cases that use your personalized values.

---

## Submission Guidelines

1. Implement all functions in `src/task2_hof.py`
2. Ensure all visible tests pass
3. Push your changes to trigger the autograder
4. Check your GitHub Actions results for your score

---

## Hints

1. **Generators:** Use `yield` to create lazy generators
2. **Iteration:** Use `for item in iterable:` to process elements
3. **StopIteration:** Manually iterating with `next()` will raise `StopIteration` when exhausted
4. **Type hints:** Follow the provided type signatures

---

## Grading Rubric

| Task | Points | Criteria |
|------|--------|----------|
| my_map | 25 | Correct transformation + returns generator |
| my_filter | 25 | Correct filtering + returns generator |
| my_reduce | 25 | Correct reduction with initial value |
| my_zip_with | 25 | Correct element-wise combination + returns generator |

**Total: 100 points**

---

Good luck with your implementation!
