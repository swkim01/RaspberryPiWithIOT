import QtQuick 2.11

Column {
    Repeater {
        model: 5
        Text {
            text: "item " + index
        }
    }
}
