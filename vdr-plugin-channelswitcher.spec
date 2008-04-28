
%define plugin	channelswitcher
%define name	vdr-plugin-%plugin
%define version	0.0.1b
%define rel	14

Summary:	VDR plugin: Channel.conf Switcher
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://www.freewebs.com/sadhome/
Source:		http://www.freewebs.com/sadhome/Plugin/Channelswitcher/vdr-%plugin-%version.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
The channelswitcher plugin administers several channel
configurations. One can change between different channel.conf.*.

%prep
%setup -q -n %plugin-%version
%vdr_plugin_prep

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY


