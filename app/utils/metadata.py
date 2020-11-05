def build_metadata(formdata):
    i = 0
    ignore = False
    temp_dict = dict()
    ordered_file_list = []

    for key, value in formdata.items():
        print(i, key, value)
        if i == 0:
            if value == "on":
                ignore = False
            else:
                ignore = True
                i += 1
        if i == 1 and (not ignore):
            temp_dict["filename"] = value
        elif i == 2 and (not ignore):
            temp_dict["start"] = int(value)
        elif i == 3:
            if not ignore:
                temp_dict["end"] = int(value)
                # print(temp_dict)
                ordered_file_list.append(temp_dict.copy())
            i = 0
            ignore = False
            continue
        i += 1

    return ordered_file_list
