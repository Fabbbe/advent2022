#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX(x, y) x > y ? x : y;

void main(void) {

	FILE *fp = fopen("./input", "r");
	if (fp == NULL) {
		printf("Could not open file!\n");
		return;
	}

	size_t line_len = 128;
	char line[line_len];
	ssize_t read;

	int largest_sum_p1 = 0;
	int sum_p1 = 0;

	while (fgets(line, line_len, fp)) {
		int line_value = 0;
		int res = sscanf(line, " %d ", &line_value);

		sum_p1 += line_value;

		if (res == -1) { // if no match
			largest_sum_p1 = MAX(largest_sum_p1, sum_p1);
			sum_p1 = 0;
		}
	}
	fseek(fp, 0, SEEK_SET); // REWIND TIME
	
	int largest_sums_p2[3] = {0};
	int sum_p2 = 0;
	while (fgets(line, line_len, fp)) {
		int line_value = 0;
		int res = sscanf(line, " %d ", &line_value);

		sum_p2 += line_value;

		if (res == -1) { // if no match
			int smallest_index = 0;
			for (int i = 0; i < 3; i++) // always replace the smallest
				if (largest_sums_p2[i] < largest_sums_p2[smallest_index]) 
					smallest_index = i;

			largest_sums_p2[smallest_index] = MAX(largest_sums_p2[smallest_index], sum_p2);
			sum_p2 = 0;
		}
	}

	int total_sum_p2 = 0;
	for (int i = 0; i < 3; i++) {
		total_sum_p2 += largest_sums_p2[i];
	}



	fclose(fp);

	printf("%d\n", largest_sum_p1);
	printf("%d\n", total_sum_p2);
}
