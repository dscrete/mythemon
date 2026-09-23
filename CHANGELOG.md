# Changelog

## 0.1.4

- Replace Aeglet's front, back, and party icon with validated grayscale PNGs that contain no palette chunk.
- Update the asset generator to emit and verify the same grayscale PNG format.
- Keep release-time PNG CRC and dimension validation enabled before packaging.

## 0.1.3

- Replace corrupted Aeglet front, back, and party icon PNGs with freshly generated valid image files.
- Add release-time PNG signature, dimension, chunk-boundary, and CRC validation so malformed assets cannot be packaged again.

## 0.1.2

- Fix MYTH CHARM not appearing on continued saves.
- Grant the charm from `save.loaded` and `save.created`, after the real player save exists, instead of the pre-title `game.ready` boot save.

## 0.1.1

- Add the MYTH CHARM permanent testing key item.
- Using MYTH CHARM outside battle arms the next successful wild encounter to become a level 5 Aeglet.
- The force flag is stored in Mythmon's per-save state and clears immediately after the forced encounter is selected.
- Existing saves automatically receive the charm when possible.
- Keep Aeglet's normal rare Viridian Forest encounter unchanged.

## 0.1.0

- Add Aeglet (`MYTHMON_AEGLET`) as Mythmon's first original species.
- Add static four-shade front/back battle sprites and two-frame party icon.
- Add original chip cry, stats, learnset and Pokedex entry.
- Add a temporary level 5 Viridian Forest encounter for testing.
- Add deterministic asset-generation script.
- Add automated tagged prerelease packaging triggered by `.release`.
