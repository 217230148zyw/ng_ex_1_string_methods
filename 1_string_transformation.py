booking = "   EVT-2026 | alice_wong | Room-305 | 14:30 | alice.wong@UniMail.edu | VIP-VIP   "

booking = booking.strip()

parts = booking.split(" | ")

event_code = parts[0]
name = parts[1]
room = parts[2]
time = parts[3]
email = parts[4]
vip = parts[5]

name_formatted = name.title()

room_formatted = room.upper()

at_index = email.find("@")
email_domain = email[at_index + 1:].lower()

vip_count = vip.count("VIP")

valid_event_code = event_code.startswith("EVT-") and event_code[4:].isdigit()

valid_username = name.replace("_", "").isalpha()

valid_room = room.startswith("Room-") and room[5:].isdigit()

valid_time = len(time) == 5 and time[2] == ":" and time[:2].isdigit() and time[3:].isdigit()

valid_email = "@" in email and "." in email

print(f"Event code: {event_code}")
print(f"Name: {name_formatted}")
print(f"Room: {room_formatted}")
print(f"Time: {time}")
print(f"Email domain: {email_domain}")
print(f"VIP tag count: {vip_count}")
print(f"Valid event code: {valid_event_code}")
print(f"Valid username: {valid_username}")
print(f"Valid room: {valid_room}")
print(f"Valid time: {valid_time}")
print(f"Valid email: {valid_email}")

