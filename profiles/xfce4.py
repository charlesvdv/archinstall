# A desktop environment using "Xfce4"

import archinstall

is_top_level_profile = False

__packages__ = ["xfce4", "xfce4-goodies", "lightdm", "lightdm-gtk-greeter"]


def _prep_function(*args, **kwargs):
	"""
	Magic function called by the importing installer
	before continuing any further. It also avoids executing any
	other code in this stage. So it's a safe way to ask the user
	for more input before any other installer steps start.
	"""

	# XFCE requires a functional xorg installation.
	profile = archinstall.Profile(None, 'xorg')
	with profile.load_instructions(namespace='xorg.py') as imported:
		if hasattr(imported, '_prep_function'):
			return imported._prep_function()
		else:
			print('Deprecated (??): xorg profile has no _prep_function() anymore')


# Ensures that this code only gets executed if executed
# through importlib.util.spec_from_file_location("xfce4", "/somewhere/xfce4.py")
# or through conventional import xfce4
if __name__ == 'xfce4':
	# Install dependency profiles
	archinstall.storage['installation_session'].install_profile('xorg')

	# Install the XFCE4 packages
	archinstall.storage['installation_session'].add_additional_packages(__packages__)

	archinstall.storage['installation_session'].enable_service('lightdm')  # Light Display Manager
