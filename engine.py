from dataclasses import dataclass
from typing import List, Set, Dict, Any

@dataclass
class Rule:
    antecedents: List[str]
    consequent: str
    priority: int = 0
    name: str = ""

class ForwardChainingEngine:
    def __init__(self, rules: List[Rule]):
        self.rules = rules
        self.facts: Set[str] = set()
        self.trace: List[Dict[str, Any]] = []

    def assert_facts(self, initial: List[str]) -> None:
        """Store initial facts into the working memory."""
        self.facts.update(initial)

    def can_fire(self, rule: Rule) -> bool:
        # Check if the rule can be fired based on the current facts.
        if rule.consequent in self.facts:
            return False
        return all(antecedent in self.facts for antecedent in rule.antecedents)

    # Run the forward chaining engine until no more rules can fire.
    def run(self) -> None:
        changed = True
        while changed: 
            changed = False
            # Iterate over the rules in order of priority, firing them if possible.
            for rule in sorted(self.rules, key=lambda r: r.priority, reverse=True):
                if self.can_fire(rule):
                    self.facts.add(rule.consequent)
                    self.trace.append({
                        "rule": rule.name,
                        "antecedents": rule.antecedents,
                        "consequent": rule.consequent
                    })
                    changed = True

    # Return the conclusions separated into recommendations, specs, and other facts.
    def conclusions(self) -> Dict[str, List[str]]:
        recommendations = []
        specs = []
        other_facts = []
        fired_facts = [entry["consequent"] for entry in self.trace]
        ordered_facts = fired_facts + sorted(self.facts.difference(fired_facts))
        for fact in ordered_facts:
            if fact.startswith("recommend:"):
                # Remove the "recommend:" prefix before adding to the list
                recommendations.append(fact.replace("recommend:", ""))
            elif fact.startswith("spec:"):
                # Remove the "spec:" prefix before adding to the list
                specs.append(fact.replace("spec:", ""))
            else:
                other_facts.append(fact)
        return {
            "recommendations": recommendations,
            "specs": specs,
            "other_facts": other_facts
        }   
    pass
