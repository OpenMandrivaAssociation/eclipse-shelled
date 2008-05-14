%define eclipse_base     %{_datadir}/eclipse

Summary:          Eclipse Shell script editor
Name:             eclipse-shelled
Version:          1.0.3
Release:          %mkrel 0.0.2
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
install -d -m755 $RPM_BUILD_ROOT/%{_datadir}/eclipse

# shelled main feature
unzip -q -d $RPM_BUILD_ROOT%{_datadir}/eclipse/.. \
            build/rpmBuild/com.something.eclipse.shelled.zip

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0644,root,root,0755)
%{_datadir}/eclipse/features/com.something.eclipse.shelled*
%{_datadir}/eclipse/plugins/com.something.eclipse.script*
%{_datadir}/eclipse/plugins/com.something.eclipse.shelled*
 