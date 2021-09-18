all:		doc nosig

doc:		calq.1 calq.1.md

nosig:		calq_nosig

calq.1:		calq
		pod2man $< > $@

calq.1.md:	calq
		pod2markdown $< > $@

calq_nosig:	calq
		perl nosig $< > $@
		chmod +x $@

clean:
		@rm -f calq.1 calq.1.md calq_nosig
