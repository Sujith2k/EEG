#include <WiFi.h>
#include "soc/soc.h"           // Disable brownour problems
#include "soc/rtc_cntl_reg.h"

const char* ssid = "Home";
const char* password =  "";
 
const uint16_t port = 8090;
const char * host = "192.168.0.107";
 
void setup()
{
  WRITE_PERI_REG(RTC_CNTL_BROWN_OUT_REG, 0);
 
  Serial.begin(115200);
 
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
 
  Serial.print("WiFi connected with IP: ");
  Serial.println(WiFi.localIP());
 
}
 
void loop()
{
    WiFiClient client;
 
    if (!client.connect(host, port)) {
 
        Serial.println("Connection to host failed");
 
        delay(500);
        return;
    }
 
    Serial.println("Connected to server successful!");
    while(1)
    {
    client.print("Hello from ESP32!");
    }
    Serial.println("Disconnecting...");
    client.stop();
 
    delay(0);
}
