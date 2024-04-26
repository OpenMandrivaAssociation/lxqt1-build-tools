%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	Various packaging tools and scripts for LXQt 1.x applications
Name:		lxqt1-build-tools
Version:	0.13.0
Release:	1
License:	BSD
Group:		System/Libraries
Url:		http://lxqt.org/
Source0:	https://github.com/lxqt/lxqt-build-tools/releases/download/%{version}/lxqt-build-tools-%{version}.tar.xz
BuildRequires:	ninja
BuildRequires:	cmake
BuildRequires:	qmake5
BuildRequires:	cmake(Qt5Core)
BuildRequires:	git-core
BuildRequires:	pkgconfig(glib-2.0)

%description
Various packaging tools and scripts for LXQt applications.

%prep
%autosetup -p1 -n lxqt-build-tools-%{version}

%cmake_qt5 -DLXQT_ETC_XDG_DIR="%{_sysconfdir}/xdg" -G Ninja

%build
# Need to be in a UTF-8 locale so grep (used by the desktop file
# translation generator) doesn't scream about translations containing
# "binary" (non-ascii) characters
export LANG=en_US.utf-8
export LC_ALL=en_US.utf-8
%ninja -C build

%install
# Need to be in a UTF-8 locale so grep (used by the desktop file
# translation generator) doesn't scream about translations containing
# "binary" (non-ascii) characters
export LANG=en_US.utf-8
export LC_ALL=en_US.utf-8
%ninja_install -C build

%files
%doc README.md
%{_bindir}/lxqt-transupdate
%{_datadir}/cmake/lxqt-build-tools
