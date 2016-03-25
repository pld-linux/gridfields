Summary:	GridFields - convenient, algebraic manipulation of unstructured grids
Summary(pl.UTF-8):	GridFields - wygodne operacje algebraiczne na tablicach bez struktury
Name:		gridfields
Version:	1.0.5
Release:	1
# COPYING and most recent source files (GFError.*) say so
License:	LGPL v2.1+
Group:		Libraries
# TODO: proper source URL when available (currently recent versions are not tagged)
#Source0:	https://github.com/OPENDAP/gridfields/%{name}-%{version}.tar.gz
# for now, use hyrax-dependencies module
Source0:	https://github.com/OPENDAP/hyrax-dependencies/raw/master/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	54819cdeb22e894921c7e84f460ae75a
URL:		https://github.com/OPENDAP/gridfields/
BuildRequires:	autoconf >= 2.68
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	netcdf-cxx-devel >= 4
BuildRequires:	netcdf-devel >= 4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GridFields library provides convenient, algebraic manipulation of
unstructured grids in C++ and Python.

%description -l pl.UTF-8
Biblioteka GridFields udostępnia wygodne operacje algebraiczne na
tablicach bez struktury z poziomu C++ i Pythona.

%package devel
Summary:	Header files for GridFields library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki GridFields
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel
Requires:	netcdf-cxx-devel >= 4
Requires:	netcdf-devel >= 4

%description devel
Header files for GridFields library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki GridFields.

%package static
Summary:	Static GridFields library
Summary(pl.UTF-8):	Statyczna biblioteka GridFields
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static GridFields library.

%description static -l pl.UTF-8
Statyczna biblioteka GridFields.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I conf
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-netcdf-include=%{_includedir} \
	--with-netcdf-libdir=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libgridfields.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgridfields.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gridfields-config
%attr(755,root,root) %{_libdir}/libgridfields.so
%{_libdir}/libgridfields.la
%{_includedir}/gridfields

%files static
%defattr(644,root,root,755)
%{_libdir}/libgridfields.a
