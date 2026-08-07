# Quiz — Plan, apply, destroy

1. Why apply a saved plan?
   - A. To apply the exact reviewed change set
   - B. To skip provider authentication
   - C. To remove state
   - D. To avoid validation

2. What does a `-/+`-style action indicate?
   - A. Replacement
   - B. Read-only refresh
   - C. Output only
   - D. Backend migration

3. Can `create_before_destroy` always avoid downtime?
   - A. Yes
   - B. No; quotas and uniqueness may prevent overlap
   - C. Only for outputs
   - D. Only without state

4. What does `prevent_destroy` do?
   - A. Rejects plans that destroy the protected resource
   - B. Backs up the resource
   - C. Blocks all updates
   - D. Encrypts state

5. Why avoid routine `-target` use?
   - A. It can produce an intentionally incomplete graph operation
   - B. It formats too much
   - C. It deletes providers
   - D. It disables outputs
