import hashlib
import base64


def main():
	digester = hashlib.sha1()
	data = give_me_data()
	print('Hashing {}'.format(data))
	digester.update(data)
	print('Digest {}'.format(base64.b64encode(digester.digest())))

def give_me_data():
	return b'Here is some data :)'

if __name__ == '__main__':
	main()
