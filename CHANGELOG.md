# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.2] 07-08-2024

### Changed

- Made minimum Python version more permissive

## [1.1] 05-08-2024

### Changed

- schema/enzyme: 'databaseIds' is now an object, with allowed database cross-links as keys (before: an array of database-crosslinks)
- schema/reactions: 'databaseIds' is now an object, with allowed database cross-links as keys (before: an array of database-crosslinks)

## [1.0] 05-08-2024

### Added

- Implemented MITE Schema and SchemaManager()

### Changed

- All schema elements are now served locally (before: 'changelog.json' and 'citation.json' were taken from MIBiG repository)