From the folder you run it in (and including that folder):

* Finds all `.md` files recursively in subdirs 
* Creates a master `index.md`, and adds Markdown relative links inside that `index.md` for all recursively found `.md` files in subdirs.

Example:

Given this folder structure and files:

```
.
├── LICENSE.txt
├── README.md
├── example_dir1
│   ├── another_dir1.md
│   └── dir1.md
├── example_dir2
│   └── dir2_subdir
│       └── subdir2.md
├── index.md
├── indexmaker.py
└── root_md.md
```

Generates this `index.md`:

```
[README.md](./README.md)

[root_md.md](./root_md.md)

[example_dir1/another_dir1.md](example_dir1/another_dir1.md)

[example_dir1/dir1.md](example_dir1/dir1.md)

[example_dir2/dir2_subdir/subdir2.md](example_dir2/dir2_subdir/subdir2.md)

```

