# import whatsApp package for sending messages at certain time

import pywhatkit

# parameters (example):
phone_number = 'country code + phone number'
message = 'Hi brother, how was your day!?'
timeInHour = 4
waited_Time_Before_Sending_InMin = 20

# open whatsApp at 4 o'clock and wait for 20 mints to send this message (4:20)
pywhatkit.sendwhatmsg(phone_number, message, timeInHour, waited_Time_Before_Sending_InMin)