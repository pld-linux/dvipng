Summary:	Convert DVI files to PNG
Summary(pl):	Konwersja plik�w DVI do PNG
Name:		dvipng
Version:	0.7
Release:	0.2
License:	GPL v2	
Group:		Applcations/Console
Source0:	http://dl.sourceforge.net/preview-latex/%{name}-%{version}.tar.gz
# Source0-md5:	00a8c39343d277f4d25878d6faf5689b
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.sourceforge.net/projects/preview-latex/
BuildRequires:	freetype-devel
BuildRequires:	gd-devel
BuildRequires:	kpathsea-devel
BuildRequires:	tetex-format-plain
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program makes PNG graphics from DVI files as obtained from TeX
and its relatives.

It is intended to produce anti-aliased screen-resolution images as
fast as is possible. The target audience is people who need to
generate and regenerate many images again and again. 

%description -l pl
Ten program tworzy obrazki PNG z plik�w DVI tworzonych przez TeXa i
pokrewne narz�dzia.

Program ma s�u�y� do tworzenie obrazk�w w rozdzielczo�ci ekranu z
antyaliasingiem tak szybko, jak to tylko mo�liwe. Jest on dla ludzi
potrzebuj�cych ci�gle generowa� lub regenerowa� wiele obrazk�w.

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

%files
%defattr(644,root,root,755)
%doc README RELEASE
%{_infodir}/*.info*
%attr(755,root,root) %{_bindir}/*
