-- CreateTable
CREATE TABLE "AlchemyProgress" (
    "id" TEXT NOT NULL PRIMARY KEY,
    "userId" TEXT NOT NULL,
    "stage" TEXT NOT NULL,
    "updatedAt" DATETIME NOT NULL
);

-- CreateIndex
CREATE UNIQUE INDEX "AlchemyProgress_userId_key" ON "AlchemyProgress"("userId");
