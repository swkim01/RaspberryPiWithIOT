import QtQuick 2.11

Rectangle {
  id: button
  width: parent.width; height: 20
  property alias label: buttonLabel.text
  property color buttonColor: "darkgrey"
  signal clicked()

  Text {
    id: buttonLabel
    anchors.horizontalCenter: parent.horizontalCenter
  }
  MouseArea {
    id: buttonMouseArea
    objectName: "buttonMouseArea"
    hoverEnabled: true
    anchors.fill: parent
    onClicked: button.clicked()
  }
  color: buttonMouseArea.pressed ? Qt.darker(buttonColor, 1.5) : buttonColor
}
