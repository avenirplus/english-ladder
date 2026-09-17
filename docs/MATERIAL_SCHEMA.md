# MATERIAL SCHEMA — English LADDER extension

The runtime continues to accept `schema: "juken-pack@1"`. English LADDER adds metadata fields:

```json
{
  "schema": "juken-pack@1",
  "id": "stable-pack-id",
  "version": 2,
  "subject": "英語",
  "schoolYear": 2026,
  "courseCode": "LE1",
  "courseName": "論理・表現Ⅰ",
  "grade": 1,
  "materialType": "practice | recitation | test | vocabulary | ...",
  "title": "...",
  "units": []
}
```

For recitation retrieval questions, `noRead:true` prevents the pre-answer `🔊よむ` control and automatic TTS. It does not remove post-answer model-sentence playback.

### ID rule
IDs are permanent once students have used a pack. A content revision increments `version` but keeps pack/question IDs where they represent the same learning item. This preserves spaced-repetition history.
