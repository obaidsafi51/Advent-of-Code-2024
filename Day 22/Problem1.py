def generate_next_secret(secret):
    """Generate the next secret number based on the given secret."""
    # Step 1: Multiply by 64, mix, and prune
    secret ^= (secret * 64)
    secret %= 16777216

    # Step 2: Divide by 32, round down, mix, and prune
    secret ^= (secret // 32)
    secret %= 16777216

    # Step 3: Multiply by 2048, mix, and prune
    secret ^= (secret * 2048)
    secret %= 16777216

    return secret

def simulate_secrets(initial_secret, steps):
    """Simulate the generation of secret numbers for the given steps."""
    secret = initial_secret
    for _ in range(steps):
        secret = generate_next_secret(secret)
    return secret

def calculate_sum_of_2000th_numbers(filename):
    """Calculate the sum of the 2000th secret numbers from a list of buyers."""
    total = 0
    with open(filename, 'r') as file:
        for line in file:
            initial_secret = int(line.strip())
            # Simulate 2000 steps to get the 2000th secret number
            secret_2000 = simulate_secrets(initial_secret, 2000)
            total += secret_2000
    return total

if __name__ == "__main__":
    input_file = input("Enter the input file name: ")
    result = calculate_sum_of_2000th_numbers(input_file)
    print(f"The sum of the 2000th secret numbers is: {result}")
