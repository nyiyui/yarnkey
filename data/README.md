This contains data collection/analysis tools for Yarnkey.

All the dependencies required to run this are either in this folder or are specified in `./flake.{nix,lock}`.
Setting up the dependencies can be done by
[Installing Nix](https://nixos.org/download.html#:~:text=Nix),
and running `nix-shell` (this is the simplest, but [enabling flakes](https://nixos.wiki/index.php?title=Flakes&oldid=8779#Enable_flakes) and running `nix develop` works too, as well as using [direnv](https://direnv.net/)).

To run the data analysis, run `make`. This will generate csv files as specified in the Makefile.

Additional Notes:
- `p1` and `p2` marks data from person 1 (researcher, me) and person 2 (Adult Supvervisor)
- `.slog.txt` means that the data is raw data (originally from the server)
- all raw data is provided in `yarnkey-log.slog.txt`. This includes the data used for the analysis in the project.
