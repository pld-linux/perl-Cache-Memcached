#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Cache
%define		pnam	Memcached
Summary:	Cache::Memcached - shared data cache using memcached
Summary(pl):	Cache::Memcached - wspó³dzielone cache dla danych przy u¿yciu memcached
Name:		perl-Cache-Memcached
Version:	1.15
Release:	0.1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b18a9c7ba62236758219cc60a25b6a4c
URL:		http://www.danga.com/memcached/
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl-String-CRC32
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the Perl API for memcached, a distributed memory cache daemon.

memcached is a high-performance, distributed memory object caching
system, generic in nature, but intended for use in speeding up dynamic
web applications by alleviating database load.

%description -l pl
To jest perlowe API dla memcached - rozproszonego demona cache'owania
pamiêci.

memcached to wysoko wydajny, rozproszony system cache'owania obiektów,
ogólny w swojej naturze, ale stworzony z my¶l± o u¿ywaniu do
przyspieszenia dynamicznych aplikacji WWW poprzez zmniejszenie
obci±¿enia bazy danych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{perl_archlib}/perllocal.pod
rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/auto/Cache/Memcached/.packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* README
%{perl_vendorlib}/Cache/Memcached.pm
%{_mandir}/man3/*
