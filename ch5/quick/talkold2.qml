import QtQuick 1.1

Rectangle {
  id: root
  width: 300
  height: 300
  property variant widgets

  Connect {
    id: connect; objectName: "connect";
    anchors.centerIn: parent; z: 100
  }

  Column {
    anchors.centerIn: root
    anchors.fill: parent

    Button {
      id: connectButton
      objectName: "connectButton"
      buttonColor: "darkgrey"
      label: "Connect"
      onClicked: connect.show()
    }
    Rectangle {
      width: parent.width; height: parent.height-40
      anchors.horizontalCenter: parent.horizontalCenter
      color: "lightgrey"
      TextEdit {
        id: textedit
        anchors.fill: parent
        anchors.horizontalCenter: parent.horizontalCenter
        textFormat: TextEdit.PlainText
      }
    }
    Flow {
      width: parent.width; height: 20
      TextInput {
        id: textinput
        objectName: "textInput"
        width: parent.width-50; height: 20
        focus: true
        onAccepted: con.send(root, text)
      }
      Button {
        id: sendButton
        objectName: "sendButton"
        width: 50; height: 20
        buttonColor: "darkgrey"
        label: "Send"
        onClicked: con.send(root, textinput.text)
      }
    }
  }
  Component.onCompleted: {
    widgets = {
      'server': connect.server,
      'port': connect.port,
      'name': connect.name,
      'textedit': textedit,
      'textinput': textinput,
      'connect': connect
    }
    con.init(root)
  }
}
