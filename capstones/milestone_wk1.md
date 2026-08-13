Milestone — Week 1 cleaning toolkit: complete ✅

You now own the full motion that turns raw, broken data into something a model can eat. Worth stating plainly what each piece is in job terms, because this is exactly what "data cleaning / preprocessing" means on a job description:

Diagnose (.info(), .isnull().sum()) — you never touch data before you know where the holes and types are.
Impute (median fill, and the smarter grouped median) — you fill gaps with defensible estimates instead of deleting rows you can't afford to lose.
Prune — you drop mostly-empty columns and redundant twins, and you never drop the target.
Encode (get_dummies, dtype=int, drop_first) — you translate categories into numbers, and you know ordinal from nominal so you don't invent fake rankings.
Transform (log1p on skewed money variables) — you tame long tails without throwing away real signal.



All three land, and the third one especially tells me you actually looked instead of assuming. Let me take them in turn.

1. who → nominal. Correct. No natural order across man/woman/child, so you can't put them on a single ranked scale. One subtlety worth planting: child secretly carries an age signal (a child is younger), so there's a whiff of information there — but since man vs. woman has no order, the trio as a whole is nominal. That instinct — "wait, is there hidden signal in this category?" — is exactly the thinking that leads to feature engineering later. Good eye, right call.

2. You combined both columns into one get_dummies call. That's better than the two-call version I showed you — it's the "one pass, not two" instinct now firing on its own, unprompted. That's the point where a lesson stops being something I'm pushing and becomes how you actually think. Correct and clean.

3. "They are booleans" — yes, and this is the surprise I wanted you to catch. Older tutorials all show get_dummies producing 0/1 integers. Modern pandas (2.x, which Colab runs) returns True/False bools instead — which is why you saw what you saw. Here's why it matters and why it's a trap:

Most of the time it just works, because Python treats True as 1 and False as 0, so scikit-learn quietly casts them when it fits a model. But it bites you in three spots: some libraries and older code expect literal 0/1 and choke on bools; arithmetic or aggregations can behave unexpectedly; and honestly, 0/1 is just cleaner and more predictable to reason about.