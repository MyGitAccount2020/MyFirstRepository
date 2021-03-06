const mongoose = require('mongoose');
const { Schema } = mongoose;

const todoSchema = new Schema({
    text: String,
    isCompleted : {
        type: Boolean,
        default: false
    },
    createdDate : {
        type: Date,
        default: Date.now
    }
})

module.exports = mongoose.model('Todo', todoSchema)