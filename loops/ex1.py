#include <stdio.h>

int main() {
    printf("=== 30 primeiros numeros pares ===\n");
    for(int i = 1; i <= 30; i++) {
        printf("%d ", i*2);
    }
    
    printf("\n\n=== 30 primeiros numeros impares ===\n");
    for(int i = 1; i <= 30; i++) {
        printf("%d ", i*2 - 1);
    }
    printf("\n");
    return 0;
}
