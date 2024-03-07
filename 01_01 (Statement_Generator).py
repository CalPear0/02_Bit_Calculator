# functions go here
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Display instructions
def instructions():
    print("Instructions go here... ")

print('''
Instructions go here...
-TEEHEE1
-TEEHEE2
-TEEHEE3
''')


# Main routine goes here
want_instructions = input("press <enter> to read the instructions "
                          "or any key to continue ")

if want_instructions == "":
    instructions()

    print("PROGRAM CONTINUES")