Summary:	Standards-compliant HTML filter library written in PHP
Name:		htmlpurifier
Version:	2.1.2
Release:	0.1
License:	GPL
Group:		Development/Languages/PHP
Source0:	http://htmlpurifier.org/releases/%{name}-%{version}.zip
# Source0-md5:	b5cbe4cb5717c671ab00fb74cbc7f12e
URL:		http://htmlpurifier.org/
BuildRequires:	rpmbuild(macros) >= 1.268
Requires:	php-common
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML Purifier is a standards-compliant HTML filter library written in
PHP. HTML Purifier will not only remove all malicious code (better
known as XSS) with a thoroughly audited, secure yet permissive
whitelist, it will also make sure your documents are standards
compliant, something only achievable with a comprehensive knowledge of
W3C's specifications.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
