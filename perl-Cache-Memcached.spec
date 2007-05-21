#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Cache
%define		pnam	Memcached
Summary:	Cache::Memcached - shared data cache using memcached
Summary(pl.UTF-8):	Cache::Memcached - współdzielone cache dla danych przy użyciu memcached
Name:		perl-Cache-Memcached
Version:	1.21
Release:	1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f8788f874f2c83a8836642bfdfa35ddd
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

%description -l pl.UTF-8
To jest perlowe API dla memcached - rozproszonego demona cache'owania
pamięci.

memcached to wysoko wydajny, rozproszony system cache'owania obiektów,
ogólny w swojej naturze, ale stworzony z myślą o używaniu do
przyspieszenia dynamicznych aplikacji WWW poprzez zmniejszenie
obciążenia bazy danych.

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* README
%{perl_vendorlib}/Cache/Memcached.pm
%dir %{perl_vendorlib}/Cache/Memcached
%{perl_vendorlib}/Cache/Memcached/GetParser.pm
%{_mandir}/man3/*
