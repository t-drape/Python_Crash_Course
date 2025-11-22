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
print("\n\nGood News! I have found a larger table and now three more pep[e will be joining us!")

guests.insert(0, "Steve Jobs")
guests.insert(3, "Trevor Bauer")
guests.append("Jensen Huang")
final_message = "\nDear " + guests[0] + "," + "\n\t" + message
print(final_message)
final_message = "Dear " + guests[1] + "," + "\n\t" + message
print(final_message)
final_message = "Dear " + guests[2] + "," + "\n\t" + message
print(final_message)
final_message = "Dear " + guests[3] + "," + "\n\t" + message
print(final_message)
final_message = "Dear " + guests[4] + "," + "\n\t" + message
print(final_message)
final_message = "Dear " + guests[5] + "," + "\n\t" + message
print(final_message)

print("\nApologies, But my new table will not arrive until the 1st of January 2024. I can only invite two guests to Christmas dinner.")
apology = "I am sorry for the inconvenience"
less = guests.pop(0)
print("\n\t" + apology + " " + less + ".")
less = guests.pop(2)
print("\n\t" + apology + " " + less + ".")
less = guests.pop(2)
print("\n\t" + apology + " " + less + ".")
less = guests.pop(2)
print("\n\t" + apology + " " + less + ".")
new_message = "\nThank you for joining me on this fine evening "
print(new_message + guests[0] + "!")
print(new_message + guests[1] + "!")
del guests[0]
del guests[0]
print(guests)