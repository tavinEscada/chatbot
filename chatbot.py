import telebot
import requests

CHAVE = '6918491527:AAGpoM819PeIx0UVoNsC_kZyWIC8kKM12_0'

bot = telebot.TeleBot(CHAVE)

def horoscopo_api(signo):
  url = f"https://horoscope-api.p.rapidapi.com/pt/{signo}"

  headers = {
	  "X-RapidAPI-Key": "ed71536b03mshb2c33d98722b6b9p15b224jsn91d368d58c59",
	  "X-RapidAPI-Host": "horoscope-api.p.rapidapi.com"
  }

  response = requests.get(url, headers=headers)

  return response.json()



@bot.message_handler()
def boas_vindas(msg):
  if(msg.text == "/horoscopo"):
    signo(msg)
  else:
    bot.reply_to(msg, "Oiii, eu sou um ChatBot desenvolvido com Python 🤖\n\nE estou aqui para lhe informar seu horóscopo 🔮\n\nEntão, para receber seu Horoscopo de Hoje, digite /horoscopo")

def signo(msg):
  signos = "Qual é seu Signo? 🔮\nEscolha um:\n*♈️ Aries*\n*♉️ Touro*\n*♊️ Gemeos*\n*♋️ Cancer*\n*♌️ Leao*\n*♍️ Virgem*\n*♎️ Libra*\n*♏️ Escorpiao*\n*♐️ Sagitario*\n*♑️ Capricornio*\n*♒️ Aquario*\n*♓️ Peixes*"
  enviar_msg = bot.send_message(msg.chat.id, signos, parse_mode="Markdown")
  bot.register_next_step_handler(enviar_msg, horoscopo)


def horoscopo(msg):
	signo = msg.text
	resposta = horoscopo_api(signo)
 
	titulo = resposta['title']
	data = resposta['date']
	texto = resposta['text']

	horoscopo_mensagem = f'*{titulo}*\n\n*Signo:* {signo}\n*Dia:* {data}\n\n{texto}'

	bot.send_message(msg.chat.id, "Aqui está o seu horóscopo!")
	bot.send_message(msg.chat.id, horoscopo_mensagem, parse_mode="Markdown")
 

bot.infinity_polling()
