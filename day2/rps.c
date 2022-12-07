
#include <stdio.h>
#include <stdlib.h>

// Points are distributed as follows:
// A = Rock     1pt
// B = Paper    2pt
// C = Scissor  3pt
// X = Rock     1pt
// Y = Paper    2pt
// Z = Scissor  3pt
//
// Win    6pt
// Draw   3pt
// Loose  0pt

char *read_data(const char* path);

int main(void) {
	char* data = NULL;
	long data_size = 0;
	data = read_input("./input", &data);

	free(data);
	return 0;
}

char* read_input(const char* path, long *size) {
	file *fp;
	long size;
	char *content = NULL;
	*length = 0;

	fp = fopen(path, "r");
	if (fp == NULL)
		return NULL;

	fseek(fp, 0, SEEK_END);
	size = ftell(fp);
	fseek(fp, 0, SEEK_SET);

	content = malloc(sizeof(char)*size+1);

	fgets(content, size, fp);
	content[size] = 0x00;
	fclose(fp);

	*length = size;
	return content;
}
