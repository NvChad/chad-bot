from discord.ext import commands
import discord

class JoinLeave(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send(
                f'{member.mention} has joined. Welcome to the NvChad discord! Check your dm\'s for more info')

        channel = await member.create_dm()

        embed=discord.Embed(title="Help", description="Help with the NvChad Discord Bot" )
        embed.add_field(name="Prefix", value="`:`")
        embed.add_field(name="Test", value="testy")

        await channel.send(embed=embed)
