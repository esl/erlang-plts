# Erlang PLTs

This repo contains Dialyzer PLTs for a number of Erlang versions.
It can be simply fetched as a dependency for the Dialyzer verification
check in a CI pipeline (e.g. Travis).

The PLT generation process driven by `scripts/kerl.py` is semi-automated.
The script uses [`kerl`](https://github.com/spawngrid/kerl)
and **installs Erlang into your $HOME!**

Actually, it installs into `$HOME/apps/erlang/[version]` where `version`
is lowercased Erlang release.
Honestly, if you're into adding more PLTs, just read the script - it's
less than 100 lines of Python.

## PLTs for Travis

PLTs contain hard coded paths to `.beam` files they are generated from.
For Travis CI use the `travis-erlang-*.plt` variants generated on
a VM provisioned using [Sous Chef](https://github.com/michaelklishin/sous-chef)
and [Travis Cookbooks](https://github.com/travis-ci/travis-cookbooks).
