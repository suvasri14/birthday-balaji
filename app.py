from flask import Flask, render_template, request, session, redirect, url_for
import os

app = Flask(__name__)   # ✅ FIXED

app.secret_key = os.environ.get("SECRET_KEY", "birthday_secret_key")

@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    user = request.form.get('user')
    pwd = request.form.get('pwd')

    if user == "Balaji" and pwd == "962001":
        session['logged_in'] = True
        return redirect(url_for('second_window'))

    return render_template('login.html', error="Invalid ID or Password")


@app.route('/second')
def second_window():
    if not session.get('logged_in'):
        return redirect(url_for('login_page'))
    return render_template('second.html')


@app.route('/birthday')
def birthday_wishes():
    if not session.get('logged_in'):
        return redirect(url_for('login_page'))
    return render_template('birthday.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login_page'))


if __name__ == "__main__":   # ✅ FIXED
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)