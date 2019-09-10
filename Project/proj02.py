
# purchase price and payment will be kept in cents

quarters = 10
dimes = 10
nickels = 10
pennies = 10

print("\nWelcome to change-making program.")

print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(
            quarters, dimes, nickels, pennies))

in_str = input("Enter the purchase price (xx.xx) or 'q' to quit: ")

while in_str != 'q':

    # Fill in the good stuff here instead of the following print
    print("Testing:",in_str)
    
    print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(
            quarters, dimes, nickels, pennies))

    in_str = input("Enter the purchase price (xx.xx) or 'q' to quit: ")
