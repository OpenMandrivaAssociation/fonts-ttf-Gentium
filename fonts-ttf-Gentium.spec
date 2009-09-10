%define pkgname		Gentium
%define name		fonts-ttf-%{pkgname}
%define version		1.02
%define release		%mkrel 2

Summary:		Free multilingual Truetype fonts
Name:			%{name}
Version:		%{version}
Release:		%{release}
Source0:		%{pkgname}_102_W.zip
License:		OFL
Group:			System/Fonts/True type
Url:			http://scripts.sil.org/%{pkgname}
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:		noarch
BuildRequires:		freetype-tools, dos2unix

%description
Gentium is a typeface family designed to enable the diverse ethnic
groups around the world who use the Latin and Greek scripts to produce
readable, high-quality publications. It supports a wide range of
Latin-based alphabets and includes glyphs that correspond to all the
Latin ranges of Unicode.

The design is intended to be highly readable, reasonably compact, and
visually attractive. The additional 'extended' Latin letters are
designed to naturally harmonize with the traditional 26
ones. Diacritics are treated with careful thought and attention to
their use. Gentium also supports both polytonic and monotonic Greek,
including a number of alternate forms. Expansion of the character set
to include more extended Latin glyphs (Unicode 5.1), archaic Greek
symbols, and full Cyrillic script support is underway and will be
released in 2008.

%prep
%setup -q -n %{pkgname}102

%install
%__rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/fonts/TTF/%{pkgname}

install -m 644 *.TTF %{buildroot}%{_datadir}/fonts/TTF/%{pkgname}
ttmkfdir %{buildroot}/%{_datadir}/fonts/TTF/%{pkgname}  > %{buildroot}%{_datadir}/fonts/TTF/%{pkgname}/fonts.dir
ln -s fonts.dir %{buildroot}%{_datadir}/fonts/TTF/%{pkgname}/fonts.scale

mkdir -p %{buildroot}%_sysconfdir/X11/fontpath.d/
ln -s ../../..%_datadir/fonts/TTF/%{pkgname} \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-%{pkgname}:pri=50

dos2unix README.txt

%clean
%__rm -rf %{buildroot}

%post
[ -x %{_bindir}/fc-cache ] && %{_bindir}/fc-cache 

%postun
if [ "$1" = "0" ]; then
  [ -x %{_bindir}/fc-cache ] && %{_bindir}/fc-cache 
fi

%files
%defattr(-,root,root)
%doc *.txt
%dir %{_datadir}/fonts/TTF/%{pkgname}
%{_datadir}/fonts/TTF/%{pkgname}/*.TTF
%verify(not mtime) %{_datadir}/fonts/TTF/%{pkgname}/fonts.dir
%{_datadir}/fonts/TTF/%{pkgname}/fonts.scale
%{_sysconfdir}/X11/fontpath.d/ttf-%{pkgname}:pri=50
