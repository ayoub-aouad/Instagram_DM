from instainfo import InstaDM
liste = []
print(len(liste))
	# Auto login
acount = InstaDM(username='', password='', headless=False)
# # Send message
for username in liste:
    acount.sendMessage(user=username, message='')