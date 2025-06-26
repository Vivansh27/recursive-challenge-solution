def main():
    import sys

    # Read all input lines at once
    input_lines = sys.stdin.read().splitlines()

    # Recursive function to process input lines
    def process(lines, index, results):
        if index >= len(lines):
            return results

        try:
            # Read count x and next line of numbers
            x = int(lines[index])
            nums = list(map(int, lines[index + 1].split()))
        except:
            return results + [-1]  # Return -1 if input is invalid

        if len(nums) != x:
            return process(lines, index + 2, results + [-1])  # Mismatch in count

        # Recursive function to calculate sum of 4th powers of non-positive numbers
        def calc_power_sum(lst, idx, total):
            if idx == len(lst):
                return total
            if lst[idx] <= 0:
                return calc_power_sum(lst, idx + 1, total + lst[idx] ** 4)
            return calc_power_sum(lst, idx + 1, total)

        result = calc_power_sum(nums, 0, 0)
        return process(lines, index + 2, results + [result])  # Move to next test case

    try:
        t = int(input_lines[0])  # First line is number of test cases (not used further)
    except:
        return

    final_results = process(input_lines[1:], 0, [])
    print("\n".join(map(str, final_results)))  # Print all results

if __name__ == "__main__":
    main()
