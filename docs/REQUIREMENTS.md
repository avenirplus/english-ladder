# REQUIREMENTS — English LADDER

## Product scope
- English LADDER is one long-lived platform for the subject English.
- It must support multiple school years, English courses, grades, classes, students, lessons, and material types without cloning the app.
- Current default context is 2026 / 論理・表現Ⅰ / Grade 1, but this is configuration, not product identity.

## Identity dimensions
- App: `english-ladder`
- School year: `schoolYear`
- Course: `courseCode`, `courseName`
- Grade: `grade`
- Class and number: `studentInfo.cls`, `studentInfo.num`
- Student/profile: profile `id`
- Material: stable pack `id` plus `version`, `lesson`, `materialType`

## Material rules
- Runtime schema remains `juken-pack@1` for backward compatibility.
- Extra English LADDER metadata is allowed and ignored by the old engine when unused.
- Stable pack/question IDs must be preserved when moving a live material from baked HTML to JSON so review history survives.
- Official materials live under `materials/` and are enumerated by `materials/manifest.json`.

## Recitation ladder
For one model sentence:
1. Stage 0 `きく`: listening input; audio is available and automatically used.
2. Stage 1 `ならべる（句）`: reconstruct by chunks; `noRead:true`.
3. Stage 2 `ならべる（語）`: reconstruct by words; `noRead:true`.
4. Stage 3 `かく`: full-sentence retrieval; `lenient:true`, `recite:true`, `noRead:true`.

After answering, the correct sentence may be played and the learner can record completion of three read-aloud repetitions.

## Compatibility
- Existing `englishQuestClassroomOS1_student` localStorage data must migrate to `englishLadder:v3` without deleting the old key.
- Existing results/review stats must continue to resolve via unchanged pack/question IDs.
