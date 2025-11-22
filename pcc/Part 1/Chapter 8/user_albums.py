def make_album(artist, title, tracks=""):
	album = {}
	album["artist"] = artist
	album["name"] = title

	if tracks:
		album["tracks"] = int(tracks)

	# return a dictionary
	return album

while True:
		print("\nGive me your artist and album: ")
		print("(Enter 'q' to stop at any time)")

		artist = input("\nWho is your artist? ")
		if artist == "q":
			break

		title = input("\nWhat is the name of your album? ")
		if title == "q":
			break
		
		album = make_album(artist, title)
		print(album)