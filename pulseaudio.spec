# TODO:
# - service is too quiet with PULSEAUDIO_SYSTEM_START=0

# Conditional build:
%bcond_with	gdbm		# use gdbm as backend for settings database
				# see https://tango.0pointer.de/pipermail/pulseaudio-discuss/2009-May/003761.html
				# thread, why it's a bad idea
%bcond_without	lirc		# without lirc module
%bcond_without	xen		# Xen paravirtualized driver
%bcond_with	static_libs	# build static libraries

Summary:	Modular sound server
Summary(pl.UTF-8):	Modularny serwer dźwięku
Name:		pulseaudio
Version:	5.0
Release:	1
License:	GPL v2+ (server and libpulsecore), LGPL v2+ (libpulse)
Group:		Libraries
Source0:	http://freedesktop.org/software/pulseaudio/releases/%{name}-%{version}.tar.xz
# Source0-md5:	c43749838612f4860465e83ed62ca38e
Source1:	%{name}.init
Source2:	%{name}.sysconfig
Source3:	%{name}.tmpfiles
Patch0:		%{name}-pa-machine-id.patch
Patch1:		mate-desktop.patch
URL:		http://pulseaudio.org/
BuildRequires:	GConf2-devel >= 2.4.0
BuildRequires:	alsa-lib-devel >= 1.0.19
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	avahi-devel >= 0.6.0
BuildRequires:	bluez-libs-devel >= 4.99
BuildRequires:	dbus-devel >= 1.4.12
BuildRequires:	fftw3-single-devel >= 3
BuildRequires:	gcc >= 6:4.1
%{?with_gdbm:BuildRequires:	gdbm-devel}
BuildRequires:	gettext-devel >= 0.18.1
BuildRequires:	glib2-devel >= 1:2.4.0
BuildRequires:	gtk+3-devel >= 3.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	jack-audio-connection-kit-devel >= 0.117.0
BuildRequires:	json-c-devel >= 0.9
BuildRequires:	libasyncns-devel >= 0.1
BuildRequires:	libcap-devel
BuildRequires:	libltdl-devel >= 2:2.4
BuildRequires:	libsamplerate-devel >= 0.1.0
BuildRequires:	libsndfile-devel >= 1.0.20
BuildRequires:	libtool >= 2:2.4
BuildRequires:	libwrap-devel
BuildRequires:	libxcb-devel >= 1.6
%{?with_lirc:BuildRequires:	lirc-devel}
BuildRequires:	m4
# for module-roap
BuildRequires:	openssl-devel > 0.9
BuildRequires:	orc-devel >= 0.4.11
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.647
BuildRequires:	rpm-pythonprov
BuildRequires:	sbc-devel >= 1.0
BuildRequires:	speex-devel >= 1:1.2-beta3
BuildRequires:	systemd-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	udev-devel >= 1:143
BuildRequires:	webrtc-audio-processing-devel
%{?with_xen:BuildRequires:	xen-devel}
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:	xz
Requires:	%{name}-libs = %{version}-%{release}
Requires:	avahi >= 0.6.0
Requires:	dbus >= 1.4.12
Obsoletes:	polypaudio
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define zshdir %{_datadir}/zsh/site-functions

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

%package server
Summary:	Init scripts to run PA as system-wide daemon
Summary(pl.UTF-8):	Skrypty startowe do uruchamiania PA jako usługi systemowej
Group:		Daemons
Requires(post,preun):	/sbin/chkconfig
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires(pre):	fileutils
Requires:	%{name} = %{version}-%{release}
Provides:	group(pulse)
Provides:	group(pulse-access)
Provides:	user(pulse)
Obsoletes:	pulseaudio-standalone
Conflicts:	pulseaudio < 0.9.21-5

%description server
Init scripts to run PA as system-wide daemon.

You don't want it, if you're not making an embedded system.

%description server -l pl.UTF-8
Skrypty startowe do uruchamiania PA jako usługi systemowej.

Nie chcesz tego o ile nie robisz systemu wbudowanego.

%package qt
Summary:	Qt-based utilities for PulseAudio (equalizer)
Summary(pl.UTF-8):	Oparte na Qt narzędzia do PulseAudio (equalizer)
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}
Requires:	python-PyQt4
Requires:	python-dbus
Requires:	python-sip

%description qt
Qt-based utilities for PulseAudio (currently just qpaeq - an
equalizer).

%description qt -l pl.UTF-8
Oparte na Qt narzędzia do PulseAudio (obecnie tylko qpaeq -
equalizer).

%package libs
Summary:	PulseAudio libraries
Summary(pl.UTF-8):	Biblioteki PulseAudio
Group:		Libraries
Requires:	dbus-libs >= 1.4.12
Requires:	glib2 >= 1:2.4.0
Requires:	json-c >= 0.9
Requires:	libasyncns >= 0.1
Requires:	libltdl >= 2:2.4
Requires:	libsamplerate >= 0.1.0
Requires:	libsndfile >= 1.0.20
Requires:	libxcb >= 1.6
Requires:	orc >= 0.4.11
Requires:	speex >= 1:1.2-beta3
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

%package -n vala-libpulse
Summary:	PulseAudio API for Vala language
Summary(pl.UTF-8):	API PulseAudio dla języka Vala
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description -n vala-libpulse
PulseAudio API for Vala language.

%description -n vala-libpulse -l pl.UTF-8
API PulseAudio dla języka Vala.

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
Requires:	alsa-lib >= 1.0.24
Obsoletes:	polypaudio-alsa

%description alsa
ALSA modules for PulseAudio.

%description alsa -l pl.UTF-8
Moduły ALSA dla PulseAudio.

%package -n udev-pulseaudio-alsa
Summary:	UDEV rules for PulseAudio ALSA mixer
Summary(pl.UTF-8):	Reguły UDEV dla miksera ALSA systemu PulseAudio
Group:		Applications/Sound
Requires:	%{name}-alsa = %{version}-%{release}
Requires:	udev-core >= 1:143

%description -n udev-pulseaudio-alsa
UDEV rules for PulseAudio ALSA mixer. They help to choose profile
depending on hardware.

%description -n udev-pulseaudio-alsa -l pl.UTF-8
Reguły UDEV dla miksera ALSA systemu PulseAudio. Pomagają wybrać
profil w zależności od sprzętu.

%package bluetooth
Summary:	Bluetooth module for PulseAudio
Summary(pl.UTF-8):	Moduł Bluetooth dla PulseAudio
License:	GPL v2+
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	bluez-libs >= 4.99
Requires:	sbc >= 1.0

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
Suggests:	gnome-media-volume-control

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
Requires:	jack-audio-connection-kit >= 0.117.0
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

%package xen
Summary:	Xen paravirtualized driver for PulseAudio
Summary(pl.UTF-8):	Sterownik parawirtualny Xen dla PulseAudio
License:	LGPL v2.1+
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description xen
Xen paravirtualized driver for PulseAudio.

%description xen -l pl.UTF-8
Sterownik parawirtualny Xen dla PulseAudio.

%package -n bash-completion-pulseaudio
Summary:	Bash completion for PulseAudio commands
Summary(pl.UTF-8):	Bashowe uzupełnianie parametrów dla poleceń PulseAudio
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	bash-completion

%description -n bash-completion-pulseaudio
Bash completion for PulseAudio commands.

%description -n bash-completion-pulseaudio -l pl.UTF-8
Bashowe uzupełnianie parametrów dla poleceń PulseAudio.

%package -n zsh-completion-pulseaudio
Summary:	zsh completion for PulseAudio commands
Summary(pl.UTF-8):	Uzupełnianie parametrów w zsh dla poleceń PulseAudio
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}

%description -n zsh-completion-pulseaudio
zsh completion for PulseAudio commands.

%description -n zsh-completion-pulseaudio -l pl.UTF-8
Uzupełnianie parametrów w zsh dla poleceń PulseAudio.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%{__sed} -i -e '1s,#!/usr/bin/env python,#!/usr/bin/python,' src/utils/qpaeq

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-hal-compat \
	%{!?with_lirc:--disable-lirc} \
	--disable-silent-rules \
	%{!?with_xen:--disable-xen} \
	--enable-static%{!?with_static_libs:=no} \
	--enable-webrtc-aec \
	--with-database=%{?with_gdbm:gdbm}%{!?with_gdbm:simple} \
	--with-access-group=pulse-access \
	--with-system-user=pulse \
	--with-system-group=pulse
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/var/run/pulse \
	$RPM_BUILD_ROOT%{systemdtmpfilesdir} \
	$RPM_BUILD_ROOT%{zshdir}

# libsocket-util.so and libipacl.so are relinked before libpulsecore.so
# so __make -jN install leads to "File not found by glob" (or they links
# with libpulsecore installed on builder)
%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

ln -sf %{_bindir}/esdcompat $RPM_BUILD_ROOT%{_bindir}/esd

# pkgconfig files exist, assume them sufficient
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/%{name}/*.la
# .la for libpulsedsp and modules are killed in am install-exec-hook

install -Dp %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/%{name}
install -Dp %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/%{name}

cp -p %{SOURCE3} $RPM_BUILD_ROOT%{systemdtmpfilesdir}/%{name}.conf

install -m644 shell-completion/pulseaudio-zsh-completion.zsh $RPM_BUILD_ROOT%{zshdir}/_pulseaudio

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

%triggerpostun -- pulseaudio < 2.0-2
%{__sed} -i -e 's/load-module module-cork-music-on-phone/load-module module-role-cork/' %{_sysconfdir}/pulse/default.pa || :

%triggerpostun -- pulseaudio < 0.9.21-4
%groupremove pulse-rt

%pre server
%groupadd -g 226 pulse
%groupadd -g 228 pulse-access
%useradd -u 226 -g 226 -d /var/run/pulse -s /bin/false -c "Pulseaudio user" pulse

%post server
/sbin/chkconfig --add %{name}
%service %{name} restart

%preun server
if [ "$1" = "0" ]; then
	%service -q %{name} stop
	/sbin/chkconfig --del %{name}
fi

%postun server
if [ "$1" = "0" ]; then
	%userremove pulse
	%groupremove pulse-access
	%groupremove pulse
fi

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%triggerpostun libs -- polypaudio-libs
if [ -f %{_sysconfdir}/polypaudio/client.conf.rpmsave ]; then
	mv -f %{_sysconfdir}/pulse/client.conf %{_sysconfdir}/pulse/client.conf.rpmnew
	mv -f %{_sysconfdir}/polypaudio/client.conf.rpmsave %{_sysconfdir}/pulse/client.conf
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc LICENSE README
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/pulse/daemon.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/pulse/default.pa
%{_sysconfdir}/xdg/autostart/pulseaudio.desktop
%{_sysconfdir}/xdg/autostart/pulseaudio-kde.desktop
%attr(755,root,root) %{_bindir}/pacat
%attr(755,root,root) %{_bindir}/pacmd
%attr(755,root,root) %{_bindir}/pactl
%attr(755,root,root) %{_bindir}/padsp
%attr(755,root,root) %{_bindir}/pamon
%attr(755,root,root) %{_bindir}/paplay
%attr(755,root,root) %{_bindir}/parec
%attr(755,root,root) %{_bindir}/parecord
%attr(755,root,root) %{_bindir}/pasuspender
%attr(755,root,root) %{_bindir}/pax11publish
%attr(755,root,root) %{_bindir}/pulseaudio
%attr(755,root,root) %{_bindir}/start-pulseaudio-kde
%attr(755,root,root) %{_bindir}/start-pulseaudio-x11
%dir %{_libdir}/pulse
%dir %{_libdir}/pulse-*
%dir %{_libdir}/pulse-*/modules
%attr(755,root,root) %{_libdir}/pulse-*/modules/libavahi-wrap.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/libcli.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/liboss-util.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/libprotocol-cli.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/libprotocol-esound.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/libprotocol-http.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/libprotocol-native.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/libprotocol-simple.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/libraop.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/librtp.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/libwebrtc-util.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-always-sink.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-augment-properties.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-card-restore.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-cli-protocol-tcp.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-cli-protocol-unix.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-cli.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-combine-sink.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-combine.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-console-kit.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-dbus-protocol.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-default-device-restore.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-detect.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-device-manager.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-device-restore.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-echo-cancel.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-equalizer-sink.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-esound-compat-spawnfd.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-esound-compat-spawnpid.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-esound-protocol-tcp.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-esound-protocol-unix.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-esound-sink.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-filter-apply.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-filter-heuristics.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-http-protocol-tcp.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-http-protocol-unix.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-intended-roles.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-ladspa-sink.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-loopback.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-match.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-mmkbd-evdev.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-native-protocol-fd.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-native-protocol-tcp.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-native-protocol-unix.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-null-sink.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-null-source.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-oss.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-pipe-sink.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-pipe-source.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-position-event-sounds.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-raop-discover.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-raop-sink.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-remap-sink.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-remap-source.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-rescue-streams.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-role-cork.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-role-ducking.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-rtp-recv.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-rtp-send.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-rygel-media-server.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-simple-protocol-tcp.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-simple-protocol-unix.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-sine-source.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-sine.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-stream-restore.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-suspend-on-idle.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-switch-on-connect.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-switch-on-port-available.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-systemd-login.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-tunnel-sink.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-tunnel-sink-new.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-tunnel-source.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-tunnel-source-new.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-udev-detect.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-virtual-sink.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-virtual-source.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-virtual-surround-sink.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-volume-restore.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-x11-bell.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-x11-cork-request.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-x11-publish.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-x11-xsmp.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-zeroconf-discover.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-zeroconf-publish.so
%{_mandir}/man1/pacat.1*
%{_mandir}/man1/pacmd.1*
%{_mandir}/man1/pactl.1*
%{_mandir}/man1/padsp.1*
%{_mandir}/man1/paplay.1*
%{_mandir}/man1/pasuspender.1*
%{_mandir}/man1/pax11publish.1*
%{_mandir}/man1/pulseaudio.1*
%{_mandir}/man1/start-pulseaudio-kde.1*
%{_mandir}/man1/start-pulseaudio-x11.1*
%{_mandir}/man5/default.pa.5*
%{_mandir}/man5/pulse-cli-syntax.5*
%{_mandir}/man5/pulse-client.conf.5*
%{_mandir}/man5/pulse-daemon.conf.5*

%files server
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/pulse/system.pa
%attr(754,root,root) /etc/rc.d/init.d/%{name}
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}
%dir %attr(750,pulse,pulse-access) /var/run/pulse
%{systemdtmpfilesdir}/%{name}.conf
/etc/dbus-1/system.d/pulseaudio-system.conf

%files qt
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qpaeq

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpulse.so.*.*.*
%attr(755,root,root) %{_libdir}/libpulse-mainloop-glib.so.*.*.*
%attr(755,root,root) %{_libdir}/libpulse-simple.so.*.*.*
%attr(755,root,root) %{_libdir}/libpulsecore-%{version}.so
%attr(755,root,root) %ghost %{_libdir}/libpulse.so.0
%attr(755,root,root) %ghost %{_libdir}/libpulse-mainloop-glib.so.0
%attr(755,root,root) %ghost %{_libdir}/libpulse-simple.so.0
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/libpulsedsp.so
%attr(755,root,root) %{_libdir}/%{name}/libpulsecommon-%{version}.so
%dir %{_sysconfdir}/pulse
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/pulse/client.conf
%dir %{_datadir}/pulseaudio

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpulse.so
%attr(755,root,root) %{_libdir}/libpulse-mainloop-glib.so
%attr(755,root,root) %{_libdir}/libpulse-simple.so
%{_includedir}/pulse
%{_pkgconfigdir}/libpulse.pc
%{_pkgconfigdir}/libpulse-mainloop-glib.pc
%{_pkgconfigdir}/libpulse-simple.pc
%{_libdir}/cmake/PulseAudio

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libpulse.a
%{_libdir}/libpulse-mainloop-glib.a
%{_libdir}/libpulse-simple.a
%{_libdir}/libpulsecommon-%{version}.a
%{_libdir}/libpulsecore-%{version}.a
%endif

%files -n vala-libpulse
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/libpulse.deps
%{_datadir}/vala/vapi/libpulse.vapi
%{_datadir}/vala/vapi/libpulse-mainloop-glib.deps
%{_datadir}/vala/vapi/libpulse-mainloop-glib.vapi

%files esound-compat
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/esd
%attr(755,root,root) %{_bindir}/esdcompat
%{_mandir}/man1/esdcompat.1*

%files alsa
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pulse-*/modules/libalsa-util.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-alsa-card.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-alsa-sink.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-alsa-source.so
%dir %{_datadir}/pulseaudio/alsa-mixer
%dir %{_datadir}/pulseaudio/alsa-mixer/paths
%{_datadir}/pulseaudio/alsa-mixer/paths/*.common
%{_datadir}/pulseaudio/alsa-mixer/paths/*.conf
%dir %{_datadir}/pulseaudio/alsa-mixer/profile-sets
%{_datadir}/pulseaudio/alsa-mixer/profile-sets/*.conf

%files -n udev-pulseaudio-alsa
%defattr(644,root,root,755)
/lib/udev/rules.d/90-pulseaudio.rules

%files bluetooth
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pulse-*/modules/libbluez4-util.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/libbluez5-util.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-bluetooth-discover.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-bluetooth-policy.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-bluez4-device.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-bluez4-discover.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-bluez5-device.so
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-bluez5-discover.so

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
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-jackdbus-detect.so

%if %{with lirc}
%files lirc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-lirc.so
%endif

%if %{with xen}
%files xen
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pulse-*/modules/module-xenpv-sink.so
%endif

%files -n bash-completion-pulseaudio
%defattr(644,root,root,755)
/etc/bash_completion.d/pulseaudio-bash-completion.sh

%files -n zsh-completion-pulseaudio
%defattr(644,root,root,755)
%{zshdir}/_pulseaudio
