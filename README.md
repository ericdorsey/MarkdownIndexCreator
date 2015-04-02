From the folder you run it in (and including that folder):

* Finds all `.md` files recursively in subdirs 
* Creates a master `index.md`, and adds Markdown relative links inside that `index.md` for all recursively found `.md` files in subdirs.

Example:

Given this folder structure and files:

```
.
├── README.md
├── derp
│   ├── derp.md
│   ├── derp.txt
│   └── derp_sub
│       ├── blah
│       │   └── okay.md
│       ├── huh.md
│       └── stay.md
├── dr_evil
│   └── okaytestfolder_go
│       └── another.md
├── foo.md
├── indexmaker.py
└── test123
    ├── second.md
    ├── test123.md
    └── test123.txt
```

Generates this `index.md`:

```
[foo.md](./foo.md)

[README.md](./README.md)

[derp/derp.md](derp/derp.md)

[derp/derp_sub/huh.md](derp/derp_sub/huh.md)

[derp/derp_sub/stay.md](derp/derp_sub/stay.md)

[derp/derp_sub/blah/okay.md](derp/derp_sub/blah/okay.md)

[dr_evil/okaytestfolder_go/another.md](dr_evil/okaytestfolder_go/another.md)

[test123/second.md](test123/second.md)

[test123/test123.md](test123/test123.md)
```

