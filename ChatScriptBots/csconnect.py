import socket
import sys

# Lokaalin testiympäristön osoite. Muistetaan muokata, kunhan CS
# on serverillä.
addr = ("localhost", 1024)

# UserID pitäisi lopulta tulla ulkopuolelta, tässä koodissa se on
# väliaikaisen tekstikäytön vuoksi stdin.
userID = sys.stdin.readline()

# Tällä hetkellä skripti yhdistää oletusbottiin. Pitää muokata, jos
# lopulta serverillä on jostain syystä useampi CS-botti.
bot = ''

# data_iniin pitää muokata CS-botille lähetettävä kysymys.
data_in = "where is COMS"

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(addr)
client_socket.sendall((userID+chr(0)+bot+chr(0)+data_in+chr(0)).encode('utf-8'))

# data_out on CS-botin vastaus lähetettyyn kysymykseen. Se pitäisi siis
# lähettää jonnekin eteenpäin.
data_out = client_socket.recv(200)
print(data_out)

client_socket.close()