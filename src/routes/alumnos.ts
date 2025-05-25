import { Router } from "express";
import prisma from "../controllers/prisma";

const router = Router();

router.get("/", async (req, res) => {
    const users = await prisma.alumnos.findMany();
    res.json(users);
});

export default router;