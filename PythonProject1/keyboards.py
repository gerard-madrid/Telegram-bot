from pyrogram.raw.types import ReplyKeyboardMarkup
from pyrogram.types import KeyboardButton, ReplyKeyboardMarkup,InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import emoji



btn_info = KeyboardButton(f'{emoji.INFORMATION} Info')
btn_games = KeyboardButton(f'{emoji.VIDEO_GAME} Game')
btn_profile = KeyboardButton(f'{emoji.PERSON} Profile')
btn_time = KeyboardButton(f'{emoji.TIMER_CLOCK} Time')

btn_rps = KeyboardButton(f'{emoji.PLAY_BUTTON} Rock-Paper-Scissors')
btn_quest = KeyboardButton(f'{emoji.CITYSCAPE_AT_DUSK} Quest')
btn_start_quest =  KeyboardButton(f'{emoji.CITYSCAPE_AT_DUSK} Quest')
btn_back = btn_profile = KeyboardButton(f'{emoji.BACK_ARROW} Back')
btn_notes = KeyboardButton(f'{emoji.NOTEBOOK} Notes')

btn_rock = KeyboardButton(f'{emoji.ROCK} Rock')
btn_paper = KeyboardButton(f'{emoji.NOTEBOOK} Paper')
btn_scissors = KeyboardButton(f'{emoji.SCISSORS} Scissors')
btn_image = KeyboardButton(f'{emoji.FRAMED_PICTURE} Image generation')
btn_add_note = KeyboardButton(f'{emoji.PLUS} Add note')
btn_show_note = KeyboardButton(f'{emoji.NOTEBOOK} Show note')
btn_remove_note = KeyboardButton(f'{emoji.MULTIPLY} Remove note')
btn_save_note = KeyboardButton(f'{emoji.SAFETY_VEST} Save')

kb_main = ReplyKeyboardMarkup(
   keyboard = [
       [btn_info, btn_games, btn_profile , btn_time,btn_image,btn_notes],
   ],
resize_keyboard = True
)
kb_games = ReplyKeyboardMarkup(
    keyboard=[
          [btn_rps],
          [btn_quest], [btn_back],
    ],
resize_keyboard = True
)

kb_rps = ReplyKeyboardMarkup(
   keyboard=[
       [btn_rock, btn_paper, btn_scissors],
       [btn_back] , [btn_add_note, btn_show_note, btn_remove_note, btn_save_note]
   ],
   resize_keyboard = True
)

inline_kb_start_quest= InlineKeyboardMarkup([
    [InlineKeyboardButton('start the quest ' , callback_data='start_quest')],
])

inline_kb_choice_pills = InlineKeyboardMarkup([
[InlineKeyboardButton('red pills' , callback_data='red_pills')],
[InlineKeyboardButton('blue pills' , callback_data='blue_pills')],
 ])

inline_kb_red_pills = InlineKeyboardMarkup([
[InlineKeyboardButton('1000 dollars per second' , callback_data='1000_dollars_per_second')],
])
inline_kb_blue_pills = InlineKeyboardMarkup([
    [InlineKeyboardButton("get superman powers", callback_data='get_superman_powers')],
])