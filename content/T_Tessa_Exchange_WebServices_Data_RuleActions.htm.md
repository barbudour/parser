# RuleActions - класс
Represents the set of actions available for a rule.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class RuleActions : ComplexProperty
VB __Копировать
     Public NotInheritable Class RuleActions
    	Inherits ComplexProperty
C++ __Копировать
     public ref class RuleActions sealed : public ComplexProperty
F# __Копировать
     [<SealedAttribute>]
    type RuleActions = 
        class
            inherit ComplexProperty
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ComplexProperty](T_Tessa_Exchange_WebServices_Data_ComplexProperty.htm) __ RuleActions
##  __Свойства
[AssignCategories](P_Tessa_Exchange_WebServices_Data_RuleActions_AssignCategories.htm)|
Gets the categories that should be stamped on incoming messages. To disable
stamping incoming messages with categories, set AssignCategories to null.  
---|---  
[CopyToFolder](P_Tessa_Exchange_WebServices_Data_RuleActions_CopyToFolder.htm)|
Gets or sets the Id of the folder incoming messages should be copied to. To
disable copying incoming messages to a folder, set CopyToFolder to null.  
[Delete](P_Tessa_Exchange_WebServices_Data_RuleActions_Delete.htm)|  Gets or
sets a value indicating whether incoming messages should be automatically
moved to the Deleted Items folder.  
[ForwardAsAttachmentToRecipients](P_Tessa_Exchange_WebServices_Data_RuleActions_ForwardAsAttachmentToRecipients.htm)|
Gets the e-mail addresses to which incoming messages should be forwarded as
attachments. To disable forwarding incoming messages as attachments, empty the
ForwardAsAttachmentToRecipients list.  
[ForwardToRecipients](P_Tessa_Exchange_WebServices_Data_RuleActions_ForwardToRecipients.htm)|
Gets the e-mail addresses to which incoming messages should be forwarded. To
disable forwarding incoming messages, empty the ForwardToRecipients list.  
[MarkAsRead](P_Tessa_Exchange_WebServices_Data_RuleActions_MarkAsRead.htm)|
Gets or sets a value indicating whether incoming messages should be marked as
read.  
[MarkImportance](P_Tessa_Exchange_WebServices_Data_RuleActions_MarkImportance.htm)|
Gets or sets the importance that should be stamped on incoming messages. To
disable the stamping of incoming messages with an importance, set
MarkImportance to null.  
[MoveToFolder](P_Tessa_Exchange_WebServices_Data_RuleActions_MoveToFolder.htm)|
Gets or sets the Id of the folder to which incoming messages should be moved.
To disable the moving of incoming messages to a folder, set CopyToFolder to
null.  
[PermanentDelete](P_Tessa_Exchange_WebServices_Data_RuleActions_PermanentDelete.htm)|
Gets or sets a value indicating whether incoming messages should be
permanently deleted. When a message is permanently deleted, it is never saved
into the recipient's mailbox. To delete a message after it has been saved into
the recipient's mailbox, use the Delete action.  
[RedirectToRecipients](P_Tessa_Exchange_WebServices_Data_RuleActions_RedirectToRecipients.htm)|
Gets the e-mail addresses to which incoming messages should be redirecteded.
To disable redirection of incoming messages, empty the RedirectToRecipients
list. Unlike forwarded mail, redirected mail maintains the original sender and
recipients.  
[SendSMSAlertToRecipients](P_Tessa_Exchange_WebServices_Data_RuleActions_SendSMSAlertToRecipients.htm)|
Gets the phone numbers to which an SMS alert should be sent. To disable
sending SMS alerts for incoming messages, empty the SendSMSAlertToRecipients
list.  
[ServerReplyWithMessage](P_Tessa_Exchange_WebServices_Data_RuleActions_ServerReplyWithMessage.htm)|
Gets or sets the Id of the template message that should be sent as a reply to
incoming messages. To disable automatic replies, set ServerReplyWithMessage to
null.  
[StopProcessingRules](P_Tessa_Exchange_WebServices_Data_RuleActions_StopProcessingRules.htm)|
Gets or sets a value indicating whether subsequent rules should be evaluated.  
## __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Exchange.WebServices.Data - пространство
имён](N_Tessa_Exchange_WebServices_Data.htm)
