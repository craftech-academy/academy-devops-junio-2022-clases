import React from "react";
import avatar1 from '../../../assets/images/hero-logo.svg';
import { Row, Col, Card } from "react-bootstrap";

const DashDefault = () => {
  return (
    <React.Fragment>
      <Row>
        <Col >
          <Card className="card-social">
            <Card.Body className="border-bottom">
              <div className="row align-items-center justify-content-center">
                <div className="col-auto">
                  <img src={avatar1} alt="activity-user" />
                </div>
              </div>
            </Card.Body>
            <Card.Body style={{ background: "#eb9c00" }}>
              <div className="row align-items-center justify-content-center card-active" >
                <div className="col-6">
                  <h4 className="text-center m-b-15">
                    <span className="mb-0" style={{ color: "white" }}>App deployment progress: 100%</span>
                  </h4>
                  <div className="progress">
                    <div
                      className="progress-bar progress-c-green"
                      role="progressbar"
                      style={{ width: "100%", height: "6px"}}
                      aria-valuenow="40"
                      aria-valuemin="0"
                      aria-valuemax="100"
                    />
                  </div>
                </div>
              </div>
            </Card.Body>
          </Card>
        </Col>
      </Row>
    </React.Fragment>
  );
};

export default DashDefault;
