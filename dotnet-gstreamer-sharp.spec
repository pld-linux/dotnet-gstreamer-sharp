Summary:	.NET bindings for GStreamer 1.0
Summary(pl.UTF-8):	Wiązania GStreamera 1.0 dla .NET
Name:		dotnet-gstreamer-sharp
Version:	1.20.1
Release:	0.1
License:	LGPL v2.1+
Group:		Libraries
Source0:	https://gstreamer.freedesktop.org/src/gstreamer-sharp/gstreamer-sharp-%{version}.tar.xz
# Source0-md5:	4d18fa3a9bba4266db8a3db0869c885a
Source1:	https://github.com/GLibSharp/GtkSharp/archive/4c85f1479cf2e0dc056c0d288785e5a1d7251cb1/GtkSharp-4c85f1479cf2e0dc056c0d288785e5a1d7251cb1.tar.gz
# Source1-md5:	0917a7cba40ceaf9ec8b4e187df24f03
Source2:	https://github.com/GLibSharp/bindinator/archive/c29b965e5ee4a9bd7fcf6b8f4d78dba6c9cbe6ac/bindinator-c29b965e5ee4a9bd7fcf6b8f4d78dba6c9cbe6ac.tar.gz
# Source2-md5:	940e8b3f838000e7b428f01a7e47dec0
Patch0:		gstreamer-sharp-system-gtk-sharp3.patch
URL:		https://gstreamer.freedesktop.org/
BuildRequires:	dotnet-gtk-sharp3-devel >= 3.22.6
BuildRequires:	glib2-devel >= 1:2.18.1
BuildRequires:	gstreamer-devel >= 1.0
BuildRequires:	gstreamer-plugins-base-devel >= 1.0
BuildRequires:	meson >= 0.59
BuildRequires:	mono-csharp >= 2.4
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.745
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	dotnet-gtk-sharp3 >= 3.22.6
Requires:	glib2 >= 1:2.18.1
Requires:	gstreamer >= 1.0
Requires:	gstreamer-plugins-base >= 1.0
Requires:	mono >= 2.4
ExclusiveArch:	%{ix86} %{x8664} %{arm} hppa ia64 ppc s390 s390x sparc sparcv9 sparc64
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
Obsoletes:	dotnet-gstreamer-sharp-static < 1.14

%description devel
Development files for GStreamer-sharp library.

%description devel -l pl.UTF-8
Pliki programistyczne biblioteki GStreamer-sharp.

%prep
%setup -q -n gstreamer-sharp-%{version} -a1 -a2
# currently not possible: relies on extensions from GLibSharp fork, openmedicus is not sufficient
#patch0 -p1

%{__mv} GtkSharp-* subprojects/gtk-sharp
%{__mv} bindinator-* subprojects/bindinator

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

# build system doesn't support installing
MESON_BUILD_ROOT=$(pwd)/build \
MESON_INSTALL_DESTDIR_PREFIX=$RPM_BUILD_ROOT%{_prefix} \
%{__python3} gacutil_install.py \
	gstreamer-sharp sources/gstreamer-sharp.dll \
	gst-editing-services-sharp ges/gst-editing-services-sharp.dll

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md
%{_prefix}/lib/mono/gac/gst-editing-services-sharp
%{_prefix}/lib/mono/gac/gstreamer-sharp

%files devel
%defattr(644,root,root,755)
%dir %{_prefix}/lib/mono/gst-editing-services-sharp
%{_prefix}/lib/mono/gst-editing-services-sharp/gst-editing-services-sharp.dll
%dir %{_prefix}/lib/mono/gstreamer-sharp
%{_prefix}/lib/mono/gstreamer-sharp/gstreamer-sharp.dll
# not included in this version
#%{_pkgconfigdir}/gstreamer-sharp-1.0.pc
