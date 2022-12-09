#include <stdlib.h>
#include <stdio.h>
#include <string.h>


int find_sop(char* message, int length);
char* read_input(const char* path, long *length);

int main(void) {
	long length;
	char *input = read_input("./input", &length);

	int start_of_package = find_sop(input, 4);
	int start_of_message = find_sop(input, 14);

	printf("%d\n", start_of_package);
	printf("%d\n", start_of_message);

	free(input);
	
	return 0;
}

/* This might be made faster if i write seperate functions for strchr and
 * strlen, or use a counter instead.
 */
int find_sop(char* message, int signature_len) {
	int message_len = strlen(message);
	int sop = 0;

	// NULL terminated just to work with string functions
	char *found_chars = calloc(signature_len, sizeof(char)+1);
	for (int i = 0; i < message_len-signature_len; i++) {

		for (int j = 0; j < signature_len; j++) {
			// If the current char is not found already add it to the founds
			if (strchr(found_chars, message[i+j]) == NULL)
				found_chars[strlen(found_chars)] = message[i+j];
			// If it is found break
			else
				break;
		}

		// If all the neccessary signature chars were found,
		if (strlen(found_chars) == signature_len) {
			sop = i + signature_len;
			break;
		}

		// Reset the chars 
		memset(found_chars, 0, signature_len);
	}

	free(found_chars);
	return sop;
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

	fgets(content, size, fp); // This only gets one line atm
	content[size] = 0x00;
	fclose(fp);

	*length = size;
	return content;
}
