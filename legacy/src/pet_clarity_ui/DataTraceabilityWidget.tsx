import React from 'react';

export const DataTraceabilityWidget = ({ provenance }: { provenance: string }) => (
    <div style={{ padding: 12, background: '#f3f4f6', border: '1px solid #a21caf', borderRadius: 8, margin: '1em 0' }}>
        <strong>Provenance:</strong> {provenance || 'N/A'}
    </div>
);
