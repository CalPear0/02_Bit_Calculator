# Ask user for width and loop until
# enter a number that is more than 0
from turtle import width


def int_check(question, low):
    error = "Please enter a number that or more than zero\n"
    while True:

        try:
            # ask the user for a number
            response = int(input(question))

            # check that the number is more than 0
            if response >= low:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

# Calculates how many bits are needed to represent an integer
def integer_calc(integer=None):
    # Get the image dimensions
    width = int_check("Width: ", 1)
    height = int_check("Height: ", 1)

    # convert the integer to binary and work out the number of bits needed
    raw_binary = bin(integer)
    num_bits = len(raw_binary)

    # Calculate the number of pixels and multiply by 24 to get the number of bits
    num_pixels = width * height
    num_bits = num_pixels * 24

    # Set up answer and return it
    answer = (f"Number of pixels: {width} * {height} = {num_pixels} "
              f"\nNumber of bits: {num_pixels} * 24 = {num_bits}")

    return answer

# Main routine goes here
image_ans = integer_calc()
print(image_ans)