// This component is used to create an AI-guided workflow
// with reusable UI elements and to show basic steps
// This component is also a test parameter for code and design implementations

import React, { useState } from 'react';
import { View, Text, Button } from 'react-native'; // Use your React Native components or similar
import guideSteps from '../data/ai_guide_steps.json'; // JSON file where you will store steps
import ActionButton from './ActionButton';

const AIGuide = () => {
    const [currentStep, setCurrentStep] = useState(0);

    const handleNext = () => {
        setCurrentStep(currentStep + 1)
    }

    const handlePrevious = () => {
        setCurrentStep(currentStep - 1)
    }

    const data = guideSteps[currentStep] || null;

    if (!data) {
        return (
            <View>
                <Text> End of guide. </Text>
            </View>
        )
    }

    return (
        <View>
            <Text>{data.title}</Text>
            <Text>{data.description}</Text>
            <ActionButton
                title="Next Step"
                onPress={handleNext}
                actionType="next_step"
                dataParams={{ step: currentStep, totalSteps: guideSteps.length }}
                testingParams={{ workflow: "automated guide" }}
            />
            <ActionButton
                title="Previous Step"
                onPress={handlePrevious}
                actionType="previous_step"
                dataParams={{ step: currentStep, totalSteps: guideSteps.length }}
                testingParams={{ workflow: "automated guide" }}
            />

            {/* UI Component that displays feedback about tests and workflow steps  */}

        </View>
    );
};

export default AIGuide;
