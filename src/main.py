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