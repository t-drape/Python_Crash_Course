guests = ["Jesus", "Grandpa Duane", "Elon Musk"]
message = "You are invited to dinner with a future successful person, by the name of TJ Drape. I would love to ask you a couple questions, probably ones you have already been asked. 5:00 PM, 12/25/2023."
final_message = "Dear " + guests[0] + "," + "\n\t" + message
print(final_message)
final_message = "Dear " + guests[1] + "," + "\n\t" + message
print(final_message)
final_message = "Dear " + guests[2] + "," + "\n\t" + message
print(final_message)
print(guests[2] + " is unavailable that evening.")
guests[2] = "Albert Einstein"
final_message = "\nDear " + guests[0] + "," + "\n\t" + message
print(final_message)
final_message = "Dear " + guests[1] + "," + "\n\t" + message
print(final_message)
final_message = "Dear " + guests[2] + "," + "\n\t" + message
print(final_message)