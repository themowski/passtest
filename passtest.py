#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Password Practice Application
Copyright 2023-2024 Kevin Palmowski
Full license terms in LICENSE.txt
"""

import sys
import tkinter as tk

# ---------------------------------------------------
#   Constants
# ---------------------------------------------------

# Character to print when true password is hidden
HIDE_CHAR = '#'

# Character to print in the Check/Guess entry
GUESS_CHAR = '*'

# Set to False to disable printing incorrect guesses to the console
PRINT_INCORRECT_GUESS = True

# Widget widths
WIDTH_BUTTON = 10
WIDTH_NUM_CORRECT = WIDTH_BUTTON
WIDTH_ENTRY = 35

# ---------------------------------------------------
#   Class
# ---------------------------------------------------


class PassTest(tk.Frame):
    """Password Testing Application"""

    def __init__(self, master: tk.Tk):
        """Initialize this object.

        Inputs:
            master (tk.Tk): This object's parent
        """
        # Run the initializer for the parent class
        super().__init__(master=master)

        # ---------------------------------
        #   Variables
        # ---------------------------------

        # Variable for the password truth entry box
        self.sv_pw_truth = tk.StringVar()

        # Variable for the password guess/check entry box
        self.sv_pw_guess = tk.StringVar()

        # Variable to track consecutive number of correct guesses
        self.iv_num_correct = tk.IntVar()

        # ---------------------------------
        #   Widgets
        # ---------------------------------

        # Row 0

        # Exit message label
        self.frame_help = tk.Frame()
        self.lbl_help_1 = tk.Label(master=self.frame_help, text="Enter")
        self.lbl_help_2 = tk.Label(master=self.frame_help,
                                   text="exit",
                                   foreground="#0033AA")
        self.lbl_help_3 = tk.Label(master=self.frame_help,
                                   text="in the Check entry to quit.")
        self.lbl_help_1.grid(row=0, column=0)
        self.lbl_help_2.grid(row=0, column=1)
        self.lbl_help_3.grid(row=0, column=2)
        # self.lbl_exit = tk.Label(text="Enter exit in the Check entry to quit.")

        # Row 1

        # Truth entry
        self.ent_pw_truth = tk.Entry(width=WIDTH_ENTRY,
                                     textvariable=self.sv_pw_truth)
        self.ent_pw_truth.bind("<KeyPress-Return>", self.toggle_truth_viz)

        # Hide/Show button
        self.btn_hide = tk.Button(text="Hide",
                                  width=WIDTH_BUTTON,
                                  command=self.toggle_truth_viz)

        # Row 2

        # Guess/Check entry
        self.ent_pw_guess = tk.Entry(width=WIDTH_ENTRY,
                                     show=GUESS_CHAR,
                                     textvariable=self.sv_pw_guess)
        self.ent_pw_guess.bind("<KeyPress-Return>", self.eval_guess)

        # Check button
        self.btn_check = tk.Button(text="Check",
                                   width=WIDTH_BUTTON,
                                   command=self.eval_guess)

        # Row 3

        # Correct/Incorrect status label
        self.lbl_status = tk.Label(foreground="#FF0000")

        # Number of correct consecutive guesses label
        self.lbl_num_correct = tk.Label(width=WIDTH_NUM_CORRECT,
                                        textvariable=self.iv_num_correct)

        # Grid the widgets
        self.__grid()

        # Give focus to the truth entry
        self.ent_pw_truth.focus_set()

    def __grid(self):
        """Grid this object's widgets."""
        row = 0
        self.frame_help.grid(row=row, columnspan=2)
        # self.lbl_exit.grid(row=row, columnspan=2)

        row = 1
        self.ent_pw_truth.grid(row=row, column=0)
        self.btn_hide.grid(row=row, column=1)

        row = 2
        self.ent_pw_guess.grid(row=row, column=0)
        self.btn_check.grid(row=row, column=1)

        row = 3
        self.lbl_status.grid(row=row, column=0)
        self.lbl_num_correct.grid(row=row, column=1)

    def toggle_truth_viz(self, *args, **kwargs):
        """Callback for the Hide/Show button.

        This function changes whether the password or HIDE_CHAR is shown
        in the password entry input.
        """
        if self.ent_pw_truth["show"] == HIDE_CHAR:
            # We are currently in "hide" mode and switching
            # to "show" mode.
            self.ent_pw_truth["show"] = ""
            self.btn_hide["text"] = "Hide"

        else:
            # We are currently in "show" mode and switching
            # to "hide" mode.
            self.ent_pw_truth["show"] = HIDE_CHAR
            self.btn_hide["text"] = "Show"

    def eval_guess(self, *args, **kwargs):
        """Callback for the Check button.

        This function verifies whether the entered text matches
        the password being practiced.
        """
        # Get the current values of the entries
        check_val = self.sv_pw_guess.get()
        truth_val = self.sv_pw_truth.get()

        # Check for exit
        if check_val == "exit":
            sys.exit(0)

        # Correct guess
        elif check_val == truth_val:
            # Reset the status label
            self.lbl_status["text"] = ""

            # Increment the counter
            n = self.iv_num_correct.get()
            self.iv_num_correct.set(n + 1)

        # Incorrect guess
        else:
            # Update the status label
            self.lbl_status["text"] = "Incorrect"

            # Print the incorrect guess, if configured
            if PRINT_INCORRECT_GUESS:
                print(check_val)

            # Reset the counter
            self.iv_num_correct.set(0)

        # Reset the guess to the empty string
        self.sv_pw_guess.set("")


# ---------------------------------------------------
#   Main block
# ---------------------------------------------------

if __name__ == "__main__":
    # Initialize a Tk instance
    window = tk.Tk()
    window.wm_title("Password Testing Application")

    # Initialize the application
    p = PassTest(master=window)
    p.grid()

    # Run the main application loop
    window.mainloop()
