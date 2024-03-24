const express = require('express');
const app = express();

const PORT = process.env.PORT || 3000;

// Route to get the server URL
app.get('/getServer', (req, res) => {
    const serverURL = `http://localhost:${PORT}`;
    res.json({ code: 200, server: serverURL });
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
