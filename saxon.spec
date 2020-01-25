# TODO:
# - update to version 9, but save it as saxon6.spec
# - split jars into java-saxon subpackage
#
# Conditional build:
%define		ver		6.5.5
%define		_ver		6-5-5
#
#
Summary:	XSLT Processor in Java
Summary(pl.UTF-8):	Procesor XSLT napisany w Javie
Name:		saxon
Version:	%{ver}
Release:	3
License:	Mozilla Public License, some parts on other license (distributable)
Group:		Applications/Publishing/XML
Source0:	http://downloads.sourceforge.net/saxon/%{name}%{_ver}.zip
# Source0-md5:	e913002af9c6bbb4c4361ff41baac3af
Source1:	%{name}.sh
Source2:	%{name}-build.xml
URL:		http://saxon.sourceforge.net/
BuildRequires:	ant
BuildRequires:	glibc-localedb-all
BuildRequires:	java-jdom
BuildRequires:	java-xml-commons
BuildRequires:	jdk
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	unzip
Requires:	java(jaxp_parser_impl)
Requires:	java-jdom
Requires:	java-xml-commons
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XSLT Processor in Java.

%description -l pl.UTF-8
Procesor XSLT napisany w Javie.

%package javadoc
Summary:	Online manual for saxon
Summary(pl.UTF-8):	Dokumentacja online dla saxon
Group:		Documentation
Requires:	jpackage-utils

%description javadoc
Documentation for saxon.

%description javadoc -l pl.UTF-8
Dokumentacja dla saxon.

%prep
%setup -q -c
install %{SOURCE2} build.xml
unzip -q source.zip

%{__rm} -rf *.jar docs/api

%build
export JAVA_HOME="%{java_home}"
export CLASSPATH=$(build-classpath xml-commons-apis jdom)
export LC_ALL=en_US # source code not US-ASCII
%ant

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_javadir},%{_javadocdir}/%{name}-%{version}}

install build/lib/saxon.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
install build/lib/saxon-jdom.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-jdom-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
ln -s %{name}-jdom-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-jdom.jar

install %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/%{name}

cp -a build/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/saxon
%{_javadir}/saxon-jdom.jar
%{_javadir}/saxon-jdom-%{version}.jar
%{_javadir}/saxon.jar
%{_javadir}/saxon-%{version}.jar

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}
