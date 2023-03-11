import pywhatkit as pw

list_name = ['Cassandra', 'Alex']
list_number = ['+628000', '+628111']
img = '/Users/macbook/Downloads/pywhatkit.jpg' # path through your image

for i, j in zip(list_name, list_number):
  msg = "Selamat Pagi " + i + '''!
Berikut ini adalah contoh penggunaan pywhatkit library'''

  # Send message in 20s, then close the tab after 5s
  pw.sendwhatmsg_instantly(j, msg, 20, True, 5)

  # Send image without caption in 30s, then close the tab after 5s
  pw.sendwhats_image(j, img, '', 30, True, 5)
  