# ServiceError - перечисление
Defines the error codes that can be returned by the Exchange Web Services.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public enum ServiceError
VB __Копировать
     Public Enumeration ServiceError
C++ __Копировать
     public enum class ServiceError
F# __Копировать
     type ServiceError
##  __Члены
NoError| 0|  NoError. Indicates that an error has not occurred.  
---|---|---  
ErrorAccessDenied| 1|  Access is denied. Check credentials and try again.  
ErrorAccessModeSpecified| 2|  The impersonation authentication header should
not be included.  
ErrorAccountDisabled| 3|  Account is disabled. Contact the account
administrator.  
ErrorAddDelegatesFailed| 4|  Failed to add one or more delegates.  
ErrorAddressSpaceNotFound| 5|  ErrorAddressSpaceNotFound  
ErrorADOperation| 6|  Active Directory operation did not succeed. Try again
later.  
ErrorADSessionFilter| 7|  Invalid search criteria.  
ErrorADUnavailable| 8|  Active Directory is unavailable. Try again later.  
ErrorAffectedTaskOccurrencesRequired| 9|  AffectedTaskOccurrences attribute is
required for Task items.  
ErrorApplyConversationActionFailed| 10|  The conversation action
alwayscategorize or alwaysmove or alwaysdelete has failed.  
ErrorArchiveMailboxNotEnabled| 11|  Archive mailbox not enabled  
ErrorArchiveFolderPathCreation| 12|  Unable to create the folder in archive
mailbox to which the items will be archived  
ErrorArchiveMailboxServiceDiscoveryFailed| 13|  Unable to discover archive
mailbox  
ErrorAttachmentNestLevelLimitExceeded| 14|  The item has attachment at more
than the maximum supported nest level.  
ErrorAttachmentSizeLimitExceeded| 15|  The file attachment exceeds the maximum
supported size.  
ErrorAutoDiscoverFailed| 16|  ErrorAutoDiscoverFailed  
ErrorAvailabilityConfigNotFound| 17|  ErrorAvailabilityConfigNotFound  
ErrorBatchProcessingStopped| 18|  Item was not processed as a result of a
previous error.  
ErrorCalendarCannotMoveOrCopyOccurrence| 19|  Can not move or copy a calendar
occurrence.  
ErrorCalendarCannotUpdateDeletedItem| 20|  Cannot update calendar item that
has already been deleted.  
ErrorCalendarCannotUseIdForOccurrenceId| 21|  The Id specified does not
represent an occurrence.  
ErrorCalendarCannotUseIdForRecurringMasterId| 22|  The specified Id does not
represent a recurring master item.  
ErrorCalendarDurationIsTooLong| 23|  Calendar item duration is too long.  
ErrorCalendarEndDateIsEarlierThanStartDate| 24|  EndDate is earlier than
StartDate  
ErrorCalendarFolderIsInvalidForCalendarView| 25|  Cannot request CalendarView
for the folder.  
ErrorCalendarInvalidAttributeValue| 26|  Attribute has an invalid value.  
ErrorCalendarInvalidDayForTimeChangePattern| 27|  The value of the DaysOfWeek
property is not valid for time change pattern of time zone.  
ErrorCalendarInvalidDayForWeeklyRecurrence| 28|  The value of the DaysOfWeek
property is invalid for a weekly recurrence.  
ErrorCalendarInvalidPropertyState| 29|  The property has invalid state.  
ErrorCalendarInvalidPropertyValue| 30|  The property has an invalid value.  
ErrorCalendarInvalidRecurrence| 31|  The recurrence is invalid.  
ErrorCalendarInvalidTimeZone| 32|  TimeZone is invalid.  
ErrorCalendarIsCancelledForAccept| 33|  A meeting that's been canceled can't
be accepted.  
ErrorCalendarIsCancelledForDecline| 34|  A canceled meeting can't be declined.  
ErrorCalendarIsCancelledForRemove| 35|  A canceled meeting can't be removed.  
ErrorCalendarIsCancelledForTentative| 36|  A canceled meeting can't be
accepted tentatively.  
ErrorCalendarIsDelegatedForAccept| 37|  AcceptItem action is invalid for a
delegated meeting message.  
ErrorCalendarIsDelegatedForDecline| 38|  DeclineItem operation is invalid for
a delegated meeting message.  
ErrorCalendarIsDelegatedForRemove| 39|  RemoveItem action is invalid for a
delegated meeting message.  
ErrorCalendarIsDelegatedForTentative| 40|  The TentativelyAcceptItem action
isn't valid for a delegated meeting message.  
ErrorCalendarIsNotOrganizer| 41|  User must be an organizer for
CancelCalendarItem action.  
ErrorCalendarIsOrganizerForAccept| 42|  The user is the organizer of this
meeting, and cannot, therefore, accept it.  
ErrorCalendarIsOrganizerForDecline| 43|  The user is the organizer of this
meeting, and cannot, therefore, decline it.  
ErrorCalendarIsOrganizerForRemove| 44|  The user is the organizer of this
meeting, and cannot, therefore, remove it.  
ErrorCalendarIsOrganizerForTentative| 45|  The user is the organizer of this
meeting, and therefore can't tentatively accept it.  
ErrorCalendarMeetingRequestIsOutOfDate| 46|  The meeting request is out of
date. The calendar couldn't be updated.  
ErrorCalendarOccurrenceIndexIsOutOfRecurrenceRange| 47|  Occurrence index is
out of recurrence range.  
ErrorCalendarOccurrenceIsDeletedFromRecurrence| 48|  Occurrence with this
index was previously deleted from the recurrence.  
ErrorCalendarOutOfRange| 49|  The calendar property falls out of valid range.  
ErrorCalendarViewRangeTooBig| 50|  The specified view range exceeds the
maximum range of two years.  
ErrorCallerIsInvalidADAccount| 51|  Failed to get valid Active Directory
information for the calling account. Confirm that it is a valid Active
Directory account.  
ErrorCannotArchiveCalendarContactTaskFolderException| 52|  Cannot archive
items in Calendar, contact to task folders  
ErrorCannotArchiveItemsInArchiveMailbox| 53|  Cannot archive items in archive
mailboxes  
ErrorCannotArchiveItemsInPublicFolders| 54|  Cannot archive items in public
folders  
ErrorCannotCreateCalendarItemInNonCalendarFolder| 55|  Cannot create a
calendar item in a non-calendar folder.  
ErrorCannotCreateContactInNonContactFolder| 56|  Cannot create a contact in a
non-contact folder.  
ErrorCannotCreatePostItemInNonMailFolder| 57|  Cannot create a post item in a
folder that is not a mail folder.  
ErrorCannotCreateTaskInNonTaskFolder| 58|  Cannot create a task in a non-task
Folder.  
ErrorCannotDeleteObject| 59|  Object cannot be deleted.  
ErrorCannotDeleteTaskOccurrence| 60|  Deleting a task occurrence is not
permitted on non-recurring tasks, on the last occurrence of a recurring task
or on a regenerating task.  
ErrorCannotDisableMandatoryExtension| 61|  Mandatory extensions cannot be
disabled by end users  
ErrorCannotEmptyFolder| 62|  Folder cannot be emptied.  
ErrorCannotGetExternalEcpUrl| 63|  Cannot get external ECP URL. This might
happen if external ECP URL isn't configured  
ErrorCannotGetSourceFolderPath| 64|  Unable to read the folder path for the
source folder while archiving items  
ErrorCannotOpenFileAttachment| 65|  The attachment could not be opened.  
ErrorCannotSetCalendarPermissionOnNonCalendarFolder| 66|  Expected a
PermissionSet but received a CalendarPermissionSet.  
ErrorCannotSetNonCalendarPermissionOnCalendarFolder| 67|  Expected a
CalendarPermissionSet but received a PermissionSet.  
ErrorCannotSetPermissionUnknownEntries| 68|  Cannot set UnknownEntries on a
PermissionSet or CalendarPermissionSet.  
ErrorCannotSpecifySearchFolderAsSourceFolder| 69|  Cannot specify search
folders as source folders while archiving items  
ErrorCannotUseFolderIdForItemId| 70|  Expected an item Id but received a
folder Id.  
ErrorCannotUseItemIdForFolderId| 71|  Expected a folder Id but received an
item Id.  
ErrorChangeKeyRequired| 72|  ChangeKey is required if overriding automatic
conflict resolution.  
ErrorChangeKeyRequiredForWriteOperations| 73|  ChangeKey is required for this
operation.  
ErrorClientDisconnected| 74|  ErrorClientDisconnected  
ErrorConnectionFailed| 75|  Connection did not succeed. Try again later.  
ErrorContainsFilterWrongType| 76|  The Contains filter can only be used for
string properties.  
ErrorContentConversionFailed| 77|  Content conversion failed.  
ErrorCorruptData| 78|  Data is corrupt.  
ErrorCreateItemAccessDenied| 79|  Unable to create item. The user account does
not have the right to create items.  
ErrorCreateManagedFolderPartialCompletion| 80|  Failed to create one or more
of the specified managed folders.  
ErrorCreateSubfolderAccessDenied| 81|  Unable to create subfolder. The user
account does not have the right to create subfolders.  
ErrorCrossMailboxMoveCopy| 82|  Move and Copy operations across mailbox
boundaries are not permitted.  
ErrorCrossSiteRequest| 83|  This request isn't allowed because the Client
Access server that's servicing the request is in a different site than the
requested resource. Use Autodiscover to find the correct URL for accessing the
specified resource.  
ErrorDataSizeLimitExceeded| 84|  Property exceeds the maximum supported size.  
ErrorDataSourceOperation| 85|  Invalid data source operation.  
ErrorDelegateAlreadyExists| 86|  The user is already a delegate for the
mailbox.  
ErrorDelegateCannotAddOwner| 87|  This is an invalid operation. Cannot add
owner as delegate.  
ErrorDelegateMissingConfiguration| 88|  Delegate is not configured properly.  
ErrorDelegateNoUser| 89|  The delegate does not map to a user in the Active
Directory.  
ErrorDelegateValidationFailed| 90|  Cannot add the delegate user. Failed to
validate the changes.  
ErrorDeleteDistinguishedFolder| 91|  Distinguished folders cannot be deleted.  
ErrorDeleteItemsFailed| 92|  The deletion failed.  
ErrorDistinguishedUserNotSupported| 93|  DistinguishedUser should not be
specified for a Delegate User.  
ErrorDistributionListMemberNotExist| 94|  The group member doesn't exist.  
ErrorDuplicateInputFolderNames| 95|  The specified list of managed folder
names contains duplicate entries.  
ErrorDuplicateLegacyDistinguishedName| 96|  A duplicate exchange legacy DN.  
ErrorDuplicateSOAPHeader| 97|  A duplicate SOAP header was received.  
ErrorDuplicateUserIdsSpecified| 98|  The specified permission set contains
duplicate UserIds.  
ErrorEmailAddressMismatch| 99|  The email address associated with a folder Id
does not match the mailbox you are operating on.  
ErrorEventNotFound| 100|  The watermark used for creating this subscription
was not found.  
ErrorExceededConnectionCount| 101|  You have exceeded the available concurrent
connections for your account. Try again once your other requests have
completed.  
ErrorExceededFindCountLimit| 102|  You have exceeded the maximum number of
objects that can be returned for the find operation. Use paging to reduce the
result size and try your request again.  
ErrorExceededSubscriptionCount| 103|  You have exceeded the available
subscriptions for your account. Remove unnecessary subscriptions and try your
request again.  
ErrorExpiredSubscription| 104|  Subscription information is not available.
Subscription is expired.  
ErrorExtensionNotFound| 105|  Extension with id specified was not found  
ErrorFolderCorrupt| 106|  The folder is corrupt.  
ErrorFolderExists| 107|  A folder with the specified name already exists.  
ErrorFolderNotFound| 108|  The specified folder could not be found in the
store.  
ErrorFolderPropertRequestFailed| 109|  ErrorFolderPropertRequestFailed  
ErrorFolderSave| 110|  The folder save operation did not succeed.  
ErrorFolderSaveFailed| 111|  The save operation failed or partially succeeded.  
ErrorFolderSavePropertyError| 112|  The folder save operation failed due to
invalid property values.  
ErrorFreeBusyDLLimitReached| 113|  ErrorFreeBusyDLLimitReached  
ErrorFreeBusyGenerationFailed| 114|  ErrorFreeBusyGenerationFailed  
ErrorGetServerSecurityDescriptorFailed| 115|
ErrorGetServerSecurityDescriptorFailed  
ErrorImContactLimitReached| 116|  ErrorImContactLimitReached  
ErrorImGroupDisplayNameAlreadyExists| 117|
ErrorImGroupDisplayNameAlreadyExists  
ErrorImGroupLimitReached| 118|  ErrorImGroupLimitReached  
ErrorImpersonateUserDenied| 119|  The account does not have permission to
impersonate the requested user.  
ErrorImpersonationDenied| 120|  ErrorImpersonationDenied  
ErrorImpersonationFailed| 121|  Impersonation failed.  
ErrorInboxRulesValidationError| 122|  ErrorInboxRulesValidationError  
ErrorIncorrectSchemaVersion| 123|  The request is valid but does not specify
the correct server version in the RequestServerVersion SOAP header. Ensure
that the RequestServerVersion SOAP header is set with the correct
RequestServerVersionValue.  
ErrorIncorrectUpdatePropertyCount| 124|  An object within a change description
must contain one and only one property to modify.  
ErrorIndividualMailboxLimitReached| 125|  ErrorIndividualMailboxLimitReached  
ErrorInsufficientResources| 126|  Resources are unavailable. Try again later.  
ErrorInternalServerError| 127|  An internal server error occurred. The
operation failed.  
ErrorInternalServerTransientError| 128|  An internal server error occurred.
Try again later.  
ErrorInvalidAccessLevel| 129|  ErrorInvalidAccessLevel  
ErrorInvalidArgument| 130|  ErrorInvalidArgument  
ErrorInvalidAttachmentId| 131|  The specified attachment Id is invalid.  
ErrorInvalidAttachmentSubfilter| 132|  Attachment subfilters must have a
single TextFilter therein.  
ErrorInvalidAttachmentSubfilterTextFilter| 133|  Attachment subfilters must
have a single TextFilter on the display name only.  
ErrorInvalidAuthorizationContext| 134|  ErrorInvalidAuthorizationContext  
ErrorInvalidChangeKey| 135|  The change key is invalid.  
ErrorInvalidClientSecurityContext| 136|  ErrorInvalidClientSecurityContext  
ErrorInvalidCompleteDate| 137|  CompleteDate cannot be set to a date in the
future.  
ErrorInvalidContactEmailAddress| 138|  The e-mail address that was supplied
isn't valid.  
ErrorInvalidContactEmailIndex| 139|  The e-mail index supplied isn't valid.  
ErrorInvalidCrossForestCredentials| 140|  ErrorInvalidCrossForestCredentials  
ErrorInvalidDelegatePermission| 141|  Invalid Delegate Folder Permission.  
ErrorInvalidDelegateUserId| 142|  One or more UserId parameters are invalid.
Make sure that the PrimarySmtpAddress, Sid and DisplayName properties refer to
the same user when specified.  
ErrorInvalidExchangeImpersonationHeaderData| 143|  An ExchangeImpersonation
SOAP header must contain a user principal name, user SID, or primary SMTP
address.  
ErrorInvalidExcludesRestriction| 144|  Second operand in Excludes expression
must be uint compatible.  
ErrorInvalidExpressionTypeForSubFilter| 145|  FieldURI can only be used in
Contains expressions.  
ErrorInvalidExtendedProperty| 146|  The extended property attribute
combination is invalid.  
ErrorInvalidExtendedPropertyValue| 147|  The extended property value is
inconsistent with its type.  
ErrorInvalidExternalSharingInitiator| 148|  The original sender of the message
(initiator field in the sharing metadata) is not valid.  
ErrorInvalidExternalSharingSubscriber| 149|  The sharing message is not
intended for this caller.  
ErrorInvalidFederatedOrganizationId| 150|  The organization is either not
federated, or it's configured incorrectly.  
ErrorInvalidFolderId| 151|  Folder Id is invalid.  
ErrorInvalidFolderTypeForOperation| 152|  ErrorInvalidFolderTypeForOperation  
ErrorInvalidFractionalPagingParameters| 153|  Invalid fractional paging offset
values.  
ErrorInvalidFreeBusyViewType| 154|  ErrorInvalidFreeBusyViewType  
ErrorInvalidGetSharingFolderRequest| 155|  Either DataType or SharedFolderId
must be specified, but not both.  
ErrorInvalidId| 156|  The Id is invalid.  
ErrorInvalidImContactId| 157|  The Im Contact id was invalid.  
ErrorInvalidImDistributionGroupSmtpAddress| 158|  The Im Distribution Group
Smtp Address was invalid.  
ErrorInvalidImGroupId| 159|  The Im Contact id was invalid.  
ErrorInvalidIdEmpty| 160|  Id must be non-empty.  
ErrorInvalidIdMalformed| 161|  Id is malformed.  
ErrorInvalidIdMalformedEwsLegacyIdFormat| 162|  The EWS Id is in EwsLegacyId
format which is not supported by the Exchange version specified by your
request. Please use the ConvertId method to convert from EwsLegacyId to EwsId
format.  
ErrorInvalidIdMonikerTooLong| 163|  Moniker exceeded allowable length.  
ErrorInvalidIdNotAnItemAttachmentId| 164|  The Id does not represent an item
attachment.  
ErrorInvalidIdReturnedByResolveNames| 165|  ResolveNames returned an invalid
Id.  
ErrorInvalidIdStoreObjectIdTooLong| 166|  Id exceeded allowable length.  
ErrorInvalidIdTooManyAttachmentLevels| 167|  Too many attachment levels.  
ErrorInvalidIdXml| 168|  The Id Xml is invalid.  
ErrorInvalidIndexedPagingParameters| 169|  The specified indexed paging values
are invalid.  
ErrorInvalidInternetHeaderChildNodes| 170|  Only one child node is allowed
when setting an Internet Message Header.  
ErrorInvalidItemForOperationAcceptItem| 171|  Item type is invalid for
AcceptItem action.  
ErrorInvalidItemForOperationArchiveItem| 172|  Item type is invalid for
ArchiveItem action.  
ErrorInvalidItemForOperationCancelItem| 173|  Item type is invalid for
CancelCalendarItem action.  
ErrorInvalidItemForOperationCreateItem| 174|  Item type is invalid for
CreateItem operation.  
ErrorInvalidItemForOperationCreateItemAttachment| 175|  Item type is invalid
for CreateItemAttachment operation.  
ErrorInvalidItemForOperationDeclineItem| 176|  Item type is invalid for
DeclineItem operation.  
ErrorInvalidItemForOperationExpandDL| 177|  ExpandDL operation does not
support this item type.  
ErrorInvalidItemForOperationRemoveItem| 178|  Item type is invalid for
RemoveItem operation.  
ErrorInvalidItemForOperationSendItem| 179|  Item type is invalid for SendItem
operation.  
ErrorInvalidItemForOperationTentative| 180|  The item of this type is invalid
for TentativelyAcceptItem action.  
ErrorInvalidLogonType| 181|  The logon type isn't valid.  
ErrorInvalidMailbox| 182|  Mailbox is invalid. Verify the specified Mailbox
property.  
ErrorInvalidManagedFolderProperty| 183|  The Managed Folder property is
corrupt or otherwise invalid.  
ErrorInvalidManagedFolderQuota| 184|  The managed folder has an invalid quota.  
ErrorInvalidManagedFolderSize| 185|  The managed folder has an invalid storage
limit value.  
ErrorInvalidMergedFreeBusyInterval| 186|  ErrorInvalidMergedFreeBusyInterval  
ErrorInvalidNameForNameResolution| 187|  The specified value is not a valid
name for name resolution.  
ErrorInvalidNetworkServiceContext| 188|  ErrorInvalidNetworkServiceContext  
ErrorInvalidOofParameter| 189|  ErrorInvalidOofParameter  
ErrorInvalidOperation| 190|  ErrorInvalidOperation  
ErrorInvalidOrganizationRelationshipForFreeBusy| 191|
ErrorInvalidOrganizationRelationshipForFreeBusy  
ErrorInvalidPagingMaxRows| 192|  MaxEntriesReturned must be greater than zero.  
ErrorInvalidParentFolder| 193|  Cannot create a subfolder within a
SearchFolder.  
ErrorInvalidPercentCompleteValue| 194|  PercentComplete must be an integer
between 0 and 100.  
ErrorInvalidPermissionSettings| 195|  The permission settings were not valid.  
ErrorInvalidPhoneCallId| 196|  The phone call ID isn't valid.  
ErrorInvalidPhoneNumber| 197|  The phone number isn't valid.  
ErrorInvalidPropertyAppend| 198|  The append action is not supported for this
property.  
ErrorInvalidPropertyDelete| 199|  The delete action is not supported for this
property.  
ErrorInvalidPropertyForExists| 200|  Property cannot be used in Exists
expression. Use IsEqualTo instead.  
ErrorInvalidPropertyForOperation| 201|  Property is not valid for this
operation.  
ErrorInvalidPropertyRequest| 202|  Property is not valid for this object type.  
ErrorInvalidPropertySet| 203|  Set action is invalid for property.  
ErrorInvalidPropertyUpdateSentMessage| 204|  Update operation is invalid for
property of a sent message.  
ErrorInvalidProxySecurityContext| 205|  The proxy security context is invalid.  
ErrorInvalidPullSubscriptionId| 206|  SubscriptionId is invalid. Subscription
is not a pull subscription.  
ErrorInvalidPushSubscriptionUrl| 207|  URL specified for push subscription is
invalid.  
ErrorInvalidRecipients| 208|  One or more recipients are invalid.  
ErrorInvalidRecipientSubfilter| 209|  Recipient subfilters are only supported
when there are two expressions within a single AND filter.  
ErrorInvalidRecipientSubfilterComparison| 210|  Recipient subfilter must have
a comparison filter that tests equality to recipient type or attendee type.  
ErrorInvalidRecipientSubfilterOrder| 211|  Recipient subfilters must have a
text filter and a comparison filter in that order.  
ErrorInvalidRecipientSubfilterTextFilter| 212|  Recipient subfilter must have
a TextFilter on the SMTP address only.  
ErrorInvalidReferenceItem| 213|  The reference item does not support the
requested operation.  
ErrorInvalidRequest| 214|  The request is invalid.  
ErrorInvalidRestriction| 215|  The restriction is invalid.  
ErrorInvalidRetentionTagTypeMismatch| 216|
ErrorInvalidRetentionIdTagTypeMismatch.  
ErrorInvalidRetentionTagInvisible| 217|  ErrorInvalidRetentionTagInvisible.  
ErrorInvalidRetentionTagInheritance| 218|
ErrorInvalidRetentionTagInheritance.  
ErrorInvalidRetentionTagIdGuid| 219|  ErrorInvalidRetentionTagIdGuid.  
ErrorInvalidRoutingType| 220|  The routing type format is invalid.  
ErrorInvalidScheduledOofDuration| 221|  ErrorInvalidScheduledOofDuration  
ErrorInvalidSchemaVersionForMailboxVersion| 222|  The mailbox that was
requested doesn't support the specified RequestServerVersion.  
ErrorInvalidSecurityDescriptor| 223|  ErrorInvalidSecurityDescriptor  
ErrorInvalidSendItemSaveSettings| 224|  Invalid combination of
SaveItemToFolder attribute and SavedItemFolderId element.  
ErrorInvalidSerializedAccessToken| 225|  Invalid serialized access token.  
ErrorInvalidServerVersion| 226|  The specified server version is invalid.  
ErrorInvalidSharingData| 227|  The sharing message metadata is not valid.  
ErrorInvalidSharingMessage| 228|  The sharing message is not valid.  
ErrorInvalidSid| 229|  A SID with an invalid format was encountered.  
ErrorInvalidSIPUri| 230|  The SIP address isn't valid.  
ErrorInvalidSmtpAddress| 231|  The SMTP address format is invalid.  
ErrorInvalidSubfilterType| 232|  Invalid subFilterType.  
ErrorInvalidSubfilterTypeNotAttendeeType| 233|  SubFilterType is not attendee
type.  
ErrorInvalidSubfilterTypeNotRecipientType| 234|  SubFilterType is not
recipient type.  
ErrorInvalidSubscription| 235|  Subscription is invalid.  
ErrorInvalidSubscriptionRequest| 236|  A subscription can only be established
on a single public folder or on folders from a single mailbox.  
ErrorInvalidSyncStateData| 237|  Synchronization state data is corrupt or
otherwise invalid.  
ErrorInvalidTimeInterval| 238|  ErrorInvalidTimeInterval  
ErrorInvalidUserInfo| 239|  A UserId was not valid.  
ErrorInvalidUserOofSettings| 240|  ErrorInvalidUserOofSettings  
ErrorInvalidUserPrincipalName| 241|  The impersonation principal name is
invalid.  
ErrorInvalidUserSid| 242|  The user SID is invalid or does not map to a user
in the Active Directory.  
ErrorInvalidUserSidMissingUPN| 243|  ErrorInvalidUserSidMissingUPN  
ErrorInvalidValueForProperty| 244|  The specified value is invalid for
property.  
ErrorInvalidWatermark| 245|  The watermark is invalid.  
ErrorIPGatewayNotFound| 246|  A valid IP gateway couldn't be found.  
ErrorIrresolvableConflict| 247|  The send or update operation could not be
performed because the change key passed in the request does not match the
current change key for the item.  
ErrorItemCorrupt| 248|  The item is corrupt.  
ErrorItemNotFound| 249|  The specified object was not found in the store.  
ErrorItemPropertyRequestFailed| 250|  One or more of the properties requested
for this item could not be retrieved.  
ErrorItemSave| 251|  The item save operation did not succeed.  
ErrorItemSavePropertyError| 252|  Item save operation did not succeed.  
ErrorLegacyMailboxFreeBusyViewTypeNotMerged| 253|
ErrorLegacyMailboxFreeBusyViewTypeNotMerged  
ErrorLocalServerObjectNotFound| 254|  ErrorLocalServerObjectNotFound  
ErrorLogonAsNetworkServiceFailed| 255|  ErrorLogonAsNetworkServiceFailed  
ErrorMailboxConfiguration| 256|  Unable to access an account or mailbox.  
ErrorMailboxDataArrayEmpty| 257|  ErrorMailboxDataArrayEmpty  
ErrorMailboxDataArrayTooBig| 258|  ErrorMailboxDataArrayTooBig  
ErrorMailboxFailover| 259|  ErrorMailboxFailover  
ErrorMailboxHoldNotFound| 260|  The specific mailbox hold is not found.  
ErrorMailboxLogonFailed| 261|  ErrorMailboxLogonFailed  
ErrorMailboxMoveInProgress| 262|  Mailbox move in progress. Try again later.  
ErrorMailboxStoreUnavailable| 263|  The mailbox database is temporarily
unavailable.  
ErrorMailRecipientNotFound| 264|  ErrorMailRecipientNotFound  
ErrorMailTipsDisabled| 265|  MailTips aren't available for your organization.  
ErrorManagedFolderAlreadyExists| 266|  The specified Managed Folder already
exists in the mailbox.  
ErrorManagedFolderNotFound| 267|  Unable to find the specified managed folder
in the Active Directory.  
ErrorManagedFoldersRootFailure| 268|  Failed to create or bind to the folder:
Managed Folders  
ErrorMeetingSuggestionGenerationFailed| 269|
ErrorMeetingSuggestionGenerationFailed  
ErrorMessageDispositionRequired| 270|  MessageDisposition attribute is
required.  
ErrorMessageSizeExceeded| 271|  The message exceeds the maximum supported
size.  
ErrorMessageTrackingNoSuchDomain| 272|  The domain specified in the tracking
request doesn't exist.  
ErrorMessageTrackingPermanentError| 273|  The log search service can't track
this message.  
ErrorMessageTrackingTransientError| 274|  The log search service isn't
currently available. Please try again later.  
ErrorMimeContentConversionFailed| 275|  MIME content conversion failed.  
ErrorMimeContentInvalid| 276|  Invalid MIME content.  
ErrorMimeContentInvalidBase64String| 277|  Invalid base64 string for MIME
content.  
ErrorMissedNotificationEvents| 278|  The subscription has missed events, but
will continue service on this connection.  
ErrorMissingArgument| 279|  ErrorMissingArgument  
ErrorMissingEmailAddress| 280|  When making a request as an account that does
not have a mailbox, you must specify the mailbox primary SMTP address for any
distinguished folder Ids.  
ErrorMissingEmailAddressForManagedFolder| 281|  When making a request with an
account that does not have a mailbox, you must specify the primary SMTP
address for an existing mailbox.  
ErrorMissingInformationEmailAddress| 282|  EmailAddress or ItemId must be
included in the request.  
ErrorMissingInformationReferenceItemId| 283|  ReferenceItemId must be included
in the request.  
ErrorMissingInformationSharingFolderId| 284|  SharingFolderId must be included
in the request.  
ErrorMissingItemForCreateItemAttachment| 285|  An item must be specified when
creating an item attachment.  
ErrorMissingManagedFolderId| 286|  The managed folder Id is missing.  
ErrorMissingRecipients| 287|  A message needs to have at least one recipient.  
ErrorMissingUserIdInformation| 288|  Missing information for delegate user.
You must either specify a valid SMTP address or SID.  
ErrorMoreThanOneAccessModeSpecified| 289|  Only one access mode header may be
specified.  
ErrorMoveCopyFailed| 290|  The move or copy operation failed.  
ErrorMoveDistinguishedFolder| 291|  Cannot move distinguished folder.  
ErrorMultiLegacyMailboxAccess| 292|  ErrorMultiLegacyMailboxAccess  
ErrorNameResolutionMultipleResults| 293|  Multiple results were found.  
ErrorNameResolutionNoMailbox| 294|  User must have a mailbox for name
resolution operations.  
ErrorNameResolutionNoResults| 295|  No results were found.  
ErrorNewEventStreamConnectionOpened| 296|  Another connection was opened
against this subscription.  
ErrorNoApplicableProxyCASServersAvailable| 297|  Exchange Web Services are not
currently available for this request because there are no available Client
Access Services Servers in the target AD Site.  
ErrorNoCalendar| 298|  ErrorNoCalendar  
ErrorNoDestinationCASDueToKerberosRequirements| 299|  Exchange Web Services
aren't available for this request because there is no Client Access server
with the necessary configuration in the Active Directory site where the
mailbox is stored. If the problem continues, click Help.  
ErrorNoDestinationCASDueToSSLRequirements| 300|  Exchange Web Services aren't
currently available for this request because an SSL connection couldn't be
established to the Client Access server that should be used for mailbox
access. If the problem continues, click Help.  
ErrorNoDestinationCASDueToVersionMismatch| 301|  Exchange Web Services aren't
currently available for this request because the Client Access server used for
proxying has an older version of Exchange installed than the Client Access
server in the mailbox Active Directory site.  
ErrorNoFolderClassOverride| 302|  You cannot specify the FolderClass when
creating a non-generic folder.  
ErrorNoFreeBusyAccess| 303|  ErrorNoFreeBusyAccess  
ErrorNonExistentMailbox| 304|  Mailbox does not exist.  
ErrorNonPrimarySmtpAddress| 305|  The primary SMTP address must be specified
when referencing a mailbox.  
ErrorNoPropertyTagForCustomProperties| 306|  Custom properties cannot be
specified using property tags. The GUID and Id/Name combination must be used
instead.  
ErrorNoPublicFolderReplicaAvailable| 307|  ErrorNoPublicFolderReplicaAvailable  
ErrorNoPublicFolderServerAvailable| 308|  There are no public folder servers
available.  
ErrorNoRespondingCASInDestinationSite| 309|  Exchange Web Services are not
currently available for this request because none of the Client Access Servers
in the destination site could process the request.  
ErrorNotAllowedExternalSharingByPolicy| 310|  Policy does not allow granting
of permissions to external users.  
ErrorNotDelegate| 311|  The user is not a delegate for the mailbox.  
ErrorNotEnoughMemory| 312|  There was not enough memory to complete the
request.  
ErrorNotSupportedSharingMessage| 313|  The sharing message is not supported.  
ErrorObjectTypeChanged| 314|  Operation would change object type, which is not
permitted.  
ErrorOccurrenceCrossingBoundary| 315|  Modified occurrence is crossing or
overlapping adjacent occurrence.  
ErrorOccurrenceTimeSpanTooBig| 316|  One occurrence of the recurring calendar
item overlaps with another occurrence of the same calendar item.  
ErrorOperationNotAllowedWithPublicFolderRoot| 317|  Operation not allowed with
public folder root.  
ErrorOrganizationNotFederated| 318|  Organization is not federated.  
ErrorOutlookRuleBlobExists| 319|  ErrorOutlookRuleBlobExists  
ErrorParentFolderIdRequired| 320|  You must specify the parent folder Id for
this operation.  
ErrorParentFolderNotFound| 321|  The specified parent folder could not be
found.  
ErrorPasswordChangeRequired| 322|  Password change is required.  
ErrorPasswordExpired| 323|  Password has expired. Change password.  
ErrorPermissionNotAllowedByPolicy| 324|  Policy does not allow granting
permission level to user.  
ErrorPhoneNumberNotDialable| 325|  Dialing restrictions are preventing the
phone number that was entered from being dialed.  
ErrorPropertyUpdate| 326|  Property update did not succeed.  
ErrorPropertyValidationFailure| 327|  At least one property failed validation.  
ErrorProxiedSubscriptionCallFailure| 328|  Subscription related request failed
because EWS could not contact the appropriate CAS server for this request. If
this problem persists, recreate the subscription.  
ErrorProxyCallFailed| 329|  Request failed because EWS could not contact the
appropriate CAS server for this request.  
ErrorProxyGroupSidLimitExceeded| 330|  Exchange Web Services (EWS) is not
available for this mailbox because the user account associated with the
mailbox is a member of too many groups. EWS limits the group membership it can
proxy between Client Access Service Servers to 3000.  
ErrorProxyRequestNotAllowed| 331|  ErrorProxyRequestNotAllowed  
ErrorProxyRequestProcessingFailed| 332|  ErrorProxyRequestProcessingFailed  
ErrorProxyServiceDiscoveryFailed| 333|  Exchange Web Services are not
currently available for this mailbox because it could not determine the Client
Access Services Server to use for the mailbox.  
ErrorProxyTokenExpired| 334|  Proxy token has expired.  
ErrorPublicFolderRequestProcessingFailed| 335|
ErrorPublicFolderRequestProcessingFailed  
ErrorPublicFolderServerNotFound| 336|  ErrorPublicFolderServerNotFound  
ErrorQueryFilterTooLong| 337|  The search folder has a restriction that is too
long to return.  
ErrorQuotaExceeded| 338|  Mailbox has exceeded maximum mailbox size.  
ErrorReadEventsFailed| 339|  Unable to retrieve events for this subscription.
The subscription must be recreated.  
ErrorReadReceiptNotPending| 340|  Unable to suppress read receipt. Read
receipts are not pending.  
ErrorRecurrenceEndDateTooBig| 341|  Recurrence end date can not exceed Sep 1,
4500 00:00:00.  
ErrorRecurrenceHasNoOccurrence| 342|  Recurrence has no occurrences in the
specified range.  
ErrorRemoveDelegatesFailed| 343|  Failed to remove one or more delegates.  
ErrorRequestAborted| 344|  ErrorRequestAborted  
ErrorRequestStreamTooBig| 345|  ErrorRequestStreamTooBig  
ErrorRequiredPropertyMissing| 346|  Required property is missing.  
ErrorResolveNamesInvalidFolderType| 347|  Cannot perform ResolveNames for non-
contact folder.  
ErrorResolveNamesOnlyOneContactsFolderAllowed| 348|  Only one contacts folder
can be specified in request.  
ErrorResponseSchemaValidation| 349|  The response failed schema validation.  
ErrorRestrictionTooComplex| 350|  The restriction or sort order is too complex
for this operation.  
ErrorRestrictionTooLong| 351|  Restriction contained too many elements.  
ErrorResultSetTooBig| 352|  ErrorResultSetTooBig  
ErrorRulesOverQuota| 353|  ErrorRulesOverQuota  
ErrorSavedItemFolderNotFound| 354|  The folder in which items were to be saved
could not be found.  
ErrorSchemaValidation| 355|  The request failed schema validation.  
ErrorSearchFolderNotInitialized| 356|  The search folder is not initialized.  
ErrorSendAsDenied| 357|  The user account which was used to submit this
request does not have the right to send mail on behalf of the specified
sending account.  
ErrorSendMeetingCancellationsRequired| 358|  SendMeetingCancellations
attribute is required for Calendar items.  
ErrorSendMeetingInvitationsOrCancellationsRequired| 359|  The
SendMeetingInvitationsOrCancellations attribute is required for calendar
items.  
ErrorSendMeetingInvitationsRequired| 360|  The SendMeetingInvitations
attribute is required for calendar items.  
ErrorSentMeetingRequestUpdate| 361|  The meeting request has already been sent
and might not be updated.  
ErrorSentTaskRequestUpdate| 362|  The task request has already been sent and
may not be updated.  
ErrorServerBusy| 363|  The server cannot service this request right now. Try
again later.  
ErrorServiceDiscoveryFailed| 364|  ErrorServiceDiscoveryFailed  
ErrorSharingNoExternalEwsAvailable| 365|  No external Exchange Web Service URL
available.  
ErrorSharingSynchronizationFailed| 366|  Failed to synchronize the sharing
folder.  
ErrorStaleObject| 367|  The current ChangeKey is required for this operation.  
ErrorSubmissionQuotaExceeded| 368|  The message couldn't be sent because the
sender's submission quota was exceeded. Please try again later.  
ErrorSubscriptionAccessDenied| 369|  Access is denied. Only the subscription
owner may access the subscription.  
ErrorSubscriptionDelegateAccessNotSupported| 370|  Subscriptions are not
supported for delegate user access.  
ErrorSubscriptionNotFound| 371|  The specified subscription was not found.  
ErrorSubscriptionUnsubscribed| 372|  The StreamingSubscription was
unsubscribed while the current connection was servicing it.  
ErrorSyncFolderNotFound| 373|  The folder to be synchronized could not be
found.  
ErrorTeamMailboxNotFound| 374|  ErrorTeamMailboxNotFound  
ErrorTeamMailboxNotLinkedToSharePoint| 375|
ErrorTeamMailboxNotLinkedToSharePoint  
ErrorTeamMailboxUrlValidationFailed| 376|  ErrorTeamMailboxUrlValidationFailed  
ErrorTeamMailboxNotAuthorizedOwner| 377|  ErrorTeamMailboxNotAuthorizedOwner  
ErrorTeamMailboxActiveToPendingDelete| 378|
ErrorTeamMailboxActiveToPendingDelete  
ErrorTeamMailboxFailedSendingNotifications| 379|
ErrorTeamMailboxFailedSendingNotifications  
ErrorTeamMailboxErrorUnknown| 380|  ErrorTeamMailboxErrorUnknown  
ErrorTimeIntervalTooBig| 381|  ErrorTimeIntervalTooBig  
ErrorTimeoutExpired| 382|  ErrorTimeoutExpired  
ErrorTimeZone| 383|  The time zone isn't valid.  
ErrorToFolderNotFound| 384|  The specified target folder could not be found.  
ErrorTokenSerializationDenied| 385|  The requesting account does not have
permission to serialize tokens.  
ErrorUnableToGetUserOofSettings| 386|  ErrorUnableToGetUserOofSettings  
ErrorUnableToRemoveImContactFromGroup| 387|
ErrorUnableToRemoveImContactFromGroup  
ErrorUnifiedMessagingDialPlanNotFound| 388|  A dial plan could not be found.  
ErrorUnifiedMessagingRequestFailed| 389|  The UnifiedMessaging request failed.  
ErrorUnifiedMessagingServerNotFound| 390|  A connection couldn't be made to
the Unified Messaging server.  
ErrorUnsupportedCulture| 391|  The specified item culture is not supported on
this server.  
ErrorUnsupportedMapiPropertyType| 392|  The MAPI property type is not
supported.  
ErrorUnsupportedMimeConversion| 393|  MIME conversion is not supported for
this item type.  
ErrorUnsupportedPathForQuery| 394|  The property can not be used with this
type of restriction.  
ErrorUnsupportedPathForSortGroup| 395|  The property can not be used for
sorting or grouping results.  
ErrorUnsupportedPropertyDefinition| 396|  PropertyDefinition is not supported
in searches.  
ErrorUnsupportedQueryFilter| 397|  QueryFilter type is not supported.  
ErrorUnsupportedRecurrence| 398|  The specified recurrence is not supported.  
ErrorUnsupportedSubFilter| 399|  Unsupported subfilter type.  
ErrorUnsupportedTypeForConversion| 400|  Unsupported type for restriction
conversion.  
ErrorUpdateDelegatesFailed| 401|  Failed to update one or more delegates.  
ErrorUpdatePropertyMismatch| 402|  Property for update does not match property
in object.  
ErrorUserNotAllowedByPolicy| 403|  Policy does not allow granting permissions
to user.  
ErrorUserNotUnifiedMessagingEnabled| 404|  The user isn't enabled for Unified
Messaging  
ErrorUserWithoutFederatedProxyAddress| 405|  The user doesn't have an SMTP
proxy address from a federated domain.  
ErrorValueOutOfRange| 406|  The value is out of range.  
ErrorVirusDetected| 407|  Virus detected in the message.  
ErrorVirusMessageDeleted| 408|  The item has been deleted as a result of a
virus scan.  
ErrorVoiceMailNotImplemented| 409|  The Voice Mail distinguished folder is not
implemented.  
ErrorWebRequestInInvalidState| 410|  ErrorWebRequestInInvalidState  
ErrorWin32InteropError| 411|  ErrorWin32InteropError  
ErrorWorkingHoursSaveFailed| 412|  ErrorWorkingHoursSaveFailed  
ErrorWorkingHoursXmlMalformed| 413|  ErrorWorkingHoursXmlMalformed  
ErrorWrongServerVersion| 414|  The Client Access server version doesn't match
the Mailbox server version of the resource that was being accessed. To
determine the correct URL to use to access the resource, use Autodiscover with
the address of the resource.  
ErrorWrongServerVersionDelegate| 415|  The mailbox of the authenticating user
and the mailbox of the resource being accessed must have the same Mailbox
server version.  
ErrorInvalidClientAccessTokenRequest| 416|  The client access token request is
invalid.  
ErrorInvalidManagementRoleHeader| 417|  invalid managementrole header value or
usage.  
ErrorSearchQueryHasTooManyKeywords| 418|  SearchMailboxes query has too many
keywords.  
ErrorSearchTooManyMailboxes| 419|  SearchMailboxes on too many mailboxes.  
ErrorInvalidRetentionTagNone| 420| There are no retention tags.  
ErrorDiscoverySearchesDisabled| 421| Discovery Searches are disabled.  
ErrorCalendarSeekToConditionNotSupported| 422| SeekToConditionPageView not
supported for calendar items.  
ErrorArchiveMailboxSearchFailed| 423| Archive mailbox search operation failed.  
ErrorGetRemoteArchiveFolderFailed| 424| Get remote archive mailbox folder
failed.  
ErrorFindRemoteArchiveFolderFailed| 425| Find remote archive mailbox folder
failed.  
ErrorGetRemoteArchiveItemFailed| 426| Get remote archive mailbox item failed.  
ErrorExportRemoteArchiveItemsFailed| 427| Export remote archive mailbox items
failed.  
ErrorClientIntentInvalidStateDefinition| 428| Invalid state definition.  
ErrorClientIntentNotFound| 429| Client intent not found.  
ErrorContentIndexingNotEnabled| 430| The Content Indexing service is required
to perform this search, but it's not enabled.  
ErrorDeleteUnifiedMessagingPromptFailed| 431| The custom prompt files you
specified couldn't be removed.  
ErrorLocationServicesDisabled| 432| The location service is disabled.  
ErrorLocationServicesInvalidRequest| 433| Invalid location service request.  
ErrorLocationServicesRequestFailed| 434| The request for location information
failed.  
ErrorLocationServicesRequestTimedOut| 435| The request for location
information timed out.  
ErrorWeatherServiceDisabled| 436| Weather service is disabled.  
ErrorMailboxScopeNotAllowedWithoutQueryString| 437| Mailbox scope not allowed
without a query string.  
ErrorNoSpeechDetected| 438| No speech detected.  
ErrorPromptPublishingOperationFailed| 439| An error occurred while accessing
the custom prompt publishing point.  
ErrorPublicFolderMailboxDiscoveryFailed| 440| Unable to discover the URL of
the public folder mailbox.  
ErrorPublicFolderOperationFailed| 441| Public folder operation failed.  
ErrorPublicFolderSyncException| 442| The operation succeeded on the primary
public folder mailbox, but failed to sync to the secondary public folder
mailbox.  
ErrorRecipientNotFound| 443| Discovery Searches are disabled.  
ErrorRecognizerNotInstalled| 444| Recognizer not installed.  
ErrorSpeechGrammarError| 445| Speech grammar error.  
ErrorTooManyObjectsOpened| 446| Too many concurrent connections opened.  
ErrorUMServerUnavailable| 447| Unified Messaging server unavailable.  
ErrorUnifiedMessagingPromptNotFound| 448| The Unified Messaging custom prompt
file you specified couldn't be found.  
ErrorUnifiedMessagingReportDataNotFound| 449| Report data for the UM call
summary couldn't be found.  
ErrorInvalidPhotoSize| 450| The requested size is invalid.  
ErrorCalendarIsGroupMailboxForAccept| 451|  AcceptItem action is invalid for a
meeting message in group mailbox.  
ErrorCalendarIsGroupMailboxForDecline| 452|  DeclineItem operation is invalid
for a meeting message in group mailbox.  
ErrorCalendarIsGroupMailboxForTentative| 453|  TentativelyAcceptItem action
isn't valid for a meeting message in group mailbox.  
ErrorCalendarIsGroupMailboxForSuppressReadReceipt| 454|  SuppressReadReceipt
action isn't valid for a meeting message in group mailbox.  
ErrorOrganizationAccessBlocked| 455|  The Organization is marked for removal.  
ErrorInvalidLicense| 456|  User doesn't have a valid license.  
ErrorMessagePerFolderCountReceiveQuotaExceeded| 457|  Receive quota message
per folder is exceeded.  
ErrorUnifiedGroupMailboxNotFound| 458|  Unified group was not found.  
ErrorInvalidChannelId| 459|  Invalid channel id.  
ErrorNewChannelConnectionOpened| 460|  Another connection is opened on the
same channel.  
ErrorChannelSubscriptionNotFound| 461|  The channel subscription cannot be
found.  
ErrorExceededChannelSubscriptionCount| 462|  The channel contains too many
subscriptions.  
ErrorChannelSubscriptionAlreadyExists| 463|  The channel subscription already
exists.  
ErrorInvalidChannelSubscriptionId| 464|  The given channel subscription id is
invalid.  
ErrorMessageSubmissionBlocked| 465| Error indicating that message submission
blocked by WASCL for a consumer mailboxes  
ErrorExceededMessageLimit| 466| Error indicating that number of submitted
messages exceeded the limit and message submission is blocked by WASCL  
ErrorExceededMaxRecipientLimitBlock| 467| Error indicating that recipients
number for a consumer mailbox has exceeded the limit defined by WASCL  
ErrorAccountSuspend| 468| Error indicating that access to the consumer mailbox
is suspended by WASCL  
ErrorExceededMaxRecipientLimit| 469| Error indicating that recipients number
for a consumer mailbox has exceeded the limit defined by WASCL  
ErrorMessageBlocked| 470| Error indicating that particular message cannot be
sent for a consumer mailbox as it is considered as SPAM by WASCL  
ErrorAccountSuspendShowTierUpgrade| 471| Error indicating that access to the
consumer mailbox is suspended by WASCL  
ErrorExceededMessageLimitShowTierUpgrade| 472| Error indicating that message
sent from a consumer mailbox has exceeded the limit defined by WASCL  
ErrorExceededMaxRecipientLimitShowTierUpgrade| 473| Error indicating that
recipients number for a consumer mailbox has exceeded the limit defined by
WASCL  
##  __См. также
#### Ссылки
[Tessa.Exchange.WebServices.Data - пространство
имён](N_Tessa_Exchange_WebServices_Data.htm)
