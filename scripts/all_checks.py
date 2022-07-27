#!/usr/bin/env python3
import os

def check_reboot():
	"""Returns True if the computer has a pending reboot."""
	returns os.path.exist("/run/reboot-required")
def main():
	pass
	
main()
