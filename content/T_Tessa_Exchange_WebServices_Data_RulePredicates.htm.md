# RulePredicates - класс
Represents the set of conditions and exceptions available for a rule.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class RulePredicates : ComplexProperty
VB __Копировать
     Public NotInheritable Class RulePredicates
    	Inherits ComplexProperty
C++ __Копировать
     public ref class RulePredicates sealed : public ComplexProperty
F# __Копировать
     [<SealedAttribute>]
    type RulePredicates = 
        class
            inherit ComplexProperty
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ComplexProperty](T_Tessa_Exchange_WebServices_Data_ComplexProperty.htm) __ RulePredicates
##  __Свойства
[Categories](P_Tessa_Exchange_WebServices_Data_RulePredicates_Categories.htm)|
Gets the categories that an incoming message should be stamped with for the
condition or exception to apply. To disable this predicate, empty the list.  
---|---  
[ContainsBodyStrings](P_Tessa_Exchange_WebServices_Data_RulePredicates_ContainsBodyStrings.htm)|
Gets the strings that should appear in the body of incoming messages for the
condition or exception to apply. To disable this predicate, empty the list.  
[ContainsHeaderStrings](P_Tessa_Exchange_WebServices_Data_RulePredicates_ContainsHeaderStrings.htm)|
Gets the strings that should appear in the headers of incoming messages for
the condition or exception to apply. To disable this predicate, empty the
list.  
[ContainsRecipientStrings](P_Tessa_Exchange_WebServices_Data_RulePredicates_ContainsRecipientStrings.htm)|
Gets the strings that should appear in either the To or Cc fields of incoming
messages for the condition or exception to apply. To disable this predicate,
empty the list.  
[ContainsSenderStrings](P_Tessa_Exchange_WebServices_Data_RulePredicates_ContainsSenderStrings.htm)|
Gets the strings that should appear in the From field of incoming messages for
the condition or exception to apply. To disable this predicate, empty the
list.  
[ContainsSubjectOrBodyStrings](P_Tessa_Exchange_WebServices_Data_RulePredicates_ContainsSubjectOrBodyStrings.htm)|
Gets the strings that should appear in either the body or the subject of
incoming messages for the condition or exception to apply. To disable this
predicate, empty the list.  
[ContainsSubjectStrings](P_Tessa_Exchange_WebServices_Data_RulePredicates_ContainsSubjectStrings.htm)|
Gets the strings that should appear in the subject of incoming messages for
the condition or exception to apply. To disable this predicate, empty the
list.  
[FlaggedForAction](P_Tessa_Exchange_WebServices_Data_RulePredicates_FlaggedForAction.htm)|
Gets or sets the flag for action value that should appear on incoming messages
for the condition or execption to apply. To disable this predicate, set it to
null.  
[FromAddresses](P_Tessa_Exchange_WebServices_Data_RulePredicates_FromAddresses.htm)|
Gets the e-mail addresses of the senders of incoming messages for the
condition or exception to apply. To disable this predicate, empty the list.  
[FromConnectedAccounts](P_Tessa_Exchange_WebServices_Data_RulePredicates_FromConnectedAccounts.htm)|
Gets the e-mail account names from which incoming messages must have been
aggregated for the condition or exception to apply. To disable this predicate,
empty the list.  
[HasAttachments](P_Tessa_Exchange_WebServices_Data_RulePredicates_HasAttachments.htm)|
Gets or sets a value indicating whether incoming messages must have
attachments for the condition or exception to apply.  
[Importance](P_Tessa_Exchange_WebServices_Data_RulePredicates_Importance.htm)|
Gets or sets the importance that should be stamped on incoming messages for
the condition or exception to apply. To disable this predicate, set it to
null.  
[IsApprovalRequest](P_Tessa_Exchange_WebServices_Data_RulePredicates_IsApprovalRequest.htm)|
Gets or sets a value indicating whether incoming messages must be approval
requests for the condition or exception to apply.  
[IsAutomaticForward](P_Tessa_Exchange_WebServices_Data_RulePredicates_IsAutomaticForward.htm)|
Gets or sets a value indicating whether incoming messages must be automatic
forwards for the condition or exception to apply.  
[IsAutomaticReply](P_Tessa_Exchange_WebServices_Data_RulePredicates_IsAutomaticReply.htm)|
Gets or sets a value indicating whether incoming messages must be automatic
replies for the condition or exception to apply.  
[IsEncrypted](P_Tessa_Exchange_WebServices_Data_RulePredicates_IsEncrypted.htm)|
Gets or sets a value indicating whether incoming messages must be S/MIME
encrypted for the condition or exception to apply.  
[IsMeetingRequest](P_Tessa_Exchange_WebServices_Data_RulePredicates_IsMeetingRequest.htm)|
Gets or sets a value indicating whether incoming messages must be meeting
requests for the condition or exception to apply.  
[IsMeetingResponse](P_Tessa_Exchange_WebServices_Data_RulePredicates_IsMeetingResponse.htm)|
Gets or sets a value indicating whether incoming messages must be meeting
responses for the condition or exception to apply.  
[IsNonDeliveryReport](P_Tessa_Exchange_WebServices_Data_RulePredicates_IsNonDeliveryReport.htm)|
Gets or sets a value indicating whether incoming messages must be non-delivery
reports (NDR) for the condition or exception to apply.  
[IsPermissionControlled](P_Tessa_Exchange_WebServices_Data_RulePredicates_IsPermissionControlled.htm)|
Gets or sets a value indicating whether incoming messages must be permission
controlled (RMS protected) for the condition or exception to apply.  
[IsReadReceipt](P_Tessa_Exchange_WebServices_Data_RulePredicates_IsReadReceipt.htm)|
Gets or sets a value indicating whether incoming messages must be read
receipts for the condition or exception to apply.  
[IsSigned](P_Tessa_Exchange_WebServices_Data_RulePredicates_IsSigned.htm)|
Gets or sets a value indicating whether incoming messages must be S/MIME
signed for the condition or exception to apply.  
[IsVoicemail](P_Tessa_Exchange_WebServices_Data_RulePredicates_IsVoicemail.htm)|
Gets or sets a value indicating whether incoming messages must be voice mails
for the condition or exception to apply.  
[ItemClasses](P_Tessa_Exchange_WebServices_Data_RulePredicates_ItemClasses.htm)|
Gets the item classes that must be stamped on incoming messages for the
condition or exception to apply. To disable this predicate, empty the list.  
[MessageClassifications](P_Tessa_Exchange_WebServices_Data_RulePredicates_MessageClassifications.htm)|
Gets the message classifications that must be stamped on incoming messages for
the condition or exception to apply. To disable this predicate, empty the
list.  
[NotSentToMe](P_Tessa_Exchange_WebServices_Data_RulePredicates_NotSentToMe.htm)|
Gets or sets a value indicating whether the owner of the mailbox must NOT be a
To recipient of the incoming messages for the condition or exception to apply.  
[Sensitivity](P_Tessa_Exchange_WebServices_Data_RulePredicates_Sensitivity.htm)|
Gets or sets the sensitivity that must be stamped on incoming messages for the
condition or exception to apply. To disable this predicate, set it to null.  
[SentCcMe](P_Tessa_Exchange_WebServices_Data_RulePredicates_SentCcMe.htm)|
Gets or sets a value indicating whether the owner of the mailbox must be a Cc
recipient of incoming messages for the condition or exception to apply.  
[SentOnlyToMe](P_Tessa_Exchange_WebServices_Data_RulePredicates_SentOnlyToMe.htm)|
Gets or sets a value indicating whether the owner of the mailbox must be the
only To recipient of incoming messages for the condition or exception to
apply.  
[SentToAddresses](P_Tessa_Exchange_WebServices_Data_RulePredicates_SentToAddresses.htm)|
Gets the e-mail addresses incoming messages must have been sent to for the
condition or exception to apply. To disable this predicate, empty the list.  
[SentToMe](P_Tessa_Exchange_WebServices_Data_RulePredicates_SentToMe.htm)|
Gets or sets a value indicating whether the owner of the mailbox must be a To
recipient of incoming messages for the condition or exception to apply.  
[SentToOrCcMe](P_Tessa_Exchange_WebServices_Data_RulePredicates_SentToOrCcMe.htm)|
Gets or sets a value indicating whether the owner of the mailbox must be
either a To or Cc recipient of incoming messages for the condition or
exception to apply.  
[WithinDateRange](P_Tessa_Exchange_WebServices_Data_RulePredicates_WithinDateRange.htm)|
Gets the date range within which incoming messages must have been received for
the condition or exception to apply. To disable this predicate, set both its
Start and End properties to null.  
[WithinSizeRange](P_Tessa_Exchange_WebServices_Data_RulePredicates_WithinSizeRange.htm)|
Gets the minimum and maximum sizes incoming messages must have for the
condition or exception to apply. To disable this predicate, set both its
MinimumSize and MaximumSize properties to null.  
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
