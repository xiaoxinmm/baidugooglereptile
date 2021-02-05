def ReadTxtName(rootdir):
    lines = []
    with open(rootdir, 'rb') as file_to_read:  #这里要是有编码错误就加上encoding='utf-8'
        while True:
            line = file_to_read.readline()
            if not line:
                break
            line = line.strip('\n')
            lines.append(line)
    return lines


