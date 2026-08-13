from collections import Counter
from collections import defaultdict

"""
2. Counter vs defaultdict — a distinction worth carrying. 
Counter is semantically for counting occurrences; 
using it to sum arbitrary amounts works but reads slightly off to a careful reviewer.
The tool that says "I'm accumulating a running total" is defaultdict:
"""


def txn_data(transactions: list[dict[str, str | float]]):
    totals_counter = Counter()
    totals_default = defaultdict(float)


    for txn in transactions:
        if 'category' in txn and 'amount' in txn:
            totals_default[txn["category"]] += txn["amount"]

    return dict(totals_default)


txn = [
    {"category": "food", "amount": 12.5},
    {"category": "food", "amount": 8},
    {"category": "travel", "amount": 40},
    {"category": "food"},  # missing amount — skip it
    {"amount": 5},  # missing category — skip it
]

print(txn_data(txn))
