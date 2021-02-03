from telegram.ext import Updater
from telegram.ext import CommandHandler
import random

token = '1614155898:AAETXKg8ZhjgFeRP8YqBFkq4P_ZHpLZJ5wc'
updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher


lista_fotos=[]
lista_stickers=[]
lista_gifs=[]
lista_chistes=["Cuando la vida te de la espalda, tócale el culo", "-Tú sabés por qué el cincuenta y nueve está de pie?\n-No, por qué?\n-Porque luego sesenta",\
	       "¿Cuál es el colmo de los colmos? Que un mudo le diga a un sordo que un ciego lo está mirando", "-Buen día, quisiera alquilar Shrek Forever\n-Lo siento pero la tiene que devolver tomorrow",\
	      "—Hola, soy paraguayo y quiero pedirle la mano de su hija para cogérmela\n—¿¡Para qué?!?\n—Paraguayo.", "Un hombre entra en un bar furioso y con una pistola en la mano y dice:\n-¿QUIÉN MIERDA SE ACOSTÓ CON MI ESPOSA?\nA lo que un hombre al fondo del bar contesta:\n-Amigo, no tienes suficientes balas...",\
	      "Érase una vez un perro que respiraba por el culo, se sentó y se murió", ""]
lista_amor=["Podré no verte, podré no hablarte, pero lo que jamás podré será olvidarte", "Tal vez no te de lo mejor del mundo, pero siempre tendrás lo mejor de mí"]

tupla_todo=(lista_amor,lista_chistes,lista_fotos)


def start(update, context):
	first_name= update.message.from_user.first_name
	msg = "Hola {} bienvenida a nuestro bot de frases para cuando estás triste, envía /comandos para conocer nuestros comandos".format(first_name)
	context.bot.sendMessage(chat_id=update.message.chat_id, text=msg)
start_handler=CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def comandos(update, context):
	context.bot.send_message(chat_id=update.message.chat_id, text= "Nuestros comandos disponibles son: /chistes (para cuando estés triste y necesites ánimo), /amor (para cuando quieras recibir algo bonito), /gif (para morirte de amor), /foto (también jajaja) y /sticker (por si Stefo no te manda stickers)")
comandos_handler=CommandHandler('comandos', comandos)
dispatcher.add_handler(comandos_handler)

def amor(update, context):
	context.bot.send_message(chat_id=update.message.chat_id, text= random.choice(lista_amor))
amor_handler=CommandHandler('amor', amor)
dispatcher.add_handler(amor_handler)

#contador_chistes=1
def chistes(update, context):
	context.bot.send_message(chat_id=update.message.chat_id, text= random.choice(lista_chistes))
chistes_handler=CommandHandler('chistes', chistes)
dispatcher.add_handler(chistes_handler)

def gif(update, context):
	with open('g1.mp4','rb') as g1, open('g2.mp4','rb') as g2, open('g3.mp4','rb') as g3, open('g4.mp4','rb') as g4, open('g5.mp4','rb') as g5, open('g6.mp4','rb') as g6, open('g7.mp4','rb') as g7, open('g8.mp4','rb') as g8, open('g9.mp4','rb') as g9, open('g10.mp4','rb') as g10,  open('g11.mp4','rb') as g11, open('g12.mp4','rb') as g12, open('g13.mp4','rb') as g13, open('g14.mp4','rb') as g14, open('g15.mp4','rb') as g15, open('g16.mp4','rb') as g16, open('g17.mp4','rb') as g17, open('g18.mp4','rb') as g18, open('g19.mp4','rb') as g19, open('g20.mp4','rb') as g20:
		lista_gifs.extend([g1,g2,g3,g4,g5,g6,g7,g8,g9,g10,g11,g12,g13,g14,g15,g16,g17,g18,g19,g20])
		context.bot.sendAnimation(chat_id=update.message.chat_id, animation=random.choice(lista_gifs))
		lista_gifs.remove(g1)
		lista_gifs.remove(g2)
		lista_gifs.remove(g3)
		lista_gifs.remove(g4)
		lista_gifs.remove(g5)
		lista_gifs.remove(g6)
		lista_gifs.remove(g7)
		lista_gifs.remove(g8)
		lista_gifs.remove(g9)
		lista_gifs.remove(g10)
		lista_gifs.remove(g11)
		lista_gifs.remove(g12)
		lista_gifs.remove(g13)
		lista_gifs.remove(g14)
		lista_gifs.remove(g15)
		lista_gifs.remove(g16)
		lista_gifs.remove(g17)
		lista_gifs.remove(g18)
		lista_gifs.remove(g19)
		lista_gifs.remove(g20)		

gif_handler=CommandHandler('gif', gif)
dispatcher.add_handler(gif_handler)

def foto(update, context):
	with open('i1.jpeg', 'rb') as i1, open('i2.jpg', 'rb') as i2, open('i3.jpg', 'rb') as i3, open('i4.jpg', 'rb') as i4, open('i5.jpg', 'rb') as i5, open('i6.jpg', 'rb') as i6, open('i7.jpg', 'rb') as i7, open('i8.jpg', 'rb') as i8, open('i9.jpg', 'rb') as i9, open('i10.jpg', 'rb') as i10, open('i11.jpg', 'rb') as i11, open('i12.png', 'rb') as i12, open('i13.jpg', 'rb') as i13, open('i14.jpg', 'rb') as i14, open('i15.jpg', 'rb') as i15, open('i16.jpg', 'rb') as i16, open('i17.jpg', 'rb') as i17, open('i18.jpg', 'rb') as i18, open('i19.jpg', 'rb') as i19, open('i20.jpg', 'rb') as i20:
		lista_fotos.extend([i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,i17,i18,i19,i20])
		context.bot.sendPhoto(chat_id=update.message.chat_id, photo=random.choice(lista_fotos))
		lista_fotos.remove(i1)
		lista_fotos.remove(i2)
		lista_fotos.remove(i3)
		lista_fotos.remove(i4)
		lista_fotos.remove(i5)
		lista_fotos.remove(i6)
		lista_fotos.remove(i7)
		lista_fotos.remove(i8)
		lista_fotos.remove(i9)
		lista_fotos.remove(i10)
		lista_fotos.remove(i11)
		lista_fotos.remove(i12)
		lista_fotos.remove(i13)
		lista_fotos.remove(i14)
		lista_fotos.remove(i15)
		lista_fotos.remove(i16)
		lista_fotos.remove(i17)
		lista_fotos.remove(i18)
		lista_fotos.remove(i19)
		lista_fotos.remove(i20)

foto_handler=CommandHandler('foto', foto)
dispatcher.add_handler(foto_handler)

def sticker(update, context):
	with open('s1.tgs', 'rb') as s1, open('s2.tgs', 'rb') as s2, open('s3.tgs', 'rb') as s3, open('s4.tgs', 'rb') as s4, open('s5.tgs', 'rb') as s5, open('s6.webp', 'rb') as s6, open('s7.webp', 'rb') as s7, open('s8.webp', 'rb') as s8, open('s9.webp', 'rb') as s9, open('s10.webp', 'rb') as s10, open('s11.webp', 'rb') as s11, open('s12.webp', 'rb') as s12, open('s13.webp', 'rb') as s13, open('s14.webp', 'rb') as s14, open('s15.webp', 'rb') as s15, open('s16.tgs', 'rb') as s16, open('s17.webp', 'rb') as s17, open('s18.webp', 'rb') as s18, open('s19.webp', 'rb') as s19, open('s20.webp', 'rb') as s20:
		lista_stickers.extend([s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20])
		context.bot.sendSticker(chat_id=update.message.chat_id, sticker=random.choice(lista_stickers))
		lista_stickers.remove(s1)
		lista_stickers.remove(s2)		
		lista_stickers.remove(s3)
		lista_stickers.remove(s4)
		lista_stickers.remove(s5)
		lista_stickers.remove(s6)
		lista_stickers.remove(s7)
		lista_stickers.remove(s8)
		lista_stickers.remove(s9)
		lista_stickers.remove(s10)
		lista_stickers.remove(s11)
		lista_stickers.remove(s12)
		lista_stickers.remove(s13)
		lista_stickers.remove(s14)
		lista_stickers.remove(s15)
		lista_stickers.remove(s16)
		lista_stickers.remove(s17)
		lista_stickers.remove(s18)
		lista_stickers.remove(s19)
		lista_stickers.remove(s20)

sticker_handler=CommandHandler('sticker', sticker)
dispatcher.add_handler(sticker_handler)


updater.start_polling()
