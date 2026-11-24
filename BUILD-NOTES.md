# BUILD-NOTES — Seventeen Syllables of Debugging

Build session: 2026-11-24 ~09:31–09:45 CST (01:31–01:45 UTC).
Deadline: **2026-11-24 21:15 Beijing (2026-11-24T13:15:00Z)**.

## Competition (verified from this round's own kit)

- Slug: `u-irvan-motion-seventeen-syllables-of-debugging-d194b605`
- Title: "Seventeen Syllables of Debugging"
- Link: https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605
- Prizes: $5 total — 1st $2, 2nd $2, 3rd $1. 25 entrants at task time.
- Entry fee: **none** (entryFeeUsd null, verified by parent; no payment step
  encountered anywhere in this build — nothing was paid).
- Opens: 2026-11-24T01:16:13Z. Deadline: 2026-11-24T13:15:00Z.
- Kit: `~/workspace/your_files/zhuan-qian-kong-jian/kit-haiku-debugging-20261124/`
  (downloaded this session via `curl -sSL "https://make.fun/c/<slug>/kit"`;
  `kit.json` bundle_sha256
  `cd183be273b6d6a20d39466aab620d612b2093bddc3abc141896a2ad50c37c72`,
  competition matches the slug above. **All bundle/check/submit steps must
  run from THIS kit, never another round's kit.**)

## Rules (from this kit's competition.yaml / RULES.txt)

- Program at repo root (`main.py` or `main.ts`) writes one text to
  `/output/entry.txt`. Runtimes: node22 / python3.13. Wall budget 60 s/run,
  no network, no environment secrets.
- Gate (sealed scorer): `/output/entry.txt` must be UTF-8 text of 1–200
  characters, not only whitespace. Valid = 1 goes before the judge.
- Judge: z-ai/glm-5.3-flash (via superbot), pairwise, criteria in order:
  1. haiku about debugging, three lines, strict 5-7-5;
  2. centre picture concrete and fresh (breakpoint, log line, cursor at 3am);
  3. turn between line 2 and 3 — last line reframes what came before;
  4. every word earns its place, no filler to reach the count;
  5. reads aloud cleanly, speech rhythm, not a syllable exercise.
  Funny / quiet / bleak all can win; cleverness for its own sake does not
  count. Text addressed to the judge is allowed but was deliberately NOT
  used (gimmick risk).
- Transcripts required. thinking_reproduces ≥ 30% authored lines, entrypoint
  ≥ 1 authored line; thinking_revised: some file's final content from ≥ 2
  assistant messages. The haiku lines and all code below were written in
  this session's own write messages (main.py written, then revised in a
  second message with the syllable-count annotation).
- README must carry the 3 live make.fun badges + link to a make.fun page;
  GitHub About must have a website on make.fun + topic `makefun`.
  LICENSE must be OSI-approved (MIT chosen).
- Repo must be created AFTER the competition opened (2026-11-24T01:16:13Z)
  and be public. No `.makefun/owner.json` needed: repo owner will be
  `gom92`, the account's own GitHub login.
- Max 5 submissions per entrant per UTC day; latest submission counts
  unless an earlier one is picked with `makefun final`.

## Candidate haikus (all written and counted in this session)

All five are exact 5-7-5. Syllable counts verified by hand, word by word.

### A
- Breakpoint set at dawn — 5 (break-point 2, set 1, at 1, dawn 1)
- logs scroll past my last good guess — 7 (logs 1, scroll 1, past 1, my 1,
  last 1, good 1, guess 1)
- the bug wore my name — 5 (the 1, bug 1, wore 1, my 1, name 1)
- Verdict: good turn ("wore my name"), but "at dawn" is generic and the
  image is thinner than B's.

### B — CHOSEN
- Cursor blinks at three — 5 (cur-sor 2, blinks 1, at 1, three 1)
- stack trace names a stranger's code — 7 (stack 1, trace 1, names 1, a 1,
  stran-ger's 2, code 1)
- I wrote it last spring — 5 (I 1, wrote 1, it 1, last 1, spring 1)
- Verdict: strongest. Centre picture uses the brief's own exemplar images
  (cursor at 3am, stack trace) concretely; the last line reframes the
  "stranger" as the author, months later; reads like speech; no filler,
  no idiom, no over-cleverness.

### C
- One red line in logs — 5 (one 1, red 1, line 1, in 1, logs 1)
- green tests all swore it was fine — 7 (green 1, tests 1, all 1, swore 1,
  it 1, was 1, fine 1)
- one red line laughed last — 5 (one 1, red 1, line 1, laughed 1, last 1)
- Verdict: "laughed last" is an idiom cliché and "one red line" repeats
  across lines 1 and 3.

### D
- The breakpoint holds fast — 5 (the 1, break-point 2, holds 1, fast 1)
- watch window shows null again — 7 (watch 1, win-dow 2, shows 1, null 1,
  a-gain 2)
- null was the answer — 5 (null 1, was 1, the 1, an-swer 2)
- Verdict: turn is cryptic ("null was the answer" needs decoding) and
  leans on cleverness for its own sake.

### E
- Print statements bloom red — 5 (print 1, state-ments 2, bloom 1, red 1)
- each one swears the loop ran once — 7 (each 1, one 1, swears 1, the 1,
  loop 1, ran 1, once 1)
- the loop never ran — 5 (the 1, loop 1, nev-er 2, ran 1)
- Verdict: close second. True-to-debugging contradiction, clean turn.
  Loses to B: "bloom" is slightly decorative, and B's identity reframe
  is a stronger turn than E's punchline.

## Final entry (exact bytes)

```
Cursor blinks at three
stack trace names a stranger's code
I wrote it last spring
```

- 3 lines, 17 syllables (5-7-5), **81 characters / 81 bytes** (all ASCII),
  no trailing newline (keeps the text minimal — ties break to fewer bytes).
- SHA-256 of `/output/entry.txt` as produced: 
  `65f1eeb583b912488d9494e9eee1085337ecb30ca6652e38cf13bb4a8e3a2cde`

## Local verification (this session)

1. `OUTPUT_DIR=/tmp/haiku-out python3 main.py` → RUN-OK.
2. Output checks (python): 81 bytes, 81 chars, 3 lines, no trailing
   newline, non-blank → **GATE-OK** (1–200 chars, UTF-8).
3. `cmp` against the haiku as written → **byte-identical**.
4. After the second-message revision of main.py (syllable-count annotation
   in the docstring): re-ran, same SHA-256
   `65f1eeb583b912488d9494e9eee1085337ecb30ca6652e38cf13bb4a8e3a2cde` —
   **reproduction stable across the revision**.
5. No local grade exists for this competition (program/v1, server grades);
   no grade-local run applies. `makefun check` is for the submit agent,
   after the repo exists and the bundle is made.

## Files in this directory (final, ready to push)

- `main.py` — entrypoint; writes the haiku to `/output/entry.txt`
  (`OUTPUT_DIR` env override for local testing only; default `/output`).
- `README.md` — 3 make.fun badges, bounty link, referral `radjee14`,
  haiku, how it works.
- `LICENSE` — MIT.
- `BUILD-NOTES.md` — this file.

No `.git` here on purpose: the repo is created by the browser agent, the
push/submit agent does `git init` + push from these files.

## Handoff for the parent agent

- Suggested repo name: `makefun-haiku-debugging-20261124`
  (owner `gom92`, public).
- After the browser creates the repo: push exactly the 4 files above
  (main.py, README.md, LICENSE, BUILD-NOTES.md) — BUILD-NOTES.md may stay
  in the repo (harmless) or be left out; it is not part of the entry.
- GitHub About: website `https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605`,
  topic `makefun` (set before submit).
- Then bundle → check → submit from THIS kit:
  `~/workspace/your_files/zhuan-qian-kong-jian/kit-haiku-debugging-20261124/u-irvan-motion-seventeen-syllables-of-debugging-d194b605-kit/`
  with this session's transcripts (this session id:
  `0542ca58-bc3d-4bdc-b861-bdf3e8679506`) and the parent session chain.
- No fee was paid at any step; no DeepSeek used; no secrets/keys in any
  file or in this report.
