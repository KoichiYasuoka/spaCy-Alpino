import setuptools

with open("README.md","r",encoding="utf-8") as r:
  long_description=r.read()
URL="https://github.com/KoichiYasuoka/spaCy-Alpino"

setuptools.setup(
  name="spacy_alpino",
  version="0.4.0",
  description="Alpino wrapper for spaCy",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url=URL,
  author="Koichi Yasuoka",
  author_email="yasuoka@kanji.zinbun.kyoto-u.ac.jp",
  license="MIT",
  keywords="spacy nlp",
  packages=setuptools.find_packages(),
  install_requires=["spacy>=2.2.2","deplacy>=1.8.1"],
  python_requires=">=3.6",
  package_data={"spacy_alpino":["./alpino2ud.sh","./universal_dependencies.xq"]},
  classifiers=[
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Operating System :: OS Independent",
    "Topic :: Text Processing :: Linguistic",
    "Natural Language :: Dutch"
  ],
  project_urls={
    "Alpino":"http://www.let.rug.nl/vannoord/alp/Alpino/",
    "Source":URL,
    "Tracker":URL+"/issues"
  }
)
