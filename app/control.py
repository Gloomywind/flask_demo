import os


def makdir(path):
	path=path.strip()
	isExists=os.path.exists(path)
	if isExists:
		os.makedies(path)
		return True
	else:
		return False