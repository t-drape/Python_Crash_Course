def make_album(artist, title, tracks=""):
	album = {}
	album["artist"] = artist
	album["name"] = title

	if tracks:
		album["tracks"] = int(tracks)

	# return a dictionary
	return album

album = make_album("NF", "Perception")
print(album)

album = make_album(artist="NF", title="Therapy Session")
print(album)

album = make_album(artist="For King and Country", title="Burn The Ships", tracks="13")
print(album)