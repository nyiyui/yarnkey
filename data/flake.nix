{
  outputs = { self, nixpkgs }: let
    pkgs = nixpkgs.legacyPackages.x86_64-linux;
  in {
    devShells.x86_64-linux.default = let
      p = pkgs.python3.withPackages (p: with p; [
        beautifulsoup4
        requests
        dateutil
        diff-match-patch
        black
      ]);
    in pkgs.mkShell {
      buildInputs = [
        pkgs.gnumake
        p
      ];
    };
  };
}
