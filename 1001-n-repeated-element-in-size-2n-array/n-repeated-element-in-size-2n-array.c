int get_index(int *key, int num, int n) {
    for(int i = 0; i < n + 1; i++)
        if(key[i] == num)
            return i;
    
    return -1;
}

int repeatedNTimes(int* nums, int numsSize) {
    int n = (numsSize / 2) + 1;
    int key[n+1];
    int value[n+1];

    for(int i = 0; i < n; i++){
        key[i] = -1;
        value[i] = 0;
    }

    int index = 0;

    for(int i = 0; i < numsSize; i++){
        int ret = get_index(key, nums[i], n);
        if(ret == -1) {
            key[index] = nums[i];
            value[index++]++;
        } else {
            value[ret]++;
        }
    }

    for(int i = 0; i < n + 1; i++) {
        if(value[i] == n - 1)
            return key[i];
    }

    return -1;
}