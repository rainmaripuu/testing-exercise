from datetime import datetime


def read_line(line: str) -> tuple:
    """
    Line format:

    2020-01-18 09:00:00, message
    """
    date, text = line.split(',', 1)
    return datetime.fromisoformat(date), text


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
    phone_number = input("Please enter phone")
    message = input('Please enter a new message (type quit to exit): ')
    return phone_number, message


def write_to_file(toAdd, file_name):
    curtimestamp = datetime.now()
    with open(file_name, 'a') as f:
        f.write(f'{curtimestamp.isoformat()}, {toAdd}\n')


def main():
    buffer, parsed = read_from_file('messages.txt')
    print(buffer)
    for date, text in parsed:
        print(date.strftime("%d.%m.%Y %H:%M:%S"), ": ", text)

    while True:
        # ask for new input
        toAdd = user_input()
        # string to write
        if toAdd:
            write_to_file(toAdd, 'messages.txt')


if __name__ == '__main__':
    main()
