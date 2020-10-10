import React, { useEffect, useState } from "react";
import "./App.css";
import { Graphviz } from "graphviz-react";
import { Button, Card, Col, Page, Row, Tree } from "@geist-ui/react";
// @ts-ignore
import useDimensions from "react-use-dimensions";

function App() {
  const [profiles, setProfiles] = useState<string[]>([]);
  const [currentProfile, setCurrentProfile] = useState<string>();
  const [dotData, setDotData] = useState<string>();
  const [ref, { width, height }] = useDimensions();

  useEffect(() => {
    (async () => {
      const profileResp = await fetch("/dotprof/profiles");
      const profileList: string[] = (await profileResp.json()).profiles;
      setProfiles(
        profileList.filter((profile) => !profile.startsWith("GET.dotprof"))
      );
    })();
  }, [setProfiles]);

  useEffect(() => {
    (async () => {
      if (currentProfile !== undefined) {
        const dotResp = await fetch(`/dotprof/profiles/${currentProfile}`);
        setDotData(await dotResp.text());
      }
    })();
  }, [currentProfile]);

  return (
    <Row
      gap={0.8}
      style={{ paddingTop: "12.8pt", paddingBottom: "12.8pt", height: "100vh" }}
    >
      <Col span={6} style={{ height: "100%" }}>
        <Card style={{ height: "100%", overflow: "scroll" }}>
          <Tree>
            <Tree.Folder name="Profiles">
              {profiles.map((profile) => (
                <Tree.File
                  name={profile}
                  onClick={() => {
                    setCurrentProfile(profile);
                  }}
                />
              ))}
            </Tree.Folder>
          </Tree>
        </Card>
      </Col>
      <Col span={18} style={{ display: "flex", height: "100%" }}>
        <div ref={ref} style={{ display: "flex", flex: "1" }}>
          <Graphviz
            dot={dotData || "digraph G {}"}
            options={{ zoom: true, height: height, width: width }}
          />
        </div>
      </Col>
    </Row>
  );
}

export default App;
