#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : linuxptp
Version  : 2.0
Release  : 4
URL      : https://sourceforge.net/projects/linuxptp/files/v2.0/linuxptp-2.0.tgz
Source0  : https://sourceforge.net/projects/linuxptp/files/v2.0/linuxptp-2.0.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: linuxptp-bin = %{version}-%{release}
Requires: linuxptp-license = %{version}-%{release}
Requires: linuxptp-man = %{version}-%{release}
Patch1: 0001-Set-standard-Clear-Linux-installation-paths.patch

%description
* Introduction
This software is an implementation of the Precision Time Protocol
(PTP) according to IEEE standard 1588 for Linux. The dual design
goals are to provide a robust implementation of the standard and to
use the most relevant and modern Application Programming Interfaces
(API) offered by the Linux kernel. Supporting legacy APIs and other
platforms is not a goal.

%package bin
Summary: bin components for the linuxptp package.
Group: Binaries
Requires: linuxptp-license = %{version}-%{release}

%description bin
bin components for the linuxptp package.


%package license
Summary: license components for the linuxptp package.
Group: Default

%description license
license components for the linuxptp package.


%package man
Summary: man components for the linuxptp package.
Group: Default

%description man
man components for the linuxptp package.


%prep
%setup -q -n linuxptp-2.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1559769364
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1559769364
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/linuxptp
cp COPYING %{buildroot}/usr/share/package-licenses/linuxptp/COPYING
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/hwstamp_ctl
/usr/bin/nsm
/usr/bin/phc2sys
/usr/bin/phc_ctl
/usr/bin/pmc
/usr/bin/ptp4l
/usr/bin/timemaster

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/linuxptp/COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man8/hwstamp_ctl.8
/usr/share/man/man8/phc2sys.8
/usr/share/man/man8/phc_ctl.8
/usr/share/man/man8/pmc.8
/usr/share/man/man8/ptp4l.8
/usr/share/man/man8/timemaster.8
