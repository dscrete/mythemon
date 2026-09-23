# Mythmon

Mythmon adds original, myth-themed Pokemon to Gen1Recomp.

## v0.1.0 proof of concept

The first species is **Aeglet**, a small unevolved Psychic-type creature designed to leave room for a later evolution.

- Static four-shade battle front sprite: 40x40
- Static four-shade battle back sprite: 32x32
- Two-frame party icon: 16x32
- Original chip cry
- Custom stats, learnset and Pokedex text
- No evolution yet
- Test encounter: rare slot in Viridian Forest at level 5

The assets intentionally use a small four-shade palette and low native resolution rather than high-detail generated artwork. `tools/make_assets.py` deterministically regenerates all current sprite assets.

## Installation

Extract the release ZIP so the top-level `mythmon` directory is inside Gen1Recomp's `mods` directory.

## Compatibility scope

This first release tests the core custom-species pipeline only. It does not yet add bespoke animated battle frames, shiny art, or Wilds of Kanto overworld/follower sprites. The species and asset IDs are namespaced to make those compatibility layers easier to add later.
