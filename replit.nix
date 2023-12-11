{ pkgs }: {
  deps = [
    pkgs.htop-vim
    pkgs.sudo install htop
  ];
}