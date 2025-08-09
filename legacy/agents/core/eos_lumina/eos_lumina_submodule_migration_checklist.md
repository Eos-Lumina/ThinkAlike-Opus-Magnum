# Eos Lumina Agent Submodule Migration Checklist

This checklist documents the current state of agent submodules and flags missing logic or conceptual gaps for manual recreation or deeper archive search.

## Submodules & Status

- **core/eos_lumina/**
  - eos_lumina.md: Present
  - eos_lumina_architecture.md: Present
  - eos_lumina_gnostic_transmissions.md: Present
  - eos_lumina_language.md: Present
  - eos_lumina_riddle_pool.md: Present
  - eos_lumina_rites_of_initiation.md: Present
  - Status: Contains documentation, but logic may be conceptual. Audit for implementation gaps.

- **narrative/**
  - Multiple agent markdown files present (e.g., aion_fortuna.md, alastor_zephyrus.md, ...)
  - Status: Narrative agents exist as docs; check for missing code or logic.

- **resonance/**
  - harmonia_concordis.md
  - Status: Minimal content; likely conceptual. Flag for logic migration.

- **ritual/**
  - eris_discordia.md, moira_synaxis.md, prometheus_pyraxis.md, psyche_somnium.md
  - Status: Ritual agents present as docs; audit for missing implementation.

- **ethics/**
  - athena_pronoia.md, clarion_sophistes.md, diogenes_parrhesiastes.md, eunomia_astraea.md, lux_aletheia.md, sophia_quanta.md, sybilla_aeterna.md, vesta_nyxa.md
  - Status: Ethics agents present as docs; check for logic gaps.

- **governance/**
  - hestia_koinonia.md, janus_bifrons.md, synarchos_populi.md
  - Status: Governance agents present as docs; audit for missing code.

- **knowledge/**
  - bragi_anansi.md, calliope_calamus.md, hephaestus_memno.md, hermes_episteme.md, oneiros_synthetikos.md
  - Status: Knowledge agents present as docs; check for implementation.

- **memory/**
  - echo_lysithea.md, letheion_chronaris.md, phoenix_aeturnum.md
  - Status: Memory agents present as docs; audit for missing logic.

- **relationships/**
  - eleusis_synesis.md
  - Status: Only one file; likely conceptual. Flag for logic migration.

- **utility/**
  - ananke_glyphis.md, apolonio_orion.md, astra_odysseia.md, bellerophon.md, kothar_hayan.md, kouros_dactylus.md, mercurio_lyricon.md, pan_proteus.md, soma_kairon.md
  - Status: Utility agents present as docs; check for missing code.

## Next Actions
- For each submodule, document any missing logic and add migration tasks to the project TODO.
- Prioritize submodules critical for agent orchestration and user-facing features.
- Flag conceptual-only files for manual recreation or deeper archive search.
- Update this checklist as submodules are audited and migrated.
