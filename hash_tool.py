import hashlib
import base64


def do_sha1(data):
	digester = hashlib.sha1()
	print('SHA1({})'.format(data))
	digester.update(data)
	result = base64.b64encode(digester.digest())
	print('Digest {}'.format(result))
	return result
	print('Digest {}'.format(base64.b64encode(digester.digest())))


def do_sha256(data):
	digester = hashlib.sha256()
	print('SHA256({})'.format(data))
	digester.update(data)
	result = base64.b64encode(digester.digest())
	print('Digest {}'.format(result))
	return result

def main(hash_type):
	data = give_me_data()
	if hash_type == 'sha256':
		return do_sha256(data)	
	else:
		return do_sha1(data)


def give_me_data():
	return b'Here is some data :)'

if __name__ == '__main__':
	main('sha256')
