char** fizzBuzz(int n, int* returnSize) {
    // Here we allocate the memory for an array of pointers to strings
    // char** in a pointer to a pointer to a character, commonly used for array of strings
    char** result = (char**)malloc(n * sizeof(char*));
    // Setting returnSize to n -> size of resulting array
    *returnSize = n;

    // Iteration of numbers from 1 to n
    for (int i = 1 ; i <= n ; i++) {
        if (i % 15 == 0) {
            result[i - 1] = "FizzBuzz";
        }
        
        else if (i % 3 == 0) {
            result[i - 1] = "Fizz";
        }

        else if (i % 5 == 0) {
            result[i - 1] = "Buzz";
        }
        
        else {
            // Here we're calculating the length of the number when it's converted to a string
            // + 1 is added for the null character (\0), required at the end of the string
            int len = snprintf(NULL, 0, "%d", i) + 1;
            // Then we allocate the memory for the string representation of the number
            result[i - 1] = (char*)malloc(len);
            // Here we're converting the integer number (i) to a string and storing it in the array
            snprintf(result[i - 1], len, "%d", i);
        }
    }
    return result;
}