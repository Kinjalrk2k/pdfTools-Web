def build_metadata(formdata):
    i = 0
    temp_dict = dict()
    ordered_file_list = []

    for key, value in formdata.items():
        print(i, key, value)
        if i == 0:
            if not value == "on":
                continue
        if i == 1:
            temp_dict["filename"] = value
        elif i == 2:
            temp_dict["start"] = int(value)
        elif i == 3:
            temp_dict["end"] = int(value)
            print(temp_dict)
            ordered_file_list.append(temp_dict.copy())
            i = 0
            continue
        i += 1

    return ordered_file_list
