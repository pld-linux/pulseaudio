Summary:	Modular sound server
Name:		polypaudio
Version:	0.7
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://0pointer.de/lennart/projects/polypaudio/%{name}-%{version}.tar.gz
# Source0-md5:	1c3693ab9c6904dbed6dfa7656778de4
Patch0:	%{name}-suid.patch
URL:		http://0pointer.de/lennart/projects/polypaudio/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	libsamplerate-devel >= 0.1.0
BuildRequires:	libsndfile-devel
BuildRequires:	libwrap-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
polypaudio is a sound server for Linux and other Unix like operating systems. It is intended to be an improved drop-in replacement for the Enlightened Sound Daemon (ESOUND). It is my ultimate ambition to get Polypaudio into Gnome as a replacement for ESOUND. In addition to the features ESOUND provides polypaudio has:

%package devel
Summary:	devel files for polypaudio
Group:	Development/Libraries

%description devel
devel files for polypaudio.

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
# create directories if necessary
#install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir /etc/polypaudio
%config /etc/polypaudio/daemon.conf
%config /etc/polypaudio/default.pa
%config /etc/polypaudio/client.conf
%attr(755,root,root) %{_bindir}/*
%{_includedir}/polyp
%attr(755,root,root) %{_libdir}/*.so.*
%dir %{_libdir}/%{name}-%{version}
%{_libdir}/%{name}-%{version}/*.la
%attr(755,root,root) %{_libdir}/%{name}-%{version}/*.so

%files devel
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/pkgconfig/*
