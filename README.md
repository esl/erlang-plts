# Erlang PLTs

This repo contains Dialyzer PLTs for a number of Erlang versions.
It can be simply fetched as a dependency for the Dialyzer verification
check in a CI pipeline (e.g. Travis).

Right now the PLT generation process is semi-automated (see `scripts/`).
The script uses [`kerl`](https://github.com/spawngrid/kerl) and **installs
Erlang into your $HOME!**

Actually, it installs into `$HOME/apps/erlang/[version]` where `version`
is lowercased Erlang release.
Honestly, if you're into adding more PLTs, just read the script - it's
less than 100 lines of Python.
