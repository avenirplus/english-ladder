# AGENTS.md — English LADDER

- Treat `docs/REQUIREMENTS.md`, `docs/DECISIONS.md`, and `docs/PROJECT_STATE.md` as source of truth.
- Preserve backward compatibility with existing learner data unless an explicit migration is implemented.
- Never rename a live pack/question ID merely for aesthetics.
- New official materials belong under `materials/` and in `materials/manifest.json`; do not paste large packs into the frozen core.
- Preserve the recitation ladder: きく → 句 → 語 → かく.
- Stage 1–3 recitation questions must keep `noRead:true`; Stage 3 must keep `lenient:true` and `recite:true`.
- `app-core-v2.5.0.html` is a frozen compatibility artifact. Do not edit it directly. Change bootstrap patches deliberately or replace the core only after regression testing.
- Current default context is not the product identity. English LADDER must remain reusable across school years and English courses.
