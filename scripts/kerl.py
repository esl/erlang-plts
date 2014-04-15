#!/usr/bin/env python

"""
Build and install predefined versions of Erlang/OTP.
Generate Dialyzer PLTs for the installations.

Requires kerl to be available in ${PATH}.
Get it with:

    curl -O https://raw.github.com/spawngrid/kerl/master/kerl
    chmod a+x kerl

"""

import os
import sys

versions = [
            #"R14B",
            #"R14B01",
            #"R14B02",
            #"R14B03",
            #"R14B04",

            #"R15B",
            #"R15B01",
            #"R15B02",
            #"R15B03",
            #"R16B",
            #"R16B01",
            "R16B02",
            #"R16B03",
            #"17.0"

            #"R15B"
           ]

def kerl_build_release(version):
    build = version.lower()
    cmd = "kerl build %s %s" % (version, build)
    print cmd
    r = os.system(cmd)
    if r != 0:
        sys.stderr.write("kerl build %s failed" % build)
    else:
        print "done"

def kerl_install_release(version):
    build = version.lower()
    path = get_build_path(build)
    cmd = "kerl install %s %s" % (build, path)
    print cmd
    r = os.system(cmd)
    if r != 0:
        sys.stderr.write("kerl install to %s failed\n" % path)
    else:
        print "done"

def generate_plt(plt_dir, version):
    """Run Dialyzer to generate a PLT in `plt_dir` for Erlang `version`."""
    plt_name = "erlang-%s.plt" % version.lower()
    build = version.lower()
    erlang_path = get_build_path(build)
    app_names = get_app_names(os.path.join(erlang_path, "lib"))
    plt_path = os.path.join(plt_dir, plt_name)
    log_path = "dialyzer-%s.log" % build
    cmd = """
. %(erlang)s/activate;
dialyzer --build_plt \\
         --output_plt %(plt)s \\
         -o %(log)s \\
         --apps %(apps)s \\
""" % {"plt": plt_path,
       "log": log_path,
       "erlang": erlang_path,
       "apps": " ".join(app_names)}
    print cmd
    r = os.system(cmd)
    if r != 0:
        sys.stderr.write("dialyzer --build_plt for %s failed\n" % build)
    else:
        print "done"

def get_app_names(lib):
    apps = os.listdir(lib)
    app_names = [app[:app.find("-")] for app in apps]
    app_names = sorted(list(set(app_names) - set(["erl_interface",
                                                  "jinterface"])))
    return app_names

def get_build_path(build):
    home = os.getenv("HOME")
    return os.path.join(home, "apps", "erlang", build)

def main(args):
    options = {"plt_dir": "plts"}
    if args[1] == "build":
        for v in versions:
            kerl_build_release(v)
    elif args[1] == "install":
        for v in versions:
            kerl_install_release(v)
    elif args[1] == "generate":
        for v in versions:
            generate_plt(options["plt_dir"], v)

if __name__ == '__main__':
    main(sys.argv)
