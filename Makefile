.PHONY: clean test
test:
	./test/test.sh

clean:
	rm -rf *.so pyvapash.egg-info/ build/ test/python/python-virtual-env/ test/c/build/ pyvapash.so test/python/*.pyc dist/ MANIFEST
