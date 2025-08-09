import React from 'react';
import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom/extend-expect';
import RuneCard from '../../../src/frontend/components/runic/RuneCard';

describe('RuneCard Component', () => {
    test('renders title and description', () => {
        render(<RuneCard title="Test Rune" description="This is a test description." />);
        expect(screen.getByText('Test Rune')).toBeInTheDocument();
        expect(screen.getByText('This is a test description.')).toBeInTheDocument();
    });

    test('renders title without description', () => {
        render(<RuneCard title="Solo Rune" />);
        expect(screen.getByText('Solo Rune')).toBeInTheDocument();
        // Description should not be rendered
        expect(screen.queryByText(/description/i)).toBeNull();
    });
});
