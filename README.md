# Installation instructions
    sudo dnf install http://download1.rpmfusion.org/free/fedora/releases/$(. /etc/os-release ; echo $VERSION_ID)/Everything/$(uname -i)/os/Packages/r/rpmfusion-free-release-$(. /etc/os-release ; echo $VERSION_ID)-1.noarch.rpm
    sudo dnf copr enable jstepanek/deepin
    sudo dnf update
    sudo dnf install startdde deepin-wm deepin-wm-switcher dde-control-center dde-daemon dde-desktop dde-dock dde-file-manager dde-launcher dde-1. session-ui deepin-desktop-base deepin-desktop-schemas deepin-file-manager-backend deepin-gtk-theme deepin-icon-theme deepin-image-viewer deepin-menu deepin-metacity deepin-mutter deepin-nautilus-properties deepin-notifications deepin-screenshot deepin-shortcut-viewer deepin-sound-theme deepin-wallpapers lightdm
    sudo systemctl disable gdm.service && sudo systemctl enable lightdm.service
    sudo sed -e "s/SELINUX=enforcing/SELINUX=disabled/g" -i /etc/selinux/config
    sudo su -c "echo -e '[Seat:*]\ngreeter-session=lightdm-deepin-greeter' > /etc/lightdm/lightdm.conf.d/deepin.conf"

After this is done, simply reboot into your new nice environment.
If you have any questions the feel free to contact me on the email address filled in the contact.

# fedora-deepin repository content

This repository contains the following .specs for integrating the deepin desktop environment into Fedora
* dbus-factory
* dde-account-faces
* dde-api
* dde-calendar
* dde-control-center
* dde-daemon
* dde-desktop
* dde-dock
* dde-file-manager
* dde-launcher
* dde-session-ui
* deepin-artwork-themes
* deepin-cogl
* deepin-dbus-factory-qml306
* deepin-desktop-base
* deepin-desktop-schemas
* deepin-file-manager-backend
* deepin-game
* deepin-gettext-tools
* deepin-grub2-themes
* deepin-gtk-theme
* deepin-icon-theme
* deepin-image-viewer
* deepin-manual
* deepin-menu
* deepin-metacity
* deepin-movie
* deepin-music
* deepin-mutter
* deepin-nautilus-properties
* deepin-notifications
* deepin-qml-widgets
* deepin-screenshot
* deepin-shortcut-viewer
* deepin-social-sharing
* deepin-sound-theme
* deepin-terminal
* deepin-tool-kit
* deepin-wallpapers
* deepin-wm
* deepin-wm-switcher
* go-dbus-generator
* go-gir-generator
* go-lib
* gsettings-qt
* python2-ass
* python2-deepin-gsettings
* python2-deepin-storm
* python2-deepin-ui
* python2-deepin-utils
* python2-jswebkit
* python2-pysrt
* python2-xpybutil
* python3-dae
* python3-xlib
* startdde
