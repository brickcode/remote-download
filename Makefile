.phony: clean

all:
	-virtualenv -p /usr/bin/python2.7 python2.7
	./python2.7/bin/pip install --upgrade 
	./python2.7/bin/pip install -r requirements.txt 
clean:
	-rm -rf python2.7
