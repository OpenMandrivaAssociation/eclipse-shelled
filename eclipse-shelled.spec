%define eclipse_base     %{_libdir}/eclipse
%define install_loc      %{_datadir}/eclipse/dropins/shelled

Summary:          Eclipse Shell script editor
Name:             eclipse-shelled
Version:          1.0.4
Release:          %mkrel 2
License:          Common Public License
URL:              http://sourceforge.net/projects/shelled
Group:            Development/Other
Source0:          http://superb-east.dl.sourceforge.net/sourceforge/shelled/shelled-src_1_0_4.tar.bz2
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
install -d -m 755 $RPM_BUILD_ROOT%{install_loc}

# shelled main feature
unzip -q -d $RPM_BUILD_ROOT%{install_loc} \
            build/rpmBuild/com.something.eclipse.shelled.zip

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{install_loc}
%doc com.something.eclipse.shelled-feature/license.html
%doc com.something.eclipse.shelled-feature/cpl-v10.html
%doc com.something.eclipse.shelled.resources/about.html
