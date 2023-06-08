CC=g++
CFLAGS=-Wall -std=c++17
BINS=fuerzaBruta
all: clean problema

problema:
	$(CC) $(CFLAGS) -o $(BINS) fuerzaBruta.cpp

clean:
	@echo " [CLN] Removing binary files"
	@rm -f $(BINS)
