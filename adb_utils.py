import subprocess as subp


def get_installed_apps(device):
    return map(lambda x: x.replace("package:", ""), device.shell("pm list packages").split("\n"))


def uninstall_package(package, device):
    device.shell("pm uninstall " + package)


def install_apks(*files):
    for file in files:
        print "Installing '%s'" % file
        subp.check_call("adb install -t " + file, stderr=subp.STDOUT, shell=True)


def start_app(device, package):
    device.shell("am force-stop %s" % package)
    device.shell("monkey -p %s -c android.intent.category.LAUNCHER 1" % package)


def wait_for_log(log_message):
    subp.check_call("adb logcat -c", stderr=subp.STDOUT, shell=True)
    subp.check_call("adb logcat -e \"%s\" -m 1" % log_message, stderr=subp.STDOUT, shell=True)
