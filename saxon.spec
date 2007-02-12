%define		ver		6.5.5
%define		_ver		6-5-5

Summary:	XSLT Processor in Java
Summary(pl.UTF-8):   Procesor XSLT napisany w Javie
Name:		saxon
Version:	%{ver}
Release:	1
Vendor:		Michael Kay
License:	Mozilla Public License, some parts on other license (distributable)
Group:		Applications/Publishing/XML
Source0:	http://dl.sourceforge.net/saxon/%{name}%{_ver}.zip
# Source0-md5:	e913002af9c6bbb4c4361ff41baac3af
Source1:	http://www.kosek.cz/xml/saxon/kosek.jar
# Source1-md5:	8871a018e1de23b77b2c0bce86176d60
URL:		http://saxon.sourceforge.net/
BuildRequires:	unzip
Requires:	jre
Requires:	xml-commons
Requires:	jaxp_parser_impl
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	%{_datadir}/java

%description
XSLT Processor in Java.

%description -l pl.UTF-8
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
