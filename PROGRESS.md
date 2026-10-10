|     Member     | Week | Exercise | Issue | Reviewer | Tests | Hours |
|----------------|------|----------|-------|----------|-------|-------|
| tlkha06112007  |  w1  |   W1-5   | #4    | Van-Huu-Phuc, NQThuan25127515 |passed | 0.5  |
| NQThuan25127515|  w1  |   W1-5   | #6    | khoavn1302 |passed | 1    |
| khoavn1302     |  w1  |   W1-1   | #10   | tmvuonghoang |passed | 1    |
| Van-Huu-Phuc   |  w1  |   W1-1   | #13   | tmvuonghoang |passed | 0.5  |
| vthung2536     |  W1  |   W1-2   | #8    | NhatQuang2007-Data |passed | 1.5  | 
| tmvuonghoang   |  w1  |   W1-3   | #22   | vthung2536 |passed | 2    |
|NhatQuang2007-Data|  w1  |  w1-6  |#21    | tlkha06112007 |passed |3     |

## Review notes

Notes prepared for the assigned reviewers, based on the current Week 1 code.

1. **Trinh → Member 1 (khoavn1302):** Clear code with correct calculations and empty-list handling. Replace `"Error !"` with a more descriptive message.
2. **Quang → Member 2 (vthung2536):** Word counting and sorting work well, including ties. Remove the unused `string` import to fix the Ruff errors.
3. **Hung → Member 3 (tmvuonghoang):** Simple and readable. Correctly checks both eligibility requirements and returns all missing conditions.
4. **Phuc → Member 5 (tlkha06112007):** Clean and concise. Courses are correctly grouped by day and sorted by name.
5. **Khoa → Member 4 (NQThuan25127515):** The algorithms passed the cases checked, and the comments are helpful. Document that `transpose` requires equal-length rows to avoid silently losing elements.
6. **Thuan → Member 5 (tlkha06112007):** The grouping logic is easy to follow. Empty input returns an empty dictionary, and the original list is left unchanged.
7. **Kha → Member 6 (NhatQuang2007-Data):** Password checks are clear, and reusing `check_password` avoids duplicated logic. Brief docstrings would help explain the two functions.
8. **Trinh → Member 7 (Van-Huu-Phuc):** Correctly merges stock quantities without changing the inputs. `low_stock` uses the right threshold and returns sorted results.
