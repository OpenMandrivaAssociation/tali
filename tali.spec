%define url_ver	%(echo %{version}|cut -d. -f1,2)
%define _disable_rebuild_configure 1

Name:		tali
Version:	3.22.0
Release:	1
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
%configure
%make

%install
%makeinstall_std

%find_lang %{name} --all-name --with-gnome

%files -f %{name}.lang
%doc COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.%{name}.gschema.xml
%{_iconsdir}/*/*/apps/%{name}*
%{_datadir}/%{name}
%{_mandir}/man6/%{name}.6*
%{_datadir}/appdata/%{name}.appdata.xml

