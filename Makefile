

.PHONY: dist default all install rpm

default: 


install: 
	./setup.py install

rpm: 
	./setup.py bdist_rpm

dist:
# We distribute a .spec file, so that it's possible to run "rpm -ta pyobfuscate.tgz"
	./setup.py bdist_rpm --spec-only
	mv dist/pyobfuscate.spec .
	./setup.py sdist --formats=gztar,zip
