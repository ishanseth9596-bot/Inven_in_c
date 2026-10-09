#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//1. DATA STRUCTURE: Singly Linked List
typedef struct Item {
    int id;
    char name[30];
    int qty;
    struct Item* next;
} Item;

Item* head = NULL; // Linked List Head Pointer

// 2. DATA STRUCTURE: Array-based Stack for Undo (LIFO)
int undoStack[10];
int top = -1;

void pushUndo(int id) {
    if (top < 9) undoStack[++top] = id;
}

int popUndo() {
    return (top >= 0) ? undoStack[top--] : -1;
}

// LINKED LIST OPERATIONS
void addItem(int id, char name[], int qty) {
    Item* newItem = (Item*)malloc(sizeof(Item));
    newItem->id = id;
    strcpy(newItem->name, name);
    newItem->qty = qty;
    
    newItem->next = head; // Insert at Beginning: O(1)
    head = newItem;
    
    pushUndo(id); // Save to Stack
    printf("✅ Item added!\n");
}

void display() {
    if (!head) { printf("Inventory Empty!\n"); return; }
    printf("\nID\tName\t\tQty\n------------------------\n");
    Item* temp = head;
    while (temp) {
        printf("%d\t%-15s\t%d\n", temp->id, temp->name, temp->qty);
        temp = temp->next;
    }
}

void deleteItem(int id) {
    Item *temp = head, *prev = NULL;
    while (temp && temp->id != id) {
        prev = temp;
        temp = temp->next;
    }
    if (!temp) { printf("❌ Item not found!\n"); return; }
    
    if (!prev) head = temp->next;
    else prev->next = temp->next;
    
    free(temp);
    printf("✅ Item deleted!\n");
}

void undo() {
    int id = popUndo();
    if (id == -1) { printf("❌ Nothing to undo!\n"); return; }
    deleteItem(id);
    printf("🔄 Undo: Removed last added item (ID: %d)\n", id);
}

// MAIN MENU
int main() {
    int choice, id, qty;
    char name[30];

    while (1) {
        printf("\n--- INVENTORY SYSTEM (DS IN C) ---\n");
        printf("1. Add  2. Display  3. Delete  4. Undo Last Add  5. Exit\nChoice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("ID, Name, Qty: ");
                scanf("%d %s %d", &id, name, &qty);
                addItem(id, name, qty);
                break;
            case 2: display(); break;
            case 3:
                printf("Enter ID to delete: ");
                scanf("%d", &id);
                deleteItem(id);
                break;
            case 4: undo(); break;
            case 5: exit(0);
            default: printf("Invalid choice!\n");
        }
    }
    return 0;
}