from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from commands import hi_command, help_command, time_command, sum_command, weather_command

app = ApplicationBuilder().token("5534677581:AAHnmARhRuDY6xe-Sw5C5RKhaiwXIICxj6k").build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("weather", weather_command))


app.run_polling()