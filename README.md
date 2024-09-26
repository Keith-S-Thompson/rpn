# rpn - A text-mode RPN calculator

**NOTE**: Since "calc" is a very common name, I changed the name
of this program from "calc" to "rpn".  If you're seeing this via the
GitHub link
[https://github.com/Keith-S-Thompson/calc](https://github.com/Keith-S-Thompson/calc)
please update to  
[https://github.com/Keith-S-Thompson/rpn](https://github.com/Keith-S-Thompson/rpn).
The old URL will redirect to the new one, both on the web interface
and for cloning.

`rpn` is implemented in Perl.  It maintains an unbounded stack of
values and supports various operations on those values.

Run `rpn -man` or `rpn man`, or `man rpn` (if the man page is
installed), or the `man` command from within `rpn`, to see the manual.
If you're viewing this on GitHub, see `rpn.1.md`.

Documentation files `rpn.1` and `rpn.1.md` are automatically
generated from `rpn` (see `Makefile`), but are included in the
git repo.

`rpn` uses the experimental `signatures` feature, introduced in
Perl 5.20 in 2014.  The included `nosig` script, invoked via `make nosig`,
creates a version of `rpn`, called `rpn_nosig`, that does not use
signatures, for use on systems with older versions of Perl.

You might need to adjust the `#!/usr/bin/perl` line for your system.

`make` with no arguments creates the documentation files and
`rpn_nosig`.

`rpn.py` is an experimental re-implementation in Python.  It's a work
in progress, and is known to be buggy (not necessarily giving wrong
answers, just not handling some operations).
