-- CreateTable
CREATE TABLE "ResonanceNode" (
    "id" TEXT NOT NULL PRIMARY KEY,
    "attributes" JSONB NOT NULL
);

-- CreateTable
CREATE TABLE "ResonanceEdge" (
    "id" TEXT NOT NULL PRIMARY KEY,
    "from" TEXT NOT NULL,
    "to" TEXT NOT NULL,
    "weight" REAL NOT NULL
);

-- CreateTable
CREATE TABLE "VerificationEvent" (
    "id" TEXT NOT NULL PRIMARY KEY,
    "userId" TEXT NOT NULL,
    "method" TEXT NOT NULL,
    "timestamp" DATETIME NOT NULL,
    "status" TEXT NOT NULL
);
