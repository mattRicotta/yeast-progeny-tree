# Yeast Progeny Tree

NOTE: Requires installation of treelib library

Python code to build a progeny tree (hierarchy) from a yeast harvesting table where Parent_ID is the ID of the parent yeast source.

Set progenitor_id to the ID of the yeast record whose progeny you want to see.

Example Output:

        4: HEF 153 | 154
        ├── 5: HEF 167 | 168
        │   └── 6: HEF 189 | 190
        │       ├── 7: AA 206
        │       ├── 7: COAST 203A
        │       ├── 7: HEF 203 | 205
        │       │   └── 8: HEF 211 | 212
        │       │       ├── 9: AA 221 | 222
        │       │       └── 9: HEF 219 | 220
        │       │           ├── 10: AA 225
        │       │           ├── 10: AA 230
        │       │           └── 10: HEF 228 | 229
        │       │               ├── 11: AA 236 | 237
        │       │               ├── 11: AA 236A
        │       │               ├── 11: AA 236B
        │       │               └── 11: HEF 240 | 241
        │       │                   ├── 12: AA 248 | 249
        │       │                   ├── 12: HEF 253
        │       │                   │   └── 13: AA 259
        │       │                   └── 12: HEF 254
        │       │                       └── 13: HEF 264 | 265
        │       └── 7: RSLAG 204
        ├── 5: HEF 181 | 182
        │   └── 6: AA 195 | 196
        └── 5: PBLAG 176