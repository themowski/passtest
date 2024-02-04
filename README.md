<!--
Password Practice Application
Copyright 2023-2024 Kevin Palmowski
Full license terms in LICENSE.txt
-->

# Password Practice Application

This application allows a user to practice typing a password.
This is helpful for building muscle memory after adopting a new password.


## Requirements

This software is a graphical application.
It requires Python 3 and the `tk` package,
which is part of the Python standard library.


## Usage

Open a terminal in this directory and run:

```bash
python passtest.py
```

A graphical user interface will open:

```text
        (Exit reminder)

___________________
|  password truth |   [ Hide  ]
-------------------
___________________
|  password guess |   [ Check ]
-------------------

    (Correct)         (streak)
```

Enter the password you want to practice into the top input box.
Press the "Hide" button to toggle visibility of the password.

Type the password in the bottom input box.
Press the Enter key or press the "Check" button to compare your guess
to the actual password.

The label at the bottom will display whether your guess was correct
or incorrect.

* If the guess matched the actual password, then "Correct" will be shown,
    and the streak counter will increment by 1.

* If the guess did not match the actual password, then "Incorrect" will
    be shown, and the streak counter will be reset to 0.
    The guess will also be printed to the command line.

You can exit the application at any time by submitting the word
    `exit`
as a guess.


## License

This software is made available under an MIT-style license.
See [`LICENSE.txt`](./LICENSE.txt) for full license terms.
