.phony: clean

all:
	-virtualenv -p python2.7 python2.7
	./python2.7/bin/pip install --upgrade
	./python2.7/bin/pip install -r requirements.txt
	-mkdir -p mobi
	-mkdir -p pdf
clean:
	-rm -rf python2.7
