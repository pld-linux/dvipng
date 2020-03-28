Summary:	Convert DVI files to PNG
Summary(pl.UTF-8):	Konwersja plików DVI do PNG
Name:		dvipng
Version:	1.17
Release:	1
License:	LGPL v3
Group:		Applications/Graphics
Source0:	http://downloads.sourceforge.net/dvipng/%{name}-%{version}.tar.gz
# Source0-md5:	122fa97e4a8988eb33dda1fb75506b09
Patch0:		%{name}-info.patch
URL:		http://sourceforge.net/projects/dvipng/
BuildRequires:	freetype-devel >= 2.0.1
BuildRequires:	gd-devel >= 2.0.28
BuildRequires:	kpathsea-devel
BuildRequires:	libpng-devel
BuildRequires:	texinfo
BuildRequires:	zlib-devel
Requires:	freetype >= 2.0.1
Requires:	gd >= 2.0.28
Conflicts:	texlive
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program makes PNG graphics from DVI files as obtained from TeX
and its relatives.

It is intended to produce anti-aliased screen-resolution images as
fast as is possible. The target audience is people who need to
generate and regenerate many images again and again.

%description -l pl.UTF-8
Ten program tworzy obrazki PNG z plików DVI tworzonych przez TeXa i
pokrewne narzędzia.

Program ma służyć do tworzenia obrazków w rozdzielczości ekranu z
antyaliasingiem tak szybko, jak to tylko możliwe. Jest on przeznaczony
dla osób potrzebujących ciągle generować lub regenerować wiele
obrazków.

%prep
%setup -q -c
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc ChangeLog README RELEASE
%attr(755,root,root) %{_bindir}/dvigif
%attr(755,root,root) %{_bindir}/dvipng
%{_mandir}/man1/dvigif.1*
%{_mandir}/man1/dvipng.1*
%{_infodir}/dvipng.info*
