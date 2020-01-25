Summary:	.NET bindings for GStreamer 1.0
Summary(pl.UTF-8):	Wiązania GStreamera 1.0 dla .NET
Name:		dotnet-gstreamer-sharp
Version:	0.99.0
Release:	1
License:	AGPL v3+
Group:		Libraries
Source0:	http://gstreamer.freedesktop.org/src/gstreamer-sharp/gstreamer-sharp-%{version}.tar.gz
# Source0-md5:	467cdfdb75e0ad568c2d7bc5c47e0c25
URL:		http://gstreamer.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	dotnet-gtk-sharp3-devel >= 2.99.2
BuildRequires:	glib2-devel >= 1:2.18.1
BuildRequires:	gstreamer-devel >= 1.0
BuildRequires:	gstreamer-plugins-base-devel >= 1.0
BuildRequires:	libtool >= 2:2
BuildRequires:	mono-csharp >= 2.4
BuildRequires:	monodoc >= 1.1
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(monoautodeps)
Requires:	dotnet-gtk-sharp3 >= 2.99.2
Requires:	glib2 >= 1:2.18.1
Requires:	gstreamer >= 1.0
Requires:	gstreamer-plugins-base >= 1.0
Requires:	mono >= 2.4
ExclusiveArch:	%{ix86} %{x8664} arm hppa ia64 ppc s390 s390x sparc sparcv9 sparc64
ExcludeArch:	i386
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides bindings for .NET to GStreamer 1.0 libraries.

%description -l pl.UTF-8
Pakiet ten dostarcza wiązania dla .NET do bibliotek GStreamera 1.0.

%package devel
Summary:	Development files for GStreamer-sharp library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki GStreamer-sharp
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	monodoc >= 1.1

%description devel
Development files for GStreamer-sharp library.

%description devel -l pl.UTF-8
Pliki programistyczne biblioteki GStreamer-sharp.

%package static
Summary:	Static gstreamer-sharp library
Summary(pl.UTF-8):	Biblioteka statyczna gstreamer-sharp
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gstreamer-sharp library.

%description static -l pl.UTF-8
Biblioteka statyczna gstreamer-sharp.

%prep
%setup -q -c

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgstreamersharpglue-1.0.0.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE NEWS README.md
%attr(755,root,root) %{_libdir}/libgstreamersharpglue-1.0.0.so
%{_prefix}/lib/mono/gac/gstreamer-sharp

%files devel
%defattr(644,root,root,755)
%dir %{_prefix}/lib/mono/gstreamer-sharp
%{_prefix}/lib/mono/gstreamer-sharp/gstreamer-sharp.dll
%{_prefix}/lib/monodoc/sources/gstreamer-sharp-docs.*
%{_pkgconfigdir}/gstreamer-sharp-1.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgstreamersharpglue-1.0.0.a
