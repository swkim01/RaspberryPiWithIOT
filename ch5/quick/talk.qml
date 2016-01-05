import QtQuick 1.1

Rectangle {
  id: root
  width: 300
  height: 300
  property variant widgets

  Dialog {
    id: connect; objectName: "connect";
    height: 100; anchors.centerIn: parent; z: 50

  Column {
    anchors.centerIn: connect
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
        onClicked: { con.connect(root); connect.page.forceClose(); }
      }
      Button {
        id: cancelButton
        width: parent.width/2-5
        objectName: "cancelButton"
        buttonColor: "darkgrey"
        label: "Cancel"
        onClicked: connect.page.forceClose();
      }
    }
  }
  }
  Dialog {
    id: error; objectName: "error";
    height: 50; anchors.centerIn: parent; z: 100

    Column {
      anchors.centerIn: error
      anchors.fill: parent
      spacing: 5

      Text {
        id: errorLabel
        text: "Error during connection!"
        width: 50; height: 20
      }
      Button {
        id: okErrorButton
        objectName: "okErrorButton"
        buttonColor: "darkgrey"
        label: "OK"
        onClicked: { error.page.forceClose(); }
      }
    }
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
      'server': serverinput,
      'port': portinput,
      'name': nameinput,
      'textedit': textedit,
      'textinput': textinput,
      'error': error
    }
    con.init(root)
  }
}
