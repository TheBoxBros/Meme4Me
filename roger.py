from mic import take_command
from rec import talk
import wikipedia
import pywhatkit

def run_roger():
	command = take_command()
	print(command)
	if 'play' in command:
		song = command.replace('play', '')
		talk('playing' + song)
		pywhatkit.playonyt(song)
	elif 'time' in command:
		time = datetime.datetime.now().strftime('%I:%M %p')
		talk('Current time is' + time)
	elif 'who the heck is' in command:
		person = command.replace('who the heck is', '')
		info = wikipedia.summary(person, 1)
		print(info)
		talk(info)
	elif 'date' in command:
		talk('sorry, I have a headache')
	elif 'joke' in command:
		talk(pyjokes.get_joke())
	else:
		talk('Please say the command again.')

while True:
	run_roger()
