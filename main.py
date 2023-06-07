import pywhatkit as pw

list_number = []
list_name = []

f = open("recipients_number.txt", "r")
for num in f:
  number = '+' + num[:-1]
  list_number.append(number)

f = open("recipients_name.txt", "r")
for recipients in f:
  list_name.append(recipients[:-1])

img = '/Users/macbook/Downloads/pywhatkit.jpg' # path through your image

for i, j in zip(list_name, list_number):
  msg = "Selamat Pagi " + i + '''!
Berikut ini adalah contoh penggunaan pywhatkit library'''

  # Send message in 20s, then close the tab after 5s
  pw.sendwhatmsg_instantly(j, msg, 20, True, 5)

  # Send image without caption in 30s, then close the tab after 5s
  pw.sendwhats_image(j, img, '', 30, True, 5)
  