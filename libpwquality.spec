Summary:	Library for password quality checking and generating random passwords
Name:		libpwquality
Version:	1.2.2
Release:	1
License:	BSD
Group:		Libraries
Source0:	https://fedorahosted.org/releases/l/i/libpwquality/%{name}-%{version}.tar.bz2
# Source0-md5:	2105bb893791fe27efc20441e617f385
URL:		https://fedorahosted.org/libpwquality/
BuildRequires:	cracklib-devel
BuildRequires:	gettext-devel
BuildRequires:	pam-devel
BuildRequires:	pkg-config
BuildRequires:	python-devel
Requires:	pam
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libpwquality is a library for password quality checks and generation
of random passwords that pass the checks. This library uses the
cracklib and cracklib dictionaries to perform some of the checks.

%package devel
Summary:	Header files for libpwquality library
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Header files for libpwquality library.

%package -n python-pwquality
Summary:	Python bindings for the libpwquality library
Group:		Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description -n python-pwquality
Python bindings for the libpwquality library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/security/pam_pwquality.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README NEWS AUTHORS
%attr(755,root,root) %{_bindir}/pwmake
%attr(755,root,root) %{_bindir}/pwscore
%attr(755,root,root) %ghost %{_libdir}/libpwquality.so.1
%attr(755,root,root) %{_libdir}/libpwquality.so.*.*.*
%attr(755,root,root) %{_libdir}/security/pam_pwquality.so
%config(noreplace) %verify(not md5 mtime size) /etc/security/pwquality.conf
%{_mandir}/man1/pwmake.1*
%{_mandir}/man1/pwscore.1*
%{_mandir}/man5/pwquality.conf.5*
%{_mandir}/man8/pam_pwquality.8*

%files devel
%defattr(644,root,root,755)
%{_includedir}/pwquality.h
%{_libdir}/libpwquality.so
%{_libdir}/libpwquality.la
%{_pkgconfigdir}/pwquality.pc

%files -n python-pwquality
%defattr(644,root,root,755)
%{py_sitedir}/pwquality.so

