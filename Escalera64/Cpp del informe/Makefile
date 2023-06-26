CC=g++
CFLAGS=-Wall -O3
BINS=fuerzaBruta
BINS1=escalera64
BINS2=escalera64LRI
BINS3=escalera64R
all: clean problema

problema:
	$(CC) $(CFLAGS) -o $(BINS) fuerzaBruta.cpp
	$(CC) $(CFLAGS) -o $(BINS1) escalera64.cpp
	$(CC) $(CFLAGS) -o $(BINS2) escalera64LowestRoadINF.cpp
	$(CC) $(CFLAGS) -o $(BINS3) escalera64Roads.cpp

clean:
	@echo " [CLN] Removing binary files"
	@rm -f $(BINS)
	@rm -f $(BINS1)
	@rm -f $(BINS2)
	@rm -f $(BINS3)
