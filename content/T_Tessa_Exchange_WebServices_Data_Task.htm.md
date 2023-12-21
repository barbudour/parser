# Task - класс
Represents a Task item. Properties available on tasks are defined in the
TaskSchema class.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public class Task : Item
VB __Копировать
     Public Class Task
    	Inherits Item
C++ __Копировать
     public ref class Task : public Item
F# __Копировать
     type Task = 
        class
            inherit Item
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ServiceObject](T_Tessa_Exchange_WebServices_Data_ServiceObject.htm) __[Item](T_Tessa_Exchange_WebServices_Data_Item.htm) __ Task
##  __Конструкторы
[Task](M_Tessa_Exchange_WebServices_Data_Task__ctor.htm)|  Initializes an
unsaved local instance of Task. To bind to an existing task, use Task.Bind()
instead.  
---|---  
## __Свойства
[ActualWork](P_Tessa_Exchange_WebServices_Data_Task_ActualWork.htm)|  Gets or
sets the actual amount of time that is spent on the task.  
---|---  
[AllowedResponseActions](P_Tessa_Exchange_WebServices_Data_Item_AllowedResponseActions.htm)|
Gets a value indicating which response actions are allowed on this item.
Examples of response actions are Reply and Forward.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[ArchiveTag](P_Tessa_Exchange_WebServices_Data_Item_ArchiveTag.htm)|  Gets or
sets the archive tag.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[AssignedTime](P_Tessa_Exchange_WebServices_Data_Task_AssignedTime.htm)|  Gets
the date and time the task was assigned.  
[Attachments](P_Tessa_Exchange_WebServices_Data_Item_Attachments.htm)|  Gets a
list of the attachments to this item.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[BillingInformation](P_Tessa_Exchange_WebServices_Data_Task_BillingInformation.htm)|
Gets or sets the billing information of the task.  
[Body](P_Tessa_Exchange_WebServices_Data_Item_Body.htm)|  Gets or sets the
body of this item.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[Categories](P_Tessa_Exchange_WebServices_Data_Item_Categories.htm)|  Gets or
sets the list of categories associated with this item.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[ChangeCount](P_Tessa_Exchange_WebServices_Data_Task_ChangeCount.htm)|  Gets
the number of times the task has changed since it was created.  
[Companies](P_Tessa_Exchange_WebServices_Data_Task_Companies.htm)|  Gets or
sets a list of companies associated with the task.  
[CompleteDate](P_Tessa_Exchange_WebServices_Data_Task_CompleteDate.htm)|  Gets
or sets the date and time on which the task was completed.  
[Contacts](P_Tessa_Exchange_WebServices_Data_Task_Contacts.htm)|  Gets or sets
a list of contacts associated with the task.  
[ConversationId](P_Tessa_Exchange_WebServices_Data_Item_ConversationId.htm)|
Gets the Id of the conversation this item is part of.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[Culture](P_Tessa_Exchange_WebServices_Data_Item_Culture.htm)|  Gets or sets
the culture associated with this item.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[DateTimeCreated](P_Tessa_Exchange_WebServices_Data_Item_DateTimeCreated.htm)|
Gets the date and time this item was created.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[DateTimeReceived](P_Tessa_Exchange_WebServices_Data_Item_DateTimeReceived.htm)|
Gets the time when this item was received.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[DateTimeSent](P_Tessa_Exchange_WebServices_Data_Item_DateTimeSent.htm)|  Gets
the date and time this item was sent.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[DelegationState](P_Tessa_Exchange_WebServices_Data_Task_DelegationState.htm)|
Gets the current delegation state of the task.  
[Delegator](P_Tessa_Exchange_WebServices_Data_Task_Delegator.htm)|  Gets the
name of the delegator of this task.  
[DisplayCc](P_Tessa_Exchange_WebServices_Data_Item_DisplayCc.htm)|  Gets a
text summarizing the Cc receipients of this item.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[DisplayTo](P_Tessa_Exchange_WebServices_Data_Item_DisplayTo.htm)|  Gets a
text summarizing the To recipients of this item.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[DueDate](P_Tessa_Exchange_WebServices_Data_Task_DueDate.htm)|  Gets or sets
the date and time on which the task is due.  
[EffectiveRights](P_Tessa_Exchange_WebServices_Data_Item_EffectiveRights.htm)|
Gets a value indicating the effective rights the current authenticated user
has on this item.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[EntityExtractionResult](P_Tessa_Exchange_WebServices_Data_Item_EntityExtractionResult.htm)|
Gets the EntityExtractionResult of the item.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[ExtendedProperties](P_Tessa_Exchange_WebServices_Data_Item_ExtendedProperties.htm)|
Gets a list of extended properties defined on this item.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[Flag](P_Tessa_Exchange_WebServices_Data_Item_Flag.htm)|  Get or set the Flag
value for this item.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[HasAttachments](P_Tessa_Exchange_WebServices_Data_Item_HasAttachments.htm)|
Gets a value indicating whether the item has attachments.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[Hashtags](P_Tessa_Exchange_WebServices_Data_Item_Hashtags.htm)|  Gets or sets
the list of hashtags associated with this item.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[IconIndex](P_Tessa_Exchange_WebServices_Data_Item_IconIndex.htm)|  Gets the
icon index.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[Id](P_Tessa_Exchange_WebServices_Data_Item_Id.htm)|  Gets the Id of this
item.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[Importance](P_Tessa_Exchange_WebServices_Data_Item_Importance.htm)|  Gets or
sets the importance of this item.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[InReplyTo](P_Tessa_Exchange_WebServices_Data_Item_InReplyTo.htm)|  Gets or
sets the In-Reply-To reference of this item.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[InstanceKey](P_Tessa_Exchange_WebServices_Data_Item_InstanceKey.htm)|  Gets
the item instance key.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[InternetMessageHeaders](P_Tessa_Exchange_WebServices_Data_Item_InternetMessageHeaders.htm)|
Gets a list of Internet headers for this item.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[IsAssociated](P_Tessa_Exchange_WebServices_Data_Item_IsAssociated.htm)|  Gets
a value indicating whether this is an associated item.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[IsAttachment](P_Tessa_Exchange_WebServices_Data_Item_IsAttachment.htm)|  Gets
a value indicating whether the item is an attachment.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[IsComplete](P_Tessa_Exchange_WebServices_Data_Task_IsComplete.htm)|  Gets a
value indicating whether the task is complete.  
[IsDirty](P_Tessa_Exchange_WebServices_Data_ServiceObject_IsDirty.htm)|  Gets
a value indicating whether the object has been modified and should be saved.  
(Унаследован от
[ServiceObject](T_Tessa_Exchange_WebServices_Data_ServiceObject.htm))  
[IsDraft](P_Tessa_Exchange_WebServices_Data_Item_IsDraft.htm)|  Gets a value
indicating whether the item is is a draft. An item is a draft when it has not
yet been sent.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[IsFromMe](P_Tessa_Exchange_WebServices_Data_Item_IsFromMe.htm)|  Gets a value
indicating whether the item has been sent by the current authenticated user.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[IsNew](P_Tessa_Exchange_WebServices_Data_Item_IsNew.htm)|  Gets a value
indicating whether this object is a real store item, or if it's a local object
that has yet to be saved.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[IsRecurring](P_Tessa_Exchange_WebServices_Data_Task_IsRecurring.htm)|  Gets a
value indicating whether the task is recurring.  
[IsReminderSet](P_Tessa_Exchange_WebServices_Data_Item_IsReminderSet.htm)|
Gets or sets a value indicating whether a reminder is set for this item.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[IsResend](P_Tessa_Exchange_WebServices_Data_Item_IsResend.htm)|  Gets a value
indicating whether the item is a resend of another item.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[IsSubmitted](P_Tessa_Exchange_WebServices_Data_Item_IsSubmitted.htm)|  Gets a
value indicating whether the message has been submitted to be sent.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[IsTeamTask](P_Tessa_Exchange_WebServices_Data_Task_IsTeamTask.htm)|  Gets a
value indicating whether the task is a team task.  
[IsUnmodified](P_Tessa_Exchange_WebServices_Data_Item_IsUnmodified.htm)|  Gets
a value indicating whether the item has been modified since it was created.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[Item](P_Tessa_Exchange_WebServices_Data_ServiceObject_Item.htm)|  Gets the
value of specified property in this instance.  
(Унаследован от
[ServiceObject](T_Tessa_Exchange_WebServices_Data_ServiceObject.htm))  
[ItemClass](P_Tessa_Exchange_WebServices_Data_Item_ItemClass.htm)|  Gets or
sets the custom class name of this item.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[LastModifiedName](P_Tessa_Exchange_WebServices_Data_Item_LastModifiedName.htm)|
Gets the name of the user who last modified this item.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[LastModifiedTime](P_Tessa_Exchange_WebServices_Data_Item_LastModifiedTime.htm)|
Gets the date and time this item was last modified.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[MentionedMe](P_Tessa_Exchange_WebServices_Data_Item_MentionedMe.htm)|  Gets a
value indicating whether the item mentions me.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[Mentions](P_Tessa_Exchange_WebServices_Data_Item_Mentions.htm)|  Gets the
Mentions associated with the message.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[Mileage](P_Tessa_Exchange_WebServices_Data_Task_Mileage.htm)|  Gets or sets
the mileage of the task.  
[MimeContent](P_Tessa_Exchange_WebServices_Data_Item_MimeContent.htm)|  Get or
sets the MIME content of this item.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[MimeContentUTF8](P_Tessa_Exchange_WebServices_Data_Item_MimeContentUTF8.htm)|
Get or sets the MimeContentUTF8 of this item.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[Mode](P_Tessa_Exchange_WebServices_Data_Task_Mode.htm)|  Gets a value
indicating the mode of the task.  
[NormalizedBody](P_Tessa_Exchange_WebServices_Data_Item_NormalizedBody.htm)|
Gets the normalized body of the item.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[Owner](P_Tessa_Exchange_WebServices_Data_Task_Owner.htm)|  Gets the name of
the owner of the task.  
[ParentFolderId](P_Tessa_Exchange_WebServices_Data_Item_ParentFolderId.htm)|
Gets the Id of the parent folder of this item.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[PercentComplete](P_Tessa_Exchange_WebServices_Data_Task_PercentComplete.htm)|
Gets or sets the completeion percentage of the task. PercentComplete must be
between 0 and 100.  
[PolicyTag](P_Tessa_Exchange_WebServices_Data_Item_PolicyTag.htm)|  Gets or
sets the policy tag.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[Preview](P_Tessa_Exchange_WebServices_Data_Item_Preview.htm)|  Gets the item
Preview.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[Recurrence](P_Tessa_Exchange_WebServices_Data_Task_Recurrence.htm)|  Gets or
sets the recurrence pattern for this task. Available recurrence pattern
classes include Recurrence.DailyPattern, Recurrence.MonthlyPattern and
Recurrence.YearlyPattern.  
[ReminderDueBy](P_Tessa_Exchange_WebServices_Data_Item_ReminderDueBy.htm)|
Gets or sets the date and time when the reminder is due for this item.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[ReminderMinutesBeforeStart](P_Tessa_Exchange_WebServices_Data_Item_ReminderMinutesBeforeStart.htm)|
Gets or sets the number of minutes before the start of this item when the
reminder should be triggered.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[RetentionDate](P_Tessa_Exchange_WebServices_Data_Item_RetentionDate.htm)|
Gets the retention date.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[Schema](P_Tessa_Exchange_WebServices_Data_ServiceObject_Schema.htm)|  Gets
the schema associated with this type of object.  
(Унаследован от
[ServiceObject](T_Tessa_Exchange_WebServices_Data_ServiceObject.htm))  
[Sensitivity](P_Tessa_Exchange_WebServices_Data_Item_Sensitivity.htm)|  Gets
or sets the sensitivity of this item.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[Service](P_Tessa_Exchange_WebServices_Data_ServiceObject_Service.htm)|  Gets
the ExchangeService the object is bound to.  
(Унаследован от
[ServiceObject](T_Tessa_Exchange_WebServices_Data_ServiceObject.htm))  
[Size](P_Tessa_Exchange_WebServices_Data_Item_Size.htm)|  Gets the size of
this item.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[StartDate](P_Tessa_Exchange_WebServices_Data_Task_StartDate.htm)|  Gets or
sets the date and time on which the task starts.  
[Status](P_Tessa_Exchange_WebServices_Data_Task_Status.htm)|  Gets or sets the
status of the task.  
[StatusDescription](P_Tessa_Exchange_WebServices_Data_Task_StatusDescription.htm)|
Gets a string representing the status of the task, localized according to the
PreferredCulture property of the ExchangeService object the task is bound to.  
[StoreEntryId](P_Tessa_Exchange_WebServices_Data_Item_StoreEntryId.htm)|  Gets
the store entry id.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[Subject](P_Tessa_Exchange_WebServices_Data_Item_Subject.htm)|  Gets or sets
the subject of this item.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[TextBody](P_Tessa_Exchange_WebServices_Data_Item_TextBody.htm)|  Gets the
text body of the item.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[TotalWork](P_Tessa_Exchange_WebServices_Data_Task_TotalWork.htm)|  Gets or
sets the total amount of work spent on the task.  
[UniqueBody](P_Tessa_Exchange_WebServices_Data_Item_UniqueBody.htm)|  Gets the
body part that is unique to the conversation this item is part of.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[WebClientEditFormQueryString](P_Tessa_Exchange_WebServices_Data_Item_WebClientEditFormQueryString.htm)|
Gets the query string that should be appended to the Exchange Web client URL
to open this item using the appropriate edit form in a web browser.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[WebClientReadFormQueryString](P_Tessa_Exchange_WebServices_Data_Item_WebClientReadFormQueryString.htm)|
Gets the query string that should be appended to the Exchange Web client URL
to open this item using the appropriate read form in a web browser.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
##  __Методы
[Bind(ExchangeService,
ItemId)](M_Tessa_Exchange_WebServices_Data_Task_Bind.htm)|  Binds to an
existing task and loads its first class properties. Calling this method
results in a call to EWS.  
---|---  
[Bind(ExchangeService, ItemId, PropertySet,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_Task_Bind_1.htm)|  Binds
to an existing task and loads the specified set of properties. Calling this
method results in a call to EWS.  
[Copy(WellKnownFolderName)](M_Tessa_Exchange_WebServices_Data_Item_Copy_1.htm)|
Creates a copy of this item in the specified folder. Calling this method
results in a call to EWS.
Copy returns null if the copy operation is across two mailboxes or between a
mailbox and a public folder.
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[Copy(FolderId,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_Item_Copy.htm)|  Creates
a copy of this item in the specified folder. Calling this method results in a
call to EWS.
Copy returns null if the copy operation is across two mailboxes or between a
mailbox and a public folder.
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[Delete(DeleteMode)](M_Tessa_Exchange_WebServices_Data_Item_Delete.htm)|
Deletes the item. Calling this method results in a call to EWS.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[Delete(DeleteMode, Boolean,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_Item_Delete_1.htm)|
Deletes the item. Calling this method results in a call to EWS.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[DeleteCurrentOccurrence](M_Tessa_Exchange_WebServices_Data_Task_DeleteCurrentOccurrence.htm)|
Deletes the current occurrence of a recurring task. After the current
occurrence isdeleted, the task represents the next occurrence. Developers
should call Load to retrieve the new property values of the task. Calling this
method results in a call to EWS.  
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
[Move(WellKnownFolderName)](M_Tessa_Exchange_WebServices_Data_Item_Move_1.htm)|
Moves this item to a the specified folder. Calling this method results in a
call to EWS.
Move returns null if the move operation is across two mailboxes or between a
mailbox and a public folder.
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[Move(FolderId,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_Item_Move.htm)|  Moves
this item to a the specified folder. Calling this method results in a call to
EWS.
Move returns null if the move operation is across two mailboxes or between a
mailbox and a public folder.
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[RemoveExtendedProperty](M_Tessa_Exchange_WebServices_Data_Item_RemoveExtendedProperty.htm)|
Removes an extended property.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[Save(CancellationToken)](M_Tessa_Exchange_WebServices_Data_Item_Save.htm)|
Saves this item in the default folder based on the item's type (for example,
an e-mail message is saved to the Drafts folder). Calling this method results
in at least one call to EWS. Mutliple calls to EWS might be made if
attachments have been added.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[Save(FolderId,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_Item_Save_1.htm)|  Saves
this item in a specific folder. Calling this method results in at least one
call to EWS. Mutliple calls to EWS might be made if attachments have been
added.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[Save(WellKnownFolderName,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_Item_Save_2.htm)|  Saves
this item in a specific folder. Calling this method results in at least one
call to EWS. Mutliple calls to EWS might be made if attachments have been
added.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[SetExtendedProperty](M_Tessa_Exchange_WebServices_Data_Item_SetExtendedProperty.htm)|
Sets the extended property.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
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
[Update(ConflictResolutionMode,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_Task_Update.htm)|
Applies the local changes that have been made to this task. Calling this
method results in at least one call to EWS. Mutliple calls to EWS might be
made if attachments have been added or removed.  
[Update(ConflictResolutionMode, Boolean,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_Item_Update.htm)|
Applies the local changes that have been made to this item. Calling this
method results in at least one call to EWS. Mutliple calls to EWS might be
made if attachments have been added or removed.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
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
