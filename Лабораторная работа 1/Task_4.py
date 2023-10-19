users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

dict_ = {
    "Общее количество": 0,
    "Уникальные посещения": 0,
}
count_all = len(users)
dict_["Общее количество"] = count_all
uniq_users = set(users)
count_uniq_users = len(uniq_users)
dict_["Уникальные посещения"] = count_uniq_users
print(dict_)
