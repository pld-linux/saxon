%define		ver		6.5.2
%define		_ver		6_5_2

Summary:	XSLT Processor in Java
Summary(pl):	Procesor XSLT napisany w Javie
Name:		saxon
Version:	%{ver}
Release:	1
Vendor:		Michael Kay
License:	Mozilla Public License, some parts on other license (distributable)
Group:		Applications/Publishing/XML
Source0:	http://dl.sf.net/%{name}/%{name}%{_ver}.zip
# Source0-md5:	6a822530943cc9ddff45ed4d77413d89
Source1:	http://www.kosek.cz/xml/saxon/kosek.jar
# Source1-md5:	8871a018e1de23b77b2c0bce86176d60
URL:		http://users.iclway.co.uk/mhkay/saxon/
Requires:	jre
Requires:	xml-commons
Requires:	jaxp_parser_impl
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	%{_datadir}/java

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
install -d $RPM_BUILD_ROOT%{_javalibdir}

install %{name}*.jar $RPM_BUILD_ROOT%{_javalibdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_javalibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc
%{_javalibdir}/*.jar
