// AgentDirectory.ts
// Canonical registry for all agents in the ThinkAlike ecosystem.
// Follows symbolic contract and traceability requirements.

export type AgentArchetype = 'DialogueAgent' | 'RitualAgent' | 'GovernanceAgent' | 'BridgeAgent';

export interface Agent {
    id: string;
    name: string;
    archetype: AgentArchetype;
    state: 'active' | 'archived' | 'pending';
    createdAt: Date;
    updatedAt: Date;
    auditTrail: string[];
    symbolicSeed: string;
}

export class AgentDirectory {
    private agents: Map<string, Agent> = new Map();

    register(agent: Agent): void {
        if (this.agents.has(agent.id)) {
            throw new Error('Agent already registered');
        }
        this.agents.set(agent.id, agent);
        this.logAudit(agent.id, `Registered agent: ${agent.name}`);
    }

    getAgent(id: string): Agent | undefined {
        return this.agents.get(id);
    }

    listAgents(archetype?: AgentArchetype): Agent[] {
        const all = Array.from(this.agents.values());
        return archetype ? all.filter(a => a.archetype === archetype) : all;
    }

    archiveAgent(id: string): void {
        const agent = this.agents.get(id);
        if (agent) {
            agent.state = 'archived';
            agent.updatedAt = new Date();
            this.logAudit(id, 'Agent archived');
        }
    }

    private logAudit(id: string, message: string): void {
        const agent = this.agents.get(id);
        if (agent) {
            agent.auditTrail.push(`[${new Date().toISOString()}] ${message}`);
        }
    }
}
