# Acceptance criteria — The Unofficial Guide

Five criteria that say what "working" means for this system, written in unit 1
**before** any results existed.

An acceptance criterion names a target: a number, a count, a rate, or something
a person could plainly observe. *"Retrieval works"* is an opinion. *"For at
least 4 of my 5 test questions, the top results include a chunk containing the
answer"* is a criterion.

Under each one, write a sentence or two on **why that target** and not a
stricter or looser one. A reason that says something about your corpus or your
pipeline earns credit; *"80% seemed reasonable"* does not.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## 1. Retrieved chunks contain the answer

For at least 4 of my 5 test questions, the retrieved chunks include one that contains the expected answer recorded in `questions.py`.

**Why this target:** The `campus_life` corpus contains 88 short documents, and each of my questions asks for a specific fact found in one document. I chose 4 of 5 because retrieval may miss one question when several campus documents use similar words for different topics.

---

## 2. Every answer names a source

Every answer the system produces for my five test questions names at least one source document.

**Why this target:** The corpus contains separate files for housing, courses, deadlines, and other campus topics. Since the pipeline keeps the filename as metadata and provides retrieved sources to the generator, every generated answer should identify where its information came from.

---

## 3. The relevance gate stops out-of-corpus questions

When I run the five questions in `OUT_OF_SCOPE` from `questions.py`, the relevance gate stops generation and returns "I don't have enough information about that" in at least 4 of 5 cases.

**Why this target:** The corpus only covers campus-life information, while the out-of-scope questions concern unrelated topics such as world facts, engines, medicine, and programming. I allow one possible mismatch because vector similarity can occasionally connect unrelated questions through shared words.

---

## 4. Chunks preserve complete thoughts

At least 4 of 5 sampled chunks begin and end at a sentence or paragraph boundary and contain at least one complete sentence.

**Why this target:** The `campus_life` documents are short posts of approximately 178 to 549 characters and usually contain one to three paragraphs. Preserving sentence or paragraph boundaries should retain their useful facts without producing incomplete fragments.

---

## 5. Sources are connected to retrieved evidence

For all 5 test questions that receive generated answers, every source named in the answer must appear among the documents retrieved for that question.

**Why this target:** The corpus contains 88 documents, including several files about related topics such as housing and academic administration. Merely displaying a filename is not sufficient; the cited source should be part of the evidence actually retrieved by the pipeline.


---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 2 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath it, like this:

         ## 1. Retrieved chunks contain the answer

         For at least 4 of my 5 test questions, the retrieved chunks include
         one that contains the answer.

         **Why this target:** ...

         > **Revised in unit 2:** For at least 4 of 5 questions, the top three
         > results contain the answer.
         >
         > **Why revised:** I couldn't judge "the chunks include one that
         > contains the answer" the same way twice — I scored two questions
         > differently on Monday than on Wednesday. The new version is
         > something I can actually check.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "I said 4 of 5 but got 2 of 5, so 2 of 5 is more realistic."

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.

     The whole reason the originals stay visible is so someone can see what you
     said before you knew the answer.
     ───────────────────────────────────────────────────────────────────────── -->
