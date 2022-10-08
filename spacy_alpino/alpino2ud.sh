#! /bin/sh
TMP=/tmp/alpino$$
trap "/bin/rm -fr $TMP ; exit 2" 1 2 3 15
mkdir $TMP

( ${1-Alpino} -flag treebank $TMP end_hook=xml -parse > /dev/null
  ( echo '<collection>'
    ls -v1 $TMP/[1-9]*.xml | sed 's?.*?<doc href="&" />?'
    echo '</collection>'
  ) > $TMP/all.xml
  xqilla -v DIR $TMP/all.xml -v LIB no -v MODE conll -v ENHANCED yes `dirname $0`/universal_dependencies.xq ) 2> /dev/null

/bin/rm -fr $TMP
exit 0
