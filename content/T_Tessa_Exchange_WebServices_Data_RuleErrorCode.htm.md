# RuleErrorCode - перечисление
Defines the error codes identifying why a rule failed validation.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public enum RuleErrorCode
VB __Копировать
     Public Enumeration RuleErrorCode
C++ __Копировать
     public enum class RuleErrorCode
F# __Копировать
     type RuleErrorCode
##  __Члены
ADOperationFailure| 0|  Active Directory operation failed.  
---|---|---  
ConnectedAccountNotFound| 1|  The e-mail account specified in the
FromConnectedAccounts predicate was not found.  
CreateWithRuleId| 2|  The Rule object in a CreateInboxRuleOperation has an Id.
The Ids of new rules are generated server side and should not be provided by
the client.  
EmptyValueFound| 3|  The value is empty. An empty value is not allowed for the
property.  
DuplicatedPriority| 4|  There already is a rule with the same priority.  
DuplicatedOperationOnTheSameRule| 5|  There are multiple operations against
the same rule. Only one operation per rule is allowed.  
FolderDoesNotExist| 6|  The folder does not exist in the user's mailbox.  
InvalidAddress| 7|  The e-mail address is invalid.  
InvalidDateRange| 8|  The date range is invalid.  
InvalidFolderId| 9|  The folder Id is invalid.  
InvalidSizeRange| 10|  The size range is invalid.  
InvalidValue| 11|  The value is invalid.  
MessageClassificationNotFound| 12|  The message classification was not found.  
MissingAction| 13|  No action was specified. At least one action must be
specified.  
MissingParameter| 14|  The required parameter is missing.  
MissingRangeValue| 15|  The range value is missing.  
NotSettable| 16|  The property cannot be modified.  
RecipientDoesNotExist| 17|  The recipient does not exist.  
RuleNotFound| 18|  The rule was not found.  
SizeLessThanZero| 19|  The size is less than zero.  
StringValueTooBig| 20|  The string value is too big.  
UnsupportedAddress| 21|  The address is unsupported.  
UnexpectedError| 22|  An unexpected error occured.  
UnsupportedRule| 23|  The rule is not supported.  
## __См. также
#### Ссылки
[Tessa.Exchange.WebServices.Data - пространство
имён](N_Tessa_Exchange_WebServices_Data.htm)
