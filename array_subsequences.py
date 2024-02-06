# description
# A subsequence is a sequence that can be derived from another sequence by removing zero or more elements, without changing the order of the remaining elements.

# More generally, we can say that for a sequence of size n, we can have (2n – 1) non-empty sub-sequences in total.


def subsequences(arr):
    n = len(arr)

    # Run a loop for each combination of bits
    for i in range(1 << n):
        subarr = []

        # Iterate over each bit of the current combination
        for j in range(n):
            # Check if j-th bit is set in the binary representation of i
            if (i & (1 << j)) > 0:
                subarr.append(arr[j])

        # Print the subsequence
        print(subarr)


arr = [1, 2, 3, 4]
print(subsequences(arr))
