Summary:	Modular sound server
Summary(pl):	Modularny serwer d¼wiêku
Name:		polypaudio
Version:	0.7
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://0pointer.de/lennart/projects/polypaudio/%{name}-%{version}.tar.gz
# Source0-md5:	1c3693ab9c6904dbed6dfa7656778de4
Patch0:		%{name}-suid.patch
URL:		http://0pointer.de/lennart/projects/polypaudio/
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel
BuildRequires:	libsamplerate-devel >= 0.1.0
BuildRequires:	libsndfile-devel
BuildRequires:	libwrap-devel
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

%package devel
Summary:	Development files for polypaudio
Summary(pl):	Pliki programistyczne polyaudio
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development files for polypaudio.

%description devel -l pl
Pliki programistyczne polyaudio.

%prep
%setup -q 
%patch0 -p1

%build
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
%doc README
%dir /etc/polypaudio
%config(noreplace) %verify(not md5 mtime size) /etc/polypaudio/daemon.conf
%config(noreplace) %verify(not md5 mtime size) /etc/polypaudio/default.pa
%config(noreplace) %verify(not md5 mtime size) /etc/polypaudio/client.conf
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so.*
%dir %{_libdir}/%{name}-%{version}
%attr(755,root,root) %{_libdir}/%{name}-%{version}/*.so
%{_libdir}/%{name}-%{version}/*.la

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_includedir}/polyp
%{_pkgconfigdir}/*
