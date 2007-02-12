Summary:	Theme based of QNX-Photon for GTK+
Summary(pl.UTF-8):   Motyw bazujący na QNX-Photon dla GTK+
Name:		gtk-theme-4Missy
Version:	1.2
Release:	2
License:	GPL
Group:		Themes/GTK+
Source0:	http://download.freshmeat.net/themes/4missy/4missy-%{version}.tar.gz
# Source0-md5:	cc9a74a8ee3ef6db3bc09f536091df46
URL:		http://debian.attica.net.nz/themes.org/gtk/
Requires:	gtk-engines
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_x11datadir	/usr/X11R6/share

%description
Theme based of QNX-Photon for GTK+.

%description -l pl.UTF-8
Motyw bazujący QNX-Photon dla GTK+.

%prep
%setup -q -n 4Missy

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_x11datadir}/themes/%{name}/gtk

install gtk/gtkrc $RPM_BUILD_ROOT%{_x11datadir}/themes/%{name}
install gtk/* $RPM_BUILD_ROOT%{_x11datadir}/themes/%{name}/gtk

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_x11datadir}/themes/%{name}
