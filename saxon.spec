Summary:	XSLT Processor in Java
Summary(pl):	Procesor XSLT napisany w Javie
Name:		saxon
#
# Please contact me before upgrading from 6.0.2
# Since version 6.2 version the API has changed /klakier
Version:	6.0.2
Release:	1
Vendor:		Michael Kay
License:	Mozilla Public License, some parts on other license (distributable)
Group:		Applications/Publishing/XML
# new version:	http://dl.sourceforge.net/saxon/saxon6_5_2.zip
Source0:	http://users.iclway.co.uk/mhkay/saxon/%{name}%{version}/%{name}.zip
Source1:	http://www.kosek.cz/xml/saxon/kosek.jar
# already in other packages (crimson, jaxp)
# ...but this version has org.w3c.dom.{html,range,traversal} not present in other ones???
#Source2:	http://www.kosek.cz/xml/saxon/crimson.jar
# new URL:	http://saxon.sourceforge.net/
URL:		http://users.iclway.co.uk/mhkay/saxon/
Requires:	jre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javaclassdir	%{_datadir}/java

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
install %{SOURCE1} $RPM_BUILD_ROOT%{_javaclassdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc
%{_javaclassdir}/*
