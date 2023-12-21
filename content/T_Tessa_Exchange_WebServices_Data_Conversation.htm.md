# Conversation - класс
Represents a collection of Conversation related properties. Properties
available on this object are defined in the ConversationSchema class.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public class Conversation : ServiceObject
VB __Копировать
     Public Class Conversation
    	Inherits ServiceObject
C++ __Копировать
     public ref class Conversation : public ServiceObject
F# __Копировать
     type Conversation = 
        class
            inherit ServiceObject
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ServiceObject](T_Tessa_Exchange_WebServices_Data_ServiceObject.htm) __ Conversation
##  __Свойства
[Categories](P_Tessa_Exchange_WebServices_Data_Conversation_Categories.htm)|
Gets a list summarizing the categories stamped on messages in this
conversation, in the current folder only.  
---|---  
[DraftItemIds](P_Tessa_Exchange_WebServices_Data_Conversation_DraftItemIds.htm)|
Gets the draft item ids.  
[FlagStatus](P_Tessa_Exchange_WebServices_Data_Conversation_FlagStatus.htm)|
Gets the flag status for this conversation, calculated by aggregating
individual messages flag status in the current folder.  
[GlobalCategories](P_Tessa_Exchange_WebServices_Data_Conversation_GlobalCategories.htm)|
Gets a list summarizing the categories stamped on messages in this
conversation, across all folders in the mailbox.  
[GlobalFlagStatus](P_Tessa_Exchange_WebServices_Data_Conversation_GlobalFlagStatus.htm)|
Gets the flag status for this conversation, calculated by aggregating
individual messages flag status across all folders in the mailbox.  
[GlobalHasAttachments](P_Tessa_Exchange_WebServices_Data_Conversation_GlobalHasAttachments.htm)|
Gets a value indicating if at least one message in this conversation, across
all folders in the mailbox, has an attachment.  
[GlobalHasIrm](P_Tessa_Exchange_WebServices_Data_Conversation_GlobalHasIrm.htm)|
Gets a value indicating if at least one message in this conversation, across
all folders in the mailbox, is an IRM.  
[GlobalIconIndex](P_Tessa_Exchange_WebServices_Data_Conversation_GlobalIconIndex.htm)|
Gets the conversation global IconIndex.  
[GlobalImportance](P_Tessa_Exchange_WebServices_Data_Conversation_GlobalImportance.htm)|
Gets the importance of this conversation, calculated by aggregating individual
messages importance across all folders in the mailbox.  
[GlobalItemClasses](P_Tessa_Exchange_WebServices_Data_Conversation_GlobalItemClasses.htm)|
Gets a list summarizing the classes of the items in this conversation, across
all folders in the mailbox.  
[GlobalItemIds](P_Tessa_Exchange_WebServices_Data_Conversation_GlobalItemIds.htm)|
Gets the Ids of the messages in this conversation, across all folders in the
mailbox.  
[GlobalLastDeliveryTime](P_Tessa_Exchange_WebServices_Data_Conversation_GlobalLastDeliveryTime.htm)|
Gets the delivery time of the message that was last received in this
conversation across all folders in the mailbox.  
[GlobalMessageCount](P_Tessa_Exchange_WebServices_Data_Conversation_GlobalMessageCount.htm)|
Gets the total number of messages in this conversation across all folders in
the mailbox.  
[GlobalSize](P_Tessa_Exchange_WebServices_Data_Conversation_GlobalSize.htm)|
Gets the size of this conversation, calculated by adding the sizes of all
messages in the conversation across all folders in the mailbox.  
[GlobalUniqueRecipients](P_Tessa_Exchange_WebServices_Data_Conversation_GlobalUniqueRecipients.htm)|
Gets a list of all the people who have received messages in this conversation
across all folders in the mailbox.  
[GlobalUniqueSenders](P_Tessa_Exchange_WebServices_Data_Conversation_GlobalUniqueSenders.htm)|
Gets a list of all the people who have sent messages in this conversation
across all folders in the mailbox.  
[GlobalUniqueUnreadSenders](P_Tessa_Exchange_WebServices_Data_Conversation_GlobalUniqueUnreadSenders.htm)|
Gets a list of all the people who have sent messages that are currently unread
in this conversation across all folders in the mailbox.  
[GlobalUnreadCount](P_Tessa_Exchange_WebServices_Data_Conversation_GlobalUnreadCount.htm)|
Gets the total number of unread messages in this conversation across all
folders in the mailbox.  
[HasAttachments](P_Tessa_Exchange_WebServices_Data_Conversation_HasAttachments.htm)|
Gets a value indicating if at least one message in this conversation, in the
current folder only, has an attachment.  
[HasIrm](P_Tessa_Exchange_WebServices_Data_Conversation_HasIrm.htm)|  Gets a
value indicating if at least one message in this conversation, in the current
folder only, is an IRM.  
[IconIndex](P_Tessa_Exchange_WebServices_Data_Conversation_IconIndex.htm)|
Gets the conversation IconIndex.  
[Id](P_Tessa_Exchange_WebServices_Data_Conversation_Id.htm)|  Gets the Id of
this Conversation.  
[Importance](P_Tessa_Exchange_WebServices_Data_Conversation_Importance.htm)|
Gets the importance of this conversation, calculated by aggregating individual
messages importance in the current folder only.  
[InstanceKey](P_Tessa_Exchange_WebServices_Data_Conversation_InstanceKey.htm)|
Gets the conversation instance key.  
[IsDirty](P_Tessa_Exchange_WebServices_Data_ServiceObject_IsDirty.htm)|  Gets
a value indicating whether the object has been modified and should be saved.  
(Унаследован от
[ServiceObject](T_Tessa_Exchange_WebServices_Data_ServiceObject.htm))  
[IsNew](P_Tessa_Exchange_WebServices_Data_ServiceObject_IsNew.htm)|  Indicates
whether this object is a real store item, or if it's a local object that has
yet to be saved.  
(Унаследован от
[ServiceObject](T_Tessa_Exchange_WebServices_Data_ServiceObject.htm))  
[Item](P_Tessa_Exchange_WebServices_Data_ServiceObject_Item.htm)|  Gets the
value of specified property in this instance.  
(Унаследован от
[ServiceObject](T_Tessa_Exchange_WebServices_Data_ServiceObject.htm))  
[ItemClasses](P_Tessa_Exchange_WebServices_Data_Conversation_ItemClasses.htm)|
Gets a list summarizing the classes of the items in this conversation, in the
current folder only.  
[ItemIds](P_Tessa_Exchange_WebServices_Data_Conversation_ItemIds.htm)|  Gets
the Ids of the messages in this conversation, in the current folder only.  
[LastDeliveryTime](P_Tessa_Exchange_WebServices_Data_Conversation_LastDeliveryTime.htm)|
Gets the delivery time of the message that was last received in this
conversation in the current folder only.  
[LastModifiedTime](P_Tessa_Exchange_WebServices_Data_Conversation_LastModifiedTime.htm)|
Gets the date and time this conversation was last modified.  
[MessageCount](P_Tessa_Exchange_WebServices_Data_Conversation_MessageCount.htm)|
Gets the total number of messages in this conversation in the current folder
only.  
[Preview](P_Tessa_Exchange_WebServices_Data_Conversation_Preview.htm)|  Gets
the conversation Preview.  
[Schema](P_Tessa_Exchange_WebServices_Data_ServiceObject_Schema.htm)|  Gets
the schema associated with this type of object.  
(Унаследован от
[ServiceObject](T_Tessa_Exchange_WebServices_Data_ServiceObject.htm))  
[Service](P_Tessa_Exchange_WebServices_Data_ServiceObject_Service.htm)|  Gets
the ExchangeService the object is bound to.  
(Унаследован от
[ServiceObject](T_Tessa_Exchange_WebServices_Data_ServiceObject.htm))  
[Size](P_Tessa_Exchange_WebServices_Data_Conversation_Size.htm)|  Gets the
size of this conversation, calculated by adding the sizes of all messages in
the conversation in the current folder only.  
[Topic](P_Tessa_Exchange_WebServices_Data_Conversation_Topic.htm)|  Gets the
topic of this Conversation.  
[UniqueRecipients](P_Tessa_Exchange_WebServices_Data_Conversation_UniqueRecipients.htm)|
Gets a list of all the people who have received messages in this conversation
in the current folder only.  
[UniqueSenders](P_Tessa_Exchange_WebServices_Data_Conversation_UniqueSenders.htm)|
Gets a list of all the people who have sent messages in this conversation in
the current folder only.  
[UniqueUnreadSenders](P_Tessa_Exchange_WebServices_Data_Conversation_UniqueUnreadSenders.htm)|
Gets a list of all the people who have sent messages that are currently unread
in this conversation in the current folder only.  
[UnreadCount](P_Tessa_Exchange_WebServices_Data_Conversation_UnreadCount.htm)|
Gets the total number of unread messages in this conversation in the current
folder only.  
## __Методы
[ClearItemFlags](M_Tessa_Exchange_WebServices_Data_Conversation_ClearItemFlags.htm)|
Clear flags for conversation items. Calling this method results in a call to
EWS.  
---|---  
[CopyItemsInConversation](M_Tessa_Exchange_WebServices_Data_Conversation_CopyItemsInConversation.htm)|
Copies items in the specified conversation to a specific folder. Calling this
method results in a call to EWS.  
[DeleteItems](M_Tessa_Exchange_WebServices_Data_Conversation_DeleteItems.htm)|
Deletes items in the specified conversation. Calling this method results in a
call to EWS.  
[DisableAlwaysCategorizeItems](M_Tessa_Exchange_WebServices_Data_Conversation_DisableAlwaysCategorizeItems.htm)|
Sets up a conversation so that any item received within that conversation is
no longer categorized. Calling this method results in a call to EWS.  
[DisableAlwaysDeleteItems](M_Tessa_Exchange_WebServices_Data_Conversation_DisableAlwaysDeleteItems.htm)|
Sets up a conversation so that any item received within that conversation is
no longer moved to Deleted Items folder. Calling this method results in a call
to EWS.  
[DisableAlwaysMoveItemsInConversation](M_Tessa_Exchange_WebServices_Data_Conversation_DisableAlwaysMoveItemsInConversation.htm)|
Sets up a conversation so that any item received within that conversation is
no longer moved to a specific folder. Calling this method results in a call to
EWS.  
[EnableAlwaysCategorizeItems](M_Tessa_Exchange_WebServices_Data_Conversation_EnableAlwaysCategorizeItems.htm)|
Sets up a conversation so that any item received within that conversation is
always categorized. Calling this method results in a call to EWS.  
[EnableAlwaysDeleteItems](M_Tessa_Exchange_WebServices_Data_Conversation_EnableAlwaysDeleteItems.htm)|
Sets up a conversation so that any item received within that conversation is
always moved to Deleted Items folder. Calling this method results in a call to
EWS.  
[EnableAlwaysMoveItems](M_Tessa_Exchange_WebServices_Data_Conversation_EnableAlwaysMoveItems.htm)|
Sets up a conversation so that any item received within that conversation is
always moved to a specific folder. Calling this method results in a call to
EWS.  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[FlagItems](M_Tessa_Exchange_WebServices_Data_Conversation_FlagItems.htm)|
Flags conversation items. Calling this method results in a call to EWS.  
[FlagItemsComplete](M_Tessa_Exchange_WebServices_Data_Conversation_FlagItemsComplete.htm)|
Flag conversation items as complete. Calling this method results in a call to
EWS.  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetLoadedPropertyDefinitions](M_Tessa_Exchange_WebServices_Data_ServiceObject_GetLoadedPropertyDefinitions.htm)|
Gets the collection of loaded property definitions.  
(Унаследован от
[ServiceObject](T_Tessa_Exchange_WebServices_Data_ServiceObject.htm))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Load(CancellationToken)](M_Tessa_Exchange_WebServices_Data_ServiceObject_Load.htm)|
Loads the first class properties. Calling this method results in a call to
EWS.  
(Унаследован от
[ServiceObject](T_Tessa_Exchange_WebServices_Data_ServiceObject.htm))  
[Load(PropertySet,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ServiceObject_Load_1.htm)|
Loads the specified set of properties. Calling this method results in a call
to EWS.  
(Унаследован от
[ServiceObject](T_Tessa_Exchange_WebServices_Data_ServiceObject.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MoveItemsInConversation](M_Tessa_Exchange_WebServices_Data_Conversation_MoveItemsInConversation.htm)|
Moves items in the specified conversation to a specific folder. Calling this
method results in a call to EWS.  
[SetReadStateForItemsInConversation(FolderId,
Boolean)](M_Tessa_Exchange_WebServices_Data_Conversation_SetReadStateForItemsInConversation.htm)|
Sets the read state of items in the specified conversation. Calling this
method results in a call to EWS.  
[SetReadStateForItemsInConversation(FolderId, Boolean,
Boolean)](M_Tessa_Exchange_WebServices_Data_Conversation_SetReadStateForItemsInConversation_1.htm)|
Sets the read state of items in the specified conversation. Calling this
method results in a call to EWS.  
[SetRetentionPolicyForItemsInConversation](M_Tessa_Exchange_WebServices_Data_Conversation_SetRetentionPolicyForItemsInConversation.htm)|
Sets the retention policy of items in the specified conversation. Calling this
method results in a call to EWS.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGetProperty(PropertyDefinitionBase,
Object)](M_Tessa_Exchange_WebServices_Data_ServiceObject_TryGetProperty.htm)|
Try to get the value of a specified property in this instance.  
(Унаследован от
[ServiceObject](T_Tessa_Exchange_WebServices_Data_ServiceObject.htm))  
[TryGetProperty<T>(PropertyDefinitionBase,
T)](M_Tessa_Exchange_WebServices_Data_ServiceObject_TryGetProperty__1.htm)|
Try to get the value of a specified property in this instance.  
(Унаследован от
[ServiceObject](T_Tessa_Exchange_WebServices_Data_ServiceObject.htm))  
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
