# 🛰️ Pivot Lab - LegionOffsec Security Sundays EP-3

## 📖 Overview

Welcome to **Episode 3** of the *LegionOffsec Security Sundays* series. This lab simulates a real-world scenario where an attacker has already compromised the DMZ (Demilitarized Zone) of a corporate network. Your mission is to leverage the existing foothold, pivot into the internal network, and capture the final flag.

This lab is designed to test and enhance your skills in:

* Network pivoting
* Post-exploitation
* Internal reconnaissance
* Exploiting internal systems

Writeup Link :  https://blog.destinyoo.com/Legion-OffSec/Legion-SS-EP03-Lab
---

## 🧪 Lab Description

This is a small-scale, Docker-based lab where you'll take control of an attacker VM and proceed to:

1. Analyze the network setup.
2. Connect to a compromised DMZ host with a running backdoor.
3. Pivot into the internal network.
4. Compromise an internal host.
5. Retrieve the final flag from `/flag.txt`.

The final goal is to demonstrate a successful breach of both the DMZ and the internal network — just like a real-world Red Team assessment.

---

## 🗒️ Note (Initial Briefing)

After SSH-ing into the attacker machine, check `note.txt`:

```bash
cat note.txt
```

Content:

> You will be engaging with a network that has already been compromised by hackers, who have been unable to fully infiltrate the internal network. Previously, the network hosted a web server, but the attackers have shut down and disabled all services, leaving only a backdoor running. Your goal is to locate the open port and host where the backdoor is running. Once discovered, you must connect to it, attempt to pivot into the internal network, identify another host, compromise it, and ultimately read the flag located at `/flag.txt`.

---

## 🧩 Network Layout

```
Kali Linux AttackBox
        |
        v
Compromised DMZ Host (Backdoor Open)
        |
        v
Internal Host (Exploit & get /flag.txt)
```

---

## 🛠️ Tools & Techniques Recommended

* SSH Tunneling / Proxychains
* Port scanning and service enumeration
* Manual payload crafting or quick one-liners
* Linux post-exploitation fundamentals

---

## 🎯 Objective

Gain access to the internal host and retrieve the flag from:

```
/flag.txt
```

---

## 🚨 Rules of Engagement

* Do **not** destroy or tamper with core services unrelated to exploitation.
* Focus on realism – avoid using automated tools unless necessary.
* Take notes; you’re encouraged to document your path as part of your red team methodology.

---

## 🧠 Tips

* Think like an attacker who found a foothold in the DMZ.
* Look for clues in the backdoor communication.
* Pivot smartly – internal hosts may not be directly accessible.

---

## 🙌 Credits

Created by **Heshan Perera** ([@Destinyoo.con](https://destinyoo.com))
Part of the **LegionOffsec Security Sundays** series.

---

## 📩 Want More?

For updates, episodes, and hands-on labs, follow **LegionOffsec**:

* 🌐 [https://legionoffensivesecurity.com](https://legionoffensivesecurity.com)
* 🐦 Twitter / X: [@LegionOffsec](https://twitter.com/LegionOffsec)

---

Happy Hacking! 🦅
**#LegionOffsec #SecuritySundays #RedTeam #PivotingLab**
