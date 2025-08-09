// Observability and Telemetry Protocols
export interface TelemetryEvent {
    agentId: string;
    event: string;
    data: any;
    timestamp: number;
}

export interface TelemetryCollector {
    record(event: TelemetryEvent): void;
    getMetrics(): Promise<any>;
}
