import QtQuick 1.1

Rectangle {
  id: page
  width: 200
  //height: 100

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
/*
  Column {
    anchors.centerIn: page
    anchors.fill: parent
    spacing: 5
  }
*/
  property alias page: page
}
