COURSE = cse107
GROUP_NAME = donovan_griego
ASSIGNMENT = lab7
TARGETS = lettercount.py date.py horoscope.py rpn_calculator.py README.md
zip: $(TARGETS)
	zip $(COURSE)_$(GROUP_NAME)_$(ASSIGNMENT).zip $(TARGETS)