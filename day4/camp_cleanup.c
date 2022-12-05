#include <stdio.h>
#include <stdlib.h>

struct Range {
	int start;
	int end;
};

struct Range *read_data(const char *path, int *range_count) {
	FILE* fp;
	struct Range *ranges;
	int row_count = 0;

	fp = fopen(path, "r");

	if (fp == NULL) {
		printf("Could not open file!");
		return NULL;
	}

	// Count rows
	for (char c = getc(fp); c != EOF; c = getc(fp)) {
		if (c == '\n') 
			row_count += 1;
	}
	fseek(fp, 0, SEEK_SET); // Rewind file pointer

	ranges = malloc(sizeof(struct Range) * 2 * row_count);

	for (int i = 0; i < row_count; i++) {
		fscanf(fp, " %d - %d , %d - %d ",
				&ranges[i*2+0].start, 
				&ranges[i*2+0].end, 
				&ranges[i*2+1].start, 
				&ranges[i*2+1].end
		);
	}

	*range_count = row_count;
	return ranges;
}

void main(void) {
	int range_count;
	struct Range *ranges = read_data("./input", &range_count);

	int sum_p1 = 0;
	int sum_p2 = 0;

	// Sum up everywhere the ranges fully overlap
	for (int i = 0; i < range_count; i++) {
		int j = i*2;
		if (ranges[j+0].start <= ranges[j+1].start && ranges[j+0].end >= ranges[j+1].end)
			sum_p1 += 1;
		else if (ranges[j+1].start <= ranges[j+0].start && ranges[j+1].end >= ranges[j+0].end)
			sum_p1 += 1;

	}

	// Sum up everywhere the ranges overlap at all
	for (int i = 0; i < range_count; i++) {
		int j = i*2;
		if (ranges[j+0].end >= ranges[j+1].start && ranges[j+0].start <= ranges[j+1].end)
			sum_p2 += 1;

	}

	printf("Part 1: %d\n", sum_p1);
	printf("Part 2: %d\n", sum_p2);

	free(ranges);
}
