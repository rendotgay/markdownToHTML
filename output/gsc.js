/*
 * highlight.js language definition for GSC (Game Script Code)
 * Based on the Sublime Text tmLanguage definition for GSC
 */

window.gsc = function(hljs) {
    const KEYWORDS = {
        keyword: 'if else while for foreach in do return continue break switch case default',
        'keyword.other': 'class function var wait thread waittill waittillmatch waittillframeend isdefined constructor destructor autoexec private const',
        operator: 'size assert assertmsg notify endon',
        literal: 'undefined false true self world classes level game anim vararg',
    };

    const PREPROCESSOR = {
        className: 'meta',
        begin: /^\s*#\s*(define|if|else|elif|endif|insert|using|precache|namespace)\b/,
        end: /$/,
        contains: [
            {
                className: 'variable',
                begin: /(?<=#\s*define\s)\S+/,
            }
        ]
    };

    const LINE_COMMENT = hljs.COMMENT('//', /$/);
    const BLOCK_COMMENT = hljs.COMMENT('/\\*', '\\*/');
    const DOC_COMMENT = hljs.COMMENT('/@', '@/');

    const NUMBER = {
        className: 'number',
        variants: [
            { begin: /\b0[xX][0-9a-fA-F]+\b/ },
            { begin: /\b(\d+\.?\d*|\.\d+)([eE][+-]?\d+)?\b/ },
        ]
    };

    const STRING = {
        className: 'string',
        variants: [
            {
                begin: /@"/,
                end: /"/,
            },
            {
                begin: /"/,
                end: /"/,
                contains: [{ begin: /\\./, className: 'char.escape' }]
            }
        ]
    };

    const FUNCTION_CALL = {
        className: 'title.function.invoke',
        begin: /\b[a-zA-Z_][a-zA-Z0-9_]*(?=\s*\()/,
    };

    const NAMESPACE_PATH = {
        className: 'title.class',
        begin: /\b[a-zA-Z_][a-zA-Z0-9_\\\/]*(?=\s*::)/,
    };

    const BUILTIN_FUNCTIONS = 'ActivateClientExploder|ActivateClientRadiantExploder|ActorIKEnabled|AddAwarenessIndicator|AddBonusCardStat|AddDemoBookmark|AddEntityInfluencer|AddFriendlyScrambler|AddInfluencer|AddOrientedInfluencer|AddSensorGrenadeArea|AddSpawnPoints|AddTestClient|AddToInterestPool|AddZombieBoxWeapon|AimAtEntityIK|AimAtPosIK|AimingAtFriendly|AllClientsPrint|AllocateSoundRandoms|AllowActionSlotInput|AllowedStances|AllowRoundAnimation|AllowScoreboard|AllowTacticalInsertion|AllWeaponAttachmentsUnlocked|AnimHasNotetrack|AnimMappingSearch|AnimRelative|AnimScripted|Announcement|ApplyBallisticTarget|AreAllMissionsAtScore|AreMeshesStreamed|ArenaGetSlot|AreTexturesLoaded|AreTexturesStreamed|ArraySort|ArraySortClosest|GetPlayers|GetTime|IPrintLn|IPrintLnBold|IsAlive|IsDefined|IsPlayer|Print|PrintLn|Spawn|SpawnStruct|Wait|GetEnt|GetEntArray|PlayFX|PlaySound|PlaySoundAtPosition|RadiusDamage|SetModel|SetOrigin|SetAngles|GetOrigin|GetAngles|GetVelocity|SetVelocity|Teleport|Delete|Kill|DoDamage|PlayRumbleOnEntity|Earthquake|MagicBullet|MagicGrenade|BulletTrace|PhysicsTrace|SightTracePassed|Attach|Detach|LinkTo|Unlink|Hide|Show|GetTagOrigin|GetTagAngles|SetDvar|GetDvarString|GetDvarInt|GetDvarFloat|TableLookup|TableLookupRow|IsSubStr|GetSubStr|ToLower|ToUpper|sprintf|StrTok|Distance|Distance2D|Length|VectorNormalize|VectorDot|VectorCross|AnglesToForward|AnglesToRight|AnglesToUp|VectorToAngles|RandomFloat|RandomFloatRange|RandomInt|RandomIntRange|Abs|Min|Max|Floor|Ceil|Sin|Cos|Tan|ASin|ACos|ATan|Sqrt|Pow|Log';

    const BUILTIN = {
        className: 'built_in',
        begin: new RegExp(`\\b(${BUILTIN_FUNCTIONS})\\b`),
    };

    return {
        name: 'GSC',
        aliases: ['gsc', 'csc', 'gsh'],
        case_insensitive: false,
        keywords: KEYWORDS,
        contains: [
            LINE_COMMENT,
            BLOCK_COMMENT,
            DOC_COMMENT,
            PREPROCESSOR,
            NUMBER,
            STRING,
            BUILTIN,
            NAMESPACE_PATH,
            FUNCTION_CALL,
        ]
    };
}
