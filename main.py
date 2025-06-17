import threading
import subprocess

def run_web():
    subprocess.run(["gunicorn", "app:app", "-b", "0.0.0.0:8080"])

def run_bot():
    subprocess.run(["python3", "bot.py"])

# Start bot in a background thread
threading.Thread(target=run_bot).start()

# Run web server in main thread (so Koyeb health check passes)
run_web()
