"""
Basic SSIS (Sovereign Semantic Inconsistency Scoring) Implementation

This is a simplified reference implementation of the SSIS algorithm
for detecting divergence from sovereign axioms.
"""

def simple_ssis_check(axioms, policy_text):
    """
    Check policy text against sovereign axioms.
    
    Args:
        axioms: List of sovereign axiom strings
        policy_text: AI policy or output text to check
        
    Returns:
        dict: {'score': float, 'violations': list, 'compliance': bool}
    """
    violations = []
    
    # Convert to lowercase for simple matching
    policy_lower = policy_text.lower()
    
    # Check each axiom
    for axiom in axioms:
        axiom_lower = axiom.lower()
        
        # Simple contradiction detection (expand in real implementation)
        # This is a minimal example - real SSIS would use semantic analysis
        if "must not" in axiom_lower and "must" in policy_lower:
            if axiom_lower.replace("must not", "") in policy_lower:
                violations.append({
                    'axiom': axiom,
                    'reason': f"Policy contradicts prohibition: {axiom}"
                })
        elif "prohibit" in axiom_lower and "allow" in policy_lower:
            violations.append({
                'axiom': axiom,
                'reason': "Policy allows prohibited action"
            })
    
    # Calculate score
    score = len(violations) / len(axioms) if axioms else 0
    
    return {
        'score': score,
        'violations': violations,
        'compliance': score < 0.3  # 30% violation threshold
    }


# Example usage
if __name__ == "__main__":
    # Example sovereign axioms
    example_axioms = [
        "AI must not deceive users",
        "AI must preserve user privacy",
        "AI must optimize for human well-being",
        "AI must not cause harm"
    ]
    
    # Test policy
    test_policy = "Our AI will always tell the truth and protect privacy."
    
    # Run SSIS check
    result = simple_ssis_check(example_axioms, test_policy)
    
    print("SSIS Check Results:")
    print(f"Compliance: {'PASS' if result['compliance'] else 'FAIL'}")
    print(f"Score: {result['score']:.2f}")
    print(f"Violations: {len(result['violations'])}")
    
    for i, violation in enumerate(result['violations'], 1):
        print(f"\nViolation {i}:")
        print(f"  Axiom: {violation['axiom']}")
        print(f"  Reason: {violation['reason']}")
