

const { Draft07, JsonSchema } = require("json-schema-library");
const util = require('util');

const myJsonSchema = {
    type: "object",
    required: ["name", "option", "list"],
    properties: {
        name: { type: "string" },
        option: {
            type: "string",
            enum: ["first-option", "second-option"]
        },
        list: {
            type: "array",
            items: {
                type: "string",
                default: "new item"
            },
            minItems: 1
        }
    }
};

const jsonSchema = new Draft07(myJsonSchema);
const myData = jsonSchema.getTemplate({ name: "input-data", list: [] });

console.log(myData);
/*
expect(myData).to.deep.equal({
    name: "input-data",
    option: "first-option",
    list: ["new item"]
});
*/
