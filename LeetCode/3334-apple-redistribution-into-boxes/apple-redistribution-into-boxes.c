int sum(int* arr, int size) {
    int total = 0;
    for (int i = 0; i < size; i++) {
        total += arr[i];
    }
    return total;
}

void quick_sort(int* arr, int left, int right) {
    if (left >= right) {
        return;
    }

    int pivot = arr[right];
    int i = left - 1;

    for (int j = left; j < right; j++) {
        if (arr[j] <= pivot) {
            i++;
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }

    int temp = arr[i + 1];
    arr[i + 1] = arr[right];
    arr[right] = temp;

    quick_sort(arr, left, i);
    quick_sort(arr, i + 2, right);
}

int minimumBoxes(int* apple, int appleSize, int* capacity, int capacitySize) {
    int min_boxes = 0;
    int sum_apples = sum(apple, appleSize);
    quick_sort(capacity, 0, capacitySize - 1);

    for (int i = capacitySize - 1; i >= 0; i--) {
        printf("%d\n", sum_apples);
        sum_apples -= capacity[i];
        min_boxes++;

        if (sum_apples <= 0) {
            return min_boxes;
        }
    }
    return min_boxes;
}