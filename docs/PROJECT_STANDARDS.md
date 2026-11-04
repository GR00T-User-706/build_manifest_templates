# Build Manifest Templates Repository Standards

This repository provides reusable packaging templates and explanatory examples. It is a template catalog, not a package builder and not a guarantee that every included file is release-ready.

## Template status

Every template must identify its target ecosystem, intended use, required substitutions, assumptions, and validation tool. Clearly label files as starter, illustrative, provisional, or ready for adaptation. Never imply that placeholder values are valid production metadata.

## Ecosystem accuracy

Keep native formats distinct. Examples include Arch `PKGBUILD` and generated `.SRCINFO`, Debian's `debian/` source-package directory, RPM spec files, Alpine `APKBUILD`, Termux create-package YAML, AppImage AppDir content, Flatpak manifests, Snapcraft manifests, and FreeBSD ports Makefiles.

Do not flatten different package ecosystems into a fictitious universal format. A higher-level project manifest may coordinate metadata, but native formats retain their own syntax and semantics.

## Placeholder discipline

Use consistent, recognizable placeholders and explain each one. Do not insert invented package names, checksums, URLs, dependencies, maintainer identities, licenses, versions, or filesystem paths as if they were verified facts. Where a valid example requires a real value, clearly mark it as illustrative or require replacement.

## Validation documentation

For each template, list the relevant native validation/build command, required toolchain, and what that command proves. Distinguish syntax/metadata validation from a successful package build, payload inspection, installation, and runtime test. Placeholder templates are not expected to validate unchanged unless explicitly stated.

## Change control

When a template changes, update its format notes and placeholder guidance if affected. Keep examples internally consistent with the documented ecosystem version and tool behavior. Do not modify generated or downstream projects as a side effect of changing a template.

## Relationship to pkgForge

The proposed pkgForge template is not proof of a released or implemented pkgForge schema. Keep it explicitly marked as a starter shape until verified against the actual versioned schema and implementation.
