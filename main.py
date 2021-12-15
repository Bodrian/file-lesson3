def create_file(file_name, file_res):
    text = []
    q_line = []
    for file in file_name:
        with open(file, 'r', encoding='UTF-8') as f:
            q_line.append(len(f.readlines()))
    q_line_set = set(q_line)
    q_line = sorted(list(q_line_set))
    for line in q_line:
        for file in file_name:
            with open(file, 'r', encoding='UTF-8') as f:
                if line == len(f.readlines()):
                    with open(file, 'r', encoding='UTF-8') as f:
                        text.append('\n' + file + '\n')
                        text.append(str(line) + '\n')
                        text += f.read()
    with open(file_res, 'w', encoding='UTF-8') as f:
        f.writelines(text)

file_name = ['1.txt', '2.txt', '3.txt']
file_res = 'result.txt'

create_file(file_name, file_res)
with open(file_res, 'r', encoding='UTF-8') as f:
    print(f.read())