# TODO:
# system-wide pulse daemon stuff:
# - init script
# - pulse:pulse uid/gid for daemon
# - realtime and pulse-access groups for users
#
# Conditional build:
%bcond_without	lirc	# without lirc module
#
Summary:	Modular sound server
Summary(pl):	Modularny serwer d¼wiêku
Name:		pulseaudio
Version:	0.9.4
Release:	1
License:	GPL (server and libpulsecore), LGPL (libpulse)
Group:		Libraries
Source0:	http://0pointer.de/lennart/projects/pulseaudio/%{name}-%{version}.tar.gz
# Source0-md5:	aadbbc68306653f9052872c11e0cc707
Patch0:		%{name}-suid.patch
URL:		http://pulseaudio.org/
BuildRequires:	alsa-lib-devel >= 1.0.0
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.4.0
BuildRequires:	avahi-devel >= 0.6.0
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
BuildRequires:	m4
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
BuildRequires:	XFree86-devel
Requires:	%{name}-libs = %{version}-%{release}
Obsoletes:	polypaudio
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PulseAudio (previously known as PolypAudio) is a sound server for
POSIX and Win32 operating systems. It allows you to do advanced
operations on your sound data as it passes between your application
and your hardware. Things like transferring the audio to a different
machine, changing the sample format or channel count and mixing
several sounds into one are easily achieved using a sound server.

%description -l pl
PulseAudio (poprzednio znany jako PolypAudio) to serwer d¼wiêku dla
systemów operacyjnych zgodnych z POSIX oraz Win32. Pozwala na
wykonywanie zaawansowanych operacji na danych d¼wiêkowych
przekazywanych miêdzy aplikacjami a sprzêtem. Przy u¿yciu tego serwera
mo¿na ³atwo osi±gn±æ takie rzeczy jak przesy³anie d¼wiêku na inn±
maszynê, zmiana formatu próbek czy liczby kana³ów oraz miksowanie
kilku d¼wiêków w jeden.

%package libs
Summary:	PulseAudio libraries
Summary(pl):	Biblioteki PulseAudio
Group:		Libraries
Requires:	glib2 >= 1:2.4.0
Requires:	libasyncns >= 0.1
Requires:	libsamplerate >= 0.1.0
Requires:	libsndfile >= 1.0.10
Obsoletes:	polypaudio-libs
Conflicts:	polypaudio < 0.7-4

%description
PulseAudio libraries.

%description libs -l pl
Biblioteki PulseAudio.

%package devel
Summary:	Development files for PulseAudio libraries
Summary(pl):	Pliki programistyczne bibliotek PulseAudio
License:	GPL (libpulsecore), LGPL (libpulse)
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	glib2-devel >= 1:2.4.0
Requires:	libasyncns-devel >= 0.1
Requires:	libcap-devel
Requires:	XFree86-devel
Obsoletes:	polypaudio-devel

%description devel
Development files for PulseAudio libraries.

%description devel -l pl
Pliki programistyczne bibliotek PulseAudio.

%package static
Summary:	Static PulseAudio libraries
Summary(pl):	Statyczne biblioteki PulseAudio
License:	GPL (libpulsecore), LGPL (libpulse)
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	polypaudio-static

%description static
Static PulseAudio libraries.

%description static -l pl
Statyczne biblioteki PulseAudio.

%package alsa
Summary:	ALSA modules for PulseAudio
Summary(pl):	Modu³y ALSA dla PulseAudio
License:	GPL
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	alsa-lib >= 1.0.0
Obsoletes:	polypaudio-alsa

%description alsa
ALSA modules for PulseAudio.

%description alsa -l pl
Modu³y ALSA dla PulseAudio.

%package jack
Summary:	JACK modules for PulseAudio
Summary(pl):	Modu³y JACK dla PulseAudio
License:	GPL
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	jack-audio-connection-kit >= 0.100
Obsoletes:	polypaudio-jack

%description jack
JACK modules for PulseAudio.

%description jack -l pl
Modu³y JACK dla PulseAudio.

%package lirc
Summary:	LIRC module for PulseAudio
Summary(pl):	Modu³ LIRC dla PulseAudio
License:	GPL
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	polypaudio-lirc

%description lirc
LIRC module for PulseAudio.

%description lirc -l pl
Modu³ LIRC dla PulseAudio.

%prep
%setup -q
%patch0 -p1

# no need for -lSM -lICE
sed -i -e 's/ \$(X_PRE_LIBS)//' src/Makefile.am

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_lirc:--disable-lirc}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# not needed (lt_dlopenext() is used)
rm -f $RPM_BUILD_ROOT%{_libdir}/pulse-*/modules/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%triggerpostun -- polypaudio
if [ -f %{_sysconfdir}/polypaudio/daemon.conf.rpmsave ]; then
	mv -f %{_sysconfdir}/pulse/daemon.conf %{_sysconfdir}/pulse/daemon.conf.rpmnew
	mv -f %{_sysconfdir}/polypaudio/daemon.conf.rpmsave %{_sysconfdir}/pulse/daemon.conf
fi
if [ -f %{_sysconfdir}/polypaudio/default.pa.rpmsave ]; then
	mv -f %{_sysconfdir}/pulse/default.pa %{_sysconfdir}/pulse/default.pa.rpmnew
	mv -f %{_sysconfdir}/polypaudio/default.pa.rpmsave %{_sysconfdir}/pulse/default.pa
fi

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%triggerpostun -- polypaudio-libs
if [ -f %{_sysconfdir}/polypaudio/client.conf.rpmsave ]; then
	mv -f %{_sysconfdir}/pulse/client.conf %{_sysconfdir}/pulse/client.conf.rpmnew
	mv -f %{_sysconfdir}/polypaudio/client.conf.rpmsave %{_sysconfdir}/pulse/client.conf
fi

%files
%defattr(644,root,root,755)
%doc README
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/pulse/daemon.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/pulse/default.pa
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/pulse-*
%dir %{_libdir}/pulse-*/modules
%attr(755,root,root) %{_libdir}/pulse-*/modules/*.so
%exclude %{_libdir}/pulse-*/modules/libalsa-util.*
%exclude %{_libdir}/pulse-*/modules/module-alsa-sink.*
%exclude %{_libdir}/pulse-*/modules/module-alsa-source.*
%exclude %{_libdir}/pulse-*/modules/module-jack-sink.*
%exclude %{_libdir}/pulse-*/modules/module-jack-source.*
%if %{with lirc}
%exclude %{_libdir}/pulse-*/modules/module-lirc.*
%endif

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%attr(755,root,root) %{_libdir}/libpulsedsp.so
%dir %{_sysconfdir}/pulse
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/pulse/client.conf

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%exclude %{_libdir}/libpulsedsp.so
%{_libdir}/lib*.la
%{_includedir}/pulse
%{_includedir}/pulsecore
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files alsa
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pulse-*/modules/libalsa-util.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-alsa-sink.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-alsa-source.so

%files jack
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-jack-sink.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-jack-source.so

%if %{with lirc}
%files lirc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-lirc.so
%endif
