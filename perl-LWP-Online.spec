#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	LWP
%define		pnam	Online
%include	/usr/lib/rpm/macros.perl
Summary:	LWP::Online - Does your process have access to the web
Name:		perl-LWP-Online
Version:	1.08
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/LWP/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	20e25b3af8b84a493c730249c2a9c50d
URL:		http://search.cpan.org/dist/LWP-Online/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-URI >= 1.35
BuildRequires:	perl-libwww >= 5.805
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module attempts to answer, as accurately as it can, one of the
nastiest technical questions there is.

Am I on the internet?

The answer is useful in a wide range of decisions. For example...

Should my test scripts run the online portion of the tests or just
skip them?

Do I try to fetch fresh data from the server?

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/LWP/Online.pm
%{_mandir}/man3/LWP::Online.3pm*
