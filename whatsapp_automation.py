import pywhatkit

phone_number = "+13144521750"

message = "test"

pywhatkit.sendwhatmsg_instantly(phone_number, message)
print("WhatsApp message sent!")