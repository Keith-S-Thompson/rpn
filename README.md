# calc - A text-mode RPN calculator

`calc` is implemented in Perl.  It maintains an unbounded stack of
values and supports various operations on those values.

Run `calc -man` or `calc man`, or `man calc` (if the man page is
installed), or the `man` command from within calc, to see the manual.
If you're viewing this on GitHub, see `calc.1.md`.

Documentation files `calc.1` and `calc.1.md` are automatically
generated from `calc` (see `Makefile`), but are included in the
git repo.

`calc` uses the experimental `signatures` feature, introduced in
Perl 5.20.  It's not difficult to back out the use of signatures,
and I'll probably provide a script to do that automatically.
