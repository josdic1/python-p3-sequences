def print_fibonacci(length):
    sequence = []
    if length == 0:
        print(sequence)
        return
    if length == 1:
        sequence = [0]
        print(sequence)
        return

    sequence = [0, 1]

    while len(sequence) < length:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    
    print(sequence)