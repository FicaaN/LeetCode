int* runningSum(int* nums, int numsSize, int* returnSize) {

    // Firstly, we need to allocate memory for the result array
    int *result = (int*)malloc(numsSize * sizeof(int));
    // We'll check if the memory was allocated successfully, and if not, returnSize goes to 0 and it'll return NULL
    if (result == NULL) {
        *returnSize = 0;
        return NULL;
    }

    int sum = 0, i;

    for (int i = 0 ; i < numsSize ; i++) {
        sum += nums[i];
        result[i] = sum;
    }

    // Setting the returnSize to the size of the input array
    *returnSize = numsSize;

    return result;
}