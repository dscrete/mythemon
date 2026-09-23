# Changelog

## 0.1.7

- Redraw Aeglet's battle art toward the intended Gen 2 visual target after the 0.1.6 native-size pass proved too visually primitive.
- Restore the front sprite to a 56x56 canvas and `frontSize = 7`, while keeping the pixel clusters deliberately cleaned and restrained.
- Replace the 32x32 back sprite with a matching tan/brown/cream/purple design derived from the same Aeglet model.
- Replace the 16x32 two-frame party icon with a purpose-built tiny icon instead of a direct reduction of the battle artwork.
- Keep full alpha transparency on all sprite assets.
- Keep release-time PNG signature, dimensions, alpha-format, chunk and CRC validation enabled.

## 0.1.6

- Rebuild Aeglet's battle art at native in-game dimensions instead of using the larger concept-sized front sprite.
- Replace the front battle sprite with a cleaned 40x40 version with simpler pixel clusters and a clearer silhouette.
- Replace the back battle sprite with a matching cleaned 32x32 version.
- Replace the party/menu art with a purpose-built 16x32 two-frame icon.
- Preserve alpha transparency across all three assets.
- Set `frontSize` back to 5 for the 40x40 front sprite.
- Update the deterministic asset generator and release validator for the native-size sprite set.

## 0.1.5

- Replace the prototype Aeglet artwork with a substantially more polished Gen 2-inspired sprite set.
- Increase the front battle sprite from 40x40 to 56x56 and set `frontSize = 7`.
- Add real alpha transparency to the front sprite, back sprite, and party icon so no white sprite box is rendered in battle.
- Rework the back sprite and icon to match the new tan, brown, cream, and purple visual identity.
- Require alpha-capable PNGs in the release asset validator in addition to CRC and dimension checks.
- Update the asset restoration script so it reproduces the exact release-tested transparent PNG bytes.

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
