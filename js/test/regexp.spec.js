
const expect = require('chai').expect

const regexp = require('../js/regexp')

describe('regexp functions', () => {
    describe('regexpReplace', () => {
        it('should export a function', () => {
            expect(regexp.regexpReplace).to.be.a('function')
        })

        it('should return string', () => {
            let template = '{{key1}}, {{key2}}? {{key1}}, {{key2}}!'
            let data = { key1: 'hello', key2: 'world' }
            expect(regexp.regexpReplace(template, data)).to.be.a('string')
        }
        )
    })


}

)