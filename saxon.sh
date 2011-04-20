#!/bin/sh -e

[ -r /usr/share/java-utils/java-functions ]
. /usr/share/java-utils/java-functions

CLASSPATH=$(find-jar saxon)
MAIN_CLASS=com.icl.saxon.StyleSheet

# Note: there is 'exec' inside run in new jpackage-utils (1.7.5), however there
# is no exec in older one (1.7.3), so do not remove exec here.
exec run ${1:+$@}
