# Inventory Management System

A small interactive inventory manager written in C. It uses a singly linked
list to store inventory items and a stack to undo the most recent additions.

## Features

- Add an item with an ID, name, and quantity.
- Display all items currently in inventory.
- Delete an item by ID.
- Undo the most recent add (up to 10 additions can be recorded for undo).

Inventory is kept in memory and is not saved when the program exits. Item names
are entered as a single word.

## Requirements

- GCC or Clang
- A terminal or command prompt

`Inven.py` contains C source code; the `.py` extension is retained in this
repository, so pass the language explicitly when compiling.

## Build and run

### Windows (PowerShell)

```powershell
gcc -x c Inven.py -o inventory.exe
.\inventory.exe
```

### Linux or macOS

```sh
gcc -x c Inven.py -o inventory
./inventory
```

## Menu

1. Add an item
2. Display inventory
3. Delete an item
4. Undo the last addition
5. Exit
