{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.python3
    pkgs.python3Packages.pynput
  ];

  shellHook = ''
    echo "Opening current directory in Visual Studio Code..."
    code "$PWD" &
  '';
}
