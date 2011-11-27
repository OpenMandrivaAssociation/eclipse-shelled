%define eclipse_base     %{_libdir}/eclipse
%define install_loc      %{_datadir}/eclipse/dropins/shelled

Summary:          Eclipse Shell script editor
Name:             eclipse-shelled
Version:          2.0.0
Release:          0.M3.1.3
License:          EPL
URL:              http://sourceforge.net/projects/shelled
Group:            Development/Java
Source0:          http://downloads.sourceforge.net/project/shelled/shelled/ShellEd%202.0.0%20M3/ShellEd-Sources-2.0.0_M3.zip
Requires:         eclipse-platform >= 1:3.4.0
Requires:         eclipse-dltk
Requires:         eclipse-manpage
BuildRequires:    eclipse-pde
BuildRequires:    eclipse-dltk
BuildRequires:    eclipse-manpage
BuildRequires:    java-devel >= 0:1.5
BuildArch:        noarch
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root

%description
ShellEd is a superb shell script editor for Eclipse. 
The great benefit of this plugin is the integration of man page information
 for content assist and text hover.

%prep
%setup -q -c

%build
# build the main shelled feature
%{eclipse_base}/buildscripts/pdebuild -d "dltk-core emf man"

%install
rm -rf $RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT%{install_loc}

# shelled main feature
unzip -q -d $RPM_BUILD_ROOT%{install_loc} \
            build/rpmBuild/net.sourceforge.shelled.zip
            
%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{install_loc}
#%doc net.sourceforge.shelled-feature/license.html
#%doc net.sourceforge.shelled-feature/epl-v10.html

