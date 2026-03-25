#!/usr/bin/env python3
"""
Patch each N*_*.md to add a model-specific explanation paragraph
after the query accounting table, explaining why the denominator is
what it is (e.g. "So every `/32` you see below means ...").
"""
import glob, os, re

REPORTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "model_reports_per_property")

# Regex to capture the Total row: | **Total** | – | **40** | **12 + 12 + 12 + 4** |
TOTAL_RE = re.compile(
    r'^\| \*\*Total\*\* \| .+? \| \*\*(\d+)\*\* \| \*\*(.+?)\*\* \|',
    re.MULTILINE,
)

# Regex to extract property rows from the accounting table
# | prop1 | 0, 2, 4 | 12 | 3 true classes × 4 non-self targets |
PROP_ROW_RE = re.compile(
    r'^\| (prop\d+) \| (.+?) \| (\d+) \| (\d+) true class',
    re.MULTILINE,
)

# Check if α=0.9 table uses a different denominator than the total
ALPHA09_DENOM_RE = re.compile(r'#### α = 0\.9\n\n\|.*\n\|.*\n\| .+? \| (\d+)/(\d+)')

MARKER = "<!-- denominator-explanation -->"


def build_explanation(model_name, total, sum_str, prop_rows, alpha09_denom):
    """Build the model-specific explanation paragraph."""
    ni, nj = model_name.replace("N", "").split("_")
    n_props = len(prop_rows)

    lines = [MARKER]
    lines.append("")

    # Build per-property breakdown sentence
    prop_parts = []
    for pname, classes, count, n_classes in prop_rows:
        class_list = classes.strip()
        prop_parts.append(f"{pname} has {n_classes} true class(es) ({class_list}) → {n_classes} × 4 = {count} queries")

    lines.append(f"**Why the denominator is {total}:**  ")
    lines.append(f"This model has {n_props} properties. "
                 f"For each property, we count how many distinct classes the network predicts "
                 f"within that property's input region (from sampling), then multiply by 4 "
                 f"(the 4 other target labels, excluding the self-target). Summing across properties:")
    lines.append("")
    for part in prop_parts:
        lines.append(f"- {part}")
    lines.append("")
    lines.append(f"**Total per ε = {sum_str} = {total}.**  ")
    lines.append(f"So every `…/{total}` you see in the tables below means "
                 f"\"out of {total} valid verification queries at that epsilon.\"  ")
    lines.append(f"The `Total Y%` column divides by {total} × 4 = **{int(total) * 4}** "
                 f"(summed across all four ε values).")

    # Special case: if α=0.9 uses a smaller denominator
    if alpha09_denom is not None and alpha09_denom != int(total):
        diff = int(total) - alpha09_denom
        lines.append("")
        lines.append(f"> **Note:** At α = 0.90 and α = 0.95, you will see `…/{alpha09_denom}` "
                     f"instead of `…/{total}`. This is because one property's experiment data "
                     f"is missing at those α levels, reducing the query count by {diff}. "
                     f"At α = 0.99 all properties have data, so the denominator is the full {total}.")

    lines.append("")
    return "\n".join(lines)


def patch_file(path):
    fname = os.path.basename(path)
    with open(path, 'r') as f:
        content = f.read()

    if MARKER in content:
        print(f"  SKIP (already patched): {fname}")
        return False

    # Extract total from accounting table
    m_total = TOTAL_RE.search(content)
    if not m_total:
        print(f"  SKIP (no Total row): {fname}")
        return False

    total = m_total.group(1)
    sum_str = m_total.group(2)

    # Extract property rows
    prop_rows = []
    for m in PROP_ROW_RE.finditer(content):
        pname = m.group(1)
        classes = m.group(2)
        count = m.group(3)
        n_classes = m.group(4)
        prop_rows.append((pname, classes, count, n_classes))

    if not prop_rows:
        print(f"  SKIP (no property rows): {fname}")
        return False

    # Check if α=0.9 uses a different denominator
    m_a09 = ALPHA09_DENOM_RE.search(content)
    alpha09_denom = None
    if m_a09:
        denom_in_table = int(m_a09.group(2))
        if denom_in_table != int(total):
            alpha09_denom = denom_in_table

    model_name = fname.replace(".md", "")
    explanation = build_explanation(model_name, total, sum_str, prop_rows, alpha09_denom)

    # Insert after the Total row line (find the end of the Total row)
    total_end = m_total.end()
    # Find the next newline after the Total row
    next_nl = content.index('\n', total_end)

    new_content = content[:next_nl + 1] + "\n" + explanation + content[next_nl + 1:]

    with open(path, 'w') as f:
        f.write(new_content)

    print(f"  PATCHED: {fname} (total={total}, props={len(prop_rows)}, α0.9_denom={alpha09_denom or total})")
    return True


def main():
    files = sorted(glob.glob(os.path.join(REPORTS_DIR, "N*_*.md")))
    print(f"Found {len(files)} model report files")
    patched = 0
    for f in files:
        if patch_file(f):
            patched += 1
    print(f"\nDone. Patched {patched}/{len(files)} files.")


if __name__ == "__main__":
    main()
