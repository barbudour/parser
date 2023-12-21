# TraceFlags - перечисление
Defines flags to control tracing details.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
    [FlagsAttribute]
    public enum TraceFlags
VB __Копировать
    <FlagsAttribute>
    Public Enumeration TraceFlags
C++ __Копировать
    [FlagsAttribute]
    public enum class TraceFlags
F# __Копировать
     [<FlagsAttribute>]
    type TraceFlags
##  __Члены
None| 0|  No tracing.  
---|---|---  
EwsRequest| 1|  Trace EWS request messages.  
EwsResponse| 2|  Trace EWS response messages.  
EwsResponseHttpHeaders| 4|  Trace EWS response HTTP headers.  
AutodiscoverRequest| 8|  Trace Autodiscover request messages.  
AutodiscoverResponse| 16|  Trace Autodiscover response messages.  
AutodiscoverResponseHttpHeaders| 32|  Trace Autodiscover response HTTP
headers.  
AutodiscoverConfiguration| 64|  Trace Autodiscover configuration logic.  
DebugMessage| 128|  Trace messages used in debugging the Exchange Web Services
Managed API  
EwsRequestHttpHeaders| 256|  Trace EWS request HTTP headers.  
AutodiscoverRequestHttpHeaders| 512|  Trace Autodiscover request HTTP headers.  
EwsTimeZones| 1,024|  Trace EWS timezone related logic.  
All| 9,223,372,036,854,775,807|  All trace types enabled.  
## __См. также
#### Ссылки
[Tessa.Exchange.WebServices.Data - пространство
имён](N_Tessa_Exchange_WebServices_Data.htm)
