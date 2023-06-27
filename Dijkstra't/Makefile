CC=g++
CFLAGS=-Wall -O3
BINS=GraficosGreedy
BINS1=solGreedy
all: clean problema

problema:
	$(CC) $(CFLAGS) -o $(BINS) GraficosGreedy.cpp
	$(CC) $(CFLAGS) -o $(BINS1) solGreedy.cpp

clean:
	@echo " [CLN] Removing binary files"
	@rm -f $(BINS)
