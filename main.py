import os
import nextcord
from nextcord.ext import commands
import random
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")

intents = nextcord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="bn!",intents=intents,help_command=None)

@bot.command(name="hi")
async def SendMessage(ctx):
    await ctx.send("Xin chào! Mình là Đậu và mình được **Rework** lại từ đầu😊")

@bot.command(name="slot")
async def SlotMessage(ctx):
    emoji_list = ['🍅','🍍','🥭']
    slot_1 = random.choice(emoji_list)
    slot_2 = random.choice(emoji_list)
    slot_3 = random.choice(emoji_list)

    if slot_1 == slot_2 and slot_2 == slot_3:
        await ctx.send(
f"""
Bạn đã **trúng số**, kết quả bạn nhận được là :
=================================
{slot_1} {slot_2} {slot_3}
=================================
Bạn có muốn chơi nữa không?🍅
""")
    else:
        await ctx.send(
f"""
Bạn đã **thua** rồi, kết quả bạn nhận được là :
=================================
{slot_1} {slot_2} {slot_3}
=================================
Bạn có muốn chơi nữa không?🍅
""")
        
@bot.command(name="help")
async def HelpMessage(ctx):
    help_dict = {
        "slot": "Chơi Xổ Số Với Đậu",
        "hi": "Kiểm tra xem Đậu còn sự sống không =))",
        "help": "Xin trợ giúp nếu cần !",
        "poems": "Đậu đọc thơ tình cho nghe",
    }

    embed = nextcord.Embed(color=0x2596be, 
                           title="Nhập môn đậu xanh 2.0",
                           description="**Beanstalk đã cập nhật lại API**🙀🙀")
    embed.set_thumbnail(url="https://media1.giphy.com/media/v1.Y2lkPTZjMDliOTUyZzljNDVsNmN1b2l4ajJkYTZ5cGFhMGR6OGpvZ3MzN2w4dzVtY3Y4bCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/OimThKQ6Q5vOg/giphy.gif")
    for c in bot.commands:
        if c.name in help_dict:
            embed.add_field(name=f"{f"`{bot.command_prefix+c.name}`"}", value=f"{help_dict[c.name]}", inline=False)
        else:
            continue
    
    embed.set_footer(text="Được rồi, giờ đã biết dùng rồi chứ!🐱")
    
    await ctx.send(embed=embed)

@bot.command(name="poems")
async def MakePoems(ctx):
    poem = random.randint(1,3)
    if poem == 1:
        await ctx.send("""
Anh chả hiểu vì sao vấn vương
Năm năm, như mấy chục năm trường
Vẫn là mắt mấy, làn môi ấy
Anh hãy còn thương, chẳng hết thương.

-- Trích từ Thơ **Vấn vương** của Xuân Diệu
""")
    elif poem == 2:
        await ctx.send("""
Ngày mai tôi bỏ làm thi sĩ
Em lấy chồng rồi hết ước mơ
Tôi sẽ đi tìm mỏm đá trắng
Ngồi lên để thả cái hồn thơ.
                       
-- Trích từ Thơ **Em Lấy Chồng** của Hàn Mặc Tử              
""")
    elif poem == 3:
        await ctx.send("""
Thôn Đoài ngồi nhớ thôn Đông
Một người chín nhớ mười mong một người.
Gió mưa là bệnh của giời
Tương tư là bệnh của tôi yêu nàng.

 
Hai thôn chung lại một làng,
Cớ sao bên ấy chẳng sang bên này?
Ngày qua ngày lại qua ngày,
Lá xanh nhuộm đã thành cây lá vàng.

 
Bảo rằng cách trở đò giang,
Không sang là chẳng đường sang đã đành.
Nhưng đây cách một đầu đình,
Có xa xôi mấy cho tình xa xôi…


Tương tư thức mấy đêm rồi,
Biết cho ai, hỏi ai người biết cho!
Bao giờ bến mới gặp đò?
Hoa khuê các bướm giang hồ gặp nhau?

 
Nhà em có một giàn giầu
Nhà anh có một hàng cau liên phòng
Thôn Đoài thì nhớ thôn Đông
Cau thôn Đoài nhớ giầu không thôn nào?

-- Trích từ Thơ **Tương Tư** của Nguyễn Bính             
""")
@bot.event
async def on_ready():
    print(f"Thằng Bel {bot.user.name} đã hoang dã!!")
    await bot.change_presence(activity=nextcord.Game(name="Goodbye Discord.py :'(("))

bot.run(TOKEN)
