from chatterbot import ChatBot


chatbot = ChatBot(
	'Mauri',
	storage_adapter='chatterbot.storage.SQLStorageAdapter',
	input_adapter='chatterbot.input.TerminalAdapter',
	output_adapter='chatterbot.output.TerminalAdapter',
	database='.database.sqlite3',
	trainer = 'chatterbot.trainers.ListTrainer'
)

while True:
	try:
		bot_input = chatbot.get_response(None)
	
	except(KeyboardInterrupt, EOFError, SystemExit):
		break
		
