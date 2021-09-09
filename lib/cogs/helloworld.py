from discord.ext.commands import command,Cog
from discord.ext import tasks
from discord import Embed

class helloworld(Cog):
    def __init__(self, bot):
        self.bot = bot
        #self.contar.start()
    
    #-----Comandos-----

    @command(name="hola", aliases=["hi", "saludar", "wena"], brief="Pritea un saludo", description="Printea un saludo, esta es la descripcion completa")
    async def hola(self, ctx):
        await ctx.send("Wena, que tal?")
    
    @command()
    async def argumentos(self, ctx, *args):
        cont = str(len(args))
        await ctx.send("Mandaste "+cont+" argumentos")
    
    @command()
    async def datos(self,ctx):
        #canal_id = 876546316484878366 #reemplazar con id de su servidor de prueba
        emb = Embed(title="Datos que se pueden sacar del comando",description="Cacha todo lo que puedo sacar")

        dis_name = ctx.author.display_name
        es_un_bot = ctx.author.bot

        if es_un_bot:
            mensaje_bot = "Es un bot"
        else:
            mensaje_bot = "No es un bot"
        nombre_del_servidor = ctx.guild.name

        emb.add_field(name="Nombre del Usuario",value=dis_name,inline=False)
        emb.add_field(name="¿Eres un bot?",value=mensaje_bot,inline=False)
        emb.add_field(name="Nombre del Servidor",value=nombre_del_servidor,inline=False)

        emb.set_thumbnail(url=(ctx.author.avatar_url)) #ponerle una imagen

        #canal = ctx.guild.get_channel(canal_id) #enviamos el embed al canal en especifico
        #mensaje = await canal.send(embed=emb) #send es un coroutine, se usa await y retorna un mensaje

        mensaje = await ctx.send(embed=emb)

        #Agreguemos emojis al embed | Emojis de servidor tienen ID
        await mensaje.add_reaction("😎")

    #-----Eventos-----

    @Cog.listener()
    async def on_ready(self):
        print("Modulo helloWorld listo")
    
    #que el bot mande el mismo msg que alguien mandó
    '''@Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            print("esto es de un bot")
            return
        canal = message.channel
        contendio = message.content
        await canal.send(contendio)
    '''
    
    @Cog.listener()
    async def on_raw_reaction_add(self, payload):
        print(payload.member.display_name+" agregó una reaccion")
    
    @Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        server = self.bot.get_guild(payload.guild_id)
        member = server.get_member(payload.user_id)
        print(member.display_name+" eliminó una reaccion")

    #-----Tasks-----

    '''@tasks.loop(seconds=10)
    async def contar(self):
        print("repitooo")

    @contar.before_loop
    async def before_you_loop(self):
        await self.bot.wait_until_ready()
    '''

def setup(bot):
    bot.add_cog(helloworld(bot))