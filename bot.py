import os
from dotenv import load_dotenv
from discord.ext import commands
import discord
import requests
import json

from lor_deckcodes import LoRDeck, CardCodeAndCount
import csv
# import timeago, datetime

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
zAPIKey= os.getenv('RIOT_API')
bot = commands.Bot(command_prefix='!!', activity=discord.Game(name="!!history name tag region"))


allchampionslist = []
with open('carddata.csv', encoding='utf-8') as csv_file:
	carddata = csv.reader(csv_file, delimiter=',')
	for row	in carddata:
		if row[5] == 'Champion':
			allchampionslist.append([row[0], row[1]])

def GetPuuID(region, gameName, tagLine, APIKey):	
	if region in ['asia', 'americas', 'europe']:
		URL = "https://" + region + ".api.riotgames.com/riot/account/v1/accounts/by-riot-id/" + gameName +"/" + tagLine + "?api_key=" + APIKey
		response = requests.get(URL).json()
		if 'status' in response:
			print(response['status']['status_code'])
			print(response['status']['message'])
			if response['status']['status_code'] == 404:
				return '404error'
			else:
				return 'error'
		else:
			return response["puuid"]
	else:
		return 'regionerror'

def ChampionsExtractor(deckcode):
	deck = LoRDeck.from_deckcode(deckcode)
	list(deck)
	championsindeck = []
	for card in deck.cards:
		cardcode = str(card)[2:]
		for champion in allchampionslist:
			if cardcode == champion[0]:
				championsindeck.append(champion[1])
	if len(championsindeck) > 0:
		return championsindeck
	else:
		return 'No Champions'

#Gets emoji code for thing
def GetEmojiCode(thing):
	return {
        'Akshan': '<:Akshan:890843134416814120>',
        'Anivia': '<:Anivia:890853460549988352>',
		'Aphelios': '<Aphelios:890853461531430943>',
		'Ashe': '<:Ashe:890853462491930624>',
		'Aurelion Sol': '<:AurelionSol:890853463309824050>',
		'Azir': '<:Azir:890851970578001942>',
		'Braum': '<:Braum:890853463469203487>',
		'Caitlyn': '<:Caitlyn:890853461233655838>',
		'Darius': '<:Darius:890853460747120661>',
		'Diana': '<:Diana:890851972591276062>',
		'Draven': '<:Draven:890853463192404010>',
		'Ekko': '<:Ekko:890853460625485825>',
		'Elise': '<:Elise:890851974424182824>',
		'Ezreal': '<:Ezreal:890851972700336138>',
		'Fiora': '<:Fiora:890851967096737853>',
		'Fizz': '<:Fizz:890830550179381279>',
		'Gangplank': '<:Gangplank:890853463272062986>',
		'Hecarim': '<:Hecarim:890853463871852545>',
		'Heimerdinger': '<:Heimerdinger:890853464043835412>',
		'Irelia': '<:Irelia:890853461904740392>',
		'Jarvan IV': '<:JarvanIV:890853463897018368>',
		'Jinx': '<:Jinx:890853464186441778>',
		'Kalista': '<:Kalista:890853462282231840>',
		'Karma': '<:Karma:890853463175606282>',
		'Katarina': '<:Katarina:890853463657967626>',
		'Kindred': '<:Kindred:890851973052633098>',
		'LeBlanc': '<:Leblanc:890851971613990952>',
		'Lee Sin': '<:LeeSin:890853463649566740>',
		'Zoe': '<:Zoe:890843134949457960>',
		'Teemo': '<:Teemo:890843134576189470>',
		'Nami': '<:Nami:890830911296385075>',
		'Lucian': '<:Lucian:890853705560231986>',
		'Lissandra': '<:Lissandra:890853697070956584>',
		'Lucian': '<:Lucian:890853705560231986>',
		'Lulu': '<:Lulu:890853708315889675>',
		'Lux': '<:Lux:890853711310626836>',
		'Malphite': '<:Malphite:890853708806639666>',
		'Maokai': '<:Maokai:890853711281287189>',
		'Miss Fortune': '<:MissFortune:890853699688214538>',
		'Nasus': '<:Nasus:890853702540353566>',
		'Nautilus': '<:Nautilus:890853712359211038>',
		'Nocturne': '<:Nocturne:890853706642362378>',
		'Poppy': '<:Poppy:890853708177481738>',
		'Pyke': '<:Pyke:890853707229589545>',
		'Quinn': '<:Quinn:890853705602195467>',
		'Rek\'Sai': '<:RekSai:890853711839117312>',
		'Renekton': '<:Renekton:890853711235137576>',
		'Riven': '<:Riven:890853703022698517>',
		'Sejuani': '<:Sejuani:890853706009018379>',
		'Senna': '<:Senna:890853712325664780>',
		'Shen': '<:Shen:890853709570007040>',
		'Shyvana': '<:Shyvana:890853707871322142>',
		'Sion': '<:Sion:890853712925425695>',
		'Sivir': '<:Sivir:890853709993619496>',
		'Soraka': '<:Soraka:890853703731527680>',
		'Swain': '<:Swain:890853711537135656>',
		'Tahm Kench': '<:TahmKench:890853707292504076>',
		'Taliyah': '<:Taliyah:890853703886712842>',
		'Taric': '<:Taric:890853704205500446>',
		'Thresh': '<:Thresh:890853708890538004>',
		'Tristana': '<:Tristana:890853709301571594>',
		'Trundle': '<:Trundle:890853709679058954>',
		'Tryndamere': '<:Tryndamere:890853711604252702>',
		'Twisted Fate': '<:TwistedFate:890853711432282122>',
		'Veigar': '<:Veigar:890853711226736690>',
		'Vi': '<:Vi:890853709872005180>',
		'Viego': '<:Viego:890853708580147220>',
		'Viktor': '<:Viktor:890853707300888606>',
		'Vladimir': '<:Vladimir:890853702712311809>',
		'Xerath': '<:Xerath:890853710878638122>',
		'Yasuo': '<:Yasuo:890853710501122059>',
		'Zed': '<:Zed:890853710761181215>',
		'Ziggs': '<:Ziggs:890853708722749450>',
		'Zilean': '<:Zilean:890853709054087198>',
		'faction_BandleCity_Name': '<:bandle:891534305879289939>',
		'faction_Bilgewater_Name': '<:bilge:891534306244194365>',
		'faction_Demacia_Name': '<:demacia:891534305950576661>',
		'faction_Freljord_Name': '<:frejlord:891534306516820008>',
		'faction_Ionia_Name': '<:ionia:891534306382589983>',
		'faction_Noxus_Name': '<:noxus:891534306126737449>',
		'faction_Piltover_Name': '<:pnz:891534306223210577>',
		'faction_Shurima_Name': '<:shurima:891534306248364032>',
		'faction_ShadowIsles_Name': '<:si:891534306130935838>',
		'faction_MtTargon_Name': '<:targon:891534306290319390>',
		'red': '<:red:891549966789640242>',
		'green': '<:green:891549966798032956>',
		'gray':	'<:gray:891552127573434398>'
		}.get(thing, '\u200b')

def GetEmojiChampions(deckcode):
	EJ = ''
	if ChampionsExtractor(deckcode) == 'No Champions':
		return ''
	else:	
		for Champion in ChampionsExtractor(deckcode):
			EJ = EJ + GetEmojiCode(Champion)
	return EJ	

def GetMatchIDS(region, puuID, APIKey):	
	URL = "https://" + region + ".api.riotgames.com/lor/match/v1/matches/by-puuid/" + puuID + "/ids?api_key=" + APIKey
	response = requests.get(URL).json()
	#check for error from API
	if 'status' in response:
		print(response['status']['status_code'])
		print(response['status']['message'])
	else:
		return response
		
		
#----------------------------------------------------Bot Events And Commands From Here-----------------------------------------------------------

@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandOnCooldown):#Does this when someone requests while on cooldown.
		await ctx.send('There have been too many requests recently.\nPlease try again in {:.0f}s.'.format(error.retry_after))
		
	

@bot.command(name = 'history')
@commands.cooldown(20, 60, commands.BucketType.default)#Limiting to 20 requests each 60 seconds
async def MatchHistory(ctx, name, tag, region):
	#Send loading message
	embed=discord.Embed(title="Retreiving your match history. Please wait...", description="")
	ldngmsg = await ctx.send(embed=embed)
	
	selfpuuid = GetPuuID(region, name, tag, zAPIKey)
	if selfpuuid == '404error':#handle errors from bad input
		await ldngmsg.delete()
		await ctx.send('The name or tag you entered was wrong. Please try again.')
	elif selfpuuid == 'error':
		await ldngmsg.delete()
		await ctx.send('There was an error retrieving the information. Please try again another time.')
	elif selfpuuid == 'regionerror':
		await ldngmsg.delete()
		await ctx.send('The region you entered was wrong. Please enter: asia/americas/europe')
	else:
		matchlist = GetMatchIDS(region, selfpuuid, zAPIKey)
		embed=discord.Embed(title = 'Match history for ' + name)
		n = 0
		for id in matchlist:#this goes through the matches in the match list and adds it as a field in the embed
			ratelimiterror = False
			if n >= 10: #this limits matches shown to 10
				break
			else:	
				print('apirequest' + id)
				URL = "https://" + region + ".api.riotgames.com/lor/match/v1/matches/" + id + "?api_key=" + zAPIKey
				response = requests.get(URL).json()
				if 'status' in response: #this checks for errors in API request
					if response['status']['status_code'] == 429:#This is rate limit error.
						n = 100
						await ldngmsg.delete()
						await ctx.send('There was an error retrieving the information. Please try again another time.')
						ratelimiterror = True
					print(response['status']['status_code'])
					print(response['status']['message'])
				else:
					gamemode = '' # this is to get the game mode
					if (response['info']['game_mode'] == 'Constructed' or response['info']['game_mode'] == 'StandardGauntletLobby') and response['info']['game_type'] != 'AI':
						if response['info']['game_type'] == 'Ranked':
							gamemode = 'Ranked'
						if response['info']['game_type'] == 'Normal':
							gamemode = 'Normal'
						if response['info']['game_type'] == 'StandardGauntlet':
							gamemode = 'Gauntlet'	

						#Get Game Outcome
						selfnumber = 0
						if selfpuuid == response['info']['players'][0]['puuid']:
							selfnumber = 0
						else:
							selfnumber = 1
							
						if response['info']['players'][selfnumber]['game_outcome'] == 'win':
							gameoutcome = GetEmojiCode('green') + 'Victory'
						elif response['info']['players'][selfnumber]['game_outcome'] == 'loss':
							gameoutcome = GetEmojiCode('red') + 'Defeat'	
						else:
							gameoutcome = GetEmojiCode('gray') + 'Draw'
						
						#GetChampions
						selfchamps = GetEmojiChampions(response['info']['players'][selfnumber]['deck_code'])
						enemychamps = GetEmojiChampions(response['info']['players'][1-selfnumber]['deck_code'])
						
						#Get Regions
						selfregions = ''
						for i in response['info']['players'][selfnumber]['factions']:
							selfregions = selfregions + GetEmojiCode(i)
						enemyregions = ''
						for i in response['info']['players'][1-selfnumber]['factions']:
							enemyregions = enemyregions + GetEmojiCode(i)
						
						
						embed.add_field(name= gameoutcome + '		' + gamemode, 
						value= '	' + selfregions + selfchamps + '	 vs		 '+ enemyregions + enemychamps, inline=False)
						n += 1


						
		if ratelimiterror == False:
			print('yahhoo done')
			embed.set_footer(text='LORMatchHistory only shows constructed ranked, normal and gauntlet games.\nIf your name has spaces, please use double quotation marks Eg. "Cool Person".')
			await ldngmsg.delete()
			await ctx.send(embed=embed)
	

bot.run(TOKEN)
