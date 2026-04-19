import React, { useEffect, useState } from 'react';
import ReactFlow, { MiniMap, Controls, useEdges, useNodes } from 'react-flow-renderer';

const AutomationDashboard = () => {
  const initialNodes = [
    { id: '1', data: { label: 'Automation Core' }, position: { x: 250, y: 250 }, style: { background: 'gray' }, draggable: true },
    { id: '2', data: { label: 'Social Media Engine' }, position: { x: 100, y: 100 }, style: { background: 'blue' }, draggable: true },
    { id: '3', data: { label: 'Freelancing Scout' }, position: { x: 100, y: 250 }, style: { background: 'blue' }, draggable: true },
    { id: '4', data: { label: 'Affiliate Pilot' }, position: { x: 100, y: 400 }, style: { background: 'blue' }, draggable: true },
    { id: '5', data: { label: 'Product Engine' }, position: { x: 400, y: 100 }, style: { background: 'blue' }, draggable: true },
    { id: '6', data: { label: 'Lead Capture/CRM' }, position: { x: 400, y: 250 }, style: { background: 'blue' }, draggable: true },
    { id: '7', data: { label: 'AI Execution Pilot' }, position: { x: 400, y: 400 }, style: { background: 'blue' }, draggable: true },
    { id: '8', data: { label: 'Data Pipeline' }, position: { x: 250, y: 500 }, style: { background: 'green' }, draggable: true },
    { id: '9', data: { label: 'Payment Pipeline' }, position: { x: 600, y: 300 }, style: { background: 'yellow' }, draggable: true },
  ];

  const initialEdges = [
    { id: 'e1-2', source: '2', target: '8', animated: true, label: 'traffic' },
    { id: 'e1-3', source: '3', target: '8', animated: true, label: 'leads' },
    { id: 'e1-4', source: '4', target: '8', animated: true, label: 'leads' },
    { id: 'e1-5', source: '5', target: '9', animated: true, label: 'cashflow' },
    { id: 'e1-6', source: '6', target: '9', animated: true, label: 'cashflow' },
    { id: 'e1-7', source: '7', target: '9', animated: true, label: 'cashflow' },
    { id: 'e1-8', source: '9', target: '1', animated: true, label: 'cashflow' },
  ];

  const [nodes, setNodes] = useState(initialNodes);
  const [edges, setEdges] = useState(initialEdges);

  // This effect will simulate the flow of leads and money every 3 seconds
  useEffect(() => {
    const interval = setInterval(() => {
      // Randomly modify the number of leads and cash flow
      // Logic for moving leads and money flow would go here
      console.log('Updating simulation...');
    }, 3000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div style={{ height: '100vh' }}>
      <ReactFlow nodes={nodes} edges={edges}>
        <MiniMap />
        <Controls />
      </ReactFlow>
      <div style={{ position: 'absolute', top: '20px', left: '20px', color: 'black' }}>
        <p>Mock data simulation:</p>
        <p>$1200 revenue</p>
        <p>340 leads</p>
      </div>
    </div>
  );
};

export default AutomationDashboard;