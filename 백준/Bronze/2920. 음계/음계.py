data_list = input().split()

if (
    data_list[0] == "1"
    and data_list[1] == "2"
    and data_list[2] == "3"
    and data_list[3] == "4"
    and data_list[4] == "5"
    and data_list[5] == "6"
    and data_list[6] == "7"
    and data_list[7] == "8"
):
    print("ascending")
elif (
    data_list[0] == "8"
    and data_list[1] == "7"
    and data_list[2] == "6"
    and data_list[3] == "5"
    and data_list[4] == "4"
    and data_list[5] == "3"
    and data_list[6] == "2"
    and data_list[7] == "1"
):
    print("descending")
else:
    print("mixed")