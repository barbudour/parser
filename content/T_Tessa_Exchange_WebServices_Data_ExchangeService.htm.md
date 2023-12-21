# ExchangeService - класс
Represents a binding to the Exchange Web Services.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ExchangeService : ExchangeServiceBase
VB __Копировать
     Public NotInheritable Class ExchangeService
    	Inherits ExchangeServiceBase
C++ __Копировать
     public ref class ExchangeService sealed : public ExchangeServiceBase
F# __Копировать
     [<SealedAttribute>]
    type ExchangeService = 
        class
            inherit ExchangeServiceBase
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ExchangeServiceBase](T_Tessa_Exchange_WebServices_Data_ExchangeServiceBase.htm) __ ExchangeService
##  __Конструкторы
[ExchangeService()](M_Tessa_Exchange_WebServices_Data_ExchangeService__ctor.htm)|
Initializes a new instance of the ExchangeService class, targeting the latest
supported version of EWS and scoped to the system's current time zone.  
---|---  
[ExchangeService(ExchangeVersion)](M_Tessa_Exchange_WebServices_Data_ExchangeService__ctor_2.htm)|
Initializes a new instance of the ExchangeService class, targeting the
specified version of EWS and scoped to the system's current time zone.  
[ExchangeService(TimeZoneInfo)](M_Tessa_Exchange_WebServices_Data_ExchangeService__ctor_1.htm)|
Initializes a new instance of the ExchangeService class, targeting the latest
supported version of EWS and scoped to the specified time zone.  
[ExchangeService(ExchangeVersion,
TimeZoneInfo)](M_Tessa_Exchange_WebServices_Data_ExchangeService__ctor_3.htm)|
Initializes a new instance of the ExchangeService class, targeting the
specified version of EWS and scoped to the specified time zone.  
## __Свойства
[AcceptGzipEncoding](P_Tessa_Exchange_WebServices_Data_ExchangeServiceBase_AcceptGzipEncoding.htm)|
Gets or sets a value indicating whether GZip compression encoding should be
accepted.  
(Унаследован от
[ExchangeServiceBase](T_Tessa_Exchange_WebServices_Data_ExchangeServiceBase.htm))  
---|---  
[ClientRequestId](P_Tessa_Exchange_WebServices_Data_ExchangeServiceBase_ClientRequestId.htm)|
Gets or sets the request id for the request.  
(Унаследован от
[ExchangeServiceBase](T_Tessa_Exchange_WebServices_Data_ExchangeServiceBase.htm))  
[ConnectionGroupName](P_Tessa_Exchange_WebServices_Data_ExchangeServiceBase_ConnectionGroupName.htm)|
Gets or sets the name of the connection group for the request.  
(Унаследован от
[ExchangeServiceBase](T_Tessa_Exchange_WebServices_Data_ExchangeServiceBase.htm))  
[CookieContainer](P_Tessa_Exchange_WebServices_Data_ExchangeServiceBase_CookieContainer.htm)|
Gets or sets the cookie container.  
(Унаследован от
[ExchangeServiceBase](T_Tessa_Exchange_WebServices_Data_ExchangeServiceBase.htm))  
[Credentials](P_Tessa_Exchange_WebServices_Data_ExchangeServiceBase_Credentials.htm)|
Gets or sets the credentials used to authenticate with the Exchange Web
Services. Setting the Credentials property automatically sets the
UseDefaultCredentials to false.  
(Унаследован от
[ExchangeServiceBase](T_Tessa_Exchange_WebServices_Data_ExchangeServiceBase.htm))  
[DateTimePrecision](P_Tessa_Exchange_WebServices_Data_ExchangeService_DateTimePrecision.htm)|
Gets or sets the DateTime precision for DateTime values returned from Exchange
Web Services.  
[EnableScpLookup](P_Tessa_Exchange_WebServices_Data_ExchangeService_EnableScpLookup.htm)|
Gets or sets a value indicating whether the AutodiscoverUrl method should
perform SCP (Service Connection Point) record lookup when determining the
Autodiscover service URL.  
[FileAttachmentContentHandler](P_Tessa_Exchange_WebServices_Data_ExchangeService_FileAttachmentContentHandler.htm)|
Gets or sets a file attachment content handler.  
[HttpHeaders](P_Tessa_Exchange_WebServices_Data_ExchangeServiceBase_HttpHeaders.htm)|
Gets a collection of HTTP headers that will be sent with each request to EWS.  
(Унаследован от
[ExchangeServiceBase](T_Tessa_Exchange_WebServices_Data_ExchangeServiceBase.htm))  
[HttpResponseHeaders](P_Tessa_Exchange_WebServices_Data_ExchangeServiceBase_HttpResponseHeaders.htm)|
Gets a collection of HTTP headers from the last response.  
(Унаследован от
[ExchangeServiceBase](T_Tessa_Exchange_WebServices_Data_ExchangeServiceBase.htm))  
[ImpersonatedUserId](P_Tessa_Exchange_WebServices_Data_ExchangeService_ImpersonatedUserId.htm)|
Gets or sets the Id of the user that EWS should impersonate.  
[KeepAlive](P_Tessa_Exchange_WebServices_Data_ExchangeServiceBase_KeepAlive.htm)|
Gets or sets if the request to the internet resource should contain a
Connection HTTP header with the value Keep-alive  
(Унаследован от
[ExchangeServiceBase](T_Tessa_Exchange_WebServices_Data_ExchangeServiceBase.htm))  
[ManagementRoles](P_Tessa_Exchange_WebServices_Data_ExchangeService_ManagementRoles.htm)|  
[PreAuthenticate](P_Tessa_Exchange_WebServices_Data_ExchangeServiceBase_PreAuthenticate.htm)|
Gets or sets a value that indicates whether HTTP pre-authentication should be
performed.  
(Унаследован от
[ExchangeServiceBase](T_Tessa_Exchange_WebServices_Data_ExchangeServiceBase.htm))  
[PreferredCulture](P_Tessa_Exchange_WebServices_Data_ExchangeService_PreferredCulture.htm)|
Gets or sets the preferred culture for messages returned by the Exchange Web
Services.  
[RequestedServerVersion](P_Tessa_Exchange_WebServices_Data_ExchangeServiceBase_RequestedServerVersion.htm)|
Gets the requested server version.  
(Унаследован от
[ExchangeServiceBase](T_Tessa_Exchange_WebServices_Data_ExchangeServiceBase.htm))  
[ReturnClientRequestId](P_Tessa_Exchange_WebServices_Data_ExchangeServiceBase_ReturnClientRequestId.htm)|
Gets or sets a flag to indicate whether the client requires the server side to
return the request id.  
(Унаследован от
[ExchangeServiceBase](T_Tessa_Exchange_WebServices_Data_ExchangeServiceBase.htm))  
[SendClientLatencies](P_Tessa_Exchange_WebServices_Data_ExchangeServiceBase_SendClientLatencies.htm)|
Gets or sets a value indicating whether client latency info is push to server.  
(Унаследован от
[ExchangeServiceBase](T_Tessa_Exchange_WebServices_Data_ExchangeServiceBase.htm))  
[ServerInfo](P_Tessa_Exchange_WebServices_Data_ExchangeServiceBase_ServerInfo.htm)|
Gets information associated with the server that processed the last request.
Will be null if no requests have been processed.  
(Унаследован от
[ExchangeServiceBase](T_Tessa_Exchange_WebServices_Data_ExchangeServiceBase.htm))  
[Timeout](P_Tessa_Exchange_WebServices_Data_ExchangeServiceBase_Timeout.htm)|
Gets or sets the timeout used when sending HTTP requests and when receiving
HTTP responses, in milliseconds. Defaults to 100000.  
(Унаследован от
[ExchangeServiceBase](T_Tessa_Exchange_WebServices_Data_ExchangeServiceBase.htm))  
[TimeZone](P_Tessa_Exchange_WebServices_Data_ExchangeService_TimeZone.htm)|
Gets the time zone this service is scoped to.  
[TimeZoneDefinition](P_Tessa_Exchange_WebServices_Data_ExchangeServiceBase_TimeZoneDefinition.htm)|
Gets a time zone definition generated from the time zone info to which this
service is scoped.  
(Унаследован от
[ExchangeServiceBase](T_Tessa_Exchange_WebServices_Data_ExchangeServiceBase.htm))  
[TraceEnabled](P_Tessa_Exchange_WebServices_Data_ExchangeServiceBase_TraceEnabled.htm)|
Gets or sets a value indicating whether tracing is enabled.  
(Унаследован от
[ExchangeServiceBase](T_Tessa_Exchange_WebServices_Data_ExchangeServiceBase.htm))  
[TraceEnablePrettyPrinting](P_Tessa_Exchange_WebServices_Data_ExchangeService_TraceEnablePrettyPrinting.htm)|
Gets or sets a value indicating whether trace output is pretty printed.  
[TraceFlags](P_Tessa_Exchange_WebServices_Data_ExchangeServiceBase_TraceFlags.htm)|
Gets or sets the trace flags.  
(Унаследован от
[ExchangeServiceBase](T_Tessa_Exchange_WebServices_Data_ExchangeServiceBase.htm))  
[TraceListener](P_Tessa_Exchange_WebServices_Data_ExchangeServiceBase_TraceListener.htm)|
Gets or sets the trace listener.  
(Унаследован от
[ExchangeServiceBase](T_Tessa_Exchange_WebServices_Data_ExchangeServiceBase.htm))  
[UnifiedMessaging](P_Tessa_Exchange_WebServices_Data_ExchangeService_UnifiedMessaging.htm)|
Provides access to the Unified Messaging functionalities.  
[Url](P_Tessa_Exchange_WebServices_Data_ExchangeService_Url.htm)|  Gets or
sets the URL of the Exchange Web Services.  
[UseDefaultCredentials](P_Tessa_Exchange_WebServices_Data_ExchangeServiceBase_UseDefaultCredentials.htm)|
Gets or sets a value indicating whether the credentials of the user currently
logged into Windows should be used to authenticate with the Exchange Web
Services. Setting UseDefaultCredentials to true automatically sets the
Credentials property to null.  
(Унаследован от
[ExchangeServiceBase](T_Tessa_Exchange_WebServices_Data_ExchangeServiceBase.htm))  
[UserAgent](P_Tessa_Exchange_WebServices_Data_ExchangeServiceBase_UserAgent.htm)|
Gets or sets the user agent.  
(Унаследован от
[ExchangeServiceBase](T_Tessa_Exchange_WebServices_Data_ExchangeServiceBase.htm))  
[WebProxy](P_Tessa_Exchange_WebServices_Data_ExchangeServiceBase_WebProxy.htm)|
Gets or sets the web proxy that should be used when sending requests to EWS.
Set this property to null to use the default web proxy.  
(Унаследован от
[ExchangeServiceBase](T_Tessa_Exchange_WebServices_Data_ExchangeServiceBase.htm))  
##  __Методы
[AddDelegates(Mailbox, Nullable<MeetingRequestsDeliveryScope>,
DelegateUser[])](M_Tessa_Exchange_WebServices_Data_ExchangeService_AddDelegates_1.htm)|
Adds delegates to a specific mailbox. Calling this method results in a call to
EWS.  
---|---  
[AddDelegates(Mailbox, Nullable<MeetingRequestsDeliveryScope>,
IEnumerable<DelegateUser>,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ExchangeService_AddDelegates.htm)|
Adds delegates to a specific mailbox. Calling this method results in a call to
EWS.  
[ArchiveItems](M_Tessa_Exchange_WebServices_Data_ExchangeService_ArchiveItems.htm)|
Archives multiple items in a single call to EWS.  
[AutodiscoverUrl(String)](M_Tessa_Exchange_WebServices_Data_ExchangeService_AutodiscoverUrl.htm)|
Initializes the Url property to the Exchange Web Services URL for the
specified e-mail address by calling the Autodiscover service.  
[AutodiscoverUrl(String,
AutodiscoverRedirectionUrlValidationCallback)](M_Tessa_Exchange_WebServices_Data_ExchangeService_AutodiscoverUrl_1.htm)|
Initializes the Url property to the Exchange Web Services URL for the
specified e-mail address by calling the Autodiscover service.  
[BindToFolders](M_Tessa_Exchange_WebServices_Data_ExchangeService_BindToFolders.htm)|
Binds to multiple folders in a single call to EWS.  
[BindToGroupItems](M_Tessa_Exchange_WebServices_Data_ExchangeService_BindToGroupItems.htm)|
Binds to multiple items in a single call to EWS.  
[BindToItems](M_Tessa_Exchange_WebServices_Data_ExchangeService_BindToItems.htm)|
Binds to multiple items in a single call to EWS.  
[BrowsePeople(ViewBase)](M_Tessa_Exchange_WebServices_Data_ExchangeService_BrowsePeople.htm)|
Retrieves all people who are relevant to the user  
[BrowsePeople(ViewBase, Dictionary<String, String>,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ExchangeService_BrowsePeople_1.htm)|
Retrieves all people who are relevant to the user  
[ConvertId](M_Tessa_Exchange_WebServices_Data_ExchangeService_ConvertId.htm)|
Converts Id from one format to another in a single call to EWS.  
[ConvertIds](M_Tessa_Exchange_WebServices_Data_ExchangeService_ConvertIds.htm)|
Converts multiple Ids from one format to another in a single call to EWS.  
[CopyItems(IEnumerable<ItemId>, FolderId,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ExchangeService_CopyItems_1.htm)|
Copies multiple items in a single call to EWS.  
[CopyItems(IEnumerable<ItemId>, FolderId, Boolean,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ExchangeService_CopyItems.htm)|
Copies multiple items in a single call to EWS.  
[CopyItemsInConversations](M_Tessa_Exchange_WebServices_Data_ExchangeService_CopyItemsInConversations.htm)|
Copies the items in the specified conversation to the specified destination
folder. Calling this method results in a call to EWS.  
[CreateItems](M_Tessa_Exchange_WebServices_Data_ExchangeService_CreateItems.htm)|
Creates multiple items in a single EWS call. Supported item classes are
EmailMessage, Appointment, Contact, PostItem, Task and Item. CreateItems does
not support items that have unsaved attachments.  
[DeleteItems(IEnumerable<ItemId>, DeleteMode, Nullable<SendCancellationsMode>,
Nullable<AffectedTaskOccurrence>)](M_Tessa_Exchange_WebServices_Data_ExchangeService_DeleteItems.htm)|
Deletes multiple items in a single call to EWS.  
[DeleteItems(IEnumerable<ItemId>, DeleteMode, Nullable<SendCancellationsMode>,
Nullable<AffectedTaskOccurrence>, Boolean,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ExchangeService_DeleteItems_1.htm)|
Deletes multiple items in a single call to EWS.  
[DeleteItemsInConversations](M_Tessa_Exchange_WebServices_Data_ExchangeService_DeleteItemsInConversations.htm)|
Deletes the items in the specified conversation. Calling this method results
in a call to EWS.  
[DisableAlwaysCategorizeItemsInConversations](M_Tessa_Exchange_WebServices_Data_ExchangeService_DisableAlwaysCategorizeItemsInConversations.htm)|
Sets up a conversation so that any item received within that conversation is
no longer categorized. Calling this method results in a call to EWS.  
[DisableAlwaysDeleteItemsInConversations](M_Tessa_Exchange_WebServices_Data_ExchangeService_DisableAlwaysDeleteItemsInConversations.htm)|
Sets up a conversation so that any item received within that conversation is
no longer moved to Deleted Items folder. Calling this method results in a call
to EWS.  
[DisableAlwaysMoveItemsInConversations](M_Tessa_Exchange_WebServices_Data_ExchangeService_DisableAlwaysMoveItemsInConversations.htm)|
Sets up a conversation so that any item received within that conversation is
no longer moved to a specific folder. Calling this method results in a call to
EWS.  
[DisableApp](M_Tessa_Exchange_WebServices_Data_ExchangeService_DisableApp.htm)|
Disable App.  
[EnableAlwaysCategorizeItemsInConversations](M_Tessa_Exchange_WebServices_Data_ExchangeService_EnableAlwaysCategorizeItemsInConversations.htm)|
Sets up a conversation so that any item received within that conversation is
always categorized. Calling this method results in a call to EWS.  
[EnableAlwaysDeleteItemsInConversations](M_Tessa_Exchange_WebServices_Data_ExchangeService_EnableAlwaysDeleteItemsInConversations.htm)|
Sets up a conversation so that any item received within that conversation is
always moved to Deleted Items folder. Calling this method results in a call to
EWS.  
[EnableAlwaysMoveItemsInConversations](M_Tessa_Exchange_WebServices_Data_ExchangeService_EnableAlwaysMoveItemsInConversations.htm)|
Sets up a conversation so that any item received within that conversation is
always moved to a specific folder. Calling this method results in a call to
EWS.  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ExpandGroup(ItemId)](M_Tessa_Exchange_WebServices_Data_ExchangeService_ExpandGroup_3.htm)|
Expands a group by retrieving a list of its members. Calling this method
results in a call to EWS.  
[ExpandGroup(String)](M_Tessa_Exchange_WebServices_Data_ExchangeService_ExpandGroup.htm)|
Expands a group by retrieving a list of its members. Calling this method
results in a call to EWS.  
[ExpandGroup(EmailAddress,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ExchangeService_ExpandGroup_2.htm)|
Expands a group by retrieving a list of its members. Calling this method
results in a call to EWS.  
[ExpandGroup(String,
String)](M_Tessa_Exchange_WebServices_Data_ExchangeService_ExpandGroup_1.htm)|
Expands a group by retrieving a list of its members. Calling this method
results in a call to EWS.  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[FindAppointments(FolderId, CalendarView,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ExchangeService_FindAppointments.htm)|
Obtains a list of appointments by searching the contents of a specific folder.
Calling this method results in a call to EWS.  
[FindAppointments(WellKnownFolderName, CalendarView,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ExchangeService_FindAppointments_1.htm)|
Obtains a list of appointments by searching the contents of a specific folder.
Calling this method results in a call to EWS.  
[FindConversation(ViewBase, FolderId,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ExchangeService_FindConversation_3.htm)|
Retrieves a collection of all Conversations in the specified Folder.  
[FindConversation(ViewBase, FolderId, String,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ExchangeService_FindConversation_2.htm)|
Retrieves a collection of all Conversations in the specified Folder.  
[FindConversation(ViewBase, FolderId, String, Boolean,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ExchangeService_FindConversation_1.htm)|
Searches for and retrieves a collection of Conversations in the specified
Folder. Along with conversations, a list of highlight terms are returned.  
[FindConversation(ViewBase, FolderId, String, Boolean,
Nullable<MailboxSearchLocation>,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ExchangeService_FindConversation.htm)|
Searches for and retrieves a collection of Conversations in the specified
Folder. Along with conversations, a list of highlight terms are returned.  
[FindFolders(WellKnownFolderName,
FolderView)](M_Tessa_Exchange_WebServices_Data_ExchangeService_FindFolders_3.htm)|
Obtains a list of folders by searching the sub-folders of the specified
folder.  
[FindFolders(FolderId, FolderView,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ExchangeService_FindFolders_1.htm)|
Obtains a list of folders by searching the sub-folders of the specified
folder.  
[FindFolders(WellKnownFolderName, SearchFilter,
FolderView)](M_Tessa_Exchange_WebServices_Data_ExchangeService_FindFolders_4.htm)|
Obtains a list of folders by searching the sub-folders of the specified
folder.  
[FindFolders(FolderId, SearchFilter, FolderView,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ExchangeService_FindFolders_2.htm)|
Obtains a list of folders by searching the sub-folders of the specified
folder.  
[FindFolders(IEnumerable<FolderId>, SearchFilter, FolderView,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ExchangeService_FindFolders.htm)|
Obtains a list of folders by searching the sub-folders of each of the
specified folders.  
[FindGroupConversation](M_Tessa_Exchange_WebServices_Data_ExchangeService_FindGroupConversation.htm)|
Retrieves a collection of all Conversations in the specified Folder.  
[FindItems(FolderId, ViewBase,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ExchangeService_FindItems_6.htm)|
Obtains a list of items by searching the contents of a specific folder.
Calling this method results in a call to EWS.  
[FindItems(WellKnownFolderName, String,
ViewBase)](M_Tessa_Exchange_WebServices_Data_ExchangeService_FindItems_8.htm)|
Obtains a list of items by searching the contents of a specific folder.
Calling this method results in a call to EWS.  
[FindItems(WellKnownFolderName, SearchFilter,
ViewBase)](M_Tessa_Exchange_WebServices_Data_ExchangeService_FindItems_10.htm)|
Obtains a list of items by searching the contents of a specific folder.
Calling this method results in a call to EWS.  
[FindItems(WellKnownFolderName, ViewBase,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ExchangeService_FindItems_12.htm)|
Obtains a list of items by searching the contents of a specific folder.
Calling this method results in a call to EWS.  
[FindItems(FolderId, String, ViewBase,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ExchangeService_FindItems_2.htm)|
Obtains a list of items by searching the contents of a specific folder.
Calling this method results in a call to EWS.  
[FindItems(FolderId, SearchFilter, ViewBase,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ExchangeService_FindItems_4.htm)|
Obtains a list of items by searching the contents of a specific folder.
Calling this method results in a call to EWS.  
[FindItems(FolderId, ViewBase, Grouping,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ExchangeService_FindItems_7.htm)|
Obtains a grouped list of items by searching the contents of a specific
folder. Calling this method results in a call to EWS.  
[FindItems(FolderId, String, Boolean, ViewBase,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ExchangeService_FindItems.htm)|
Obtains a list of items by searching the contents of a specific folder. Along
with conversations, a list of highlight terms are returned. Calling this
method results in a call to EWS.  
[FindItems(FolderId, String, ViewBase, Grouping,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ExchangeService_FindItems_3.htm)|
Obtains a grouped list of items by searching the contents of a specific
folder. Calling this method results in a call to EWS.  
[FindItems(FolderId, SearchFilter, ViewBase, Grouping,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ExchangeService_FindItems_5.htm)|
Obtains a grouped list of items by searching the contents of a specific
folder. Calling this method results in a call to EWS.  
[FindItems(WellKnownFolderName, String, ViewBase, Grouping,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ExchangeService_FindItems_9.htm)|
Obtains a grouped list of items by searching the contents of a specific
folder. Calling this method results in a call to EWS.  
[FindItems(WellKnownFolderName, SearchFilter, ViewBase, Grouping,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ExchangeService_FindItems_11.htm)|
Obtains a grouped list of items by searching the contents of a specific
folder. Calling this method results in a call to EWS.  
[FindItems(FolderId, String, Boolean, ViewBase, Grouping,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ExchangeService_FindItems_1.htm)|
Obtains a list of items by searching the contents of a specific folder. Along
with conversations, a list of highlight terms are returned. Calling this
method results in a call to EWS.  
[FindPeople(WellKnownFolderName, SearchFilter,
ViewBase)](M_Tessa_Exchange_WebServices_Data_ExchangeService_FindPeople_2.htm)|
This method is for browse scenarios. Retrieves a set of personas satisfying
the specified browse conditions. Browse scenarios don't require query string.  
[FindPeople(FolderId, SearchFilter, ViewBase,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ExchangeService_FindPeople_1.htm)|
This method is for browse scenarios. Retrieves a set of personas satisfying
the specified browse conditions. Browse scenariosdon't require query string.  
[FindPeople(WellKnownFolderName, SearchFilter, ViewBase,
String)](M_Tessa_Exchange_WebServices_Data_ExchangeService_FindPeople_3.htm)|
This method is for search scenarios. Retrieves a set of personas satisfying
the specified search conditions.  
[FindPeople(FolderId, SearchFilter, ViewBase, String,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ExchangeService_FindPeople.htm)|
This method is for search scenarios. Retrieves a set of personas satisfying
the specified search conditions.  
[GetAppManifests(CancellationToken)](M_Tessa_Exchange_WebServices_Data_ExchangeService_GetAppManifests_1.htm)|
Get the app manifests.  
[GetAppManifests(String, String,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ExchangeService_GetAppManifests.htm)|
Get the app manifests. Works with Exchange 2013 SP1 or later EWS.  
[GetAppMarketplaceUrl()](M_Tessa_Exchange_WebServices_Data_ExchangeService_GetAppMarketplaceUrl.htm)|
Get App Marketplace Url.  
[GetAppMarketplaceUrl(String, String,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ExchangeService_GetAppMarketplaceUrl_1.htm)|
Get App Marketplace Url. Works with Exchange 2013 SP1 or later EWS.  
[GetAttachments(Attachment[], Nullable<BodyType>,
IEnumerable<PropertyDefinitionBase>,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ExchangeService_GetAttachments_1.htm)|
Gets attachments.  
[GetAttachments(String[], Nullable<BodyType>,
IEnumerable<PropertyDefinitionBase>,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ExchangeService_GetAttachments.htm)|
Gets attachments.  
[GetClientAccessToken(IEnumerable<KeyValuePair<String,
ClientAccessTokenType>>)](M_Tessa_Exchange_WebServices_Data_ExchangeService_GetClientAccessToken.htm)|
GetClientAccessToken  
[GetClientAccessToken(ClientAccessTokenRequest[],
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ExchangeService_GetClientAccessToken_1.htm)|
GetClientAccessToken  
[GetClientExtension](M_Tessa_Exchange_WebServices_Data_ExchangeService_GetClientExtension.htm)|
Get the client extension data. This method is used in server-to-server calls
to retrieve ORG extensions for admin powershell/UMC access and user's
powershell/UMC access as well as user's activation for OWA/Outlook. This is
expected to never be used or called directly from user client.  
[GetConversationItems(IEnumerable<ConversationRequest>, PropertySet,
IEnumerable<FolderId>, Nullable<ConversationSortOrder>,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ExchangeService_GetConversationItems_1.htm)|
Gets the items for a set of conversations.  
[GetConversationItems(ConversationId, PropertySet, String,
IEnumerable<FolderId>, Nullable<ConversationSortOrder>,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ExchangeService_GetConversationItems_2.htm)|
Gets the items for a conversation.  
[GetConversationItems(IEnumerable<ConversationRequest>, PropertySet,
IEnumerable<FolderId>, Nullable<ConversationSortOrder>,
Nullable<MailboxSearchLocation>,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ExchangeService_GetConversationItems.htm)|
Gets the items for a set of conversations.  
[GetDelegates(Mailbox, Boolean, IEnumerable<UserId>,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ExchangeService_GetDelegates.htm)|
Retrieves the delegates of a specific mailbox. Calling this method results in
a call to EWS.  
[GetDelegates(Mailbox, Boolean, CancellationToken,
UserId[])](M_Tessa_Exchange_WebServices_Data_ExchangeService_GetDelegates_1.htm)|
Retrieves the delegates of a specific mailbox. Calling this method results in
a call to EWS.  
[GetDiscoverySearchConfiguration](M_Tessa_Exchange_WebServices_Data_ExchangeService_GetDiscoverySearchConfiguration.htm)|
Get dicovery search configuration  
[GetGroupConversationItems](M_Tessa_Exchange_WebServices_Data_ExchangeService_GetGroupConversationItems.htm)|
Gets the items for a conversation.  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHoldOnMailboxes](M_Tessa_Exchange_WebServices_Data_ExchangeService_GetHoldOnMailboxes.htm)|
Get hold on mailboxes  
[GetInboxRules(CancellationToken)](M_Tessa_Exchange_WebServices_Data_ExchangeService_GetInboxRules_1.htm)|
Retrieves inbox rules of the authenticated user.  
[GetInboxRules(String,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ExchangeService_GetInboxRules.htm)|
Retrieves the inbox rules of the specified user.  
[GetNonIndexableItemDetails(String[])](M_Tessa_Exchange_WebServices_Data_ExchangeService_GetNonIndexableItemDetails.htm)|
Get non indexable item details  
[GetNonIndexableItemDetails(GetNonIndexableItemDetailsParameters,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ExchangeService_GetNonIndexableItemDetails_2.htm)|
Get non indexable item details  
[GetNonIndexableItemDetails(String[], Nullable<Int32>, String,
Nullable<SearchPageDirection>)](M_Tessa_Exchange_WebServices_Data_ExchangeService_GetNonIndexableItemDetails_1.htm)|
Get non indexable item details  
[GetNonIndexableItemStatistics(String[])](M_Tessa_Exchange_WebServices_Data_ExchangeService_GetNonIndexableItemStatistics.htm)|
Get non indexable item statistics  
[GetNonIndexableItemStatistics(GetNonIndexableItemStatisticsParameters,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ExchangeService_GetNonIndexableItemStatistics_1.htm)|
Get non indexable item statistics  
[GetOMEConfiguration](M_Tessa_Exchange_WebServices_Data_ExchangeService_GetOMEConfiguration.htm)|
Get the OME (i.e. Office Message Encryption) configuration data. This method
is used in server-to-server calls to retrieve OME configuration  
[GetPasswordExpirationDate](M_Tessa_Exchange_WebServices_Data_ExchangeService_GetPasswordExpirationDate.htm)|
Get the password expiration date  
[GetPeopleInsights](M_Tessa_Exchange_WebServices_Data_ExchangeService_GetPeopleInsights.htm)|
This method is for retreiving people insight for given email addresses  
[GetRoomLists](M_Tessa_Exchange_WebServices_Data_ExchangeService_GetRoomLists.htm)|
Retrieves a collection of all room lists in the organization.  
[GetRooms](M_Tessa_Exchange_WebServices_Data_ExchangeService_GetRooms.htm)|
Retrieves a collection of all rooms in the specified room list in the
organization.  
[GetSearchableMailboxes](M_Tessa_Exchange_WebServices_Data_ExchangeService_GetSearchableMailboxes.htm)|
Get searchable mailboxes  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetUnifiedGroupUnseenCount](M_Tessa_Exchange_WebServices_Data_ExchangeService_GetUnifiedGroupUnseenCount.htm)|
Gets the UnifiedGroupsUnseenCount for the group specfied  
[GetUserAvailability(IEnumerable<AttendeeInfo>, TimeWindow,
AvailabilityData)](M_Tessa_Exchange_WebServices_Data_ExchangeService_GetUserAvailability.htm)|
Gets detailed information about the availability of a set of users, rooms, and
resources within a specified time window.  
[GetUserAvailability(IEnumerable<AttendeeInfo>, TimeWindow, AvailabilityData,
AvailabilityOptions,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ExchangeService_GetUserAvailability_1.htm)|
Gets detailed information about the availability of a set of users, rooms, and
resources within a specified time window.  
[GetUserOofSettings](M_Tessa_Exchange_WebServices_Data_ExchangeService_GetUserOofSettings.htm)|
Gets Out of Office (OOF) settings for a specific user. Calling this method
results in a call to EWS.  
[GetUserPhoto](M_Tessa_Exchange_WebServices_Data_ExchangeService_GetUserPhoto.htm)|
Get a user's photo.  
[GetUserRetentionPolicyTags](M_Tessa_Exchange_WebServices_Data_ExchangeService_GetUserRetentionPolicyTags.htm)|
Get user retention policy tags.  
[GetUserUnifiedGroups(IEnumerable<RequestedUnifiedGroupsSet>,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ExchangeService_GetUserUnifiedGroups_1.htm)|
Gets the list of unified groups associated with the user  
[GetUserUnifiedGroups(IEnumerable<RequestedUnifiedGroupsSet>, String,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ExchangeService_GetUserUnifiedGroups.htm)|
Gets the list of unified groups associated with the user  
[InstallApp](M_Tessa_Exchange_WebServices_Data_ExchangeService_InstallApp.htm)|
Install App.  
[LoadPropertiesForItems](M_Tessa_Exchange_WebServices_Data_ExchangeService_LoadPropertiesForItems.htm)|
Loads the properties of multiple items in a single call to EWS.  
[MarkAsJunk](M_Tessa_Exchange_WebServices_Data_ExchangeService_MarkAsJunk.htm)|
Mark items as junk.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MoveItems(IEnumerable<ItemId>, FolderId,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ExchangeService_MoveItems_1.htm)|
Moves multiple items in a single call to EWS.  
[MoveItems(IEnumerable<ItemId>, FolderId, Boolean,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ExchangeService_MoveItems.htm)|
Moves multiple items in a single call to EWS.  
[MoveItemsInConversations](M_Tessa_Exchange_WebServices_Data_ExchangeService_MoveItemsInConversations.htm)|
Moves the items in the specified conversation to the specified destination
folder. Calling this method results in a call to EWS.  
[RegisterConsent](M_Tessa_Exchange_WebServices_Data_ExchangeService_RegisterConsent.htm)|
Sets the consent state of an extension.  
[RemoveDelegates(Mailbox, IEnumerable<UserId>,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ExchangeService_RemoveDelegates.htm)|
Removes delegates on a specific mailbox. Calling this method results in a call
to EWS.  
[RemoveDelegates(Mailbox, CancellationToken,
UserId[])](M_Tessa_Exchange_WebServices_Data_ExchangeService_RemoveDelegates_1.htm)|
Removes delegates on a specific mailbox. Calling this method results in a call
to EWS.  
[ResolveName(String)](M_Tessa_Exchange_WebServices_Data_ExchangeService_ResolveName.htm)|
Finds contacts in the user's Contacts folder and the Global Address List (in
that order) that have names that match the one passed as a parameter. Calling
this method results in a call to EWS.  
[ResolveName(String, ResolveNameSearchLocation,
Boolean)](M_Tessa_Exchange_WebServices_Data_ExchangeService_ResolveName_3.htm)|
Finds contacts in the Global Address List that have names that match the one
passed as a parameter. Calling this method results in a call to EWS.  
[ResolveName(String, IEnumerable<FolderId>, ResolveNameSearchLocation,
Boolean)](M_Tessa_Exchange_WebServices_Data_ExchangeService_ResolveName_1.htm)|
Finds contacts in the Global Address List and/or in specific contact folders
that have names that match the one passed as a parameter. Calling this method
results in a call to EWS.  
[ResolveName(String, ResolveNameSearchLocation, Boolean,
PropertySet)](M_Tessa_Exchange_WebServices_Data_ExchangeService_ResolveName_4.htm)|
Finds contacts in the Global Address List that have names that match the one
passed as a parameter. Calling this method results in a call to EWS.  
[ResolveName(String, IEnumerable<FolderId>, ResolveNameSearchLocation,
Boolean, PropertySet,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ExchangeService_ResolveName_2.htm)|
Finds contacts in the Global Address List and/or in specific contact folders
that have names that match the one passed as a parameter. Calling this method
results in a call to EWS.  
[SearchMailboxes(SearchMailboxesParameters,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ExchangeService_SearchMailboxes_2.htm)|
Search mailboxes  
[SearchMailboxes(IEnumerable<MailboxQuery>, SearchResultType,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ExchangeService_SearchMailboxes_1.htm)|
Search mailboxes  
[SearchMailboxes(IEnumerable<MailboxQuery>, SearchResultType, String,
SortDirection, Int32, SearchPageDirection, String,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ExchangeService_SearchMailboxes.htm)|
Search mailboxes  
[SearchPeople(ViewBase,
String)](M_Tessa_Exchange_WebServices_Data_ExchangeService_SearchPeople.htm)|
Searches for people who are relevant to the user, automatically determining
the best sources to use.  
[SearchPeople(ViewBase, String, Dictionary<String, String>, PeopleQueryMode,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ExchangeService_SearchPeople_1.htm)|
Searches for people who are relevant to the user  
[SetClientExtension](M_Tessa_Exchange_WebServices_Data_ExchangeService_SetClientExtension.htm)|
Set the client extension data. This method is used in server-to-server calls
to install/uninstall/configure ORG extensions to support admin's management of
ORG extensions via powershell/UMC.  
[SetFlagStatusForItemsInConversations](M_Tessa_Exchange_WebServices_Data_ExchangeService_SetFlagStatusForItemsInConversations.htm)|
Sets flag status for items in conversation. Calling this method would result
in call to EWS.  
[SetHoldOnMailboxes(SetHoldOnMailboxesParameters,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ExchangeService_SetHoldOnMailboxes_3.htm)|
Set hold on mailboxes  
[SetHoldOnMailboxes(String, HoldAction, String,
String)](M_Tessa_Exchange_WebServices_Data_ExchangeService_SetHoldOnMailboxes.htm)|
Set hold on mailboxes  
[SetHoldOnMailboxes(String, HoldAction, String, String[],
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ExchangeService_SetHoldOnMailboxes_2.htm)|
Set hold on mailboxes  
[SetHoldOnMailboxes(String, HoldAction, String, String, String,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ExchangeService_SetHoldOnMailboxes_1.htm)|
Set hold on mailboxes  
[SetOMEConfiguration](M_Tessa_Exchange_WebServices_Data_ExchangeService_SetOMEConfiguration.htm)|
Set the OME (i.e. Office Message Encryption) configuration data. This method
is used in server-to-server calls to set encryption configuration  
[SetReadStateForItemsInConversations(IEnumerable<KeyValuePair<ConversationId,
Nullable<DateTime>>>, FolderId, Boolean,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ExchangeService_SetReadStateForItemsInConversations_1.htm)|
Sets the read state for items in conversation. Calling this method would
result in call to EWS.  
[SetReadStateForItemsInConversations(IEnumerable<KeyValuePair<ConversationId,
Nullable<DateTime>>>, FolderId, Boolean, Boolean,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ExchangeService_SetReadStateForItemsInConversations.htm)|
Sets the read state for items in conversation. Calling this method would
result in call to EWS.  
[SetRetentionPolicyForItemsInConversations](M_Tessa_Exchange_WebServices_Data_ExchangeService_SetRetentionPolicyForItemsInConversations.htm)|
Sets the retention policy for items in conversation. Calling this method would
result in call to EWS.  
[SetTeamMailbox](M_Tessa_Exchange_WebServices_Data_ExchangeService_SetTeamMailbox.htm)|
Set a TeamMailbox  
[SetUnifiedGroupLastVisitedTime](M_Tessa_Exchange_WebServices_Data_ExchangeService_SetUnifiedGroupLastVisitedTime.htm)|
Sets the LastVisitedTime for the group specfied  
[SetUserOofSettings](M_Tessa_Exchange_WebServices_Data_ExchangeService_SetUserOofSettings.htm)|
Sets the Out of Office (OOF) settings for a specific mailbox. Calling this
method results in a call to EWS.  
[SubscribeToGroupPushNotifications](M_Tessa_Exchange_WebServices_Data_ExchangeService_SubscribeToGroupPushNotifications.htm)|
Subscribes to push notifications on a group mailbox. Calling this method
results in a call to EWS.  
[SubscribeToPullNotifications](M_Tessa_Exchange_WebServices_Data_ExchangeService_SubscribeToPullNotifications.htm)|
Subscribes to pull notifications. Calling this method results in a call to
EWS.  
[SubscribeToPullNotificationsOnAllFolders](M_Tessa_Exchange_WebServices_Data_ExchangeService_SubscribeToPullNotificationsOnAllFolders.htm)|
Subscribes to pull notifications on all folders in the authenticated user's
mailbox. Calling this method results in a call to EWS.  
[SubscribeToPushNotifications(IEnumerable<FolderId>, Uri, Int32, String,
CancellationToken,
EventType[])](M_Tessa_Exchange_WebServices_Data_ExchangeService_SubscribeToPushNotifications_1.htm)|
Subscribes to push notifications. Calling this method results in a call to
EWS.  
[SubscribeToPushNotifications(IEnumerable<FolderId>, Uri, Int32, String,
String, CancellationToken,
EventType[])](M_Tessa_Exchange_WebServices_Data_ExchangeService_SubscribeToPushNotifications.htm)|
Subscribes to push notifications. Calling this method results in a call to
EWS.  
[SubscribeToPushNotificationsOnAllFolders(Uri, Int32, String,
CancellationToken,
EventType[])](M_Tessa_Exchange_WebServices_Data_ExchangeService_SubscribeToPushNotificationsOnAllFolders_1.htm)|
Subscribes to push notifications on all folders in the authenticated user's
mailbox. Calling this method results in a call to EWS.  
[SubscribeToPushNotificationsOnAllFolders(Uri, Int32, String, String,
CancellationToken,
EventType[])](M_Tessa_Exchange_WebServices_Data_ExchangeService_SubscribeToPushNotificationsOnAllFolders.htm)|
Subscribes to push notifications on all folders in the authenticated user's
mailbox. Calling this method results in a call to EWS.  
[SubscribeToStreamingNotifications](M_Tessa_Exchange_WebServices_Data_ExchangeService_SubscribeToStreamingNotifications.htm)|
Subscribes to streaming notifications. Calling this method results in a call
to EWS.  
[SubscribeToStreamingNotificationsOnAllFolders](M_Tessa_Exchange_WebServices_Data_ExchangeService_SubscribeToStreamingNotificationsOnAllFolders.htm)|
Subscribes to streaming notifications on all folders in the authenticated
user's mailbox. Calling this method results in a call to EWS.  
[SyncFolderHierarchy(PropertySet,
String)](M_Tessa_Exchange_WebServices_Data_ExchangeService_SyncFolderHierarchy_1.htm)|
Synchronizes the entire folder hierarchy of the mailbox this Service is
connected to. Calling this method results in a call to EWS.  
[SyncFolderHierarchy(FolderId, PropertySet, String,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ExchangeService_SyncFolderHierarchy.htm)|
Synchronizes the sub-folders of a specific folder. Calling this method results
in a call to EWS.  
[SyncFolderItems(FolderId, PropertySet, IEnumerable<ItemId>, Int32,
SyncFolderItemsScope,
String)](M_Tessa_Exchange_WebServices_Data_ExchangeService_SyncFolderItems_1.htm)|
Synchronizes the items of a specific folder. Calling this method results in a
call to EWS.  
[SyncFolderItems(FolderId, PropertySet, IEnumerable<ItemId>, Int32, Int32,
SyncFolderItemsScope, String,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ExchangeService_SyncFolderItems.htm)|
Synchronizes the items of a specific folder. Calling this method results in a
call to EWS.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[UninstallApp](M_Tessa_Exchange_WebServices_Data_ExchangeService_UninstallApp.htm)|
Uninstall app.  
[UnpinTeamMailbox](M_Tessa_Exchange_WebServices_Data_ExchangeService_UnpinTeamMailbox.htm)|
Unpin a TeamMailbox  
[UpdateDelegates(Mailbox, Nullable<MeetingRequestsDeliveryScope>,
IEnumerable<DelegateUser>,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ExchangeService_UpdateDelegates.htm)|
Updates delegates on a specific mailbox. Calling this method results in a call
to EWS.  
[UpdateDelegates(Mailbox, Nullable<MeetingRequestsDeliveryScope>,
CancellationToken,
DelegateUser[])](M_Tessa_Exchange_WebServices_Data_ExchangeService_UpdateDelegates_1.htm)|
Updates delegates on a specific mailbox. Calling this method results in a call
to EWS.  
[UpdateInboxRules(IEnumerable<RuleOperation>, Boolean,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ExchangeService_UpdateInboxRules_1.htm)|
Updates the authenticated user's inbox rules by applying the specified
operations.  
[UpdateInboxRules(IEnumerable<RuleOperation>, Boolean, String,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ExchangeService_UpdateInboxRules.htm)|
Update the specified user's inbox rules by applying the specified operations.  
[UpdateItems(IEnumerable<Item>, FolderId, ConflictResolutionMode,
Nullable<MessageDisposition>,
Nullable<SendInvitationsOrCancellationsMode>)](M_Tessa_Exchange_WebServices_Data_ExchangeService_UpdateItems.htm)|
Updates multiple items in a single EWS call. UpdateItems does not support
items that have unsaved attachments.  
[UpdateItems(IEnumerable<Item>, FolderId, ConflictResolutionMode,
Nullable<MessageDisposition>, Nullable<SendInvitationsOrCancellationsMode>,
Boolean,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_ExchangeService_UpdateItems_1.htm)|
Updates multiple items in a single EWS call. UpdateItems does not support
items that have unsaved attachments.  
## __События
[OnResponseHeadersCaptured](E_Tessa_Exchange_WebServices_Data_ExchangeServiceBase_OnResponseHeadersCaptured.htm)|
Occurs when the http response headers of a server call is captured.  
(Унаследован от
[ExchangeServiceBase](T_Tessa_Exchange_WebServices_Data_ExchangeServiceBase.htm))  
---|---  
[OnSerializeCustomSoapHeaders](E_Tessa_Exchange_WebServices_Data_ExchangeServiceBase_OnSerializeCustomSoapHeaders.htm)|
Provides an event that applications can implement to emit custom SOAP headers
in requests that are sent to Exchange.  
(Унаследован от
[ExchangeServiceBase](T_Tessa_Exchange_WebServices_Data_ExchangeServiceBase.htm))  
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
