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

INSTALL_FILE    = install -p -m 644
INSTALL_PROGRAM = install -p -m 755

prefix_is_defined:
ifeq ($(strip $(PREFIX)),)
	$(error PREFIX is not set)
endif

install: prefix_is_defined all
	$(info Installing in $(PREFIX))
	mkdir -p $(PREFIX)/bin $(PREFIX)/share/man/man1
	$(INSTALL_FILE) README.md $(PREFIX)
	$(INSTALL_FILE) rpn.1.md $(PREFIX)
	$(INSTALL_PROGRAM) rpn $(PREFIX)/bin
	$(INSTALL_PROGRAM) rpn_nosig $(PREFIX)/bin
	$(INSTALL_PROGRAM) rpn.py $(PREFIX)/bin
	$(INSTALL_FILE) rpn.1 $(PREFIX)/share/man/man1

clean:
		@rm -f rpn.1 rpn.1.md rpn_nosig
