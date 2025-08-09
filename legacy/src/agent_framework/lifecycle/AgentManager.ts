// AgentManager.ts
// Handles agent lifecycle, orchestration, and ethical checks.

import { Agent, AgentDirectory } from './AgentDirectory';

export class AgentManager {
    constructor(private directory: AgentDirectory) { }

    emerge(agent: Agent): void {
        // Register and initialize agent
        this.directory.register(agent);
        this.logLifecycle(agent.id, 'Emerged');
    }

    persist(id: string): void {
        // Mark agent as persistent/long-term
        const agent = this.directory.getAgent(id);
        if (agent) {
            agent.state = 'active';
            this.logLifecycle(id, 'Persisted');
        }
    }

    terminate(id: string): void {
        // Archive agent and log termination
        this.directory.archiveAgent(id);
        this.logLifecycle(id, 'Terminated');
    }

    private logLifecycle(id: string, message: string): void {
        // Could be extended to log to external traceability layer
        const agent = this.directory.getAgent(id);
        if (agent) {
            agent.auditTrail.push(`[${new Date().toISOString()}] [Lifecycle] ${message}`);
        }
    }
}
