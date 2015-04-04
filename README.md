From the folder you run it in:

* Finds all Markdown files in current folder (folder it was run from)
* Recursively finds all Markdown files in subdirs 
* Creates `index.md`, and adds Markdown relative links inside that `index.md` for all found Markdown files.

Supported file extensions: `.markdown`, `.mdown`, `.mkdn`, `.md`, `.mkd`, `.mdwn`

Example; given this folder structure and files:

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

If an existing `index.md` is found it is renamed `index_old.md`

Note the script doesn't add a link for itself, ie, no link is created for `index.md` or `index_old.md`. In the scenario above `indexmaker.py` had previously been run so there was already a prior `index.md` in the root of the folder.


