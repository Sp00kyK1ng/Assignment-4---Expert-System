from kb_loader import load_rules
from engine import ForwardChainingEngine

KB_PATH = "kb/laptop_rules.json"

# Collect initial facts from the user to feed into the expert system engine
def collect_initial_facts():
    facts = []
    if input("Is portability important? (y/n): ").lower().startswith("y"):
        facts.append("portable")
    if input("Do you need long battery life? (y/n): ").lower().startswith("y"):
        facts.append("long_battery")
    budget = input("What is your budget? (high/medium/low): ").lower()
    if budget == "low":
        facts.append("budget_low")
    elif budget == "medium":
        facts.append("budget_medium")
    elif budget == "high":
        facts.append("budget_high")
    work = input("What will you primarily use the laptop for? (office/gaming/creative): ").lower()
    if work == "office":
        facts.append("office_only")
    elif work == "gaming":
        facts.append("gaming")
    elif work == "creative":
        facts.append("creative_work")
    if input("Do you travel often? (y/n): ").lower().startswith("y"):
        facts.append("travel_often")
    if input("Do you need linux compatibility? (y/n): ").lower().startswith("y"):
        facts.append("pref_os_linux")
    if input("Do you need macOS compatibility? (y/n): ").lower().startswith("y"):
        facts.append("pref_os_macos")
    if input("Do you need AI Acceleration? (y/n): ").lower().startswith("y"):
        facts.append("needs_ai_accel")
    if input("Do you need a large screen? (y/n): ").lower().startswith("y"):
        facts.append("large_screen")
    return facts

# Main function to run the expert system
def main():
    # Load the rules from the knowledge base file
    rules = load_rules(KB_PATH)
    while True:
        engine = ForwardChainingEngine(rules)
        facts = collect_initial_facts()
        engine.assert_facts(facts)
        engine.run()
        results = engine.conclusions()

        # Print the results of the expert system inference
        print("Recommendation(s):")
        if results["recommendations"]:
            for rec in results["recommendations"]:
                print(" -", rec)
        else:
            print(" - None")

        print("Specs:")
        if results["specs"]:
            for spec in results["specs"]:
                print(" -", spec)
        else:
            print(" - None")

        print("Rules Fired:")
        if engine.trace:
            for fired in engine.trace:
                print(f" - {fired['rule']} -> {fired['consequent']}")
        else:
            print(" - None")
        # Prompt the user to run the expert system again for easy evaluation of multiple test cases
        if not input("Run the expert system again? (y/n): ").strip().lower().startswith("y"):
            break

if __name__ == "__main__":
    main()
