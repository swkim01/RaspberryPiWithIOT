#include <stdio.h>
#include <wiringPi.h>

#define LED1 1				/* BCM_GPIO 18 */
int main (void)
{
    if (wiringPiSetup () == -1)
        return 1 ;

    pinMode (LED1, OUTPUT) ;
    for (;;) {
        digitalWrite (LED1, 1) ;	/* Turn On */
        delay (1000) ; /* 1000 msec = 1 sec */
        digitalWrite (LED1, 0) ;	/* Turn Off */
        delay (1000) ;
    }
    return 0 ;
}
