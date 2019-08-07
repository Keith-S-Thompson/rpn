all:		doc nosig

doc:		calc.1 calc.1.md

nosig:		calc_nosig

calc.1:		calc
		pod2man $< > $@

calc.1.md:	calc
		pod2markdown $< > $@

calc_nosig:	calc
		perl nosig $< > $@
		chmod +x $@

clean:
		@rm -f calc.1 calc.1.md calc_nosig
