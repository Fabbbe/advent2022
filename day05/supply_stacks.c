
#include <stdio.h>
#include <stdlib.h>

#define COLUMN_COUNT 9
// 9*8 Max number of boxes possible in one stack (not really but for simplicity)
#define BOX_COUNT 72 

struct Column {
	char boxes[BOX_COUNT];
};

struct Move {
	int count;
	int from;
	int to;
};

void read_data(const char *path, struct Move **moves, struct Column **columns) {
	FILE *fp;
	long size;
	fp = fopen(path, "r");

	char* content = NULL;
	*moves = NULL;
	*columns = NULL;

	if (fp == NULL) {
		return;
	}
	fseek(fp, 0, SEEK_END);

	size = ftell(fp);
	
	fseek(fp, 0, SEEK_SET);

	content = malloc(sizeof(char)*size+1);

	fgets(content, size, fp);

	printf("%s\n", content);
	printf("%d\n", size);
}

void main(void) {
	struct Move *moves;
	struct Column *columns;

	read_data("./input", &moves, &columns);

	free(moves);
	free(columns);
}
