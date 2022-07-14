from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from pytube import YouTube

app = ApplicationBuilder().token("5534677581:AAHnmARhRuDY6xe-Sw5C5RKhaiwXIICxj6k").build()


async def download_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global app
    msg = update.message.text
    link = msg.split(' ')[1]
    yt = YouTube(link)
    video_best = yt.streams.order_by('resolution').filter(progressive=True, file_extension='mp4').desc().first()
    video_best.download(output_path=r'/home/sasha/Videos', filename = 'yt_video.mp4')
    video = open('/home/sasha/Videos/yt_video.mp4', 'rb')
    await update.message.reply_video(video)


app.add_handler(CommandHandler("download", download_command))

print('server starts')
app.run_polling()