Summary:	Convert DVI files to PNG
Summary(pl):	Konwersja plików DVI do PNG
Name:		dvipng
Version:	1.2
Release:	1
License:	GPL v2
Group:		Applications/Console
Source0:	http://dl.sourceforge.net/dvipng/%{name}-%{version}.tar.gz
# Source0-md5:	3e6223f96d73b466ca433ca04918d886
Patch0:		%{name}-info.patch
URL:		http://www.sourceforge.net/projetcs/dvipng/
BuildRequires:	freetype-devel
BuildRequires:	gd-devel
BuildRequires:	kpathsea-devel
BuildRequires:	tetex-format-plain
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program makes PNG graphics from DVI files as obtained from TeX
and its relatives.

It is intended to produce anti-aliased screen-resolution images as
fast as is possible. The target audience is people who need to
generate and regenerate many images again and again.

%description -l pl
Ten program tworzy obrazki PNG z plików DVI tworzonych przez TeXa i
pokrewne narzêdzia.

Program ma s³u¿yæ do tworzenie obrazków w rozdzielczo¶ci ekranu z
antyaliasingiem tak szybko, jak to tylko mo¿liwe. Jest on dla ludzi
potrzebuj±cych ci±gle generowaæ lub regenerowaæ wiele obrazków.

%prep
%setup -q
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

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc README RELEASE
%{_infodir}/*.info*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
