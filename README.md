# Factorial-Time

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


