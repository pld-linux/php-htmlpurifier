Summary:	Standards-compliant HTML filter library written in PHP
Summary(pl.UTF-8):	Zgodna ze standardami biblioteka filtrująca HTML napisana w PHP
Name:		htmlpurifier
Version:	2.1.3
Release:	0.1
License:	LGPL v2.1
Group:		Development/Languages/PHP
Source0:	http://htmlpurifier.org/releases/%{name}-%{version}.zip
# Source0-md5:	6c6294789ef1d4198ce0dcb7fcd4d7de
URL:		http://htmlpurifier.org/
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	sed >= 4.0
Requires:	php-common >= 3:4.3.2
Suggests:	php(iconv)
Suggests:	php(tidy)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_phpdir		%{_datadir}/php

%description
HTML Purifier is a standards-compliant HTML filter library written in
PHP. HTML Purifier will not only remove all malicious code (better
known as XSS) with a thoroughly audited, secure yet permissive
whitelist, it will also make sure your documents are standards
compliant, something only achievable with a comprehensive knowledge of
W3C's specifications.

%description -l pl.UTF-8
HTML Purifier to zgodna ze standardami biblioteka filtrująca HTML
napisana w PHP. Nie tylko usuwa cały niebezpieczny kod (bardziej znany
jako XSS) z dobrze zaudytowaną i bezpieczną listą przypadków
akceptowanych, ale także upewnia się, że dokumenty są zgodne ze
standardami, co jest zwykle osiągalne tylko z dobrą znajomością
specyfikacji W3C.

%prep
%setup -q
%{__sed} -i -e 's,\r$,,' CREDITS INSTALL README TODO WHATSNEW WYSIWYG
find -name '*.php' -print0 | xargs -0 %{__sed} -i -e 's,\r$,,'

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_phpdir}
cp -a library/* $RPM_BUILD_ROOT%{_phpdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS INSTALL README TODO WHATSNEW WYSIWYG
%{_phpdir}/*
