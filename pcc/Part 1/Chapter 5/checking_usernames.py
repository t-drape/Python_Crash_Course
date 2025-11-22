current_users = ["Tom", "TJ", "Beth", 'Lia', "Glo"]
new_users = ["Beth", "Johnny", "Jimmy", "Joe", "Jordan"]

for user in range(len(current_users)):
	current_users[user] = current_users[user].lower()
for user in new_users:
	if user.lower() in current_users:
		print("Username in use. Please choose a different one.")
	else:
		print("Congrats! This is your new account and username.")