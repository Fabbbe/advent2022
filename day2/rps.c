
#include <stdio.h>
#include <stdlib.h>

// Points are distributed as follows:
// A = Rock     1pt
// B = Paper    2pt
// C = Scissor  3pt
//
// X = Rock     1pt
// Y = Paper    2pt
// Z = Scissor  3pt
//
// Win    6pt
// Draw   3pt
// Loose  0pt

char* read_input(const char* path, long *length);

int main(void) {
	char* data = NULL;
	long data_size = 0;
	data = read_input("./input", &data_size);
	if (data == NULL)
		return -1;
	
	// The data is structured like:
	// "X Y\n" 4 bytes for every line where X is the opponents move and Y is 
	// yours.
	// For both parts it is only necessary to calculate our score
	
	int points_p1 = 0; // First part
	for (int i = 0; i < data_size/4; i++) {
		// Could use scanf here to get rid of whitespaces if the data is 
		// non-standard
		unsigned char their = data[i*4+0];
		unsigned char yours = data[i*4+2];
		
		// Make all hands 0, 1 and 3
		their = their - 65; 
		yours = yours - 88;

		points_p1 += yours+1; // points for the hand thrown
		
		if (their == yours) {// TIE
			points_p1 += 3;
		} else if ((their+1)%3 == yours) {// WIN
			points_p1 += 6;
		}
	}

	int points_p2 = 0;
	for (int i = 0; i < data_size/4; i++) {
		// Could use scanf here to get rid of whitespaces if the data is 
		// non-standard
		unsigned char their = data[i*4+0];
		unsigned char yours = data[i*4+2];
		
		// Make all hands 0, 1 and 3
		their = their - 65; 
		yours = yours - 88;

		switch (yours) { // This determines your hand
			case 0:
				yours = (their + 2)%3;
				break;
			case 1:
				yours = their;
				break;
			case 2:
				yours = (their + 1)%3;
				break;
			default:
				break;
		}
		
		points_p2 += yours+1; // points for the hand thrown
		
		if (their == yours) {// TIE
			points_p2 += 3;
		} else if ((their+1)%3 == yours) {// WIN
			points_p2 += 6;
		}
	}

	printf("Points part 1: %d\n", points_p1);
	printf("Points part 2: %d\n", points_p2);

	free(data);
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

	fread(content, size, 1, fp);
	content[size] = 0x00;
	fclose(fp);

	*length = size;
	return content;
}
