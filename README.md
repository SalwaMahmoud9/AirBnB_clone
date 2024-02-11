# AirBnB clone - The console

**Run the console**
```
$ ./console.py
(hbnb) 
```

**command interpreter**

- Create a new object
    EX: create class names  attributes

- Update an object
    EX: update class name id  attributes

- Retrieve an object
    EX: show class name id 

- Count an object items
    EX: class name.count()

- Destroy an object
    EX: destroy class name id


## Execution
  
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF help quit

(hbnb)
(hbnb)
(hbnb) quit
$
```

But also in non-interactive mode: (like the Shell project in C)

```
$ echo "help" | ./console.py

(hbnb)

Documented commands (type help <topic>):
========================================

EOF help quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

  
Documented commands (type help <topic>):
========================================
EOF help quit
(hbnb)
$

```