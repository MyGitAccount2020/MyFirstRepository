const express = require("express");
require("./db");
const TodoRouter = require("./routes/todo.routes");

const app = express();

app.use(express.json());

app.use("/api/todos", TodoRouter);
//http://localhost:9000/api/todos
module.exports = app;