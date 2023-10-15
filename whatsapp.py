
import pywhatkit as kit
import datetime

# Replace these variables with the recipient's phone number and the message you want to send
phone_number = "+918328579570"  # Include country code without '+' (e.g., for the US: "1" followed by the area code and number)
message = "I love u baby"

# Get current time
now = datetime.datetime.now()
hour = now.hour
minute = now.minute

# Send WhatsApp message
kit.sendwhatmsg(phone_number, message, hour, minute + 1)  # The message will be sent 1 minute from now
