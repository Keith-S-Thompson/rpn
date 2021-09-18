# calq - A text-mode RPN calculator

**NOTE**: Since "calc" is a very common name, I've changed name of this
program from "calc" to "calq".  (The 'q' has no intended meaning
beyond making the spelling reasonably unique.)  If you're seeing this
via the GitHub link  
[https://github.com/Keith-S-Thompson/calc](https://github.com/Keith-S-Thompson/calc)  
please update to  
[https://github.com/Keith-S-Thompson/calq](https://github.com/Keith-S-Thompson/calq).  
The old URL will redirect to the new one, both on the web interface
and for cloning.

`calq` is implemented in Perl.  It maintains an unbounded stack of
values and supports various operations on those values.

Run `calq -man` or `calq man`, or `man calq` (if the man page is
installed), or the `man` command from within calq, to see the manual.
If you're viewing this on GitHub, see `calq.1.md`.

Documentation files `calq.1` and `calq.1.md` are automatically
generated from `calq` (see `Makefile`), but are included in the
git repo.

`calq` uses the experimental `signatures` feature, introduced in
Perl 5.20 in 2014.  The included `nosig` script, invoked via `make nosig`,
creates a version of `calq`, called `calq_nosig`, that does not use
signatures, for use on systems with older versions of Perl.

You might need to adjust the `#!/usr/bin/perl` line for your system.

`make` with no arguments creates the documentation files and
`calq_nosig`.
