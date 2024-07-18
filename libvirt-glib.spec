# -*- rpm-spec -*-

%global with_mingw 0
%if 0%{?fedora}
%global with_mingw 0%{!?_without_mingw:1}
%endif

Name: libvirt-glib
Version: 5.0.0
Release: 1%{?dist}
Summary: libvirt glib integration for events
License: LGPL-2.1-or-later
URL: https://libvirt.org/
Source0: https://libvirt.org/sources/glib/%{name}-%{version}.tar.xz

BuildRequires: meson
BuildRequires: glib2-devel
BuildRequires: libvirt-devel
BuildRequires: gobject-introspection-devel
BuildRequires: libxml2-devel
BuildRequires: vala
BuildRequires: gettext
BuildRequires: gtk-doc

%if %{with_mingw}
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-glib2
BuildRequires:  mingw32-libvirt

BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-glib2
BuildRequires:  mingw64-libvirt
%endif

%package devel
Summary: libvirt glib integration for events development files
Requires: %{name} = %{version}-%{release}

%package -n libvirt-gconfig
Summary: libvirt object APIs for processing object configuration

%package -n libvirt-gobject
Summary: libvirt object APIs for managing virtualization hosts

%package -n libvirt-gconfig-devel
Summary: libvirt object APIs for processing object configuration development files
Requires: libvirt-gconfig = %{version}-%{release}

%package -n libvirt-gobject-devel
Summary: libvirt object APIs for managing virtualization hosts development files
Requires: %{name}-devel = %{version}-%{release}
Requires: libvirt-gconfig-devel = %{version}-%{release}
Requires: libvirt-gobject = %{version}-%{release}
Requires: libvirt-devel

%description
This package provides integration between libvirt and the glib
event loop.

%description devel
This package provides development header files and libraries for
integration between libvirt and the glib event loop.

%description -n libvirt-gconfig
This package provides APIs for processing the object configuration
data

%description -n libvirt-gconfig-devel
This package provides development header files and libraries for
the object configuration APIs.

%description -n libvirt-gobject
This package provides APIs for managing virtualization host
objects

%description -n libvirt-gobject-devel
This package provides development header files and libraries for
managing virtualization host objects

%if %{with_mingw}
%package -n mingw32-libvirt-glib
Summary: MingwGW Windows libvirt-gconfig virtualization library
BuildArch: noarch
Requires: pkgconfig

%package -n mingw32-libvirt-gconfig
Summary: MingwGW Windows libvirt-gconfig virtualization library
BuildArch: noarch
Requires: pkgconfig

%package -n mingw32-libvirt-gobject
Summary: MingwGW Windows libvirt-gobject virtualization library
BuildArch: noarch
Requires: pkgconfig

%package -n mingw64-libvirt-glib
Summary: MingwGW Windows libvirt-gconfig virtualization library
BuildArch: noarch
Requires: pkgconfig

%package -n mingw64-libvirt-gconfig
Summary: MingwGW Windows libvirt-gconfig virtualization library
BuildArch: noarch
Requires: pkgconfig

%package -n mingw64-libvirt-gobject
Summary: MingwGW Windows libvirt-gobject virtualization library
BuildArch: noarch
Requires: pkgconfig

%description -n mingw32-libvirt-glib
MinGW Windows libvirt-glib virtualization library.

%description -n mingw32-libvirt-gconfig
MinGW Windows libvirt-gconfig virtualization library.

%description -n mingw32-libvirt-gobject
MinGW Windows libvirt-gobject virtualization library.


%description -n mingw64-libvirt-glib
MinGW Windows libvirt-glib virtualization library.

%description -n mingw64-libvirt-gconfig
MinGW Windows libvirt-gconfig virtualization library.

%description -n mingw64-libvirt-gobject
MinGW Windows libvirt-gobject virtualization library.

%{?mingw_debug_package}
%endif

%prep
%setup -q

%build
%meson -Drpath=disabled
%meson_build

%if %{with_mingw}
%mingw_meson -Drpath=disabled -Ddocs=disabled -Dintrospection=disabled -Dvapi=disabled
%mingw_ninja
%endif

%install
%meson_install

%find_lang %{name}

%if %{with_mingw}
%mingw_ninja_install

%mingw_debug_install_post

%mingw_find_lang libvirt-glib
%endif

%check
%meson_test

%files -f %{name}.lang
%doc README COPYING AUTHORS NEWS
%{_libdir}/libvirt-glib-1.0.so.*
%{_libdir}/girepository-1.0/LibvirtGLib-1.0.typelib

%files -n libvirt-gconfig
%{_libdir}/libvirt-gconfig-1.0.so.*
%{_libdir}/girepository-1.0/LibvirtGConfig-1.0.typelib

%files -n libvirt-gobject
%{_libdir}/libvirt-gobject-1.0.so.*
%{_libdir}/girepository-1.0/LibvirtGObject-1.0.typelib

%files devel
%doc examples/event-test.c
%{_libdir}/libvirt-glib-1.0.so
%{_libdir}/pkgconfig/libvirt-glib-1.0.pc
%dir %{_includedir}/libvirt-glib-1.0
%dir %{_includedir}/libvirt-glib-1.0/libvirt-glib
%{_includedir}/libvirt-glib-1.0/libvirt-glib/libvirt-glib.h
%{_includedir}/libvirt-glib-1.0/libvirt-glib/libvirt-glib-*.h
%{_datadir}/gir-1.0/LibvirtGLib-1.0.gir
%{_datadir}/gtk-doc/html/Libvirt-glib
%{_datadir}/vala/vapi/libvirt-glib-1.0.deps
%{_datadir}/vala/vapi/libvirt-glib-1.0.vapi

%files -n libvirt-gconfig-devel
%doc examples/event-test.c
%{_libdir}/libvirt-gconfig-1.0.so
%{_libdir}/pkgconfig/libvirt-gconfig-1.0.pc
%dir %{_includedir}/libvirt-gconfig-1.0
%dir %{_includedir}/libvirt-gconfig-1.0/libvirt-gconfig
%{_includedir}/libvirt-gconfig-1.0/libvirt-gconfig/libvirt-gconfig.h
%{_includedir}/libvirt-gconfig-1.0/libvirt-gconfig/libvirt-gconfig-*.h
%{_datadir}/gir-1.0/LibvirtGConfig-1.0.gir
%{_datadir}/gtk-doc/html/Libvirt-gconfig
%{_datadir}/vala/vapi/libvirt-gconfig-1.0.deps
%{_datadir}/vala/vapi/libvirt-gconfig-1.0.vapi

%files -n libvirt-gobject-devel
%doc examples/event-test.c
%{_libdir}/libvirt-gobject-1.0.so
%{_libdir}/pkgconfig/libvirt-gobject-1.0.pc
%dir %{_includedir}/libvirt-gobject-1.0
%dir %{_includedir}/libvirt-gobject-1.0/libvirt-gobject
%{_includedir}/libvirt-gobject-1.0/libvirt-gobject/libvirt-gobject.h
%{_includedir}/libvirt-gobject-1.0/libvirt-gobject/libvirt-gobject-*.h
%{_datadir}/gir-1.0/LibvirtGObject-1.0.gir
%{_datadir}/gtk-doc/html/Libvirt-gobject
%{_datadir}/vala/vapi/libvirt-gobject-1.0.deps
%{_datadir}/vala/vapi/libvirt-gobject-1.0.vapi

%if %{with_mingw}
%files -n mingw32-libvirt-glib -f mingw32-libvirt-glib.lang
%doc README COPYING AUTHORS NEWS
%{mingw32_bindir}/libvirt-glib-1.0-0.dll

%{mingw32_libdir}/libvirt-glib-1.0.dll.a

%{mingw32_libdir}/pkgconfig/libvirt-glib-1.0.pc

%dir %{mingw32_includedir}/libvirt-glib-1.0
%dir %{mingw32_includedir}/libvirt-glib-1.0/libvirt-glib
%{mingw32_includedir}/libvirt-glib-1.0/libvirt-glib/libvirt-glib.h
%{mingw32_includedir}/libvirt-glib-1.0/libvirt-glib/libvirt-glib-*.h

%files -n mingw64-libvirt-glib -f mingw64-libvirt-glib.lang
%doc README COPYING AUTHORS NEWS
%{mingw64_bindir}/libvirt-glib-1.0-0.dll

%{mingw64_libdir}/libvirt-glib-1.0.dll.a

%{mingw64_libdir}/pkgconfig/libvirt-glib-1.0.pc

%dir %{mingw64_includedir}/libvirt-glib-1.0
%dir %{mingw64_includedir}/libvirt-glib-1.0/libvirt-glib
%{mingw64_includedir}/libvirt-glib-1.0/libvirt-glib/libvirt-glib.h
%{mingw64_includedir}/libvirt-glib-1.0/libvirt-glib/libvirt-glib-*.h



%files -n mingw32-libvirt-gconfig
%{mingw32_bindir}/libvirt-gconfig-1.0-0.dll

%{mingw32_libdir}/libvirt-gconfig-1.0.dll.a

%{mingw32_libdir}/pkgconfig/libvirt-gconfig-1.0.pc

%dir %{mingw32_includedir}/libvirt-gconfig-1.0
%dir %{mingw32_includedir}/libvirt-gconfig-1.0/libvirt-gconfig
%{mingw32_includedir}/libvirt-gconfig-1.0/libvirt-gconfig/libvirt-gconfig.h
%{mingw32_includedir}/libvirt-gconfig-1.0/libvirt-gconfig/libvirt-gconfig-*.h

%files -n mingw64-libvirt-gconfig
%{mingw64_bindir}/libvirt-gconfig-1.0-0.dll

%{mingw64_libdir}/libvirt-gconfig-1.0.dll.a

%{mingw64_libdir}/pkgconfig/libvirt-gconfig-1.0.pc

%dir %{mingw64_includedir}/libvirt-gconfig-1.0
%dir %{mingw64_includedir}/libvirt-gconfig-1.0/libvirt-gconfig
%{mingw64_includedir}/libvirt-gconfig-1.0/libvirt-gconfig/libvirt-gconfig.h
%{mingw64_includedir}/libvirt-gconfig-1.0/libvirt-gconfig/libvirt-gconfig-*.h



%files -n mingw32-libvirt-gobject
%{mingw32_bindir}/libvirt-gobject-1.0-0.dll

%{mingw32_libdir}/libvirt-gobject-1.0.dll.a

%{mingw32_libdir}/pkgconfig/libvirt-gobject-1.0.pc

%dir %{mingw32_includedir}/libvirt-gobject-1.0
%dir %{mingw32_includedir}/libvirt-gobject-1.0/libvirt-gobject
%{mingw32_includedir}/libvirt-gobject-1.0/libvirt-gobject/libvirt-gobject.h
%{mingw32_includedir}/libvirt-gobject-1.0/libvirt-gobject/libvirt-gobject-*.h

%files -n mingw64-libvirt-gobject
%{mingw64_bindir}/libvirt-gobject-1.0-0.dll

%{mingw64_libdir}/libvirt-gobject-1.0.dll.a

%{mingw64_libdir}/pkgconfig/libvirt-gobject-1.0.pc

%dir %{mingw64_includedir}/libvirt-gobject-1.0
%dir %{mingw64_includedir}/libvirt-gobject-1.0/libvirt-gobject
%{mingw64_includedir}/libvirt-gobject-1.0/libvirt-gobject/libvirt-gobject.h
%{mingw64_includedir}/libvirt-gobject-1.0/libvirt-gobject/libvirt-gobject-*.h

%endif

%changelog
