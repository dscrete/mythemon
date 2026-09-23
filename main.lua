local SPECIES = "MYTHMON_AEGLET"
local CHARM = "MYTHMON_MYTH_CHARM"
local CHARM_EFFECT = "MYTHMON_FORCE_ENCOUNTER"
local FORCE_KEY = "forceAegletEncounter"

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
  local Bag = require("src.inventory.Bag")

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

  -- A permanent testing utility for Mythmon development. Using it outside
  -- battle arms the next real wild encounter; the species hook consumes the
  -- flag only after an encounter has actually rolled, so empty grass steps do
  -- not waste it. The item itself is never consumed.
  mod.content.item_effects:register(CHARM_EFFECT, {
    field = true,
    battle = false,
    needsTarget = false,
    use = function()
      if mod.save:get(FORCE_KEY, false) then
        return "kept", { "The MYTH CHARM is\nalready resonating." }
      end
      mod.save:set(FORCE_KEY, true)
      return "kept", { "The MYTH CHARM\nbegins to hum...\fA strange presence\ndraws near." }
    end,
  })

  mod.content.items:register(CHARM, {
    id = CHARM,
    name = "MYTH CHARM",
    price = 0,
    keyItem = true,
    tossable = false,
    needsTarget = false,
    effect = CHARM_EFFECT,
  })

  mod.hooks:wrap("encounter.species", function(next, enc, ctx)
    local rolled = next(enc, ctx)
    if rolled and mod.save:get(FORCE_KEY, false) then
      mod.save:set(FORCE_KEY, false)
      rolled.species = SPECIES
      rolled.level = 5
      mod.log:info("MYTH CHARM forced the next wild encounter to Aeglet")
    end
    return rolled
  end)

  -- Existing saves receive the testing charm automatically. If the Gen 1 bag
  -- is full, leave the save untouched and log a useful warning instead.
  mod.events:on("game.ready", function(ev)
    local game = ev and ev.game
    local save = game and game.save
    if not save then return end
    save.inventory = save.inventory or {}
    if save.inventory[CHARM] then return end
    if Bag.add(save, CHARM, 1, game.data) then
      mod.log:info("MYTH CHARM added to the bag")
    else
      mod.log:warn("MYTH CHARM could not be added because the bag is full")
    end
  end)

  -- Normal placement remains deliberately rare. Replace only the rarest
  -- Viridian Forest slot while preserving whatever encounter table exists
  -- ahead of this mod.
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
