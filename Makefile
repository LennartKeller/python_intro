NOTEBOOKS=$(wildcard *.ipynb)
PDFS=$(NOTEBOOKS:.ipynb=.pdf)
SLIDES=$(NOTEBOOKS:.ipynb=.slides.html)

default : pdf slides

pdf : $(PDFS)

slides: $(SLIDES)

clean : 
	-rm -f $(PDFS) $(SLIDES)


%.pdf : %.md
	pandoc --template=tvd -V links-as-notes --pdf-engine=lualatex --filter=pandoc-svg -o $@ $<

%.tex : %.md
	pandoc --template=tvd --standalone -V links-as-notes --pdf-engine=lualatex --filter=pandoc-svg -o $@ $<

%.md : %.ipynb
	jupyter nbconvert --to markdown $<


%.slides.html : %.ipynb
	jupyter nbconvert --to slides $<
