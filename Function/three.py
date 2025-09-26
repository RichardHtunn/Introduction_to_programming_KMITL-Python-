def deleteDuplicate(lst=None):
    print("Before delete :",lst)
    new_list = []
    deleted_data = []
    deleted_count = []

    for item in lst:
        if item not in new_list:
            new_list.append(item)
        else:
            if item in deleted_data:
                index = deleted_data.index(item)
                deleted_count[index] += 1
            else:
                deleted_data.append(item)
                deleted_count.append(1)
    print("Deleted Data :")
    for i in range(len(deleted_data)):
        print(f"data : {deleted_data[i]}, data_count : {deleted_count[i]}")

    print("After delete :", new_list)
    print("===== End of program =====")
    return new_list, deleted_data, deleted_count

print("*** Delete duplicate ***")
lst = input("Enter list : ").split()
deleteDuplicate(lst)