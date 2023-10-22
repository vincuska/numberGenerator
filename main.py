import os


def generate(length: int) -> list[str]:
    start: int = 0
    end: int = 10 ** length
    numbers: list[str] = []
    for num in range(start, end):
        numbers.append(str(num).zfill(length))
    return numbers


userInput = int(input("length $ "))

if __name__ == '__main__':
    output_file_name = "output.txt"
    file_number = 1

    while os.path.isfile(output_file_name):
        output_file_name = f"output{file_number}.txt"
        file_number += 1

    with open(output_file_name, 'w') as output_file:
        for number in generate(userInput):
            output_file.write(number + '\n')

    print(f"Numbers written to {output_file_name}")
