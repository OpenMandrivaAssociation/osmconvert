# To update the sources use the createsrc_archive.sh script.

Name:		osmconvert
Version:	0.8.11
Release:	3
Source0:	%{name}-%{version}.tar
Source1:	http://m.m.i24.cc/osmconvert.c
Summary:	Tool to convert and merge OpenStreetMap files
URL:		http://wiki.openstreetmap.org/wiki/Osmconvert
License:	AGPLv3
Group:		Sciences/Geosciences
BuildRequires:	pkgconfig(zlib)

%description
Tool to convert and merge OpenStreetMap files.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%{__cc} %{optflags} -o %{name} %{name}.c -lz

%install
mkdir -p %{buildroot}%{_bindir}
cp ./%{name} /%{buildroot}%{_bindir}

%files
%{_bindir}/osmconvert
