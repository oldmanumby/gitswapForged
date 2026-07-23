import re

with open('CHANGELOG.md', 'r') as f:
    content = f.read()

# Replace ### [ with ## [
content = re.sub(r'^### \[', '## [', content, flags=re.MULTILINE)

# Remove the 1.3.8 section which is empty and invalid
content = re.sub(r'## \[1\.3\.8\][^\n]*\n+', '', content)

# Add descriptors for 1.3.9
replacement_139 = """## [1.3.9](https://github.com/oldmanumby/gitwarp/compare/v1.3.7...v1.3.9) (2026-07-23)

### Refactors

- resolve complexity errors across core modules ([c1684f9](https://github.com/oldmanumby/gitwarp/commit/c1684f9458b6114e7430bd6b2f87214cce0a6b50))
"""
content = re.sub(r'## \[1\.3\.9\][^\n]*\n+', replacement_139 + '\n', content)

# Add descriptors for 1.3.6
replacement_136 = """## [1.3.6](https://github.com/oldmanumby/gitwarp/compare/v1.3.5...v1.3.6) (2026-07-22)

### Chores

- format font quotes ([0acace0](https://github.com/oldmanumby/gitwarp/commit/0acace0))
"""
content = re.sub(r'## \[1\.3\.6\][^\n]*\n+', replacement_136 + '\n', content)

# Note: 1.3.4 and 1.3.5 have exactly the same commits in the current file!
# 1.3.4:
# - brute force CSS variables for blume docs theme ([40960a3]...
# - resolve docs styling issues by using native theme.css ([0f337bf]...
# 1.3.5:
# - brute force CSS variables for blume docs theme ([40960a3]...
# - resolve docs styling issues by using native theme.css ([0f337bf]...
# Let's clean up 1.3.4 since they are duplicates (standard-version got confused earlier).
content = re.sub(r'## \[1\.3\.4\].*?## \[1\.3\.3\]', '## [1.3.3]', content, flags=re.DOTALL)

with open('CHANGELOG.md', 'w') as f:
    f.write(content)
