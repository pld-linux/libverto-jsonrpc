#
# Conditional build:
%bcond_without	static_libs	# static library
#
Summary:	JSON-RPC support for libverto
Summary(pl.UTF-8):	Obsługa JSON-RPC dla libverto
Name:		libverto-jsonrpc
Version:	0.1.0
Release:	3
License:	MIT
Group:		Libraries
Source0:	https://fedorahosted.org/releases/l/i/libverto-jsonrpc/%{name}-%{version}.tar.gz
# Source0-md5:	5076eadc3e3b43f7139d0b8cf96e575d
Patch0:		%{name}-json.patch
URL:		https://fedorahosted.org/libverto/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.11
BuildRequires:	json-c-devel
BuildRequires:	libtool >= 2:2
BuildRequires:	libverto-devel >= 0.2.4
BuildRequires:	pkgconfig
Requires:	libverto >= 0.2.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A library for doing JSON-RPC over a socket, using the libverto API.

%description -l pl.UTF-8
Biblioteka do wykonywania JSON-RPC na gnieździe przy użyciu API
biblioteki libverto.

%package devel
Summary:	Header files for verto-jsonrpc library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki verto-jsonrpc
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	json-c-devel
Requires:	libverto-devel >= 0.2.4

%description devel
Header files for verto-jsonrpc library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki verto-jsonrpc.

%package static
Summary:	Static verto-jsonrpc library
Summary(pl.UTF-8):	Statyczna biblioteka verto-jsonrpc
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static verto-jsonrpc library.

%description static -l pl.UTF-8
Statyczna biblioteka verto-jsonrpc.

%prep
%setup -q
%patch -P0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules \
	%{?with_static_libs:--enable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libverto-jsonrpc.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/libverto-jsonrpc.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libverto-jsonrpc.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libverto-jsonrpc.so
%{_includedir}/verto-jsonrpc.h
%{_pkgconfigdir}/libverto-jsonrpc.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libverto-jsonrpc.a
%endif
