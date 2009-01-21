# TODO:
#	- service is too quiet with PULSEAUDIO_SYSTEM_START=0
#
# Conditional build:
%bcond_without	lirc		# without lirc module
%bcond_without	static_libs	# don't build static libraries
#
Summary:	Modular sound server
Summary(pl.UTF-8):	Modularny serwer dźwięku
Name:		pulseaudio
Version:	0.9.14
Release:	1
License:	GPL v2+ (server and libpulsecore), LGPL v2+ (libpulse)
Group:		Libraries
Source0:	http://0pointer.de/lennart/projects/pulseaudio/%{name}-%{version}.tar.gz
# Source0-md5:	0ed1115222d1d8c64cc14961cccb2eb0
Source1:	%{name}.init
Source2:	%{name}.sysconfig
Patch0:		%{name}-suid.patch
Patch1:		%{name}-link.patch
Patch2:		%{name}-path.patch
URL:		http://pulseaudio.org/
BuildRequires:	GConf2-devel >= 2.4.0
BuildRequires:	PolicyKit-devel
BuildRequires:	alsa-lib-devel >= 1.0.0
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake
BuildRequires:	avahi-devel >= 0.6.0
BuildRequires:	bluez-libs-devel >= 3.0
BuildRequires:	dbus-devel >= 1.0.0
BuildRequires:	glib2-devel >= 1:2.4.0
BuildRequires:	gdbm-devel
BuildRequires:	hal-devel >= 0.5.7
BuildRequires:	jack-audio-connection-kit-devel >= 0.100
BuildRequires:	libasyncns-devel >= 0.1
BuildRequires:	libatomic_ops >= 1.2-2
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
BuildRequires:	rpmbuild(macros) >= 1.228
BuildRequires:	speex-devel >= 1:1.2-beta3
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libX11-devel
Requires(post,preun):	/sbin/chkconfig
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires(pre):	fileutils
Requires:	%{name}-libs = %{version}-%{release}
Provides:	group(pulse)
Provides:	group(pulse-access)
Provides:	group(pulse-rt)
Provides:	user(pulse)
Obsoletes:	polypaudio
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PulseAudio (previously known as PolypAudio) is a sound server for
POSIX and Win32 operating systems. It allows you to do advanced
operations on your sound data as it passes between your application
and your hardware. Things like transferring the audio to a different
machine, changing the sample format or channel count and mixing
several sounds into one are easily achieved using a sound server.

%description -l pl.UTF-8
PulseAudio (poprzednio znany jako PolypAudio) to serwer dźwięku dla
systemów operacyjnych zgodnych z POSIX oraz Win32. Pozwala na
wykonywanie zaawansowanych operacji na danych dźwiękowych
przekazywanych między aplikacjami a sprzętem. Przy użyciu tego serwera
można łatwo osiągnąć takie rzeczy jak przesyłanie dźwięku na inną
maszynę, zmiana formatu próbek czy liczby kanałów oraz miksowanie
kilku dźwięków w jeden.

%package libs
Summary:	PulseAudio libraries
Summary(pl.UTF-8):	Biblioteki PulseAudio
Group:		Libraries
Requires:	glib2 >= 1:2.4.0
Requires:	libasyncns >= 0.1
Requires:	libsamplerate >= 0.1.0
Requires:	libsndfile >= 1.0.10
Obsoletes:	polypaudio-libs
Conflicts:	polypaudio < 0.7-4

%description libs
PulseAudio libraries.

%description libs -l pl.UTF-8
Biblioteki PulseAudio.

%package devel
Summary:	Development files for PulseAudio libraries
Summary(pl.UTF-8):	Pliki programistyczne bibliotek PulseAudio
License:	GPL v2+ (libpulsecore), LGPL v2+ (libpulse)
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	glib2-devel >= 1:2.4.0
Requires:	libasyncns-devel >= 0.1
Requires:	libatomic_ops >= 1.2-2
Requires:	libcap-devel
Requires:	xorg-lib-libX11-devel
Obsoletes:	polypaudio-devel

%description devel
Development files for PulseAudio libraries.

%description devel -l pl.UTF-8
Pliki programistyczne bibliotek PulseAudio.

%package static
Summary:	Static PulseAudio libraries
Summary(pl.UTF-8):	Statyczne biblioteki PulseAudio
License:	GPL v2+ (libpulsecore), LGPL v2+ (libpulse)
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	polypaudio-static

%description static
Static PulseAudio libraries.

%description static -l pl.UTF-8
Statyczne biblioteki PulseAudio.

%package esound-compat
Summary:	EsounD compatibility start script
Summary(pl.UTF-8):	Skrypt uruchamiający kompatybilny z EsounD
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}
Conflicts:	esound

%description esound-compat
EsounD compatibility start script, which allows to run pulseaudio
daemon using "esd" command.

NOTE: it ignores all command-line options!

%description esound-compat -l pl.UTF-8
Skrypt uruchamiający kompatybilny z EsounD, pozwalający na
uruchamianie demona pulseaudio przy użyciu polecenia "esd".

UWAGA: ignoruje wszystkie opcje z linii poleceń!

%package alsa
Summary:	ALSA modules for PulseAudio
Summary(pl.UTF-8):	Moduły ALSA dla PulseAudio
License:	GPL v2+
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	alsa-lib >= 1.0.0
Obsoletes:	polypaudio-alsa

%description alsa
ALSA modules for PulseAudio.

%description alsa -l pl.UTF-8
Moduły ALSA dla PulseAudio.

%package bluetooth
Summary:	Bluetooth module for PulseAudio
Summary(pl.UTF-8):	Moduł Bluetooth dla PulseAudio
License:	GPL v2+
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	bluez-libs >= 3.0

%description bluetooth
Bluetooth module for PulseAudio.

%description bluetooth -l pl.UTF-8
Moduł Bluetooth dla PulseAudio.

%package gconf
Summary:	GConf module for PulseAudio
Summary(pl.UTF-8):	Moduł GConf dla PulseAudio
License:	GPL v2+
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	GConf2 >= 2.4.0

%description gconf
GConf adapter for PulseAudio.

%description gconf -l pl.UTF-8
Interfejs do GConfa dla PulseAudio.

%package hal
Summary:	HAL module for PulseAudio
Summary(pl.UTF-8):	Moduł HAL dla PulseAudio
License:	GPL v2+
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	hal-libs >= 0.5.7

%description hal
HAL module for PulseAudio to detect available audio hardware and load
matching drivers.

%description hal -l pl.UTF-8
Moduł HAL dla PulseAudio wykrywający dostępny sprzęt dźwiękowy i
wczytujący pasujące sterowniki.

%package jack
Summary:	JACK modules for PulseAudio
Summary(pl.UTF-8):	Moduły JACK dla PulseAudio
License:	GPL v2+
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	jack-audio-connection-kit >= 0.100
Obsoletes:	polypaudio-jack

%description jack
JACK modules for PulseAudio.

%description jack -l pl.UTF-8
Moduły JACK dla PulseAudio.

%package lirc
Summary:	LIRC module for PulseAudio
Summary(pl.UTF-8):	Moduł LIRC dla PulseAudio
License:	GPL v2+
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	polypaudio-lirc

%description lirc
LIRC module for PulseAudio.

%description lirc -l pl.UTF-8
Moduł LIRC dla PulseAudio.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-ltdl-install=no \
	--with-system-user=pulse \
	--with-system-group=pulse \
	--with-realtime-group=pulse-rt \
	--with-access-group=pulse-access \
	%{!?with_lirc:--disable-lirc} \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/var/run/pulse

# libsocket-util.so and libipacl.so are relinked before libpulsecore.so
# so __make -jN install leads to "File not found by glob" (or they links
# with libpulsecore installed on builder)
%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

ln -sf %{_bindir}/esdcompat $RPM_BUILD_ROOT%{_bindir}/esd

# not needed (lt_dlopenext() is used)
rm -f $RPM_BUILD_ROOT%{_libdir}/pulse-*/modules/*.la

install -D %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/%{name}
install -D %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/%{name}

%find_lang %{name}

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

%pre
%groupadd -g 226 pulse
%groupadd -g 227 pulse-rt
%groupadd -g 228 pulse-access
%useradd -u 226 -g 226 -d /var/run/pulse -s /bin/false -c "Pulseaudio user" pulse

%post
/sbin/chkconfig --add %{name}
%service %{name} restart

%preun
if [ "$1" = "0" ]; then
	%service -q %{name} stop
	/sbin/chkconfig --del %{name}
fi
%postun
if [ "$1" = "0" ]; then
	%userremove pulse
	%groupremove pulse-access
	%groupremove pulse-rt
	%groupremove pulse
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/pulse/daemon.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/pulse/default.pa
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/pulse/system.pa
%attr(754,root,root) /etc/rc.d/init.d/%{name}
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}
%dir %attr(750,pulse,pulse-access) /var/run/pulse
%{_sysconfdir}/xdg/autostart/pulseaudio.desktop
%attr(755,root,root) %{_bindir}/pabrowse
%attr(755,root,root) %{_bindir}/pacat
%attr(755,root,root) %{_bindir}/pacmd
%attr(755,root,root) %{_bindir}/pactl
%attr(755,root,root) %{_bindir}/padsp
%attr(755,root,root) %{_bindir}/paplay
%attr(755,root,root) %{_bindir}/parec
%attr(755,root,root) %{_bindir}/pasuspender
%attr(755,root,root) %{_bindir}/pax11publish
%attr(755,root,root) %{_bindir}/pulseaudio
%attr(755,root,root) %{_bindir}/start-pulseaudio-x11
%dir %{_libdir}/pulse
%dir %{_libdir}/pulse-*
%dir %{_libdir}/pulse-*/modules
%attr(755,root,root) %{_libdir}/pulse-*/modules/libauth-cookie.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/libauthkey.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/libavahi-wrap.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/libcli.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/libdbus-util.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/libiochannel.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/libioline.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/libipacl.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/liboss-util.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/libpacket.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/libparseaddr.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/libpdispatch.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/libprotocol-cli.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/libprotocol-esound.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/libprotocol-http.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/libprotocol-native.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/libprotocol-simple.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/libpstream.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/libpstream-util.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/librtp.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/libsocket-client.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/libsocket-server.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/libsocket-util.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/libstrlist.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/libtagstruct.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/libx11prop.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/libx11wrap.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-always-sink.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-cli.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-cli-protocol-tcp.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-cli-protocol-unix.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-console-kit.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-combine.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-default-device-restore.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-detect.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-device-restore.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-esound-compat-spawnfd.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-esound-compat-spawnpid.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-esound-protocol-tcp.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-esound-protocol-unix.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-esound-sink.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-http-protocol-tcp.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-http-protocol-unix.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-ladspa-sink.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-match.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-mmkbd-evdev.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-native-protocol-fd.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-native-protocol-tcp.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-native-protocol-unix.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-null-sink.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-oss.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-pipe-sink.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-pipe-source.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-position-event-sounds.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-remap-sink.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-rescue-streams.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-rtp-recv.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-rtp-send.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-simple-protocol-tcp.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-simple-protocol-unix.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-sine.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-stream-restore.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-suspend-on-idle.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-tunnel-sink.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-tunnel-source.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-volume-restore.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-x11-bell.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-x11-publish.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-x11-xsmp.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-zeroconf-discover.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-zeroconf-publish.so
%{_datadir}/PolicyKit/policy/org.pulseaudio.policy
%{_mandir}/man1/pabrowse.1*
%{_mandir}/man1/pacat.1*
%{_mandir}/man1/pacmd.1*
%{_mandir}/man1/pactl.1*
%{_mandir}/man1/padsp.1*
%{_mandir}/man1/paplay.1*
%{_mandir}/man1/pasuspender.1*
%{_mandir}/man1/pax11publish.1*
%{_mandir}/man1/pulseaudio.1*
%{_mandir}/man5/default.pa.5*
%{_mandir}/man5/pulse-client.conf.5*
%{_mandir}/man5/pulse-daemon.conf.5*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpulse.so.*.*.*
%attr(755,root,root) %{_libdir}/libpulse-browse.so.*.*.*
%attr(755,root,root) %{_libdir}/libpulse-mainloop-glib.so.*.*.*
%attr(755,root,root) %{_libdir}/libpulse-simple.so.*.*.*
%attr(755,root,root) %{_libdir}/libpulsecore.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpulse.so.0
%attr(755,root,root) %ghost %{_libdir}/libpulse-browse.so.0
%attr(755,root,root) %ghost %{_libdir}/libpulse-mainloop-glib.so.0
%attr(755,root,root) %ghost %{_libdir}/libpulse-simple.so.0
%attr(755,root,root) %ghost %{_libdir}/libpulsecore.so.9
%attr(755,root,root) %{_libdir}/libpulsedsp.so
%dir %{_sysconfdir}/pulse
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/pulse/client.conf

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpulse.so
%attr(755,root,root) %{_libdir}/libpulse-browse.so
%attr(755,root,root) %{_libdir}/libpulse-mainloop-glib.so
%attr(755,root,root) %{_libdir}/libpulse-simple.so
%attr(755,root,root) %{_libdir}/libpulsecore.so
%{_libdir}/libpulse.la
%{_libdir}/libpulse-browse.la
%{_libdir}/libpulse-mainloop-glib.la
%{_libdir}/libpulse-simple.la
%{_libdir}/libpulsecore.la
%{_includedir}/pulse
%{_pkgconfigdir}/libpulse.pc
%{_pkgconfigdir}/libpulse-browse.pc
%{_pkgconfigdir}/libpulse-mainloop-glib.pc
%{_pkgconfigdir}/libpulse-simple.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libpulse.a
%{_libdir}/libpulse-browse.a
%{_libdir}/libpulse-mainloop-glib.a
%{_libdir}/libpulse-simple.a
%{_libdir}/libpulsecore.a
%endif

%files esound-compat
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/esd
%attr(755,root,root) %{_bindir}/esdcompat
%{_mandir}/man1/esdcompat.1*

%files alsa
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pulse-*/modules/libalsa-util.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-alsa-sink.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-alsa-source.so

%files bluetooth
%defattr(644,root,root,755)
%attr(4755,root,root) %{_libdir}/pulse/proximity-helper
%attr(755,root,root) %{_libdir}/pulse-*/modules/libbluetooth-ipc.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/libbluetooth-sbc.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-bluetooth-device.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-bluetooth-discover.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-bluetooth-proximity.so

%files gconf
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pulse/gconf-helper
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-gconf.so

%files hal
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-hal-detect.so

%files jack
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-jack-sink.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-jack-source.so

%if %{with lirc}
%files lirc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-lirc.so
%endif
