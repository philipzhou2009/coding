
// template: {{key1}}, {{key2}}? {{key1}}, {{key2}}! 
// data: {key1:"hello", key2:"world"}
const regexpReplace = (template, data) => {
    let keys = Object.keys(data)

    let str = template
    keys.forEach((key, index) => {
        let re = new RegExp('{{' + key + '}}', 'gi')
        str = str.replace(re, data[key])
    })

    return str
}

function escapeRegExp(string) {
    return string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'); // $& means the whole matched string
}

module.exports = {
    regexpReplace,
}