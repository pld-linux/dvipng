Summary:	-
Summary(pl):	-
Name:		dvipng
Version:	0.7
Release:	0.1
License:	GPL v2	
Group:		Applcations/Console
Source0:	http://dl.sourceforge.net/preview-latex/%{name}-%{version}.tar.gz
# Source0-md5:	00a8c39343d277f4d25878d6faf5689b
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.sourceforge.net/projects/preview-latex/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
foo

%description -l pl
shmoo

%prep
%setup -q
%patch0 -p1

%build
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
%doc README RELEASE
%attr(755,root,root) %{_bindir}/*
