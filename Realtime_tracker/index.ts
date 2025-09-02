import express from 'express'
import {createServer} from 'node:http'
import { Server } from 'socket.io';
import path from 'path';
import cors from 'cors';

const PORT = 3000;

const app = express();
const server = createServer(app);
const io = new Server(server);

app.use(express.json());
app.use(cors())
app.set("view engine", "ejs");
app.use(express.static(path.join(__dirname, "public")));

app.get('/', (req,res) => {
    res.render("index");
});

io.on('connection', (socket) => {
    console.log('a user connected');

    socket.on("send-location", function(data) {
        io.emit("receive-location", {id:socket.id, ...data});
    });

    socket.on("disconnect", function(){
        io.emit("user-disconnect", socket.id);
    });
})

server.listen(PORT, () => {
    console.log(`http://localhost:${PORT}`);
})