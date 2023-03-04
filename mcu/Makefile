all: clean data.py

clean:
	rm -f data.py

data.py:
	cp data.py data.py.bak
	wget -O data.py https://nyiyui.ca/render/data.py

.PHONY: all clean
