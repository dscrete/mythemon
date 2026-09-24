# Mythmon agent guidance

Mythmon is a Gen1Recomp mod adding original myth-themed Pokemon.

## Battle sprite workflow

For Fakemon battle-sprite work, the primary agent acts as the art director.

The primary agent should:
- understand the user's concept and reference images;
- establish the creature's visual identity and important locked features;
- formulate detailed PixelLab art direction when needed;
- judge subjective design problems;
- maintain consistency between front and back sprites.

Routine PixelLab rendering should be delegated to the `pixellab_renderer` subagent.

Once art direction is established, do not repeatedly use the primary agent for mechanical PixelLab calls or simple revisions.

Concrete user feedback such as "shorter ears", "smaller eyes", "use version B", or "keep everything else unchanged" should normally remain with `pixellab_renderer`.

Return to the primary agent for subjective feedback, substantial redesign, or unresolved consistency problems.

## Asset handling

Production battle assets currently live in `assets/`.

Do not use production asset paths as scratch space.

Do not overwrite an existing production sprite until the user explicitly approves the replacement.

The current battle asset conventions are:
- front sprite: transparent 56x56 PNG;
- back sprite: transparent 32x32 PNG.

`tools/make_assets.py` restores the release-tested Aeglet assets and overwrites the existing Aeglet PNGs. Do not run it during sprite generation or revision unless explicitly requested.
