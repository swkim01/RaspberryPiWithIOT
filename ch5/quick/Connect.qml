import QtQuick 1.1

Rectangle {
  id: page
  width: 200
  height: 100

  signal closed
  signal opened

  function forceClose() {
    if (page.opacity == 0)
      return;
    page.closed();
    page.opacity = 0;
  }
  function show() {
    page.opened();
    page.opacity = 1;
  }
  opacity: 0
  visible: opacity > 0
  Behavior on opacity {
    NumberAnimation { duration: 500 }
  }

  Column {
    anchors.centerIn: page
    anchors.fill: parent
    spacing: 5

    Rectangle {
      width: parent.width; height: 20
      color: "darkgrey"

      Text {
        id: serverLabel
        text: "Server:"
        width: 50; height: 20
      }
      TextInput {
        id: serverinput
        objectName: "serverInput"
        width: parent.width-50; height: 20
        anchors.left: serverLabel.right
        text: "localhost"
        focus: true
      }
    }
    Rectangle {
      width: parent.width; height: 20
      color: "darkgrey"

      Text {
        id: portLabel
        text: "Port:"
        width: 50; height: 20
      }
      TextInput {
        id: portinput
        objectName: "portInput"
        width: parent.width-50; height: 20
        anchors.left: portLabel.right
        text: "8080"
        focus: true
      }
    }
    Rectangle {
      width: parent.width; height: 20
      color: "darkgrey"

      Text {
        id: nameLabel
        text: "Name:"
        width: 50; height: 20
      }
      TextInput {
        id: nameinput
        objectName: "nameInput"
        width: parent.width-50; height: 20
        anchors.left: nameLabel.right
        text: "홍길동"
        focus: true
      }
    }
    Row {
      width: parent.width; height: 20
      spacing: 10

      Button {
        id: okButton
        width: parent.width/2-5
        objectName: "okButton"
        buttonColor: "darkgrey"
        label: "OK"
        onClicked: { con.connect(root); forceClose(); }
      }
      Button {
        id: cancelButton
        width: parent.width/2-5
        objectName: "cancelButton"
        buttonColor: "darkgrey"
        label: "Cancel"
        onClicked: forceClose();
      }
    }
  }
  property alias server: serverinput
  property alias port: portinput
  property alias name: nameinput

}
