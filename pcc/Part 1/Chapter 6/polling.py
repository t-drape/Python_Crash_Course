favorite_languages = {
	"jen": "python",
	"sarah": "c",
	"edward": "ruby",
	"phil": "python",
	}

names = ["jen", "jonah", "bethany", "phil", "paul", "john"]

for name in names:
	if name not in favorite_languages.keys():
		print(name + ", please take our survey!")
	else:
		print(name + ", thank you for your responses!")