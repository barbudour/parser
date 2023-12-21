# Appointment - класс
Represents an appointment or a meeting. Properties available on appointments
are defined in the AppointmentSchema class.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public class Appointment : Item
VB __Копировать
     Public Class Appointment
    	Inherits Item
C++ __Копировать
     public ref class Appointment : public Item
F# __Копировать
     type Appointment = 
        class
            inherit Item
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ServiceObject](T_Tessa_Exchange_WebServices_Data_ServiceObject.htm) __[Item](T_Tessa_Exchange_WebServices_Data_Item.htm) __ Appointment
##  __Конструкторы
[Appointment](M_Tessa_Exchange_WebServices_Data_Appointment__ctor.htm)|
Initializes an unsaved local instance of Appointment. To bind to an existing
appointment, use Appointment.Bind() instead.  
---|---  
## __Свойства
[AdjacentMeetingCount](P_Tessa_Exchange_WebServices_Data_Appointment_AdjacentMeetingCount.htm)|
Gets the number of calendar entries that are adjacent to this appointment in
the authenticated user's calendar.  
---|---  
[AdjacentMeetings](P_Tessa_Exchange_WebServices_Data_Appointment_AdjacentMeetings.htm)|
Gets a list of meetings that conflict with this appointment in the
authenticated user's calendar.  
[AllowedResponseActions](P_Tessa_Exchange_WebServices_Data_Item_AllowedResponseActions.htm)|
Gets a value indicating which response actions are allowed on this item.
Examples of response actions are Reply and Forward.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[AllowNewTimeProposal](P_Tessa_Exchange_WebServices_Data_Appointment_AllowNewTimeProposal.htm)|
Gets or sets a value indicating whether new time proposals are allowed for
attendees of this meeting.  
[AppointmentReplyTime](P_Tessa_Exchange_WebServices_Data_Appointment_AppointmentReplyTime.htm)|
Gets the time when the attendee replied to the meeting request.  
[AppointmentSequenceNumber](P_Tessa_Exchange_WebServices_Data_Appointment_AppointmentSequenceNumber.htm)|
Gets the sequence number of this appointment.  
[AppointmentState](P_Tessa_Exchange_WebServices_Data_Appointment_AppointmentState.htm)|
Gets the state of this appointment.  
[AppointmentType](P_Tessa_Exchange_WebServices_Data_Appointment_AppointmentType.htm)|
Gets a value indicating the type of this appointment.  
[ArchiveTag](P_Tessa_Exchange_WebServices_Data_Item_ArchiveTag.htm)|  Gets or
sets the archive tag.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[Attachments](P_Tessa_Exchange_WebServices_Data_Item_Attachments.htm)|  Gets a
list of the attachments to this item.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[Body](P_Tessa_Exchange_WebServices_Data_Item_Body.htm)|  Gets or sets the
body of this item.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[Categories](P_Tessa_Exchange_WebServices_Data_Item_Categories.htm)|  Gets or
sets the list of categories associated with this item.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[ConferenceType](P_Tessa_Exchange_WebServices_Data_Appointment_ConferenceType.htm)|
Gets or sets the type of conferencing that will be used during the meeting.  
[ConflictingMeetingCount](P_Tessa_Exchange_WebServices_Data_Appointment_ConflictingMeetingCount.htm)|
Gets the number of calendar entries that conflict with this appointment in the
authenticated user's calendar.  
[ConflictingMeetings](P_Tessa_Exchange_WebServices_Data_Appointment_ConflictingMeetings.htm)|
Gets a list of meetings that conflict with this appointment in the
authenticated user's calendar.  
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
[DeletedOccurrences](P_Tessa_Exchange_WebServices_Data_Appointment_DeletedOccurrences.htm)|
Gets a list of deleted occurrences for this meeting.  
[DisplayCc](P_Tessa_Exchange_WebServices_Data_Item_DisplayCc.htm)|  Gets a
text summarizing the Cc receipients of this item.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[DisplayTo](P_Tessa_Exchange_WebServices_Data_Item_DisplayTo.htm)|  Gets a
text summarizing the To recipients of this item.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[Duration](P_Tessa_Exchange_WebServices_Data_Appointment_Duration.htm)|  Gets
the duration of this appointment.  
[EffectiveRights](P_Tessa_Exchange_WebServices_Data_Item_EffectiveRights.htm)|
Gets a value indicating the effective rights the current authenticated user
has on this item.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[End](P_Tessa_Exchange_WebServices_Data_Appointment_End.htm)|  Gets or sets
the end time of the appointment.  
[EndTimeZone](P_Tessa_Exchange_WebServices_Data_Appointment_EndTimeZone.htm)|
Gets or sets time zone of the end property of this appointment.  
[EnhancedLocation](P_Tessa_Exchange_WebServices_Data_Appointment_EnhancedLocation.htm)|
Gets or sets the Enhanced location object.  
[EntityExtractionResult](P_Tessa_Exchange_WebServices_Data_Item_EntityExtractionResult.htm)|
Gets the EntityExtractionResult of the item.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[ExtendedProperties](P_Tessa_Exchange_WebServices_Data_Item_ExtendedProperties.htm)|
Gets a list of extended properties defined on this item.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[FirstOccurrence](P_Tessa_Exchange_WebServices_Data_Appointment_FirstOccurrence.htm)|
Gets an OccurrenceInfo identifying the first occurrence of this meeting.  
[Flag](P_Tessa_Exchange_WebServices_Data_Item_Flag.htm)|  Get or set the Flag
value for this item.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[HasAttachments](P_Tessa_Exchange_WebServices_Data_Item_HasAttachments.htm)|
Gets a value indicating whether the item has attachments.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[Hashtags](P_Tessa_Exchange_WebServices_Data_Item_Hashtags.htm)|  Gets or sets
the list of hashtags associated with this item.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[ICalDateTimeStamp](P_Tessa_Exchange_WebServices_Data_Appointment_ICalDateTimeStamp.htm)|
Gets the ICalendar DateTimeStamp.  
[ICalRecurrenceId](P_Tessa_Exchange_WebServices_Data_Appointment_ICalRecurrenceId.htm)|
Gets the ICalendar RecurrenceId.  
[ICalUid](P_Tessa_Exchange_WebServices_Data_Appointment_ICalUid.htm)|  Gets or
sets the ICalendar Uid.  
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
[IsAllDayEvent](P_Tessa_Exchange_WebServices_Data_Appointment_IsAllDayEvent.htm)|
Gets or sets a value indicating whether this appointment is an all day event.  
[IsAssociated](P_Tessa_Exchange_WebServices_Data_Item_IsAssociated.htm)|  Gets
a value indicating whether this is an associated item.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[IsAttachment](P_Tessa_Exchange_WebServices_Data_Item_IsAttachment.htm)|  Gets
a value indicating whether the item is an attachment.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[IsCancelled](P_Tessa_Exchange_WebServices_Data_Appointment_IsCancelled.htm)|
Gets a value indicating whether the appointment has been cancelled.  
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
[IsMeeting](P_Tessa_Exchange_WebServices_Data_Appointment_IsMeeting.htm)|
Gets a value indicating whether the appointment is a meeting.  
[IsNew](P_Tessa_Exchange_WebServices_Data_Item_IsNew.htm)|  Gets a value
indicating whether this object is a real store item, or if it's a local object
that has yet to be saved.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[IsOnlineMeeting](P_Tessa_Exchange_WebServices_Data_Appointment_IsOnlineMeeting.htm)|
Gets or sets a value indicating whether this is an online meeting.  
[IsRecurring](P_Tessa_Exchange_WebServices_Data_Appointment_IsRecurring.htm)|
Gets a value indicating whether the appointment is recurring.  
[IsReminderSet](P_Tessa_Exchange_WebServices_Data_Item_IsReminderSet.htm)|
Gets or sets a value indicating whether a reminder is set for this item.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[IsResend](P_Tessa_Exchange_WebServices_Data_Item_IsResend.htm)|  Gets a value
indicating whether the item is a resend of another item.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[IsResponseRequested](P_Tessa_Exchange_WebServices_Data_Appointment_IsResponseRequested.htm)|
Gets or sets a value indicating whether responses are requested when
invitations are sent for this meeting.  
[IsSubmitted](P_Tessa_Exchange_WebServices_Data_Item_IsSubmitted.htm)|  Gets a
value indicating whether the message has been submitted to be sent.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
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
[JoinOnlineMeetingUrl](P_Tessa_Exchange_WebServices_Data_Appointment_JoinOnlineMeetingUrl.htm)|
Gets the Url for joining an online meeting  
[LastModifiedName](P_Tessa_Exchange_WebServices_Data_Item_LastModifiedName.htm)|
Gets the name of the user who last modified this item.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[LastModifiedTime](P_Tessa_Exchange_WebServices_Data_Item_LastModifiedTime.htm)|
Gets the date and time this item was last modified.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[LastOccurrence](P_Tessa_Exchange_WebServices_Data_Appointment_LastOccurrence.htm)|
Gets an OccurrenceInfo identifying the last occurrence of this meeting.  
[LegacyFreeBusyStatus](P_Tessa_Exchange_WebServices_Data_Appointment_LegacyFreeBusyStatus.htm)|
Gets or sets a value indicating the free/busy status of the owner of this
appointment.  
[Location](P_Tessa_Exchange_WebServices_Data_Appointment_Location.htm)|  Gets
or sets the location of this appointment.  
[MeetingRequestWasSent](P_Tessa_Exchange_WebServices_Data_Appointment_MeetingRequestWasSent.htm)|
Gets a value indicating whether the meeting request has already been sent.  
[MeetingWorkspaceUrl](P_Tessa_Exchange_WebServices_Data_Appointment_MeetingWorkspaceUrl.htm)|
Gets or sets the URL of the meeting workspace. A meeting workspace is a shared
Web site for planning meetings and tracking results.  
[MentionedMe](P_Tessa_Exchange_WebServices_Data_Item_MentionedMe.htm)|  Gets a
value indicating whether the item mentions me.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[Mentions](P_Tessa_Exchange_WebServices_Data_Item_Mentions.htm)|  Gets the
Mentions associated with the message.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[MimeContent](P_Tessa_Exchange_WebServices_Data_Item_MimeContent.htm)|  Get or
sets the MIME content of this item.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[MimeContentUTF8](P_Tessa_Exchange_WebServices_Data_Item_MimeContentUTF8.htm)|
Get or sets the MimeContentUTF8 of this item.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[ModifiedOccurrences](P_Tessa_Exchange_WebServices_Data_Appointment_ModifiedOccurrences.htm)|
Gets a list of modified occurrences for this meeting.  
[MyResponseType](P_Tessa_Exchange_WebServices_Data_Appointment_MyResponseType.htm)|
Gets a value indicating what was the last response of the user that loaded
this meeting.  
[NetShowUrl](P_Tessa_Exchange_WebServices_Data_Appointment_NetShowUrl.htm)|
Gets or sets the URL of the Microsoft NetShow online meeting.  
[NormalizedBody](P_Tessa_Exchange_WebServices_Data_Item_NormalizedBody.htm)|
Gets the normalized body of the item.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[OnlineMeetingSettings](P_Tessa_Exchange_WebServices_Data_Appointment_OnlineMeetingSettings.htm)|
Gets the Online Meeting Settings  
[OptionalAttendees](P_Tessa_Exchange_WebServices_Data_Appointment_OptionalAttendees.htm)|
Gets a list of optional attendeed for this meeting.  
[Organizer](P_Tessa_Exchange_WebServices_Data_Appointment_Organizer.htm)|
Gets the organizer of this meeting. The Organizer property is read-only and is
only relevant for attendees. The organizer of a meeting is automatically set
to the user that created the meeting.  
[OriginalStart](P_Tessa_Exchange_WebServices_Data_Appointment_OriginalStart.htm)|
Gets the original start time of this appointment.  
[ParentFolderId](P_Tessa_Exchange_WebServices_Data_Item_ParentFolderId.htm)|
Gets the Id of the parent folder of this item.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[PolicyTag](P_Tessa_Exchange_WebServices_Data_Item_PolicyTag.htm)|  Gets or
sets the policy tag.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[Preview](P_Tessa_Exchange_WebServices_Data_Item_Preview.htm)|  Gets the item
Preview.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[Recurrence](P_Tessa_Exchange_WebServices_Data_Appointment_Recurrence.htm)|
Gets or sets the recurrence pattern for this appointment. Available recurrence
pattern classes include Recurrence.DailyPattern, Recurrence.MonthlyPattern and
Recurrence.YearlyPattern.  
[ReminderDueBy](P_Tessa_Exchange_WebServices_Data_Item_ReminderDueBy.htm)|
Gets or sets the date and time when the reminder is due for this item.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[ReminderMinutesBeforeStart](P_Tessa_Exchange_WebServices_Data_Item_ReminderMinutesBeforeStart.htm)|
Gets or sets the number of minutes before the start of this item when the
reminder should be triggered.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[RequiredAttendees](P_Tessa_Exchange_WebServices_Data_Appointment_RequiredAttendees.htm)|
Gets a list of required attendees for this meeting.  
[Resources](P_Tessa_Exchange_WebServices_Data_Appointment_Resources.htm)|
Gets a list of resources for this meeting.  
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
[Start](P_Tessa_Exchange_WebServices_Data_Appointment_Start.htm)|  Gets or
sets the start time of the appointment.  
[StartTimeZone](P_Tessa_Exchange_WebServices_Data_Appointment_StartTimeZone.htm)|
Gets or sets time zone of the start property of this appointment.  
[StoreEntryId](P_Tessa_Exchange_WebServices_Data_Item_StoreEntryId.htm)|  Gets
the store entry id.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[Subject](P_Tessa_Exchange_WebServices_Data_Item_Subject.htm)|  Gets or sets
the subject of this item.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[TextBody](P_Tessa_Exchange_WebServices_Data_Item_TextBody.htm)|  Gets the
text body of the item.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[TimeZone](P_Tessa_Exchange_WebServices_Data_Appointment_TimeZone.htm)|  Gets
the name of the time zone this appointment is defined in.  
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
[When](P_Tessa_Exchange_WebServices_Data_Appointment_When.htm)|  Gets a text
indicating when this appointment occurs. The text returned by When is
localized using the Exchange Server culture or using the culture specified in
the PreferredCulture property of the ExchangeService object this appointment
is bound to.  
## __Методы
[Accept](M_Tessa_Exchange_WebServices_Data_Appointment_Accept.htm)|  Accepts
the meeting. Calling this method results in a call to EWS.  
---|---  
[AcceptTentatively](M_Tessa_Exchange_WebServices_Data_Appointment_AcceptTentatively.htm)|
Tentatively accepts the meeting. Calling this method results in a call to EWS.  
[Bind(ExchangeService,
ItemId)](M_Tessa_Exchange_WebServices_Data_Appointment_Bind.htm)|  Binds to an
existing appointment and loads its first class properties. Calling this method
results in a call to EWS.  
[Bind(ExchangeService, ItemId, PropertySet,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_Appointment_Bind_1.htm)|
Binds to an existing appointment and loads the specified set of properties.
Calling this method results in a call to EWS.  
[BindToOccurrence(ExchangeService, ItemId,
Int32)](M_Tessa_Exchange_WebServices_Data_Appointment_BindToOccurrence.htm)|
Binds to an occurence of an existing appointment and loads its first class
properties. Calling this method results in a call to EWS.  
[BindToOccurrence(ExchangeService, ItemId, Int32,
PropertySet)](M_Tessa_Exchange_WebServices_Data_Appointment_BindToOccurrence_1.htm)|
Binds to an occurence of an existing appointment and loads the specified set
of properties. Calling this method results in a call to EWS.  
[BindToRecurringMaster(ExchangeService,
ItemId)](M_Tessa_Exchange_WebServices_Data_Appointment_BindToRecurringMaster.htm)|
Binds to the master appointment of a recurring series and loads its first
class properties. Calling this method results in a call to EWS.  
[BindToRecurringMaster(ExchangeService, ItemId,
PropertySet)](M_Tessa_Exchange_WebServices_Data_Appointment_BindToRecurringMaster_1.htm)|
Binds to the master appointment of a recurring series and loads the specified
set of properties. Calling this method results in a call to EWS.  
[CancelMeeting()](M_Tessa_Exchange_WebServices_Data_Appointment_CancelMeeting.htm)|
Cancels the meeting and sends cancellation messages to all attendees. Calling
this method results in a call to EWS.  
[CancelMeeting(String)](M_Tessa_Exchange_WebServices_Data_Appointment_CancelMeeting_1.htm)|
Cancels the meeting and sends cancellation messages to all attendees. Calling
this method results in a call to EWS.  
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
[CreateAcceptMessage](M_Tessa_Exchange_WebServices_Data_Appointment_CreateAcceptMessage.htm)|
Creates a local meeting acceptance message that can be customized and sent.  
[CreateCancelMeetingMessage](M_Tessa_Exchange_WebServices_Data_Appointment_CreateCancelMeetingMessage.htm)|
Creates a local meeting cancellation message that can be customized and sent.  
[CreateDeclineMessage](M_Tessa_Exchange_WebServices_Data_Appointment_CreateDeclineMessage.htm)|
Creates a local meeting declination message that can be customized and sent.  
[CreateForward](M_Tessa_Exchange_WebServices_Data_Appointment_CreateForward.htm)|
Creates a forward message from this appointment.  
[CreateReply](M_Tessa_Exchange_WebServices_Data_Appointment_CreateReply.htm)|
Creates a reply response to the organizer and/or attendees of the meeting.  
[Decline](M_Tessa_Exchange_WebServices_Data_Appointment_Decline.htm)|
Declines the meeting invitation. Calling this method results in a call to EWS.  
[Delete(DeleteMode)](M_Tessa_Exchange_WebServices_Data_Item_Delete.htm)|
Deletes the item. Calling this method results in a call to EWS.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[Delete(DeleteMode, SendCancellationsMode,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_Appointment_Delete.htm)|
Deletes this appointment. Calling this method results in a call to EWS.  
[Delete(DeleteMode, Boolean,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_Item_Delete_1.htm)|
Deletes the item. Calling this method results in a call to EWS.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
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
[Forward(MessageBody,
IEnumerable<EmailAddress>)](M_Tessa_Exchange_WebServices_Data_Appointment_Forward.htm)|
Forwards the appointment. Calling this method results in a call to EWS.  
[Forward(MessageBody,
EmailAddress[])](M_Tessa_Exchange_WebServices_Data_Appointment_Forward_1.htm)|
Forwards the appointment. Calling this method results in a call to EWS.  
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
[Reply](M_Tessa_Exchange_WebServices_Data_Appointment_Reply.htm)|  Replies to
the organizer and/or the attendees of the meeting. Calling this method results
in a call to EWS.  
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
[Save(SendInvitationsMode,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_Appointment_Save_1.htm)|
Saves this appointment in the Calendar folder. Calling this method results in
at least one call to EWS. Mutliple calls to EWS might be made if attachments
have been added.  
[Save(WellKnownFolderName,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_Item_Save_2.htm)|  Saves
this item in a specific folder. Calling this method results in at least one
call to EWS. Mutliple calls to EWS might be made if attachments have been
added.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[Save(FolderId, SendInvitationsMode,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_Appointment_Save.htm)|
Saves this appointment in the specified folder. Calling this method results in
at least one call to EWS. Mutliple calls to EWS might be made if attachments
have been added.  
[Save(WellKnownFolderName, SendInvitationsMode,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_Appointment_Save_2.htm)|
Saves this appointment in the specified folder. Calling this method results in
at least one call to EWS. Mutliple calls to EWS might be made if attachments
have been added.  
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
CancellationToken)](M_Tessa_Exchange_WebServices_Data_Item_Update_1.htm)|
Applies the local changes that have been made to this item. Calling this
method results in at least one call to EWS. Mutliple calls to EWS might be
made if attachments have been added or removed.  
(Унаследован от [Item](T_Tessa_Exchange_WebServices_Data_Item.htm))  
[Update(ConflictResolutionMode, SendInvitationsOrCancellationsMode,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_Appointment_Update.htm)|
Applies the local changes that have been made to this appointment. Calling
this method results in at least one call to EWS. Mutliple calls to EWS might
be made if attachments have been added or removed.  
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
