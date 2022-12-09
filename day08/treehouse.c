#include <stdio.h>
#include <stdlib.h>

char* read_input(const char* path, long *length);

// The theory behind this solution was suggested by my friend over @ 
// https://github.com/christoffer-ridderland
//
// You make 4 arrays that each check for if any tree is visible from each 
// direction. Then the resulting array is OR:d together
// 
// This method only really works for the first part
//
int main(void) {
	char *content;
	long content_length;
	content = read_input("./input", &content_length);

	int width = 0;
	int height = 0;
	char line[256];
	sscanf(content, "%s%n", line, &width);
	height = content_length / (width+1); // Calculate height
	//printf("%dx%d\n", width, height);

	// Every tree visible from the each direction
	char *visible_north = calloc(width*height, sizeof(char));
	char *visible_east  = calloc(width*height, sizeof(char));
	char *visible_south = calloc(width*height, sizeof(char));
	char *visible_west  = calloc(width*height, sizeof(char));

	// north
	for (int x = 0; x < width; x++) {
		char tallest_tree = -1;
		for (int y = 0; y < height; y++) {
			char tree = content[x+y*(width+1)] - 48; // 0 is ascii 48
			if (tree > tallest_tree) {
				visible_north[x+y*width] = 1;
				tallest_tree = tree;
			}
		}
	}

	// south
	for (int x = 0; x < width; x++) {
		char tallest_tree = -1;
		for (int y = height-1; y >= 0; y--) {
			char tree = content[x+y*(width+1)] - 48; // 0 is ascii 48
			if (tree > tallest_tree) {
				visible_south[x+y*width] = 1;
				tallest_tree = tree;
			}
		}
	}

	// west
	for (int y = 0; y < height; y++) {
		char tallest_tree = -1;
		for (int x = 0; x < width; x++) {
			char tree = content[x+y*(width+1)] - 48; 
			if (tree > tallest_tree) {
				visible_north[x+y*width] = 1;
				tallest_tree = tree;
			} 
		}
	}

	// east
	for (int y = 0; y < height; y++) {
		char tallest_tree = -1;
		for (int x = width-1; x >= 0; x--) {
			char tree = content[x+y*(width+1)] - 48; 
			if (tree > tallest_tree) {
				visible_south[x+y*width] = 1;
				tallest_tree = tree;
			}
		}
	}

	int count = 0;
	for (int y = 0; y < height; y++) {
		for (int x = 0; x < width; x++) {
			count += 
				visible_north[x+y*width] || visible_east[x+y*width] ||
				visible_south[x+y*width] || visible_west[x+y*width];
		}
	}

	printf("%d\n", count);

	free(visible_north);
	free(visible_east);
	free(visible_south);
	free(visible_west);
	free(content);
	return 0;
}


char* read_input(const char* path, long *length) {
	FILE *fp;
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

	fread(content, sizeof(char), size, fp); // This only gets one line atm
	content[size] = 0x00;
	fclose(fp);

	*length = size;
	return content;
}
