#include <stdio.h>

int main() {
  int x = 10000000;
  int* y = &x;
  int** z = &y;
  int*** z_address = &z;
  int**** add_z_add = &z_address;
  printf("x = %d, y = %d, z = %d , z address = %d, address_of_z_address = %d", x, y, z, z_address, add_z_add);
}