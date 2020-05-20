# 宇佐見 蓮子 // Usami Renko

**星を見ただけで今の時間が分かり、月を見ただけで今居る場所が分かる程度の能力**

Usami Renko is a character from the Touhou Project series that has the ability to tell what time it is by the stars, and where she is by the moon. Needless to say, these traits make her a friend of any mapper. 

Here, she exists as a utility Discord bot, converting timestamps copied from the osu! editor (currently only supporting osu! standard) into clickable links on Discord. Any message sent containing an osu! editor timestamp will be replaced by a message from Renko that replaces the timestamps with clickable versions and maintains the rest of the message as it was originally sent. 

Invite her to your server [here](https://discord.com/api/oauth2/authorize?client_id=299298159191130113&permissions=92160&scope=bot)! She's doing her best at the moment but please be advised she's still learning!

If she causes you any trouble or refuses to do something, you can open an issue here on this repository or message me [@thunderbird2678](https://twitter.com/thunderbird2678) or on Discord (thunderbird#2678)!

---

Changes as of 19 May 2020:

* Added support for osu! Mania
* Added support for copying editor times without hitobjects
* Fixed a bug where timestamps over 256 characters wouldn't show properly
* Implemented additional logging
* Added the dash behind the timestamp back in (I think it looks cleaner for modding but I may be mistaken)
* Updated OAUTH URL (please reinvite her if you added her before this update!)

---

ToDo: 

* Add a react-based system to allow the original message sender to delete their message
* Investigate possibility of hyperlinking so I can display mania timestamps as something other than a jumbled mess

---

This is the continuation of the sextant project that I initially made for Discord's Hack Week 2019. The project is now renamed as I could not find an adequately cute picture of an anime girl using a sextant. I've been listening to ZUN's music CD's quite a bit recently and Renko seemed like a good fit. 

The source for the art is [@cyclo_stars123](https://twitter.com/cyclo_stars123/status/984554714443337729) on twitter