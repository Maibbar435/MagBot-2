import disnake
from disnake.ext import commands
from disnake import VoiceClient

bot = commands.Bot(command_prefix = "$", help_command = None, intents = disnake.Intents.all())

@bot.event
async def on_ready():
    print(f'{bot.user} is ready for work!')

@bot.event
async def on_voice_state_update(member, before, after):
    channels = ['Channel #1']
    print(before.channel)
    try:
        channel = member.voice.channel.id
        def role1(member):
                return disnake.utils.get(member.guild.roles, id = 1104862662799675472)
    except AttributeError:
        channel = 0
    if channel == 1104847357809541190:
        voice = bot.get_channel(1104852410289111151)
        if len(voice.members) == 0:
            await member.move_to(voice)
            await member.add_roles(role1(member))
            return
        else:
            voice = bot.get_channel(1104852452131483748)
        if len(voice.members) == 0:
            await member.move_to(voice)
            def role2(member):
                return disnake.utils.get(member.guild.roles, id = 1104863115599937538)
            await member.add_roles(role2(member))
            return
        else:
            voice = bot.get_channel(1104852598625939537)
        if len(voice.members) == 0:
            await member.move_to(voice)
            def role3(member):
                return disnake.utils.get(member.guild.roles, id = 1104863130166759494)
            await member.add_roles(role3(member))
            return
        else:
            voice = bot.get_channel(1104852635821031484)
        if len(voice.members) == 0:
            await member.move_to(voice)
            def role4(member):
                return disnake.utils.get(member.guild.roles, id = 1104863137808797836)
            await member.add_roles(role4(member))
            return
        else:
            voice = bot.get_channel(1104852692993585273)
        if len(voice.members) == 0:
            await member.move_to(voice)
            def role5(member):
                return disnake.utils.get(member.guild.roles, id = 1104863146637799475)
            await member.add_roles(role5(member))
            return
        else:
            text = bot.get_channel(1104850320993034269)
            await text.send(f'{member.mention} каналы кончились!')

    if before.channel == "Channel #1" or "Channel #2":
        await member.remove_roles(disnake.utils.get(member.guild.roles, id = 1104862662799675472))
        await member.remove_roles(disnake.utils.get(member.guild.roles, id = 1104863115599937538))
        await member.remove_roles(disnake.utils.get(member.guild.roles, id = 1104863130166759494))
        await member.remove_roles(disnake.utils.get(member.guild.roles, id = 1104863137808797836))
        await member.remove_roles(disnake.utils.get(member.guild.roles, id = 1104863146637799475))

@bot.command()
async def test(ctx):
    voice = bot.get_channel(1104847357809541190)
    await voice.connect()

bot.run('OTcyNTIxMTQyOTIzNDYwNjU4.GA-fE2.mgw03qkTof3NJEtF-jCMBD_-U_dO0j7uqpWbvI')
