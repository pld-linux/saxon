# TODO:
# - update to version 9, but save it as saxon6.spec
#
# Conditional build:
%define		ver		6.5.5
%define		_ver		6-5-5
#
%include	/usr/lib/rpm/macros.java
#
Summary:	XSLT Processor in Java
Summary(pl.UTF-8):	Procesor XSLT napisany w Javie
Name:		saxon
Version:	%{ver}
Release:	2
License:	Mozilla Public License, some parts on other license (distributable)
Group:		Applications/Publishing/XML
Source0:	http://downloads.sourceforge.net/saxon/%{name}%{_ver}.zip
# Source0-md5:	e913002af9c6bbb4c4361ff41baac3af
Source1:	http://www.kosek.cz/xml/saxon/kosek.jar
# Source1-md5:	8871a018e1de23b77b2c0bce86176d60
Source2:	%{name}-build.xml
URL:		http://saxon.sourceforge.net/
BuildRequires:	ant
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
%ant

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_javadir},%{_javadocdir}/%{name}-%{version}}

install build/lib/saxon*.jar $RPM_BUILD_ROOT%{_javadir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_javadir}

cp -a build/api/* $RPM_BUILD_ROOT/%{_javadocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_javadir}/*.jar

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{name}-%{version}
