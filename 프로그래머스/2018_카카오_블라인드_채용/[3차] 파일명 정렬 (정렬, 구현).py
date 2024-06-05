def solution(files):
    characters = []
    file_dict = {}

    for i in range(26):
        characters.append(chr(65+i))
        characters.append(chr(97+i))
    characters.append(" ")
    characters.append("-")
    characters.append(".")

    for fi, file in enumerate(files):
        head = ""
        number = ""
        number_index = 0
        for i in range(len(file)):
            if file[i] not in characters:
                head = file[:i]
                number_index = i
                break

        for i in range(number_index, len(file)):
            if i+1 == len(file) or file[i+1] in characters:
                number = file[number_index:i+1]
                break

        file_dict[file] = (head, number, fi)

    sorted_files = sorted(file_dict.items(), key=lambda x:(x[1][0].lower(), int(x[1][1]), x[1][2]))

    return [sorted_files[i][0] for i in range(len(sorted_files))]