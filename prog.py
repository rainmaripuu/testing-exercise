from datetime import datetime


def read_line(line: str) -> tuple:
    """
    Line format:

    2020-01-18 09:00:00, message
    """
    phone_number, message = line.split(',', 1)
    return phone_number, message


def read_from_file(file_name) -> tuple:
    buffer = ""
    # read the text file with our message log
    buffer += 'Reading messages.txt\n'
    parsed_content = []
    try:
        with open(file_name) as file:
            for line in file:
                parsed_content.append(read_line(line))
    except FileNotFoundError:
        buffer += 'File not found\n'

    return buffer, parsed_content


def user_input():

    phone_number = int(input("Please enter phone: "))
    if type(phone_number) is int:
        message = input('Please enter a new message (type quit to exit): ')
    else:
        raise ValueError
#    message = input('Please enter a new message (type quit to exit): ')
    return phone_number, message


def write_to_file(toAdd, file_name):
    curtimestamp = datetime.now()
    with open(file_name, 'a') as f:
        f.write(f'{curtimestamp.isoformat()}, {toAdd}\n')


def main():
    buffer, parsed = read_from_file('messages.txt')
    print(buffer)
    for phone_number, message in parsed:
        print(phone_number, ": ", message)

    # while True:
    #     # ask for new input
    try: user_input()
    except ValueError:
        print('Please enter correct phone number')
    toAdd = user_input()
    #     # string to write
    if toAdd:
        write_to_file(toAdd, 'messages.txt')


if __name__ == '__main__':
    main()
