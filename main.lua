local SPECIES = "MYTHMON_AEGLET"

local function cloneSlots(slots)
  local out = {}
  for i, slot in ipairs(slots or {}) do
    out[i] = {
      level = slot.level,
      species = slot.species,
    }
  end
  return out
end

return function(mod)
  local ChipAsm = require("src.audio.ChipAsm")

  local front = mod.path .. "/assets/aeglet_front.png"
  local back = mod.path .. "/assets/aeglet_back.png"
  local icon = mod.path .. "/assets/aeglet_icon.png"

  -- A short, soft two-note cry. It is authored here rather than borrowing a
  -- vanilla species cry so Aeglet remains self-contained.
  mod.content.cries:register(SPECIES, {
    chip = ChipAsm.sfx{
      channels = {
        {
          hw = 1,
          program = {
            { squareNote = { len = 4, volume = 11, fade = 2, frequency = 0x5B0 } },
            { squareNote = { len = 5, volume = 9, fade = 2, frequency = 0x670 } },
          },
        },
      },
    }.chip,
    pitch = 128,
    length = 112,
  })

  mod.content.icons:register(SPECIES, {
    image = icon,
    frames = 2,
  })

  mod.content.pokemon:register(SPECIES, {
    id = SPECIES,
    name = "AEGLET",
    -- Kept after the complete Gen 2 dex so future Johto compatibility does
    -- not force this proof-of-concept species to change identity.
    dex = 252,
    types = { "PSYCHIC" },
    baseStats = {
      hp = 45,
      attack = 40,
      defense = 45,
      speed = 60,
      special = 65,
    },
    catchRate = 190,
    baseExp = 62,
    growthRate = "MEDIUM_FAST",
    level1Moves = { "TACKLE", "GROWL" },
    learnset = {
      { level = 7, move = "CONFUSION" },
      { level = 12, move = "QUICK_ATTACK" },
      { level = 18, move = "DOUBLE_TEAM" },
      { level = 26, move = "PSYBEAM" },
    },
    evolutions = {},
    spriteFront = front,
    spriteBack = back,
    frontSize = 5,
    cry = SPECIES,
    icon = { image = icon, frames = 2 },
    dexEntry = {
      kind = "FABLE",
      heightFt = 1,
      heightIn = 4,
      weight = 132,
      text = "A quiet creature that lingers near places tied to old tales.",
      text2 = "Its curled tail twitches when it senses something forgotten.",
    },
  })

  -- First-pass test placement: replace only the rarest Viridian Forest slot
  -- while preserving whatever encounter table exists ahead of this mod.
  -- This makes Aeglet obtainable without owning the whole encounter table.
  local forest = mod.content.encounters:get("VIRIDIAN_FOREST")
  if forest and forest.grass and type(forest.grass.slots) == "table"
      and #forest.grass.slots >= 10 then
    local slots = cloneSlots(forest.grass.slots)
    slots[10] = { level = 5, species = SPECIES }
    mod.content.encounters:patch("VIRIDIAN_FOREST", {
      grass = { slots = slots },
    })
    mod.log:info("Aeglet registered; Viridian Forest slot 10 replaced for testing")
  else
    mod.log:warn("Aeglet registered, but Viridian Forest encounter injection was skipped")
  end
end
