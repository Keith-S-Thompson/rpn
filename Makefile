doc:		calc.1 calc.1.md

calc.1:		calc
		pod2man $< > $@

calc.1.md:	calc
		pod2markdown $< > $@

clean:
		@rm -f calc.1 calc.1.md
