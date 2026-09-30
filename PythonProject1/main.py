import base64
import datetime
import random
import json



import config
import keyboards
from Stablecog_AI import generate


from pyrogram import Client, filters
from pyrogram.types import ForceReply

bot = Client(api_id=config.API_ID, api_hash=config.API_HASH, bot_token=config.BOT_TOKEN, name="my bot")



@bot.on_message(filters.command("start"))


def button_filter(button):
   async def func(_, __ , msg):
     return msg.text == button.text
   return filters.create(func, "Button_Filter" , button = button)

@bot.on_message(filters.command("start"))
async def start(bot, message):
    await message.reply_text("welcome nice to meet you",
                               reply_markup=keyboards.kb_main)
    with open("users.json", "r") as file:
        users = json.load(file)
    if str(message.from_user.id) not in users.keys():
       users[message.from_user.id] = 100
    with open("users.json", "w") as file:
        json.dump(users, file)
@bot.on_message(filters.command("info") | button_filter(keyboards.btn_info))
async def info(bot, message):
    await message.reply_text("this is for how many commands are in this bot ")

@bot.on_message(filters.command("time") | button_filter(keyboards.btn_time))
async def time(bot, message):
    await message.reply_text(f"current time is: {datetime.datetime.today()}")

@bot.on_message(filters.command("games") | button_filter(keyboards.btn_games))
async def games(bot, message):
    await message.reply_text("choose a game" , reply_markup=keyboards.kb_games)

@bot.on_message(filters.command("back")  | button_filter(keyboards.btn_back))
async def back(bot, message):
    await message.reply_text("back to main menu", reply_markup=keyboards.kb_main)

@bot.on_message(filters.command("game") | button_filter(keyboards.btn_rps))
async def game(bot, message):
    await message.reply('your turn', reply_markup=keyboards.kb_rps)
    with open("users.json", "r") as file:
        users = json.load(file)
    if users[str(message.from_user.id)] >= 10:
       await message.reply_text("Your turn", reply_markup=keyboards.kb_rps)
    else:
         await message.reply(f"not enough money. you have {users[str(message.from_user.id)]} money the minimum to play the game is 10 coins")


@bot.on_message(button_filter(keyboards.btn_rock) |
                button_filter(keyboards.btn_paper) |
                button_filter(keyboards.btn_scissors) )
async def choice_rps(bot, message):
   with open("users.json", "r") as file:
    users = json.load(file)

    rock = keyboards.btn_rock.text
    paper = keyboards.btn_paper.text
    scissors = keyboards.btn_scissors.text
    user = message.text
    pc = random.choice([rock, paper, scissors])

    if user == pc:
        await message.reply_text("draw")
    elif (user == rock and pc == scissors) or (user == scissors and pc == paper) or (user == paper and pc == rock):
       await message.reply_text(f"you won. The Bot chose {pc} " , reply_markup=keyboards.kb_games)
       users[str(message.from_user.id)] += 10
    else:
      await  message.reply(f'you lost. The bot chose {pc}' , reply_markup=keyboards.kb_games)
      users[str(message.from_user.id)] -= 10

    with open("user.json", "w") as file:
            json.dump(users, file)

@bot.on_message(button_filter("quest") | button_filter(keyboards.btn_quest))
async def quest(bot, message):
    await message.reply_text("would you like to go on an exciting journey full of adventure and mystery ?",
                             reply_markup=keyboards.inline_kb_start_quest)
@bot.on_callback_query()
async def handle_query(bot, query):
    if query.data == "start_quest":
        await bot.answer_callback_query(query.id, text="welcome to this room", show_alert=True)
        await query.message.reply_text("you're standing in front of two pills. Which one you're going to choose?",
                                       reply_markup=keyboards.inline_kb_choice_pills)

    elif query.data == "blue_pill":
        await query.message.reply_text(" you already have ate the blue pill you got one option  " , reply_markup=keyboards.inline_kb_blue_pills )

    elif query.data == "red_pill":
        await bot.answer.callback_query(" you already have ate the red pill you got one option " , reply_markup=keyboards.inline_kb_red_pills )

    elif query.data == "super_man_powers":
        await bot.answer_callback_query(query.id,text="you ate the red pill you got superman hero powers", show_alert=True)

    elif query.data == "1000_dollars_per_second":
        await bot.answer_callback_query(query.id,text="you ate the blue pill you got 1000_dollars_per_second", show_alert=True)
@bot.on_message(filters.command("image"))
async def image(bot, message):
    if len(message.text.split()) > 1:
        query = message.text.replace('/image', '')
        await message.reply_text(f"Generating an image for the prompt '{query}', please wait a moment...")
        images = generate(query)
        if images:
            await bot.send_photo(message.chat.id, images[0], reply_to_message_id=message.id)
        else:
            await message.reply_text("An error occurred, please try again", reply_to_message_id=message.id)
    else:
        await message.reply_text("Please enter a prompt")

query_text= "enter your prompt to generate an image"
@bot.on_message(button_filter(keyboards.btn_image))
async def image_command(bot, message):
 await message.reply(query_text , reply_markup=ForceReply(True))

@bot.on_message(filters.reply)
async def reply(bot, message):
    if message.reply_to_message.text == query_text:
        query = message.text
    await message.reply_text(f"Generating an image for the prompt **{query}**. please wait a moment...")

    #images = await generate(query)
    #if images:
        #image_data = base64.b64encode(images[0])
        #img_num = random.randint(1,99)
        #with open(f'images/image{img_num}.jpg', 'wb') as file:
            #file.write(image_data)
        #await bot.send_photo(message.chat.id, f"images/image{img_num}.jpg", reply_to_message_id=message.id, reply_markup=keyboards.kb_main)

    #else:
        #await message.reply_text("An error occurred, please try again", reply_to_message_id=message.id, reply_markup=keyboards.kb_main)




bot.run()