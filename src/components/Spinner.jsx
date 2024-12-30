import React from "react";
import "../styles/SpinnerPage.scss";

const Spinner = ({ size = 50, color = "#ffffff" }) => {
  return (
    <div
      className="spinner-wheel"
      style={{
        width: size,
        height: size,
        borderWidth: size / 12,
        borderColor: `transparent`,
        borderTopColor: color,
      }}
    ></div>
  );
};

export default Spinner;
