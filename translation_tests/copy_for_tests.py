if __name__ == "__main__":
    info = None
    with open("./translations/translation.rpy") as f:
        info = f.read().split('\n')
    info = info[1:]
    new_info = ""
    for line in info:
        new_info = f"{new_info}{line[4:] if len(line) >= 4 else ''}\n"
    with open("./translation_tests/temp.py", 'w') as f:
        f.write(new_info)

