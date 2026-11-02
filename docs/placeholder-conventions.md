# Placeholder conventions

Values use explicit `{{UPPER_SNAKE_CASE}}` placeholders.

Common placeholders include `{{PACKAGE_NAME}}`, `{{VERSION}}`, `{{RELEASE}}`, `{{DESCRIPTION}}`, `{{SPDX_LICENSE}}`, `{{MAINTAINER_NAME}}`, `{{MAINTAINER_EMAIL}}`, `{{SOURCE_URL}}`, `{{SOURCE_SHA256}}`, `{{ARCH}}`, `{{BUILD_DEPENDENCIES}}`, `{{RUNTIME_DEPENDENCIES}}`, `{{BUILD_COMMAND}}` and `{{INSTALL_COMMAND}}`.

1. Never invent unknown values.
2. Only insert a checksum after hashing the exact source artifact.
3. Use dependency names and syntax native to each target ecosystem.
4. Keep upstream version and package release/revision distinct.
5. Do not conflate install, upgrade, remove and purge lifecycle events.
6. Generate derived metadata with native tools when practical.
7. Review paths, permissions, ownership, service handling, config preservation, generated caches and uninstall behavior before production use.
