from flask import Flask
import os
import datetime
import pytz
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Your Full Name"  # Replace with your actual name
    username = os.getenv("USER", "codespace")  # Get system username
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S.%f")
    
    # Get top command output
    top_output = subprocess.run(["top", "-b", "-n", "1"], capture_output=True, text=True).stdout

    # Format output as HTML
    return f"""
    <pre>
    Name: {name}
    Username: {username}
    Server Time (IST): {server_time}

    TOP output:
    {top_output}
    </pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
