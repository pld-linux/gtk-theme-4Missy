Summary:	Theme based of QNX-Photon for GTK
Summary(pl):	Temat bazuj±cy na QNX-Photon dla GTK
Name:		4Missy
Version:	1.2
Release:	1
License:	GPL
Group:		Themes/Gtk
Source0:	http://debian.attica.net.nz/themes.org/gtk/%{name}-%{version}.tar.gz
URL:		http://debian.attica.net.nz/themes.org/gtk/
Requires:	gtk-engines
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_x11datadir	/usr/X11R6/share

%description
Theme based of QNX-Photon for GTK.

%description -l pl
Temat bazuj±cy QNX-Photon dla GTK.

%prep
%setup  -q -n %{name}

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
