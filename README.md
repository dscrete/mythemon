# Mythmon

Mythmon adds original, myth-themed Pokemon to Gen1Recomp.

## Current proof of concept

The first species is **Aeglet**, a small unevolved Psychic-type creature designed to leave room for a later evolution.

- Static transparent battle front sprite: 56x56, refined for a Gen 2-style battle presentation
- Static transparent battle back sprite: 32x32
- Transparent two-frame party icon: 16x32
- Original chip cry
- Custom stats, learnset and Pokedex text
- No evolution yet
- Normal encounter: rare slot in Viridian Forest at level 5

Aeglet's current art keeps the established fox-like mythic design while aiming for a middle ground between the overly detailed concept pass and the overly primitive 0.1.6 reduction. The front and back sprites use controlled pixel clusters, a restrained tan/brown/cream/purple palette, and full alpha transparency. Aeglet's battle art and party icon are registered as true-color assets so Gen1Recomp preserves the authored colors instead of remapping them through the legacy four-shade battle palette pipeline.

`tools/make_assets.py` restores the exact release-tested sprite bytes deterministically.

## MYTH CHARM testing utility

Mythmon automatically adds **MYTH CHARM** to the Bag on an existing or new save when there is room.

Use MYTH CHARM outside battle to arm the next successful wild encounter. The next wild Pokemon that actually appears is replaced with a level 5 Aeglet, then the charm automatically disarms. Empty grass steps do not consume the armed state, and the key item itself is never consumed.

If the charm is already armed, using it again simply reports that it is already resonating.

This utility is intended to remain in Mythmon as a development/testing aid. Once more Mythmon species exist, it can be expanded into a species-selection tool.

## Installation

Extract the release ZIP so the top-level `mythmon` directory is inside Gen1Recomp's `mods` directory.

## Compatibility scope

Mythmon uses Mod API 2 and currently declares Gen1Recomp compatibility from **0.3.3 through 0.5.0 inclusive**. Development builds are also allowed for local testing. Versions newer than 0.5.0 are intentionally not claimed yet; the range can be widened after they are checked.

The current engine API still provides the custom Pokemon/icon registries, item-effects registry, `save.loaded`/`save.created` lifecycle events, `encounter.species` hook, and true-color sprite support used by Mythmon, so no gameplay-code migration was required for the 0.5.0 compatibility update.

This release tests the core custom-species pipeline only. It does not yet add bespoke animated battle frames, shiny art, or Wilds of Kanto overworld/follower sprites. The species and asset IDs are namespaced to make those compatibility layers easier to add later.
