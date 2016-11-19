#!/bin/sh
for ui in `ls *.ui`
do
    py=`basename $ui .ui`.py
    tmp=`basename $ui .ui`.tmp

    echo pyuic4 -o ../$py $ui
    pyuic4 -o ../$tmp $ui
    sed 's/qwt_plot/PyQt4.Qwt5/' ../$tmp > ../$py
done
