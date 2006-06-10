#
# Conditional build:
%bcond_without	lirc	# without lirc module
#
Summary:	Modular sound server
Summary(pl):	Modularny serwer d¼wiêku
Name:		polypaudio
Version:	0.9.1
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://0pointer.de/lennart/projects/polypaudio/%{name}-%{version}.tar.gz
# Source0-md5:	552741fc972a98319cf0414d704e9b78
Patch0:		%{name}-suid.patch
Patch1:		%{name}-libdir.patch
URL:		http://0pointer.de/lennart/projects/polypaudio/
BuildRequires:	XFree86-devel
BuildRequires:	alsa-lib-devel >= 1.0.0
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.4.0
BuildRequires:	howl-devel >= 0.9.8
BuildRequires:	jack-audio-connection-kit-devel >= 0.100
BuildRequires:	libasyncns-devel >= 0.1
BuildRequires:	libcap-devel
BuildRequires:	libltdl-devel
BuildRequires:	liboil-devel >= 0.3.0
BuildRequires:	libsamplerate-devel >= 0.1.0
BuildRequires:	libsndfile-devel >= 1.0.10
BuildRequires:	libtool
BuildRequires:	libwrap-devel
%{?with_lirc:BuildRequires:	lirc-devel}
BuildRequires:	lynx
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
polypaudio is a sound server for Linux and other Unix like operating
systems. It is intended to be an improved drop-in replacement for the
Enlightened Sound Daemon (EsounD). It is my ultimate ambition to get
Polypaudio into GNOME as a replacement for EsounD.

%description -l pl
polypaudio to serwer d¼wiêku dla Linuksa i innych uniksowych systemów
operacyjnych. Ma byæ zamiennikiem O¶wieconego Demona D¼wiêku (EsounD),
a ambicj± autora jest zast±pienie EsounD w GNOME.

%package libs
Summary:	Libraries for polypaudio
Summary(pl):	Biblioteki dla polypaudio
Group:		Libraries
Requires:	glib2 >= 1:2.4.0
Requires:	libasyncns >= 0.1
Requires:	libsamplerate >= 0.1.0
Requires:	libsndfile >= 1.0.10
Conflicts:	polypaudio < 0.7-4

%description
Libraries for polypaudio.

%description libs -l pl
Biblioteki dla polypaudio.

%package devel
Summary:	Development files for polypaudio
Summary(pl):	Pliki programistyczne polyaudio
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	glib2-devel >= 1:2.4.0
Requires:	libasyncns-devel >= 0.1
Requires:	libcap-devel
Requires:	XFree86-devel

%description devel
Development files for polypaudio.

%description devel -l pl
Pliki programistyczne polypaudio.

%package static
Summary:	Static polypaudio libraries
Summary(pl):	Statyczne biblioteki polypaudio
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static polypaudio libraries.

%description static -l pl
Statyczne biblioteki polypaudio.

%package alsa
Summary:	ALSA modules for polypaudio
Summary(pl):	Modu³y ALSA dla polypaudio
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	alsa-lib >= 1.0.0

%description alsa
ALSA modules for polypaudio.

%description alsa -l pl
Modu³y ALSA dla polypaudio.

%package jack
Summary:	JACK modules for polypaudio
Summary(pl):	Modu³y JACK dla polypaudio
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	jack-audio-connection-kit >= 0.100

%description jack
JACK modules for polypaudio.

%description jack -l pl
Modu³y JACK dla polypaudio.

%package lirc
Summary:	LIRC module for polypaudio
Summary(pl):	Modu³ LIRC dla polypaudio
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description lirc
LIRC module for polypaudio.

%description lirc -l pl
Modu³ LIRC dla polypaudio.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

# glib2 version should be sufficient
sed -i -e 's/HAVE_GLIB12=1/HAVE_GLIB12=0/' configure.ac

# no need for -lSM -lICE
sed -i -e 's/ \$(X_PRE_LIBS)//' src/Makefile.am

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_lirc:ac_cv_header_lirc_lirc_client_h=no}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# not needed (lt_dlopenext() is used)
rm -f $RPM_BUILD_ROOT%{_libdir}/polypaudio-*/modules/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/polypaudio/daemon.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/polypaudio/default.pa
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/polypaudio-*
%dir %{_libdir}/polypaudio-*/modules
%attr(755,root,root) %{_libdir}/polypaudio-*/modules/*.so
%exclude %{_libdir}/polypaudio-*/modules/libalsa-util.*
%exclude %{_libdir}/polypaudio-*/modules/module-alsa-sink.*
%exclude %{_libdir}/polypaudio-*/modules/module-alsa-source.*
%exclude %{_libdir}/polypaudio-*/modules/module-jack-sink.*
%exclude %{_libdir}/polypaudio-*/modules/module-jack-source.*
%if %{with lirc}
%exclude %{_libdir}/polypaudio-*/modules/module-lirc.*
%endif

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%attr(755,root,root) %{_libdir}/libpolypdsp.so
%dir %{_sysconfdir}/polypaudio
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/polypaudio/client.conf

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%exclude %{_libdir}/libpolypdsp.so
%{_libdir}/lib*.la
%{_includedir}/polyp
%{_includedir}/polypcore
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files alsa
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/polypaudio-*/modules/libalsa-util.so
%attr(755,root,root) %{_libdir}/polypaudio-*/modules/module-alsa-sink.so
%attr(755,root,root) %{_libdir}/polypaudio-*/modules/module-alsa-source.so

%files jack
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/polypaudio-*/modules/module-jack-sink.so
%attr(755,root,root) %{_libdir}/polypaudio-*/modules/module-jack-source.so

%if %{with lirc}
%files lirc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/polypaudio-*/modules/module-lirc.so
%endif
