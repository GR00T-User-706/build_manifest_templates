# Build Manifest Templates

Reusable starter templates for package build manifests and native package-manager metadata. These files are placeholders and references, not complete release-ready packages.

## Layout

- `templates/pkgforge/package.yaml`: proposed PKGforge project-level manifest.
- `templates/arch/PKGBUILD`, `.SRCINFO.example`: Arch makepkg recipe and generated metadata example.
- `templates/debian/`: Debian source package control, rules, changelog, copyright and source format.
- `templates/rpm/package.spec`: RPM spec.
- `templates/alpine/APKBUILD`: Alpine build recipe.
- `templates/termux/termux-create-package.yaml`: separate Termux create-package input starter.
- `templates/appimage/`: AppDir launcher, desktop entry and appimage-builder configuration.
- `templates/flatpak/manifest.yml`: Flatpak Builder manifest.
- `templates/snap/snapcraft.yaml`: Snapcraft manifest.
- `templates/freebsd/Makefile`: FreeBSD ports Makefile starter.
- `templates/generic/`: tool-neutral build and lifecycle examples.

## Important distinctions

PKGforge's canonical manifest is not a native package-manager manifest. The Arch `PKGBUILD` is an executable Bash recipe; `.SRCINFO` should be generated from it. Debian packaging is a `debian/` directory, not one YAML file. Termux's `termux-create-package` input is deliberately separate from both PKGforge YAML and Debian control metadata.

The PKGforge manifest here is a proposed starter shape, not a claim about an already implemented schema. The Termux example is explicitly provisional: verify exact keys and value types against the installed `termux-create-package` version before use.

See [format notes](docs/formats.md) and [placeholder conventions](docs/placeholder-conventions.md).

## Validation

Use native tools after replacing placeholders: Arch `makepkg --printsrcinfo`; Debian `dpkg-parsechangelog` and `dpkg-buildpackage`; RPM `rpmspec -P`; Alpine `abuild -n`; Flatpak `flatpak-builder --show-manifest`; Snap `snapcraft validate`. Incomplete placeholder files are not expected to validate unchanged.

This repository stores templates and documentation. It does not implement PKGforge or replace ecosystem packaging documentation.
