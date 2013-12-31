Summary:	A companion library to Apache Portable Runtime
Name:		apr-util
Version:	1.5.3
Release:	1
License:	Apache v2.0
Group:		Libraries
Source0:	http://www.apache.org/dist/apr/%{name}-%{version}.tar.bz2
# Source0-md5:	6f3417691c7a27090f36e7cf4d94b36e
URL:		http://apr.apache.org/
BuildRequires:	apr-devel
BuildRequires:	autoconf
BuildRequires:	db-devel
BuildRequires:	expat-devel
BuildRequires:	gdbm-devel
BuildRequires:	libtool
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
	--with-dbm=db44			\
	--with-iconv=%{_prefix}		\
	--without-mysql			\
	--without-pgsql			\
	--without-sqlite2		\
	--without-sqlite3

%{__make} \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/apr-util-1/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /usr/sbin/ldconfig
%postun	libs -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES
%dir %{_libdir}/apr-util-1
%attr(755,root,root) %{_libdir}/apr-util-1/*.so

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libaprutil-1.so.0
%attr(755,root,root) %{_libdir}/libaprutil-1.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libaprutil-1.so
%{_libdir}/libaprutil-1.la
%{_libdir}/aprutil.exp
%{_includedir}
%{_pkgconfigdir}/apr-util-1.pc

