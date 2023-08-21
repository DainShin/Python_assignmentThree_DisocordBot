"""
assignmentThree.py
The Assignment 3 of COMP1112-01-235

General purpose
- By creating and using Discord Bot, we can extract the proper data
- We can make the csv file which includes the data we need

Name : Dain Shin
Date : July 26, 2023
"""

# import os, discord and datetime library
import os
import discord
from datetime import datetime

# Token number, Server name and csv file name
TOKEN = "MTEzMjAzNTI3MDE2Njk3ODcyMg.G4CFJg.xkLh-0Goukfa-JYlfeg7tUgVJwSPA3p1wWOtcg"
GUILD = "GC-01"
fname = "memberLogon.csv"

intents = discord.Intents.default()
intents.members = True

# Create bot client
client = discord.Client(intents=intents)

# Header in csv file
headerline = "ID, Name, Join Date"

# When this program execute, this event handler will be called at first
@client.event 
async def on_ready():
    print(f'{client.user} logged in')

    # If csv file is not exit, the csv file will be created
    with open(fname, 'w') as file:
        file.write(headerline)

    server = discord.utils.get(client.guilds, name=GUILD)
    # If member is in the server, store the memeber information
    if server:
        for member in server.members:
            id = str(member.id)
            name = member.name
            join_date = member.joined_at.strftime('%Y-%m-%d %H:%M:%S') # strftime is for changing the date time type into string type
            
            # Add the member information in the csv file
            with open(fname, 'a') as file:
                file.write(f"\n{id}, {name}, {join_date}")

# When the user join the server, this will be called
@client.event
async def on_member_join(member):
    id = int(member.id)
    name = member.name
    join_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Add the user information in the csv file
    with open(fname, 'a') as file:
        file.write(f"\n{id}, {name}, {join_date}")

# When the user exit the server, this will be called
@client.event
async def on_member_remove(member):
    id = member.id

    # Read the current member and if the user is in the server, he will be stored in loginList
    loginList = []
    with open(fname, 'r') as file:
        for i in file:
            if str(id) not in i:
                loginList.append(i)

    # The users in the loginList will be in the csv file
    with open(fname, 'w') as file:
        for i in loginList:
            file.write(i)            

client.run(TOKEN)