Summary:	XSLT Processor in Java
Summary(pl):	Procesor XSLT napisany w Javie
Name:		saxon
Version:	6.2
Release:	1
Vendor:		Michael Kay
License:	Mozilla Public License, some parts on other license (Distributable)
Group:		Applications/Publishing/XML
Group(pl):	Aplikacje/Publikowanie/XML
URL:		http://users.iclway.co.uk/mhkay/saxon/
Source0:	http://users.iclway.co.uk/mhkay/saxon/%{name}%{version}/%{name}.zip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%define	_javaclassdir	%{_datadir}/java/classes
%define	_jredir		%{_libdir}/jre

%description

%description -l pl 

%prep
%setup -q -c -T
unzip -qa %{SOURCE0}
chmod -R a+rX *

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javaclassdir}
install %{name}.jar $RPM_BUILD_ROOT%{_javaclassdir}

#gzip -9nf copying.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc
%{_javaclassdir}/*
