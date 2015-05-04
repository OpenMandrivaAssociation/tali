%define url_ver	%(echo %{version}|cut -d. -f1,2)

Name:		tali
Version:	3.14.0
Release:	%mkrel 3
Summary:	GNOME Tali game
License:	GPLv2+ and GFDL
Group:		Games/Cards
URL:		https://wiki.gnome.org/Tali
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.4.0
BuildRequires:	pkgconfig(librsvg-2.0) >= 2.32.0
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	libxml2-utils
Obsoletes:	gtali
# For help
Requires:	yelp

%description
Sort of poker with dice and less money. An ancient Roman game.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%find_lang %{name} --all-name --with-gnome --with-help

%files -f %{name}.lang
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.%{name}.gschema.xml
%{_iconsdir}/*/*/apps/%{name}.*
%{_datadir}/%{name}
%{_mandir}/man6/%{name}.6*
%{_datadir}/appdata/%{name}.appdata.xml


%changelog
* Tue Feb 17 2015 wally <wally> 3.14.0-3.mga5
+ Revision: 815347
- require yelp for showing help

* Wed Oct 15 2014 umeabot <umeabot> 3.14.0-2.mga5
+ Revision: 748013
- Second Mageia 5 Mass Rebuild

* Sun Sep 28 2014 wally <wally> 3.14.0-1.mga5
+ Revision: 731384
- new version 3.14.0

* Tue Sep 16 2014 umeabot <umeabot> 3.13.92-2.mga5
+ Revision: 689685
- Mageia 5 Mass Rebuild

* Tue Sep 16 2014 ovitters <ovitters> 3.13.92-1.mga5
+ Revision: 676938
- new version 3.13.92

* Mon Sep 01 2014 ovitters <ovitters> 3.13.91-1.mga5
+ Revision: 670757
- new version 3.13.91

* Tue Aug 19 2014 ovitters <ovitters> 3.13.90-1.mga5
+ Revision: 665285
- new version 3.13.90

* Mon Jul 21 2014 ovitters <ovitters> 3.13.4-1.mga5
+ Revision: 655259
- new version 3.13.4

* Thu May 29 2014 ovitters <ovitters> 3.13.1-1.mga5
+ Revision: 627591
- new version 3.13.1

* Mon May 12 2014 ovitters <ovitters> 3.12.2-1.mga5
+ Revision: 622279
- new version 3.12.2

* Mon Apr 14 2014 ovitters <ovitters> 3.12.1-1.mga5
+ Revision: 614229
- new version 3.12.1

* Sun Mar 23 2014 ovitters <ovitters> 3.12.0-1.mga5
+ Revision: 606987
- new version 3.12.0

* Mon Mar 17 2014 ovitters <ovitters> 3.11.92-1.mga5
+ Revision: 604626
- new version 3.11.92

* Mon Mar 03 2014 ovitters <ovitters> 3.11.91-1.mga5
+ Revision: 599036
- new version 3.11.91

* Mon Feb 17 2014 ovitters <ovitters> 3.11.90-1.mga5
+ Revision: 593895
- new version 3.11.90

* Wed Feb 05 2014 dams <dams> 3.11.5-1.mga5
+ Revision: 582960
- new version 3.11.5

* Mon Nov 11 2013 ovitters <ovitters> 3.10.2-1.mga4
+ Revision: 550453
- new version 3.10.2

* Sat Nov 09 2013 ovitters <ovitters> 3.10.0-3.mga4
+ Revision: 550202
- fix url

* Sat Oct 19 2013 umeabot <umeabot> 3.10.0-2.mga4
+ Revision: 536486
- Mageia 4 Mass Rebuild

* Mon Sep 23 2013 ovitters <ovitters> 3.10.0-1.mga4
+ Revision: 484345
- new version 3.10.0

* Tue Sep 17 2013 ovitters <ovitters> 3.9.92-1.mga4
+ Revision: 480459
- new version 3.9.92

* Wed Aug 21 2013 fwang <fwang> 3.9.90-1.mga4
+ Revision: 468755
- new version 3.9.90
- cleanup spec

* Sun Jun 09 2013 dams <dams> 3.8.0-1.mga4
+ Revision: 440921
- imported package tali

