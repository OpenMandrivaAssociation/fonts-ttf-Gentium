%define pkgname		Gentium
%define name		fonts-ttf-%{pkgname}
%define version		1.02
%define release		6

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
BuildRequires: fontconfig
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

%files
%defattr(-,root,root)
%doc *.txt
%dir %{_datadir}/fonts/TTF/%{pkgname}
%{_datadir}/fonts/TTF/%{pkgname}/*.TTF
%verify(not mtime) %{_datadir}/fonts/TTF/%{pkgname}/fonts.dir
%{_datadir}/fonts/TTF/%{pkgname}/fonts.scale
%{_sysconfdir}/X11/fontpath.d/ttf-%{pkgname}:pri=50


%changelog
* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 1.02-5mdv2011.0
+ Revision: 675547
- br fontconfig for fc-query used in new rpm-setup-build

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.02-4mdv2011.0
+ Revision: 610729
- rebuild

* Wed Jan 20 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.02-3mdv2010.1
+ Revision: 494141
- fc-cache is now called by an rpm filetrigger

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 1.02-2mdv2010.0
+ Revision: 437571
- rebuild

* Tue Nov 11 2008 Lev Givon <lev@mandriva.org> 1.02-1mdv2009.1
+ Revision: 302290
- import fonts-ttf-Gentium


