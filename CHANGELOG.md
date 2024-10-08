# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.4] 08-10-2024

### Added

- CLI: returns exit code 0 when file passes, returns 1 if file does not pass

### Changed

- schema/entry: removed "quality" flag due to lack of objectiveness (all MITE entries were set to medium; difficult to define quality objectively)
- schema/reactions: removed "isBalanced" flag since this information is already contained in the reaction SMARTS/SMILES
- schema/reactions: removed "isIterative" flag: was not used by any entry so far, reaction SMARTS can be applied 

## [1.3] 11-08-2024

### Changed

- schema/reactions: 'databaseIds' accepts now arrays of strings (before: a single string, see also v1.1). This allows to e.g. specify multiple MITE cross-references instead of a single one.

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