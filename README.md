# Mythmon

Mythmon adds original, myth-themed Pokemon to Gen1Recomp.

## Current proof of concept

The first species is **Aeglet**, a small unevolved Psychic-type creature designed to leave room for a later evolution.

- Static four-shade battle front sprite: 40x40
- Static four-shade battle back sprite: 32x32
- Two-frame party icon: 16x32
- Original chip cry
- Custom stats, learnset and Pokedex text
- No evolution yet
- Normal encounter: rare slot in Viridian Forest at level 5

The assets intentionally use a small four-shade palette and low native resolution rather than high-detail generated artwork. `tools/make_assets.py` deterministically regenerates all current sprite assets.

## MYTH CHARM testing utility

Mythmon automatically adds **MYTH CHARM** to the Bag on an existing or new save when there is room.

Use MYTH CHARM outside battle to arm the next successful wild encounter. The next wild Pokemon that actually appears is replaced with a level 5 Aeglet, then the charm automatically disarms. Empty grass steps do not consume the armed state, and the key item itself is never consumed.

If the charm is already armed, using it again simply reports that it is already resonating.

This utility is intended to remain in Mythmon as a development/testing aid. Once more Mythmon species exist, it can be expanded into a species-selection tool.

## Installation

Extract the release ZIP so the top-level `mythmon` directory is inside Gen1Recomp's `mods` directory.

## Compatibility scope

This release tests the core custom-species pipeline only. It does not yet add bespoke animated battle frames, shiny art, or Wilds of Kanto overworld/follower sprites. The species and asset IDs are namespaced to make those compatibility layers easier to add later.
