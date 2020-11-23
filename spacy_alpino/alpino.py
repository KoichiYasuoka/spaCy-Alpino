#! /usr/bin/python3 -i
# coding=utf-8

import os
PACKAGE_DIR=os.path.abspath(os.path.dirname(__file__))
ALPINO2UD=os.path.join(PACKAGE_DIR,"alpino2ud.sh")
ALPINO_URL="https://urd2.let.rug.nl/~vannoord/bin/"

import numpy
from spacy.symbols import LEMMA,POS,TAG,DEP,HEAD
from spacy.tokens import Doc
from spacy.language import Language
SPACY_V3=hasattr(Language,"component")

class AlpinoParser(object):
  name="Alpino"
  def __init__(self,command,vocab):
    try:
      import subprocess
      s=subprocess.check_output([ALPINO2UD,command],input="Ja".encode("utf-8")).decode("utf-8")
      self.alpino=s.startswith("# source =")
    except:
      self.alpino=False
    self.command=command
    self.vocab=vocab
  def __call__(self,doc):
    if len(doc)==0:
      return doc
    t="".join([" ".join([str(t) for t in s])+"\n" for s in doc.sents])
    if self.alpino:
      import subprocess
      u=subprocess.check_output([ALPINO2UD,self.command],input=t.encode("utf-8")).decode("utf-8")
      if not u.startswith("# source ="):
        self.alpino=False
    if not self.alpino:
      import urllib.request,urllib.parse
      with urllib.request.urlopen(ALPINO_URL+"alpino?words="+urllib.parse.quote(t)) as r:
        q=r.read().decode("utf-8")
      i=q.index("conllu?tmp/")
      with urllib.request.urlopen(ALPINO_URL+q[i:q.index("'",i)]) as r:
        u=r.read().decode("utf-8")
    vs=self.vocab.strings
    r=vs.add("ROOT")
    lemmas=[]
    pos=[]
    tags=[]
    morphs=[]
    heads=[]
    deps=[]
    for t in u.split("\n"): 
      if t=="" or t.startswith("#"):
        continue
      s=t.split("\t")
      if len(s)!=10:
        continue
      id,_,lemma,upos,xpos,feats,head,deprel,_,_=s
      lemmas.append(vs.add(lemma))
      pos.append(vs.add(upos))
      tags.append(vs.add(xpos))
      morphs.append(feats)
      if deprel=="root" or deprel=="ROOT":
        heads.append(0)
        deps.append(r)
      elif head=="0":
        heads.append(0)
        deps.append(vs.add(deprel))
      else:
        heads.append(int(head)-int(id))
        deps.append(vs.add(deprel))
    a=numpy.array(list(zip(lemmas,pos,tags,deps,heads)),dtype="uint64")
    doc.from_array([LEMMA,POS,TAG,DEP,HEAD],a)
    if SPACY_V3:
      for i,j in enumerate(morphs):
        if j!="_" and j!="":
          doc[i].set_morph(j)
    else:
      doc.is_tagged=True
      doc.is_parsed=True
    return doc

def load(command="Alpino"):
  from spacy.lang.nl import Dutch
  nlp=Dutch()
  if SPACY_V3:
    nlp.add_pipe("sentencizer")
    Language.component("Alpino",func=AlpinoParser(command,nlp.vocab))
    nlp.add_pipe("Alpino")
  else:
    nlp.add_pipe(nlp.create_pipe("sentencizer"))
    nlp.add_pipe(AlpinoParser(command,nlp.vocab))
  nlp.meta["lang"]="nl_Alpino"
  return nlp

