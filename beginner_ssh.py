from paramiko import SSHClient
client = SSHClient()
client.connect('10.31.50.3', username='', key_filename='/Users/saurbane/.ssh/saurabh.pem', passphrase="")
client.close()