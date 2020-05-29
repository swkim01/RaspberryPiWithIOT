import QtQuick 2.11

Rectangle {
  id: root
  width: 100; height: 40
  property variant widgets

  Column {
    Rectangle {
      id: input
      width: 100; height: 20
      property string inputText: textinput.text
      TextInput {
        id: textinput
        objectName: "textinput"
        anchors.fill: parent
        text: "홍길동"
        focus: true
        onAccepted: { con.textEnter(root, text); }
      }
    }
    Rectangle {
      id: button
      width: 100; height: 20
      color: "lightgrey"
      Text {
        anchors.horizontalCenter: parent.horizontalCenter
        text: "입력"
      }
      MouseArea {
        id: buttonMouseArea
        objectName: "inputbutton"
        anchors.fill: parent
        onPressed: parent.color = "darkgrey"
        onReleased: parent.color = "lightgrey"
        onClicked: { con.buttonClick(root); }
      }
    }
  }
  Component.onCompleted: {
    widgets = {
      'button': button,
      'textinput': textinput
    }
    //con.testFunc()
    con.init(root)
  }
}
