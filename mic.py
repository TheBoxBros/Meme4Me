import speechRecognition as sr

listener = sr.Recognizer()

def take_command():
	try:
		with sr.Microphone() as source:
			print('listening...')
			voice = listener.listen(source)
			command = listener.recognize_google(voice)
			command = command.lower()
			if 'roger' in command:
				command = command.replace('roger', '')
				print(command)
	except:
		pass
	return command
