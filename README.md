# QuikSim3 Templates

Curated content distributed alongside [QuikSim3](https://github.com/DSI-JBenway/QuikSim3),
Dynamic Systems Inc.'s Gleeble simulation client. This repository ships:

- **Example programs** — ready-to-run `.qhd` / `.qst` / `.qhz` programs
  surfaced read-only in QuikSim3's **Examples** panel.
- **GIN templates** — per-machine GSL boilerplate templates used to render a
  program's GSL (under `gins/<machine>/<doctype>/`). *Coming soon.*

Templates are distributed as a separate repository so they can be added,
corrected, and tagged more frequently than QuikSim3 itself. QuikSim3
fetches the latest release on startup, unpacks it under
`%LOCALAPPDATA%\QuikSim3\templates\<tag>\`, and falls back to whatever is
already cached on disk when offline.

## Repository layout

```
QuikSim3-Templates/
├── README.md              # this file
├── manifest.json          # generated index of all examples + templates
├── examples/
│   ├── <example-id>/
│   │   ├── meta.json      # user-facing metadata (name, category, tags, …)
│   │   ├── program.qhd    # the program file (.qhd / .qst / .qhz)
│   │   └── README.md      # description + key parameters + how to use
│   └── …
├── gins/                  # GIN templates (coming soon)
│   └── <machine_model>/<doctype>/<name>.gin.j2
├── tools/
│   └── generate_manifest.py   # scans examples/ + gins/ and writes manifest.json
└── .github/workflows/
    └── release.yml        # packages content for a GitHub Release on tag push
```

## Adding a new example

1. Pick an `example-id` (kebab-case, short).
2. Create `examples/<example-id>/` and drop in:
   - the program file, named `program.qhd`, `program.qst`, or `program.qhz`
     depending on the document type;
   - a `README.md` describing what it does and how to use it;
   - a `meta.json` with the fields described below.
3. Regenerate the manifest: `python tools/generate_manifest.py`.
4. Commit everything and open a PR.

### `meta.json` schema

```json
{
  "id": "tensile-basic",
  "name": "Basic Tensile Test",
  "category": "Tensile",
  "description": "A short user-facing description.",
  "tags": ["tensile", "basic"],
  "difficulty": "beginner",
  "program": "program.qhd",
  "min_quiksim3": "3.0.0"
}
```

- `min_quiksim3` is the oldest QuikSim3 version that can open the program.
  Bump it whenever an example relies on a newer `schemaVersion`. The QuikSim3
  client filters the manifest by this field so stale installs only see
  examples they can actually load.

## Releases

Tagged commits (`v*`) trigger `.github/workflows/release.yml`, which:

1. Regenerates `manifest.json` so the release is self-consistent.
2. Packs the repository content into a release archive.
3. Uploads the archive and `manifest.json` as assets on a new GitHub
   Release with the same tag.

QuikSim3 fetches the latest release assets on startup. To cut a new release:

```
git tag v0.2.0
git push origin v0.2.0
```

## License

These templates are provided as-is for educational use. See individual
example READMEs for any specific attribution.
