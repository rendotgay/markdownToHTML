window.zone = function(hljs) {
    const ASSET_TYPES = [
        'xmodel', 'material', 'image', 'sound', 'scriptparsetree', 'stringtable',
        'col_map', 'gfx_map', 'include', 'class', 'group', 'fx', 'xanim',
        'weapon', 'localize', 'physpreset', 'physconstraints', 'destructibledef',
        'aitype', 'character', 'xmodelalias', 'rawfile', 'menufile', 'menu',
        'clipmap', 'loadscreen', 'font', 'fonticon', 'localizeentry', 'gesture',
        'attachment', 'attachmentunique', 'weaponcamo', 'tag', 'snddriverglobals',
        'structureddatadef', 'tracer', 'vehicle', 'addon_map_ents'
    ];

    return {
        name: 'Zone',
        aliases: ['zone'],
        case_insensitive: true,
        contains: [
            // // comments
            hljs.COMMENT('//', /$/),
            // >directive lines
            {
                className: 'meta',
                begin: /^>/,
                end: /$/,
                contains: [
                    {
                        className: 'keyword',
                        begin: /(?<=>)\w+/,
                    }
                ]
            },
            // asset type before the comma
            {
                className: 'keyword',
                begin: new RegExp(`^(${ASSET_TYPES.join('|')})(?=,)`),
            },
            // the comma
            {
                className: 'punctuation',
                begin: /,/,
            },
            // the value after the comma
            {
                className: 'string',
                begin: /(?<=,).+$/,
            }
        ]
    };
};