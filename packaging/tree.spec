#

Name:           tree
Version:        1.6.0
Release:        1
License:        GPL-2.0+
Summary:        File listing as a tree
Url:            http://mama.indstate.edu/users/ice/tree/
Group:          System/Tools
Source0:        %{name}-%{version}.tar.bz2

%description
Tree is a recursive directory listing command that produces a depth
indented listing of files, which is colorized ala dircolors if the
LS_COLORS environment variable is set and output is to tty.

%prep
%setup -q

%build
make OPTFLAGS="%{optflags}" CC="gcc"

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
install -m 644 doc/%{name}.1 %{buildroot}%{_mandir}/man1
install -m 755 %{name} %{buildroot}%{_bindir}

%files
%defattr(-,root,root)
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz

%changelog
