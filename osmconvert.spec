Name: osmconvert
Version:	0.8.11
Release: 1
Source0: http://m.m.i24.cc/osmconvert.c
Summary: Tool to convert and merge OpenStreetMap files
URL: http://wiki.openstreetmap.org/wiki/Osmconvert
License: AGPLv3
Group: Sciences/Geosciences
BuildRequires: pkgconfig(zlib)

%description
Tool to convert and merge OpenStreetMap files.

%prep

%build
%set_build_flags
mkdir -p %{buildroot}%{_bindir}
%{__cc} %{optflags} -o %{buildroot}%{_bindir}/osmconvert %{SOURCE0} -lz

%install

%files
%{_bindir}/osmconvert
