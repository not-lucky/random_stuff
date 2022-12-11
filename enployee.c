#include <stdio.h>
#include <string.h>

#define N 10
int filled_pos[N];

struct employee {
  int id;
  int salary;
  char name[50];
  char dept[30];
} typedef Employee;

void print_message() {
  printf(
      "Choose options to manage the employee database:\n\n1. Insert\n2. "
      "Display\n3. Delete\n4. Edit\n5. Search\n6. Sort\n7. Exit\n\n\n");
}

int search(Employee db[], int id) {
  for (int i = 0; i < N; i++) {
    if (db[i].id == id) {
      return i;
    }
  }
  return -1;
}

void insert(Employee db[N]) {
  int id;
  printf(
      "Enter employee detail to add to the database (ID, Name, Department and "
      "Salary) each in new line:\n");
  int i = search(db, id);
  if (i == -1) {
    for (int j = 0; j < N; j++) {
      if (db[j].id != -1 && filled_pos[j] == 0) {
        scanf("%d", db[j].id);
        gets(db[j].name);
        gets(db[j].dept);
        scanf("%d", db[j].salary);
        filled_pos[j] = 1;
        return;
      }
    }
  }
  printf("Employee ID already exists.\nPlease enter different ID.");
  return;
}

void display_info(Employee db[]) {
  int never_ran = 1;
  for (int j = 0; j < N; j++) {
    if (filled_pos[j] == 1) {
      printf("%d.\nID: %d\nName: %s\nDepartment: %s\nSalary: %d\n\n", db[j].id,
             db[j].name, db[j].dept, db[j].salary);
      never_ran = 0;
    }
  }
  if (never_ran) {
    printf(
        "Employee database is empty.\nPlease insert an employee info first.");
  }
}

int do_stuff(Employee db[], int opt) {
  switch (opt) {
    case 1: {
      insert(db);
      break;
    }
    case 2: {
      display_info(db);
      break;
    }
  }
  return 1;
}

int main() {
  Employee db[N];

  for (int i = 0; i < N; i++) {
    db[i].id = -1;
  }

  for (int i = 0; i < N; i++) {
    printf("%d\n", db[i].id);
  }

  int filled_pos[N] = {0};
  while (1) {
    print_message();
    int opt;
    scanf("%d", &opt);
    do_stuff(db, opt);
  }
}