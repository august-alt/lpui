%define _unpackaged_files_terminate_build 1

Name: lpui
Version: 0.1.0
Release: alt1

Summary: Local group policy editor
License: GPLv2+
Group: Other
Url: https://github.com/august-alt/lpui

BuildRequires(pre): rpm-build-python3

Requires: admx-basealt gpui

Source0: %name-%version.tar

%description
Local group policy editor

%prep
%setup -q

%install
mkdir -p %buildroot%_bindir
install -T -m 755 lpui.py %buildroot%_bindir/lpui

%files
%doc README.md
%_bindir/lpui

%changelog
* Wed Jun 08 2022 Vladimir Rubanov <august@altlinux.org> 0.1.0-alt1
- Initial build