import QtQuick 1.1
Rectangle {
  width: 100
  height: 100
  color: "grey"
  Text {
      anchors.centerIn: parent
      text: "<공지사항>"
    }
  Rectangle {
    width: 50
    height: 80
    color: "darkgrey"
    //z: 1
    clip: true
    Text {
      text: "월요일 10시는"
    }
  }
  Rectangle {
    width: 25
    height: 40
    color: "lightgrey"
    Text {
      anchors.verticalCenter: parent.verticalCenter
      text: "커피타임!"
    }
  }
}
