# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.5.0] - 2026-08-15

### Added

- Added support for Blender 4.5 LTS and Blender 5.2 LTS
- Added Blender Extension packaging

### Changed

- Updated the fixed-width presets to `140`, `240`, `340`, `440`, `540`, `640`, and `700`
- Consolidated the fixed-width actions into one namespaced operator
- Updated the panel layout to emphasize the most-used widths

### Removed

- Removed the `200` and `400` fixed-width presets

## [1.4.0] - 2023-06-30

### Changed

- Added Blender 3.6 LTS compatibility
- Removed node width options `440`, `540`, and `640`
- Replaced node width option `700` with `400` to accommodate Blender 3.6 LTS's maximum node width of 400

## [1.3.0] - 2023-01-31

### Added

- Added node width option `200`

## 1.2.1 - 2022-12-17

### Changed

- Refactored code
- Applied PEP 8 formatting

## [1.2.0] - 2022-03-18

### Changed

- Moved **Set Node Width** label inside the `if` statement

## [1.1.0] - 2020-09-24

### Added

- Added support for assigning a fixed width to selected nodes

## [1.0.0] - 2020-09-22

### Added

- Initial release
- Added support for assigning a fixed width to the active node in the Shader Editor

[1.5.0]: https://github.com/don1138/blender-qrn/releases/tag/v1.5.0
[1.4.0]: https://github.com/don1138/blender-qrn/releases/tag/v1.4.0
[1.3.0]: https://github.com/don1138/blender-qrn/releases/tag/1.3.0
[1.2.0]: https://github.com/don1138/blender-qrn/releases/tag/1.2
[1.1.0]: https://github.com/don1138/blender-qrn/releases/tag/1.1
[1.0.0]: https://github.com/don1138/blender-qrn/releases/tag/1.0
