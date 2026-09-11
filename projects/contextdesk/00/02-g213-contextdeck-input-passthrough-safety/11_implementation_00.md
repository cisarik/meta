#! Fresh Implementation Worker — fix uinput ACL ordering

Logical whole:
g213-contextdeck-input-passthrough-safety

Worker session ordinal:
11

Worker exchange ordinal:
00

Worker session target:
fresh-worker-session

Native planning mode:
not-used

Status:
bounded S5/G3 production fix

Repository:
 /home/agile/Projects/contextdesk

Baseline candidate:
899df8fc14a2ad67594ff432f1b00d9ab155fd79

Required AP pin:
7ef45da756ed3cc14808e89bf25d0a9f9aba5d26

The fresh S5/G4 acceptance reached a new blocker. The current rule:

KERNEL=="uinput", RUN+="/usr/bin/setfacl -m u:contextdeck-broker:rw /dev/uinput"

is inside 62-contextdeck-broker.rules. `udevadm test --action=add` proves that the rule matches and queues this RUN command, but the queued order is:

1. /usr/bin/setfacl -m u:contextdeck-broker:rw /dev/uinput
2. uaccess builtin

Afterward `/dev/uinput` still has the session ACL but not the contextdeck-broker ACL. Therefore the later uaccess processing overwrites the earlier setfacl result.

Implement the smallest robust repository fix:

- Keep the G213 event-node rule in 62-contextdeck-broker.rules unchanged in security meaning.
- Remove the uinput RUN rule from that early file.
- Add a later udev rule file, preferably:
  packaging/udev/99-contextdeck-broker-uinput.rules
- The later rule must narrowly match the uinput misc device and add:
  user:contextdeck-broker:rw-
  without changing the existing group, mode, or session-user uaccess ACL.
- Preserve all existing G213 event-node, hidraw, /dev/port, and /dev/i2c-* policy.
- Do not use OWNER for the broker user.
- Do not grant the session user access to G213 event nodes.
- Do not modify input-remapper.

Update the documented privileged install and rollback procedures so the new rule is installed and removed, and so the uinput trigger is included:

sudo udevadm control --reload-rules
sudo udevadm trigger --action=add --sysname-match=uinput --settle

Update verification documentation to require:

- /dev/uinput retains the session-user ACL;
- /dev/uinput gains user:contextdeck-broker:rw-;
- the contextdeck-broker user can read and write /dev/uinput;
- G213 event/hidraw, /dev/port, and /dev/i2c-* policies remain unchanged.

Add or update device-free/static tests where useful. Validate udev rule syntax and run the existing build and CTest suite using the documented clean PATH workaround if needed.

Strict exclusions:

- Do not start, enable, restart, reload, arm, or grab contextdeck-broker.
- Do not open G213 event nodes or /dev/uinput from product code.
- Do not modify input-remapper.
- Do not modify META, AP, AGENTS.md, or handout files.
- Do not log key codes, key names, scan values, raw HID data, serials, or typed text.
- Do not perform privileged host installation in this Worker session.

The Worker may commit and push the ContextDeck repository change if the resulting implementation is complete. It must not modify or archive META.

Report exact changed paths, tests, commit hash, and remaining host-install steps. Do not claim G4 acceptance or logical-whole closure.

Expected manual META archive:

projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/11_implementation_00.md
projects/contextdesk/00/02-g213-contextdeck-input-passthrough-safety/11_report_00.md