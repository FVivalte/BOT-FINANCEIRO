from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
import os

# Pegando token do ambiente
TOKEN = os.environ["BOT_TOKEN"]

metas = {
    "monday": 168.90,
    "tuesday": 0.00,
    "wednesday": 209.35,
    "thursday": 209.35,
    "friday": 209.35,
    "saturday": 249.85,
    "sunday": 249.85,
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Olá! Eu sou seu bot financeiro!\n\n"
        "📌 Use /meta para ver sua meta de hoje\n"
        "📌 Use /registrar <valor> para informar quanto você faturou"
    )

async def meta(update: Update, context: ContextTypes.DEFAULT_TYPE):
    hoje = datetime.datetime.now().strftime("%A").lower()
    meta_valor = metas.get(hoje, 200)
    await update.message.reply_text(f"🎯 Sua meta de hoje ({hoje.title()}): R$ {meta_valor:.2f}")

async def registrar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        valor = float(context.args[0])
        await update.message.reply_text(f"✅ Faturamento registrado: R$ {valor:.2f}")
    except:
        await update.message.reply_text("❗ Use assim: /registrar 230")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("meta", meta))
app.add_handler(CommandHandler("registrar", registrar))

print("🤖 Bot rodando...")
app.run_polling()