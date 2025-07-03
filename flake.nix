{
  description = "Recommendation Engine development environment";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils, ... }:
    flake-utils.lib.eachDefaultSystem (system:
      let pkgs = import nixpkgs { inherit system; };
      in with pkgs; {
        devShells.default = mkShell {
          nativeBuildInputs = [ ];

          buildInputs = [
            (python313.withPackages (python313Packages:
              with python313Packages; [
                venvShellHook
                pip
              ]))

            gcc
          ];

          venvDir = ".venv";

          LD_LIBRARY_PATH =
            "${stdenv.cc.cc.lib.outPath}/lib:${pythonManylinuxPackages.manylinux2014Package}/lib:$LD_LIBRARY_PATH";

          shellHook = "source ./.venv/bin/activate";
        };
      });
}
