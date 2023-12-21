# ResponseActions - перечисление
Defines the response actions that can be taken on an item.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
    [FlagsAttribute]
    public enum ResponseActions
VB __Копировать
    <FlagsAttribute>
    Public Enumeration ResponseActions
C++ __Копировать
    [FlagsAttribute]
    public enum class ResponseActions
F# __Копировать
     [<FlagsAttribute>]
    type ResponseActions
##  __Члены
None| 0|  No action can be taken.  
---|---|---  
Accept| 1|  The item can be accepted.  
TentativelyAccept| 2|  The item can be tentatively accepted.  
Decline| 4|  The item can be declined.  
Reply| 8|  The item can be replied to.  
ReplyAll| 16|  The item can be replied to.  
Forward| 32|  The item can be forwarded.  
Cancel| 64|  The item can be cancelled.  
RemoveFromCalendar| 128|  The item can be removed from the calendar.  
SuppressReadReceipt| 256|  The item's read receipt can be suppressed.  
PostReply| 512|  A reply to the item can be posted.  
## __См. также
#### Ссылки
[Tessa.Exchange.WebServices.Data - пространство
имён](N_Tessa_Exchange_WebServices_Data.htm)
