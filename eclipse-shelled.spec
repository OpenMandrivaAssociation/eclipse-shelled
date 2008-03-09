Summary:          Eclipse Shell script editor
Name:             eclipse-shelled
Version:          1.0.3
Release:          %mkrel 0.0.1
License:          Common Public License
URL:              http://sourceforge.net/projects/shelled
Group:            Development/Java
Source0:          shelled-1.0.3.tar.lzma
Requires:         eclipse-platform >= 1:3.2.1
Requires:         git-core
BuildRequires:    eclipse-pde
BuildRequires:    java-rpmbuild >= 0:1.5
BuildRequires:    zip
BuildArch:        noarch
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root

%description
The eclipse-egit package contains Eclipse plugins for
interacting with Git repositories.

%prep
%setup -q -c 

%build
# Copy the SDK for build
/bin/sh -x %{_datadir}/eclipse/buildscripts/copy-platform SDK %{_datadir}/eclipse
SDK=$(cd SDK > /dev/null && pwd)

# Eclipse may try to write to the home directory.
mkdir home
homedir=$(cd home > /dev/null && pwd)

# build the main egit feature
%{java} -cp $SDK/startup.jar                              \
     -Dosgi.sharedConfiguration.area=%{_libdir}/eclipse/configuration  \
     org.eclipse.core.launcher.Main                    \
     -application org.eclipse.ant.core.antRunner       \
     -Dtype=feature                                    \
     -Did=com.something.eclipse.shelled                \
     -DbaseLocation=$SDK                               \
     -DjavacSource=1.5  -DjavacTarget=1.5              \
     -DsourceDirectory=$(pwd)                          \
     -DbuildDirectory=$(pwd)/build                     \
     -Dbuilder=%{_datadir}/eclipse/plugins/org.eclipse.pde.build/templates/package-build \
     -f %{_datadir}/eclipse/plugins/org.eclipse.pde.build/scripts/build.xml \
     -vmargs -Duser.home=$homedir

%install
rm -rf $RPM_BUILD_ROOT
install -d -m755 $RPM_BUILD_ROOT/%{_datadir}/eclipse

# egit main feature
unzip -q -d $RPM_BUILD_ROOT%{_datadir}/eclipse/.. \
            build/rpmBuild/com.something.eclipse.shelled.zip

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0644,root,root,0755)
%{_datadir}/eclipse/features/com.something.eclipse.shelled*
%{_datadir}/eclipse/plugins/com.something.eclipse.script*
%{_datadir}/eclipse/plugins/com.something.eclipse.shelled*
%{_datadir}/eclipse/plugins/com.something.eclipse.shelled.resource*
%{_datadir}/eclipse/plugins/com.something.eclipse.shelled.ui*
 