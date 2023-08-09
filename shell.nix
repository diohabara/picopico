{ pkgs ? import <nixpkgs> {} }:

with pkgs;
mkShell {
  nativeBuildInputs = [
    # for ctf
    exiftool
    john

    # for nix
    shellcheck
    direnv
  ];

  shellHook = ''
    if [ ! -d "SecLists" ]; then
      git clone --depth 1 \
        https://github.com/danielmiessler/SecLists.git
    fi
  '';
}
