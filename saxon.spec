Summary:	XSLT Processor in Java
Summary(pl):	Procesor XSLT napisany w Javie
Name:		saxon
#
# Please contact me before upgrading from 6.0.2
# Since version 6.2 version the API has changed /klakier
Version:	6.5.1
Release:	0.1
Vendor:		Michael Kay
License:	Mozilla Public License, some parts on other license (distributable)
Group:		Applications/Publishing/XML
Source0:	http://users.iclway.co.uk/mhkay/saxon/%{name}%{version}/%{name}6_5_1.zip
Source1:	http://www.kosek.cz/xml/saxon/kosek.jar
Source2:	http://www.kosek.cz/xml/saxon/crimson.jar
URL:		http://users.iclway.co.uk/mhkay/saxon/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	jre
BuildArch:	noarch
AutoReqProv:	0

%define	_javaclassdir	%{_datadir}/java/classes
%define	_jredir		%{_libdir}/jre

%description
XSLT Processor in Java.

%description -l pl
Procesor XSLT napisany w Javie.

%prep
%setup -q -c -T
unzip -qa %{SOURCE0}
chmod -R a+rX *

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javaclassdir}

install %{name}.jar $RPM_BUILD_ROOT%{_javaclassdir}
install %{SOURCE1} %{SOURCE2} $RPM_BUILD_ROOT%{_javaclassdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc
%{_javaclassdir}/*
