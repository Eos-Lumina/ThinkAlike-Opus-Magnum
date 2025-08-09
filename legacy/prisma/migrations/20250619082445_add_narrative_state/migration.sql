-- CreateTable
CREATE TABLE "NarrativeState" (
    "id" TEXT NOT NULL PRIMARY KEY,
    "userId" TEXT NOT NULL,
    "currentNode" TEXT NOT NULL,
    "history" JSONB NOT NULL,
    "forkId" TEXT,
    "updatedAt" DATETIME NOT NULL
);
