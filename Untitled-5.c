#include <math.h>
#include <stdio.h>

int rev(int num) {
  static int reversed = 0;
  if (num == 0) {
    return reversed;
  }

  reversed = (reversed * 10) + (num % 10);
  return (rev(num / 10));
}

int main() { 
  printf("%d", rev(1423489)); 
}