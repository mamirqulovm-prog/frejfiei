"""
Keep Alive — Render.com uxlamaslik uchun
Flask server port 8080 da ishlaydi
UptimeRobot har 5 daqiqada ping qiladi → bot hech qachon uxlamaydi
"""

from flask import Flask
from threading import Thread
import logging

log = logging.getLogger("werkzeug")
log.setLevel(logging.ERROR)  # Flask loglarini jimlashtirish

app = Flask("")


@app.route("/")
def home():
    return "✅ Bot ishlayapti!", 200


@app.route("/health")
def health():
    return {"status": "ok", "bot": "running"}, 200


def run():
    app.run(host="0.0.0.0", port=8080, debug=False, use_reloader=False)


def keep_alive():
    t = Thread(target=run, daemon=True)
    t.start()
