%define		_disable_ld_no_undefined	1

Name:		ggobi
Version:	2.1.9
Release:	3
License:	Common Public License
Group:		Graphics
Summary:	Interactive and dynamic graphics
URL:		http://www.ggobi.org
Source0:	http://www.ggobi.org/downloads/%{name}-%{version}.tar.bz2
Source1:	ggobi.desktop
BuildRequires:  desktop-file-utils
BuildRequires:	gtk2-devel     
BuildRequires:  libxml2-devel
BuildRequires:	libtool-devel
Patch0:		ggobi-2.1.9-format.patch
Patch1:		ggobi-2.1.9-underlink.patch
Patch2:		ggobi-2.1.9-graphviz.patch

%description
GGobi is an open source visualization program for exploring high-dimensional
data. It provides highly dynamic and interactive graphics such as tours,
as well as familiar graphics such as the scatterplot, barchart and parallel
coordinates plots. Plots are interactive and linked with brushing and
identification.

GGobi is fully documented in the GGobi book:
"Interactive and Dynamic Graphics for Data Analysis".

%files
%doc ABOUT-NLS AUTHORS ChangeLog COPYING CPLicense.txt INSTALL README
%{_bindir}/ggobi
%{_datadir}/pixmaps/ggobi.png
%{_datadir}/applications/*.desktop
%{_datadir}/%{name}
%{_libdir}/*.so.0*
%{_sysconfdir}/xdg/%{name}

#-----------------------------------------------------------------------
%package	devel
Summary:	Open source visualization for exploring high-dimensional data
Group:		Development/C
Requires:	%{name} = %{EVRD}

%description	devel
GGobi development files.

%files		devel
%{_includedir}/ggobi
%{_libdir}/*.so
%{_libdir}/pkgconfig/ggobi.pc

#-----------------------------------------------------------------------
%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

#-----------------------------------------------------------------------
%build
%configure2_5x --with-all-plugins --disable-rpath

#-----------------------------------------------------------------------
%install
%makeinstall_std
make ggobirc
mkdir -p %{buildroot}%{_datadir}/pixmaps

desktop-file-install					\
    --vendor mandriva					\
    --dir %{buildroot}%{_datadir}/applications		\
    %{SOURCE1}


%changelog
* Mon Feb 20 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.1.9-2
+ Revision: 777694
- Rebuild with proper dependency generation.

* Mon Feb 20 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.1.9-1
+ Revision: 777666
- Import ggobi (partly based on fedora ggobi package)
- Import ggobi

