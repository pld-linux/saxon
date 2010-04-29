#!/bin/sh -e

[ -r /usr/share/java-utils/java-functions ]
. /usr/share/java-utils/java-functions

CLASSPATH=$(find-jar saxon)
MAIN_CLASS=com.icl.saxon.StyleSheet

run ${1:+$@}
