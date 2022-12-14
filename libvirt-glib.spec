# -*- rpm-spec -*-

Name: libvirt-glib
Version: 4.0.0
Release: 1%{?dist}
Summary: libvirt glib integration for events
License: LGPLv2+
URL: https://libvirt.org/
Source0: https://libvirt.org/sources/glib/%{name}-%{version}.tar.xz

BuildRequires: meson
BuildRequires: glib2-devel
BuildRequires: libvirt-devel
BuildRequires: gobject-introspection-devel
BuildRequires: libxml2-devel
BuildRequires: vala-tools
BuildRequires: gettext

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

%prep
%setup -q

%build
%meson -Drpath=disabled
%meson_build

%install
%meson_install

%find_lang %{name}

%check
%meson_test

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post -n libvirt-gconfig -p /sbin/ldconfig

%postun -n libvirt-gconfig -p /sbin/ldconfig

%post -n libvirt-gobject -p /sbin/ldconfig

%postun -n libvirt-gobject -p /sbin/ldconfig

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

%changelog
