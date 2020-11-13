[![Current PyPI packages](https://badge.fury.io/py/spacy-alpino.svg)](https://pypi.org/project/spacy-alpino/)

# spaCy-Alpino

[Alpino](http://www.let.rug.nl/vannoord/alp/Alpino/) wrapper for spaCy

## Basic Usage

```py
>>> import spacy_alpino
>>> nlp=spacy_alpino.load()
>>> doc=nlp("Zorg dat daar geen zwarte hond tussen komt.")
>>> for t in doc:
...   print("\t".join([str(t.i+1),t.orth_,t.lemma_,t.pos_,t.tag_,"_",str(0 if t.head==t else t.head.i+1),t.dep_,"_","_" if t.whitespace_ else "SpaceAfter=No"]))
...
1	Zorg	zorgen	VERB	WW|pv|tgw|ev	_	0	ROOT	_	_
2	dat	dat	SCONJ	VG|onder	_	8	mark	_	_
3	daar	daar	ADV	VNW|aanw|adv-pron|obl|vol|3o|getal	_	8	obl	_	_
4	geen	geen	DET	VNW|onbep|det|stan|prenom|zonder|agr	_	6	det	_	_
5	zwarte	zwart	ADJ	ADJ|prenom|basis|met-e|stan	_	6	amod	_	_
6	hond	hond	NOUN	N|soort|ev|basis|zijd|stan	_	8	nsubj	_	_
7	tussen	tussen	ADP	VZ|fin	_	3	case	_	_
8	komt	komen	VERB	WW|pv|tgw|met-t	_	1	ccomp	_	SpaceAfter=No
9	.	.	PUNCT	LET	_	1	punct	_	SpaceAfter=No
>>> import deplacy
>>> deplacy.render(doc)
Zorg   VERB  ═════════════╗═╗ ROOT
dat    SCONJ <══════════╗ ║ ║ mark
daar   ADV   ═════╗<══╗ ║ ║ ║ obl
geen   DET   <══╗ ║   ║ ║ ║ ║ det
zwarte ADJ   <╗ ║ ║   ║ ║ ║ ║ amod
hond   NOUN  ═╝═╝ ║<╗ ║ ║ ║ ║ nsubj
tussen ADP   <════╝ ║ ║ ║ ║ ║ case
komt   VERB  ═══════╝═╝═╝<╝ ║ ccomp
.      PUNCT <══════════════╝ punct
```

## Installation for Linux (Debian)

First, install [xqilla](http://xqilla.sourceforge.net/) and necessary packages:

```sh
sudo apt update
sudo apt install xqilla libxss1 python3-pip python3-dev g++ curl
```

Second, install Alpino:

```sh
cd /tmp
curl -L https://www.let.rug.nl/vannoord/alp/Alpino/versions/binary/latest.tar.gz | tar xzf -
sudo mkdir -p /usr/local/bin
sudo mv Alpino /usr/local/Alpino
( echo '#! /bin/sh' ; echo 'exec /usr/local/Alpino/bin/Alpino "$@"' ) > Alpino
sudo install Alpino /usr/local/bin
```

And at last, install spaCy-Alpino:

```sh
pip3 install spacy_alpino --user
```

## Installation for Linux (Ubuntu)

Same as Debian.

## Installation for Linux (Kali)

Same as Debian.

