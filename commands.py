from index import *

async def userCommands(message, command, args): 
	
	if command == 'ping':
		await message.channel.send('Pong!')
		
	if command == 'version':
		await message.channel.send(f'Skybot {version}')
	
	if command == 'rolljonycube':
		 await message.channel.send('You rolled the Jony Cube, and it came up as: Jony')
		 
	if command == 'echo':
		await message.channel.send(message.content.replace((botInfo['commandChar']+'echo '),''))
			
		 

async def messageResponses(message):
	if 'spoopy' in message.content.lower():
		await message.add_reaction('🚫')