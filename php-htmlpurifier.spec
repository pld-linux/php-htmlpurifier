# TODO
# - phorum-mod-htmlpurifier package: plugins/phorum
# - apidocs package: docs
# - run tests
%include	/usr/lib/rpm/macros.php
%define		php_min_version 5.1.2
Summary:	Standards-compliant HTML filter library written in PHP
Summary(pl.UTF-8):	Zgodna ze standardami biblioteka filtrująca HTML napisana w PHP
Name:		php-htmlpurifier
Version:	4.1.0
Release:	1
License:	LGPL v2.1
Group:		Development/Languages/PHP
Source0:	http://htmlpurifier.org/releases/htmlpurifier-%{version}.tar.gz
# Source0-md5:	d8a4388a7fe475db6a625f0c1b30bcae
URL:		http://www.htmlpurifier.org/
BuildRequires:	rpm-php-pearprov
BuildRequires:	rpmbuild(macros) >= 1.553
BuildRequires:	sed >= 4.0
Requires:	php-common >= 4:%{php_min_version}
Requires:	php-ctype
Requires:	php-dom
Requires:	php-pcre
Requires:	php-spl
Requires:	php-xml
Suggests:	php-iconv
Suggests:	php-tidy
Obsoletes:	htmlpurifier
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# bad depsolver
%define		_noautopear	pear

# exclude optional php dependencies
%define		_noautophp	php-curl

# put it together for rpmbuild
%define		_noautoreq	%{?_noautophp} %{?_noautopear}

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
%setup -qn htmlpurifier-%{version}
find -name '*.php' -print0 | xargs -0 %undos
mv INSTALL.fr{.utf8,}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}
cp -a library/* $RPM_BUILD_ROOT%{php_data_dir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS INSTALL README TODO WHATSNEW WYSIWYG
%doc FOCUS NEWS VERSION WHATSNEW
%doc %lang(fr) INSTALL.fr
%{php_data_dir}/*
