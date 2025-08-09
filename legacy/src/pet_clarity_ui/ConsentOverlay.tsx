import React from 'react';

export const ConsentOverlay = ({ message, onConsent, onReject }: { message: string; onConsent: () => void; onReject: () => void }) => (
    <div style={{ padding: 24, background: '#fff', border: '2px solid #a21caf', borderRadius: 12, textAlign: 'center' }}>
        <p>{message || 'Do you consent?'}</p>
        <button onClick={onConsent} style={{ marginRight: 12 }}>Consent</button>
        <button onClick={onReject}>Reject</button>
    </div>
);
