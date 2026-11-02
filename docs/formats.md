# Packaging format notes

## PKGforge
The PKGforge manifest is the project-level source of packaging intent. It can describe source identity, version, targets, dependencies, build steps, artifacts, staged files, lifecycle hooks and generated-file policy. The exact schema must be defined by PKGforge itself; the template is a proposed starter, not a confirmed schema contract.

## Arch Linux
`PKGBUILD` is a Bash recipe consumed by `makepkg`. `.SRCINFO` is derived repository metadata. Generate it with `makepkg --printsrcinfo`. Respect makepkg configuration, especially `PKGDEST`, `SRCDEST`, `SRCPKGDEST` and `BUILDDIR`; do not hard-code output paths.

## Debian
The `debian/` directory contains source packaging metadata. `rules` is a makefile. Optional maintainer scripts include `preinst`, `postinst`, `prerm` and `postrm`; add only those required and follow Debian lifecycle semantics.

## RPM
The spec file defines metadata, sources, build/install phases, files and optional scriptlets. RPM transaction scriptlets are not interchangeable with Debian maintainer scripts.

## Alpine
`APKBUILD` is the shell build recipe consumed by `abuild`.

## Termux
Termux package creation has its own `termux-create-package` input schema and package layout. Its template is separate from the PKGforge manifest and Debian metadata. Confirm the schema against the installed tool version.

## AppImage
An AppImage bundles an AppDir, including an executable entry point and desktop integration metadata. Builder configuration is tool-specific.

## Flatpak
A Flatpak manifest declares application identity, runtime, SDK, modules and sources.

## Snap
A Snapcraft manifest declares snap identity, confinement, apps, plugs, parts and sources.

## FreeBSD
The Ports framework uses a Makefile with metadata and build/install targets. Adapt this starter to current ports framework conventions.
