Name:    kf6-qqc2-breeze-style
Version: 6.2.0
Release: 0%{?dist}
Summary: QtQuickControls2 breeze style

License: CC0-1.0 and GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/plasma/%{name}

Source0:    %{name}-%{version}.tar.bz2

## upstream patches

BuildRequires: cmake
BuildRequires: clang
BuildRequires: kf6-extra-cmake-modules
BuildRequires: kf6-rpm-macros

BuildRequires: kf6-kcolorscheme-devel
BuildRequires: kf6-kconfig-devel
BuildRequires: kf6-kcoreaddons-devel
BuildRequires: kf6-kguiaddons-devel
BuildRequires: kf6-kiconthemes-devel
BuildRequires: kf6-kirigami-devel
BuildRequires: kf6-kquickcharts-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtdeclarative-devel

%description
This is a pure Qt Quick/Kirigami Qt Quick Controls style.

%prep
%autosetup -n %{name}-%{version}/upstream -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install


%files
%doc README.md
%license LICENSES/*.txt
%{_kf6_plugindir}/kirigami/platform/org.kde.breeze.so
%{_qt6_qmldir}/org/kde/breeze/
%{_kf6_libdir}/cmake/QQC2BreezeStyle/
