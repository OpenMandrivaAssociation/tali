%define url_ver	%(echo %{version}|cut -d. -f1,2)
%define _disable_rebuild_configure 1

Name:		tali
Version:	40.2
Release:	1
Summary:	GNOME Tali game
License:	GPLv2+ and GFDL
Group:		Games/Cards
URL:		https://wiki.gnome.org/Tali
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:  pkgconfig(libgnome-games-support-1)
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.4.0
BuildRequires:	pkgconfig(librsvg-2.0) >= 2.32.0
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	libxml2-utils
BuildRequires:  meson
BuildRequires:  cmake
Obsoletes:	gtali
# For help
Requires:	yelp

%description
Sort of poker with dice and less money. An ancient Roman game.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name} --all-name --with-gnome

%files -f %{name}.lang
%doc COPYING
%{_bindir}/%{name}
%{_datadir}/applications/org.gnome.Tali.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.Tali.gschema.xml
%{_iconsdir}/*/*/apps/org.gnome.Tali*
%{_datadir}/%{name}
%{_mandir}/man6/%{name}.6*
%{_datadir}/metainfo/org.gnome.Tali.appdata.xml
