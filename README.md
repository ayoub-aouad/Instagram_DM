# Instagram_DM
This app will help you to bot to send direct messages in instegram without the need of your interaction with the app
# Setup App
First you have to install the required models bellow:
- pip install selenium 
- pip install webdriver_manager
- pip install time 
- pip install logging
- pip install sqlite3
- pip install random

# Runing Code
Open the senddm python file and than enter your account informations :
"account = InstaDM(username='Here' ,password='Here',headless=False)"

also liste of users you wanna send message to :
"liste = ['Here']"

and finally the message you want to send :
account.sendMessage(user=username, message='Here')


