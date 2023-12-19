from flask import Flask, render_template, request
from smtplib import SMTP

# constructor creating an app 
app = Flask(__name__)

# https://www.python.org/about
# protocol : https, ftp, smtp, ssh(ssl)
# domain name: www.python.org
# route: '/about'
# 234567fgh#RTYufghjkweryui

@app.route('/')
def homepage(): # route : '/'
    return render_template('home.html')

@app.route('/about')
def about():
    return 'this is the ABOUT page'

@app.route('/downloads')
def down():
    return 'this is the DOWNLOADS PAGE'

@app.route('/send_mail', methods=['GET', 'POST'])
def sending_a_mail():
    #-----get----emailID---from---PAGE
    if request.method == 'POST':
        user_email = request.form.get('u_email')
        

    #-----get----emailID---from---PAGE

    #sending-----a-------mail---------
    #establish a connection
    s = SMTP('smtp.gmail.com', 587)
    s.starttls() # security
    s.login('devangsingh101@gmail.com', 'lemdqvvzjcryivfv')
    s.sendmail('devangsingh101@gmail.com', user_email,'HELLO FROM FLASK APP')
    s.quit()
    #sending-----a-------mail---------

    return "EMAIL SENT!!"

if __name__ == '__main__':
    app.run() # run this application
    # start the development server

