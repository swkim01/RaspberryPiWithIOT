import QtQuick 1.1

Column {
    Repeater {
        model: 5
        Text {
            text: "item " + index
        }
    }
}
