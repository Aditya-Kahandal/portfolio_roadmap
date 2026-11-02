# Day 3 — Monday, 2 November 2026

## Focus

Set up a reusable Python environment and continue arrays/hash maps practice. Actual study time was not recorded.

## Completed

### Reusable Python environment

- Created the virtual environment at the root of the roadmap workspace so child project folders can use it throughout the plan.
- Installed and checked the planned Python learning packages and Jupyter.
- Added a root-level `.gitignore` for the shared workspace setup.
- Created a Jupyter notebook in the workspace directory.
- Saved the environment/package version information as part of the setup task. Exact versions were not recorded in this log.

### LeetCode 1282 — Group the People Given the Group Size They Belong To

- Built a dictionary that groups person IDs by their required group size.
- Split each bucket into groups using a step size equal to the required group size and list slices.
- Reviewed the solution as correct for the problem constraints. LeetCode acceptance status was not reported.
- Complexity: `O(n)` time and `O(n)` space, including the grouped people and output.
- Learning note: two linear passes are still `O(n)`; using one pass would be a streaming style change, not an asymptotic improvement.

## Not completed / in progress

### Custom problem — Longest Alert Segment with At Most `k` Distinct IDs

- Not solved today. The original description was unclear, so the task was clarified as finding the longest contiguous section of the list containing no more than `k` distinct IDs. A sliding-window direction was discussed, but no implementation was submitted.

## Reflection

The Python environment and notebook are now set up for reuse across the roadmap workspace. The custom problem needs a clearer manual walkthrough before implementation. No completion is claimed for that problem.

## Next session

Continue the Day 4 Python exercise from the roadmap. Before returning to the custom problem, manually trace a small input, identify which contiguous segments are valid, and write down what the algorithm must keep track of. Then attempt the implementation independently.
