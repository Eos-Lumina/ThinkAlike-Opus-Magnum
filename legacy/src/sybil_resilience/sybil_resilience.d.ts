export class SybilResilience {
    constructor();
    verifyUser(userId: string, method: string): {
        userId: string;
        method: string;
        status: string;
        timestamp: string;
        details: string;
    };
}
