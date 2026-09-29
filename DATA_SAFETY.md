# Public portfolio data-safety checklist

- [ ] No TrackMan CSVs
- [ ] No raw player-level tracking observations
- [ ] No internal snapshots or downloaded databases
- [ ] No API keys, passwords, tokens, or credentials
- [ ] No private workplace URLs
- [ ] No proprietary roster/name mapping files
- [ ] No generated exports containing raw workplace data
- [x] Published CCL screenshots/result-level statistics have been confirmed shareable by the author
- [x] CCL synthetic demo uses fictional records
- [x] Research documents are public/shareable
- [ ] Internship/workplace code is included only if authorized

## Important

`.gitignore` is a safety net, not a deletion mechanism. A file that was already committed can remain in Git history even after being ignored or deleted. Review history if a sensitive file has ever been committed.
