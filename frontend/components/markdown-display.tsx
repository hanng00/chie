import React from "react";
import ReactMarkdown from "react-markdown";

const MarkdownDisplay = ({ markdownText }: { markdownText: string }) => {
  return (
    <div className="text-md text-foreground/70 max-w-2xl mx-auto mt-6">
      <ReactMarkdown>{markdownText}</ReactMarkdown>
    </div>
  );
};

export default MarkdownDisplay;
