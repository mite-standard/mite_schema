# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.8.3] 30-09-2025

### Changed

- Switched installer from `hatch` to `uv`
- Updated dependencies
- Updated CITATION.cff

## [1.8.2] 29-08-2025

### Changed

- Shortened validation error messages to human-readable length.

## [1.8.1] 29-08-2025

### Changed

- Removed "minItems: 1" from changelog to facilitate data submission via web portal. Change is backwards-compatible.

## [1.8.0] 17-06-2025

### Added

- Added optional "cofactor" to "enzyme"
- Added optional "wikidata" crossref to "databaseIds" of "enzyme" and "auxiliary enzymes"

## [1.7.1] 13-02-2025

### Added

- Added "Chemical probe" to evidence code controlled vocabulary

## [1.7.0] 11-02-2025

### Changed

- Simplified schema by combining definitions into a single schema file
- Removed wildcard "attachments" parameter

## [1.6.0] 30-11-2024

### Added

- Additional terms for "tailoring" controlled vocabulary: 'Sulfonation', 'Ring contraction', 'Ring expansion'

## [1.5.1] 09-11-2024

### Changed

- Reaction: made "description" of reaction examples optional for backward compatibility
- Made DOI pattern matching less stringent

## [1.5.0] 08-11-2024

### Changed

- Changelog: flattened structure, changed identifiers to ORCID, changed versioning to major alone (before 'major.minor')
- Evidence: flattened structure to a single object (before: a list of objects)
- Reaction database IDs: flattened structure, changed formatting of EC to the code (e.g. 1.2.3.4) alone (before: string had to start with 'EC'), drop MITE crosslinks
- References: removed non-peristing reference types, only DOI allowed (before: url, pubmed, patent)
- Tailoring reaction terms: removed 'FADH2 supply for chlorination' since it is not tailoring per se
- Status: removed 'embargoed' specification

## [1.4.1] 08-10-2024

### Changed

- CLI: added support for multiple input files checking at once

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
