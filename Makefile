all:		doc nosig

doc:		rpn.1 rpn.1.md

nosig:		rpn_nosig

rpn.1:		rpn
		pod2man $< > $@

rpn.1.md:	rpn
		pod2markdown $< > $@

rpn_nosig:	rpn
		perl nosig $< > $@
		chmod +x $@

clean:
		@rm -f rpn.1 rpn.1.md rpn_nosig
