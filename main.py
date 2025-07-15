# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

    print('Your name is a palindrome!' if is_palindrome(name) else 'Your name is not a palindrome.')


def is_palindrome(name):
    # Normalize the name by removing spaces and converting to lowercase
    normalized_name = name.replace(" ", "").lower()
    # Check if the normalized name is equal to its reverse
    return normalized_name == normalized_name[::-1]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('AI AGENT')