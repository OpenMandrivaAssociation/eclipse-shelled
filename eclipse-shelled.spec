%define eclipse_base     %{_libdir}/eclipse

Summary:          Eclipse Shell script editor
Name:             eclipse-shelled
Version:          1.0.3
Release:          %mkrel 3.0.3
License:          Common Public License
URL:              http://sourceforge.net/projects/shelled
Group:            Development/Other
Source0:          shelled-1.0.3.tar.lzma
Requires:         eclipse-platform >= 1:3.2.1
Requires:         git-core
BuildRequires:    eclipse-pde
BuildRequires:    java-rpmbuild >= 0:1.5
BuildRequires:    zip
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
%{eclipse_base}/buildscripts/pdebuild -f com.something.eclipse.shelled \
  -a "-DjavacTarget=1.5 -DjavacSource=1.5"

%install
rm -rf $RPM_BUILD_ROOT
installDir=${RPM_BUILD_ROOT}/%{_datadir}/eclipse/dropins/shelled
install -d -m755 $installDir

# shelled main feature
unzip -q -d $installDir \
            build/rpmBuild/com.something.eclipse.shelled.zip

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0644,root,root,0755)
%{_datadir}/eclipse/dropins/shelled 