double* convertTemperature(double celsius, int* returnSize) {
    // Firstly, we need to allocate the memory for the result array - ans
    // Since we always need to return 2 values (kelvin and fahrenheit), we need space for 2 doubles
    double* ans = (double*)malloc(2 * sizeof(double));

    // If memory allocation fails, it returns NULL
    if  (ans == NULL) {
        *returnSize = 0;
        return NULL;
    }

    ans[0] = celsius + 273.15;

    ans[1] = celsius * 1.80 + 32.00;

    // Setting the size of the return array
    *returnSize = 2;

    return ans;
}