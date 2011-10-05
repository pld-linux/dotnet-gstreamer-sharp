%include	/usr/lib/rpm/macros.mono
Summary:	.NET bindings for GStreamer
Summary(pl.UTF-8):	Wiązania GStreamera dla .NET
Name:		dotnet-gstreamer-sharp
Version:	0.9.2
Release:	2
License:	LGPL v2+
Group:		Libraries
Source0:	http://gstreamer.freedesktop.org/src/gstreamer-sharp/gstreamer-sharp-%{version}.tar.bz2
# Source0-md5:	767bdba4dd753ba766352360c7053c14
Patch0:		%{name}-destdir.patch
URL:		http://gstreamer.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.18.1
BuildRequires:	gstreamer-devel >= 0.10.25
BuildRequires:	gstreamer-plugins-base-devel >= 0.10.25
BuildRequires:	libtool
BuildRequires:	mono-csharp >= 2.4
BuildRequires:	monodoc >= 1.1
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(monoautodeps)
Requires:	glib2 >= 1:2.18.1
Requires:	gstreamer >= 0.10.25
Requires:	gstreamer-plugins-base >= 0.10.25
Requires:	mono >= 2.4
ExclusiveArch:	%{ix86} %{x8664} arm hppa ia64 ppc s390 s390x sparc sparcv9 sparc64
ExcludeArch:	i386
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides bindings for .NET to GStreamer libraries.

%description -l pl.UTF-8
Pakiet ten dostarcza wiązania dla .NET do bibliotek GStreamera.

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
%setup -q -n gstreamer-sharp-%{version}
%patch0 -p1

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

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README RELEASE TODO
%attr(755,root,root) %{_libdir}/libgstreamersharpglue-0.10.so
# needed for DllImport on basename
%{_libdir}/libgstreamersharpglue-0.10.la
%{_prefix}/lib/mono/gac/gstreamer-sharp

%files devel
%defattr(644,root,root,755)
%dir %{_prefix}/lib/mono/gstreamer-sharp-0.10
%{_prefix}/lib/mono/gstreamer-sharp-0.10/gstreamer-sharp.dll
%{_prefix}/lib/monodoc/sources/gstreamer-sharp-docs.*
%{_datadir}/gapi/gstreamer-api.xml
%{_pkgconfigdir}/gstreamer-sharp-0.10.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgstreamersharpglue-0.10.a
