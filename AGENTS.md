# HIVESOC working agreements

## Source synchronization

- The owner authorizes committing and pushing completed HIVESOC code updates to the corresponding GitHub repositories as part of delivery. Preserve unrelated work, run relevant checks, and exclude credentials, runtime data and generated artifacts. Report the exact pushed commits and any blocker; never claim synchronization before verifying the remote refs.
- Update component commits first, then Web compatibility pins and the parent repository version lock. A source push does not authorize a production deployment or a CI permission change.
