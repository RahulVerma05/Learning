def distance(strand_a, strand_b):
    total = 0
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    for i in range(len(strand_a)):
        if strand_a[i] != strand_b[i]:
            total += 1

    return total
