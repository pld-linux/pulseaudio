%bcond_without  broken_rpm # dont BC packages because of logic error in Ac
Summary:	Modular sound server
Summary(pl):	Modularny serwer d¼wiêku
Name:		polypaudio
Version:	0.7
Release:	4
License:	LGPL
Group:		Libraries
Source0:	http://0pointer.de/lennart/projects/polypaudio/%{name}-%{version}.tar.gz
# Source0-md5:	1c3693ab9c6904dbed6dfa7656778de4
Patch0:		%{name}-suid.patch
URL:		http://0pointer.de/lennart/projects/polypaudio/
BuildRequires:	XFree86-devel
BuildRequires:	alsa-lib-devel >= 1.0.0
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.4.0
BuildRequires:	libcap-devel
BuildRequires:	libltdl-devel
BuildRequires:	libtool
BuildRequires:	libsamplerate-devel >= 0.1.0
BuildRequires:	libsndfile-devel >= 1.0.10
BuildRequires:	libwrap-devel
BuildRequires:	lynx
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
Requires:	glib2 >= 1:2.4.0
Requires:	libsamplerate >= 0.1.0
Requires:	libsndfile >= 1.0.10
Obsoletes:	polypaudio < 0.7-4
%if %{with broken_rpm}
BuildConflicts:	polypaudio < 0.7-4
%endif
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

%description
Libraries for polypaudio.

%description libs -l pl
Biblioteki dla polypaudio.

%package devel
Summary:	Development files for polypaudio
Summary(pl):	Pliki programistyczne polyaudio
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	XFree86-devel
Requires:	glib2-devel >= 1:2.4.0

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
BuildRequires:	alsa-lib >= 1.0.0

%description alsa
ALSA modules for polypaudio.

%description alsa -l pl
Modu³y ALSA dla polypaudio.

%prep
%setup -q
%patch0 -p1

# glib2 version should be sufficient
sed -i -e 's/HAVE_GLIB12=1/HAVE_GLIB12=0/' configure.ac

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# *.la are needed (libltdl is used)
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}-%{version}/*.a

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%dir %{_sysconfdir}/polypaudio
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/polypaudio/daemon.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/polypaudio/default.pa
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/polypaudio/client.conf
%attr(755,root,root) %{_bindir}/*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*-*.so.*.*.*
%dir %{_libdir}/%{name}-%{version}
%attr(755,root,root) %{_libdir}/%{name}-%{version}/*.so
%{_libdir}/%{name}-%{version}/*.la
%exclude %{_libdir}/%{name}-%{version}/libalsa-util.*
%exclude %{_libdir}/%{name}-%{version}/module-alsa-sink.*
%exclude %{_libdir}/%{name}-%{version}/module-alsa-source.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*-*.so
%{_libdir}/lib*-*.la
%{_includedir}/polyp
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*-*.a

%files alsa
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}-%{version}/libalsa-util.so
%attr(755,root,root) %{_libdir}/%{name}-%{version}/module-alsa-sink.so
%attr(755,root,root) %{_libdir}/%{name}-%{version}/module-alsa-source.so
%{_libdir}/%{name}-%{version}/libalsa-util.la
%{_libdir}/%{name}-%{version}/module-alsa-sink.la
%{_libdir}/%{name}-%{version}/module-alsa-source.la
