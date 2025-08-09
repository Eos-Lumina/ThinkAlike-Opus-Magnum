// Asynchronous Event Bus Protocol
export interface Event {
    type: string;
    payload: any;
    timestamp: number;
}

export interface EventBus {
    publish(event: Event): void;
    subscribe(type: string, handler: (event: Event) => void): void;
}
