contest_data = input()
contests_dict = dict()

while contest_data != "end of contests":
    (contest, password) = contest_data.split(":")
    contests_dict[contest] = password
    contest_data = input()

submission_data = input()
users_dict = dict()

while submission_data != "end of submissions":
    (contest, password, user, points) = submission_data.split("=>")

    if contest in contests_dict and contests_dict[contest] == password:

            if user not in users_dict:
                users_dict[user] = dict()

            if contest not in users_dict[user]:
                users_dict[user][contest] = int(points)
            else:
                if users_dict[user][contest] < int(points):
                    users_dict[user][contest] = int(points)

    submission_data = input()

best_user = ""
best_points = 0

for user in users_dict.keys():
    total_points = sum(users_dict[user].values())
    if total_points > best_points:
        best_points = total_points
        best_user = user

print(f"Best candidate is {best_user} with total {best_points} points.")
print("Ranking:")
for user in sorted(users_dict.keys()):
    print(user)
    for (contest, points) in sorted(users_dict[user].items(), key= lambda cp: cp[1], reverse=True):
        print(f"#  {contest} -> {points}")