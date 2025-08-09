-- CreateTable
CREATE TABLE "Agent" (
    "id" TEXT NOT NULL PRIMARY KEY,
    "archetype" TEXT NOT NULL,
    "memory" JSONB NOT NULL
);
