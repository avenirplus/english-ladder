# DECISIONS — English LADDER

## 2026-09-17
1. `avenirplus/english-ladder` is the canonical repository.
2. English LADDER is not tied to LE1. It is the English-subject platform; 論理・表現 / 英語コミュニケーション / 選択英語等 are course contexts.
3. Do not create a separate app repository for every year/course/class.
4. Materials are external JSON selected through a manifest. Large baked material blocks are legacy compatibility only.
5. The four-stage recitation ladder is a core pedagogical feature and must be preserved.
6. Retrieval stages suppress pre-answer audio with `noRead:true`.
7. The application storage namespace is `englishLadder:v3`; year/course/class/student separation lives inside data, not in separate localStorage apps.
8. Existing v2.5 monolith is frozen as `app-core-v2.5.0.html` during the safe migration. The v3 bootstrap layers configuration and external materials on top without discarding proven functionality.
