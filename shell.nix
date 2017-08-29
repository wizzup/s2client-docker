{ pkgs ? import <nixpkgs> {} }:

with pkgs;

let 
  py3s = python3.buildEnv.override  {
    extraLibs = with pkgs.python3Packages; [ 
      neovim
      jedi
      pylint

    ];};

  ccs = [gcc cmake];
in stdenv.mkDerivation {
  name = "sc2-dev";
  buildInputs = [ py3s ccs ];

  shellHook = ''
    export PS1="\[\033[1;32m\][nix-py3:\W]\n$ \[\033[0m\]"
  '';
}

