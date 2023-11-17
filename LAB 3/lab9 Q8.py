def get_max_length():
    while True:
        try:
            max_length = int(input("Enter the maximum length in feet: "))
            if max_length > 0:
                return max_length
            else:
                print("Error! Please enter a valid positive integer.")
        except ValueError:
            print("Error! Please enter a valid positive integer.")

def print_conversion_chart(max_length):
    conversion_factor = 0.3048

    print("Feet\tMeters")
    print("-----------------")

    for feet in range(1, max_length + 1):
        meters = feet * conversion_factor
        print(f"{feet}\t{meters:.4f}")

max_length = get_max_length()
print_conversion_chart(max_length)