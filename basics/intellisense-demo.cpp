#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>


typedef struct {
    uint32_t mode;
    uint8_t status;
} GPIO_Config;

int main() {
    GPIO_Config myPin;
    myPin.mode = 0x01; // Set mode to output
    myPin.status = 0x01; // Set status to high
    printf("Pin mode: %u, Pin status: %u\n", myPin.mode, myPin.status);
}

int main2() {
    int arr[] = {10, 5, 4, 6, 9};
    int n = sizeof(arr) / sizeof(arr[0]);
 
    qsort(arr, n, n, compare);
    
}
