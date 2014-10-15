Summary:	A companion library to Apache Portable Runtime
Name:		apr-util
Version:	1.5.4
Release:	1
License:	Apache v2.0
Group:		Libraries
Source0:	http://www.apache.org/dist/apr/%{name}-%{version}.tar.bz2
# Source0-md5:	2202b18f269ad606d70e1864857ed93c
URL:		http://apr.apache.org/
BuildRequires:	apr-devel
BuildRequires:	autoconf
BuildRequires:	db-devel
BuildRequires:	expat-devel
BuildRequires:	gdbm-devel
BuildRequires:	libtool
BuildRequires:	nss-devel
BuildRequires:	openssl-devel
BuildRequires:	sqlite3-devel
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A companion library to Apache Portable Runtime.

%package libs
Summary:	apr-util library
Group:		Development/Libraries

%description libs
apr-util library.

%package devel
Summary:	Header files and development documentation for apr-util
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files and development documentation for apr-util.

%prep
%setup -q

%{__rm} -r xml/expat

%build
%configure \
	--enable-static=no		\
	--with-apr=%{_bindir}		\
	--with-berkeley-db=%{_prefix}	\
	--with-dbm=db47			\
	--with-iconv=%{_prefix}		\
	--with-nss=%{_prefix}		\
	--with-openssl=%{_prefix}	\
	--without-mysql			\
	--without-pgsql			\
	--with-sqlite3=%{_prefix}	\
	--without-sqlite2

%{__make} \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/{,apr-util-1/}*.la

%check
%{__make} -j1 check

%clean
rm -rf $RPM_BUILD_ROOT
%post	libs -p /usr/sbin/ldconfig
%postun	libs -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES
%dir %{_libdir}/apr-util-1
%attr(755,root,root) %{_libdir}/apr-util-1/apr_dbd_sqlite3-1.so
%attr(755,root,root) %{_libdir}/apr-util-1/apr_dbd_sqlite3.so
%attr(755,root,root) %{_libdir}/apr-util-1/apr_dbm_db-1.so
%attr(755,root,root) %{_libdir}/apr-util-1/apr_dbm_db.so

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libaprutil-1.so.0
%attr(755,root,root) %{_libdir}/libaprutil-1.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libaprutil-1.so
%{_libdir}/aprutil.exp
%{_includedir}
%{_pkgconfigdir}/apr-util-1.pc

