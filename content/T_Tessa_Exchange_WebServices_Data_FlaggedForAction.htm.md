# FlaggedForAction - перечисление
Defines the follow-up actions that may be stamped on a message.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public enum FlaggedForAction
VB __Копировать
     Public Enumeration FlaggedForAction
C++ __Копировать
     public enum class FlaggedForAction
F# __Копировать
     type FlaggedForAction
##  __Члены
Any| 0|  The message is flagged with any action.  
---|---|---  
Call| 1|  The recipient is requested to call the sender.  
DoNotForward| 2|  The recipient is requested not to forward the message.  
FollowUp| 3|  The recipient is requested to follow up on the message.  
FYI| 4|  The recipient received the message for information.  
Forward| 5|  The recipient is requested to forward the message.  
NoResponseNecessary| 6|  The recipient is informed that a response to the
message is not required.  
Read| 7|  The recipient is requested to read the message.  
Reply| 8|  The recipient is requested to reply to the sender of the message.  
ReplyToAll| 9|  The recipient is requested to reply to everyone the message
was sent to.  
Review| 10|  The recipient is requested to review the message.  
## __См. также
#### Ссылки
[Tessa.Exchange.WebServices.Data - пространство
имён](N_Tessa_Exchange_WebServices_Data.htm)
