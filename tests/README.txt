Expert System Test Cases

Test 1: Premium ultrabook
Input facts: ["budget_high", "portable", "long_battery"]
Expected recommendations: ["premium_ultrabook"]
Expected specs: []
Expected fired rules: ["Premium Ultrabook"]

Test 2: Budget ultrabook
Input facts: ["budget_low", "portable", "office_only"]
Expected recommendations: ["budget_ultrabook"]
Expected specs: []
Expected fired rules: ["Budget Ultrabook"]

Test 3: Midrange gaming laptop
Input facts: ["budget_medium", "gaming"]
Expected recommendations: ["midrange_gaming_laptop"]
Expected specs: []
Expected fired rules: ["Gaming"]

Test 4: High-end gaming laptop
Input facts: ["budget_high", "gaming"]
Expected recommendations: ["high_end_gaming_laptop"]
Expected specs: []
Expected fired rules: ["Pro Gaming"]

Test 5: Creative work with portability
Input facts: ["creative_work", "portable"]
Expected recommendations: []
Expected specs: ["ram_16_plus"]
Expected fired rules: ["Creative Portable"]

Test 6: Creative work with a large screen
Input facts: ["creative_work", "large_screen"]
Expected recommendations: []
Expected specs: ["display_15_plus_color_accurate"]
Expected fired rules: ["Creative Display"]

Test 7: Frequent travel and long battery life
Input facts: ["travel_often", "long_battery"]
Expected recommendations: []
Expected specs: ["battery_60wh_plus"]
Expected fired rules: ["Travel + Battery"]

Test 8: macOS preference
Input facts: ["pref_os_macos"]
Expected recommendations: []
Expected specs: ["macos_required"]
Expected fired rules: ["OS Preference Mapping"]

Test 9: AI acceleration requirement
Input facts: ["needs_ai_accel"]
Expected recommendations: []
Expected specs: ["gpu_with_tensor_cores"]
Expected fired rules: ["AI Acceleration"]

Test 10: Linux preference for office use
Input facts: ["pref_os_linux", "office_only"]
Expected recommendations: []
Expected specs: ["linux_friendly_hw"]
Expected fired rules: ["Linux Suitability"]

Test 11: Several rules fire
Input facts: ["creative_work", "portable", "large_screen", "travel_often", "long_battery"]
Expected recommendations: []
Expected specs: ["ram_16_plus", "display_15_plus_color_accurate", "battery_60wh_plus"]
Expected fired rules:
  - "Creative Portable"
  - "Creative Display"
  - "Travel + Battery"

Test 12: No rule matches
Input facts: ["portable"]
Expected recommendations: []
Expected specs: []
Expected fired rules: []

