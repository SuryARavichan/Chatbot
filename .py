pip install chatterbot
pip install chatterbot_corpus
from chatterbot import ChatBot
bot = ChatBot('buddy')from chatterbot.trainers import ListTrainer

trainer = ListTrainer(bot)

trainer.train(['hi','hello','i need an help regarding my recent order','could you please tell me your order id','458462522','yes how can i help you today?','when will my order will be delivered','an order usually takes 2 business working days to be delivered','could you tell me where is my order','your order is at the leicester depot and soon will get delivered','ok','do you need any other help regarding your order','no thanks'])

response = bot.get_response('i have a complaint')

print("bot response:", response)

name = input("enter your name: ")
print("welcome to the bot service: ")
while True:
  request=input(name+':')
  if request == 'Bye':
    print('THANK YOU FOR USING CHATBOT SERVICE')
    break
  else:
    response = bot.get_response(request)
    print('Bot:',response)


