# PROJECT STATE — 2026-09-17

## Current
- Canonical repo: `avenirplus/english-ladder`
- Runtime generation: v3.0.0 bootstrap + frozen v2.5.0 core
- Default teaching context: 2026 / LE1 / 論理・表現Ⅰ / Grade 1
- Lesson 8 practice and recitation moved to external JSON with stable IDs
- Recitation `noRead` behavior enabled for Stage 1–3
- Legacy localStorage migration enabled

## Material inventory migrated today
- `pack_e_lesson8_jodoushi1_yoshu`
- `pack_e_lesson8_anshou` (23 model sentences, 92 ladder questions)

## Next material work
- Add Lesson 9+ JSON via the manifest; do not enlarge the frozen core.
- When a future course/year is introduced, add its metadata and folders rather than copying the app.

## Known boundary
- The repository is currently public. Client-side phrase/password gates are not server-side access control. Deployment/access-control work is separate from the learning-engine refactor.
