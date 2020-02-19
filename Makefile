all: install

clean:
	rm -rf build

build:
	mkdir -p build/libs build/zip-content/rundeck-ldap-plugin
	cp -r contents resources plugin.yaml build/zip-content/rundeck-ldap-plugin
	cd build/zip-content; zip -r rundeck-ldap-plugin.zip *
	mv build/zip-content/rundeck-ldap-plugin.zip build/libs

