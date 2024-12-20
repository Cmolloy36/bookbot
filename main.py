import string

lowercase_letters = string.ascii_lowercase

def main():

    # call from bookbot directory in ubuntu
    pth = input('Please input the relative path to your text: ') or './books/frankenstein.txt'

    with open(pth) as f:
        file_contents = f.read()
        # print(file_contents)

    def count_words(file_contents):
        count = 0
        for word in file_contents.split():
            count += 1
        return count

    def count_chars(file_contents):
        file_contents_lower = file_contents.lower()
        char_dict = {}
        for ele in file_contents_lower:
            if ele in lowercase_letters:
                if ele not in char_dict.keys():
                    char_dict[ele] = 1
                else:
                    char_dict[ele] += 1
        return char_dict


    #report section
    print(f'{count_words(file_contents)} words were found in the document \n')
    char_dict = count_chars(file_contents)
    sorted_dict = dict(sorted(char_dict.items(), key=lambda item: item[1]))
    for key in reversed(sorted_dict.keys()):
        print(f"The '{key}' character was found {char_dict[key]} times")
    print('--- End report ---')


if __name__ == '__main__':
    main()

