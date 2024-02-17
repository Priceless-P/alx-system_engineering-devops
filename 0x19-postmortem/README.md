# Postmortem: WordPress Misconfiguration

![Captain Debug vs. Typo Troublemaker](https://github.com/Priceless-P/alx-system_engineering-devops/assets/88077456/aad41702-4e59-4e62-8344-fe1b637bc3f6)

## Summary of the issue:
- **Duration:** February 13, 2024, from 04:00 AM to 08:30 AM (UTC)
- Our WordPress site was down for about 4 hours and 30 minutes, showing a 500 error message to visitors.
- **Root Cause:** A small mistake in one of the WordPress setup files made the server confused about how to handle certain things, leading to the site crashing.

## Timeline:
- **04:11 AM:** Our system noticed lots of errors popping up as people tried to visit the site.
- **05:15 AM:** We started looking into it, thinking something might be wrong with the server.
- **05:20 AM:** We went down the wrong path, thinking it was a hardware issue, which was a dead end.
- **07:25 AM:** We got our developers involved, and they found out it was actually a little typo in one of the setup files.
- **08:30 AM:** We quickly fixed the typo using Puppet, and everything went back to normal.

## Root Cause and Resolution:
- **Root Cause:** There was a small mistake in one of the WordPress settings files that confused the server and caused it to crash. Instead of “php” we wrote “phpp”.
- **Resolution:** We used a tool called Puppet to find and fix the mistake in the settings file, so the server knew what to do again.

## Corrective and Preventative Measures:
- **Improvements/Fixes:**
  - We're going to be more careful with setup files in the future and double-check them to avoid simple mistakes.
  - We'll keep a closer eye on our monitoring systems to catch problems earlier.
  - We'll make sure everyone on the team knows how to use Puppet to fix these kinds of issues quickly.

- **Tasks:**
  - Update our documentation to include best practices for setting up WordPress.
  - Train our team on how to spot and fix these kinds of mistakes.
  - Set up automated tests to catch similar mistakes before they cause problems.

This issue taught us the importance of paying attention to the small details in our setup files. By fixing the mistake quickly and learning from it, we've made our site more stable and prevented similar issues in the future. Remember, even small typos can cause big problems, so always double-check your work!
