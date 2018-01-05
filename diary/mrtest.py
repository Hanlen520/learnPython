# Imports the monkeyrunner modules used by this program
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage
 # Connects to the current device, returning a MonkeyDevice object
device = MonkeyRunner.waitForConnection()
 # Installs the Android package. Notice that this method returns a boolean, so you can test

  # to see if the installation worked.
device.installPackage('./yzmd1510901.apk')
  # Runs the component
device.startActivity(component='com.lianchuan.yzmd.activity/.SplashActivity')
  # Presses the Menu button
device.press('KEYCODE_MENU','DOWN_AND_UP')
  # Takes a screenshot
result = device.takeSnapshot()
  # Writes the screenshot to a file
result.writeToFile('./shot1.png','png')