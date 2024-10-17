%define plugin	channelswitcher

Summary:	VDR plugin: Channel.conf Switcher
Name:		vdr-plugin-%plugin
Version:	0.0.1b
Release:	19
Group:		Video
License:	GPL
URL:		https://www.freewebs.com/sadhome/
Source:		http://www.freewebs.com/sadhome/Plugin/Channelswitcher/vdr-%plugin-%version.tar.bz2
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
%vdr_plugin_install

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY




%changelog
* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.0.1b-16mdv2010.0
+ Revision: 401088
- rebuild for new VDR

* Fri Mar 20 2009 Anssi Hannula <anssi@mandriva.org> 0.0.1b-15mdv2009.1
+ Revision: 359298
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.0.1b-14mdv2009.0
+ Revision: 197910
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.0.1b-13mdv2009.0
+ Revision: 197641
- add vdr_plugin_prep
- bump buildrequires on vdr-devel

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.0.1b-12mdv2008.1
+ Revision: 145048
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.0.1b-11mdv2008.1
+ Revision: 103074
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.0.1b-10mdv2008.0
+ Revision: 49980
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.0.1b-9mdv2008.0
+ Revision: 42067
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.0.1b-8mdv2008.0
+ Revision: 22727
- rebuild for new vdr


* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 0.0.1b-7mdv2007.0
+ Revision: 90902
- rebuild for new vdr

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 0.0.1b-6mdv2007.1
+ Revision: 73973
- rebuild for new vdr
- Import vdr-plugin-channelswitcher

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 0.0.1b-5mdv2007.0
- rebuild for new vdr

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 0.0.1b-4mdv2007.0
- stricter abi requires

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 0.0.1b-3mdv2007.0
- rebuild for new vdr

* Wed Jul 26 2006 Anssi Hannula <anssi@mandriva.org> 0.0.1b-2mdv2007.0
- rebuild for new vdr

* Wed Jun 21 2006 Anssi Hannula <anssi@mandriva.org> 0.0.1b-1mdv2007.0
- initial Mandriva release

