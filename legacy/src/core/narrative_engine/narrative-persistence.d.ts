export interface NarrativeState {
    userId: string;
    currentNode: string;
    history: string[];
    forkId?: string;
}

export function getNarrativeState(userId: string): Promise<NarrativeState | null>;
export function upsertNarrativeState(state: NarrativeState): Promise<void>;
