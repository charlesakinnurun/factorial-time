<!-- # Factorial-Time

**Explanation of Factorial Time Complexity (O(n!))**

This repository provides examples and explanations related to **factorial time complexity** — a type of algorithmic complexity where the running time grows proportionally to the factorial of the input size.

---

## 📈 What Is Factorial Time Complexity?

In algorithm analysis, factorial time complexity, written as **O(n!)**, describes algorithms whose execution time grows extremely rapidly with input size.

A factorial time algorithm often involves generating **all permutations** or exhaustive combinations of elements where the number of possible arrangements is n! (n factorial), which quickly becomes very large even for modest n (e.g., 5! = 120, 10! ≈ 3.6 million). :contentReference[oaicite:0]{index=0}

---

## 🔍 Examples of Factorial Time Algorithms

Common examples of O(n!) behavior include:

- **Generating all permutations of a list**  
  There are n! possible permutations of n distinct elements, and listing all of them produces factorial growth. :contentReference[oaicite:1]{index=1}

- **Brute-force solutions to some combinatorial problems**  
  Certain naive approaches to optimization or search problems examine every possible ordering or configuration.

---

## 📁 Source Code
```python
import time
import itertools

def factorial_time_example(elements):
    """
    Factorial Time Complexity: O(n!)
    
    This complexity class grows extremely fast. For context:
    - 5! = 120
    - 10! = 3,628,800
    - 20! = 2,432,902,008,176,640,000
    
    A common example is the 'Traveling Salesperson Problem' via brute force
    or generating all possible permutations of a list.
    """

    n = len(elements)
    print(f"----- Processing {n} elements -----")

    # Starting timer to demonstarte performance drop
    start_time = time.time()

    # itertools.permutations generates all n! possible
    # This is the wotk that takes Factorial Time

    count = 0
    for p in itertools.permutations(elements):
        count += 1
        # In a real O(n!) scenario, we might be checking the cost
        # of every single one of these paths/permutations

    end_time = time.time()


    print(f"Nmber of elements (n): {n}")
    print(f"Number of elements (n!): {count}")
    print(f"Execution time: {end_time - start_time:.6f} seconds")



def main():
    """
    We will run the same logic with increasing input sizes to show how
    O(n!) quickly becomes unmanageable for even modern CPUs.
    """

    # 1. Small n: Very fast
    small_list = [1,2,3,4,5]
    factorial_time_example(small_list)

    # 2. Medium n: Noticeable but still fast
    medium_list = list(range(10))
    factorial_time_example(medium_list)

    # 3. Warning: Adding just a few more elements makes a massive difference
    # If we tried range(15), it might take several minutes
    # if we tried range(20), it would likey take years

    large_list = list(range(11))
    factorial_time_example(large_list)

    print("TECHNICAL SUMMARY:")
    print("O(n!) means for every +1 added to the input size, the amount of")
    print("work is multiplied by the new input size. It is generally")
    print("considered an 'intractable' complexity for large datasets.")


if __name__ == "__main__":
    main()
```
---
## 🚀 Why It Matters

Factorial time complexity grows faster than most other complexity classes (e.g., exponential O(2ⁿ), polynomial O(nᵏ)), meaning such algorithms quickly become impractical as n increases. Understanding this helps in:

- Recognizing when an algorithm won’t scale
- Avoiding factorial complexity where possible
- Choosing better algorithms for combinatorial problems


-->







<!-- # 📘 Factorial Time – README -->

<h1 align="center">Factorial Time</h1>

## Overview

**Factorial Time** refers to an algorithm whose runtime grows proportional to the factorial of the input size.

If the input size is n, the runtime is roughly n! (n factorial).

In algorithm analysis, this is expressed as:

```
O(n!)
```

Factorial time algorithms become extremely slow even for small input sizes.

<a href="/src/main.py">Check out for source code</a>

---

## ⚙️ What Factorial Time Means

An algorithm runs in factorial time when it must examine every possible permutation of the input.

Common examples:

* Solving the Traveling Salesman Problem (TSP) by brute force
* Generating all possible arrangements of a set
* Certain combinatorial search problems without optimization

Factorial growth is much faster than exponential growth and becomes impractical very quickly.

---

## 🧠 Python Examples

### Example 1 — Generating All Permutations

```python id="fact_perm1"
from itertools import permutations

def all_permutations(arr):
    return list(permutations(arr))

arr = [1, 2, 3]
print(all_permutations(arr))
# Output: [(1,2,3),(1,3,2),(2,1,3),(2,3,1),(3,1,2),(3,2,1)]
```

For n elements, there are n! permutations → O(n!).

---

### Example 2 — Brute-Force Traveling Salesman Problem

```python id="fact_tsp2"
from itertools import permutations

def tsp_bruteforce(distances):
    n = len(distances)
    min_cost = float('inf')
    best_path = None
    
    for perm in permutations(range(n)):
        cost = sum(distances[perm[i]][perm[i+1]] for i in range(n-1))
        if cost < min_cost:
            min_cost = cost
            best_path = perm
    return best_path, min_cost

distances = [
    [0, 1, 3],
    [1, 0, 2],
    [3, 2, 0]
]

print(tsp_bruteforce(distances))
```

Checking all n! paths → O(n!) time.

---

### Example 3 — Generating All Seating Arrangements

```python id="fact_seating3"
def seating_arrangements(arr):
    if len(arr) == 0:
        return [[]]
    result = []
    for i in range(len(arr)):
        rest = arr[:i] + arr[i+1:]
        for perm in seating_arrangements(rest):
            result.append([arr[i]] + perm)
    return result

people = ['Alice', 'Bob', 'Charlie']
print(seating_arrangements(people))
```

All possible orderings → O(n!) time.

---

## ⏱️ Time Complexity Comparison

| Complexity | Meaning           |
| ---------- | ----------------- |
| O(1)       | Constant time     |
| O(log n)   | Logarithmic time  |
| O(n)       | Linear time       |
| O(n²)      | Quadratic time    |
| O(n log n) | Linearithmic time |
| O(2ⁿ)      | Exponential time  |
| **O(n!)**  | Factorial time    |

Factorial time algorithms are extremely inefficient for large inputs.

---

## 👍 Advantages

* Guarantees exploration of all possible solutions
* Can find exact solutions to combinatorial problems
* Conceptually simple for brute-force approaches

## 👎 Disadvantages

* Extremely slow, even for moderate input sizes
* Not practical for real-world problems without optimization
* Only feasible for very small n

---

## 📌 When Factorial Time Occurs

Factorial time operations appear in:

* Brute-force combinatorial problems
* Permutations and arrangements
* Exhaustive search in TSP or scheduling problems
* Certain recursive algorithms without pruning

---

## 🏁 Summary

Factorial time complexity O(n!) grows faster than exponential time and becomes impractical very quickly.
It is typically seen in brute-force combinatorial algorithms and should be avoided for large inputs, unless optimizations like dynamic programming or pruning are applied.
