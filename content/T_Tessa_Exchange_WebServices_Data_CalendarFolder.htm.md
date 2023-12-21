# CalendarFolder - класс
Represents a folder containing appointments.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public class CalendarFolder : Folder
VB __Копировать
     Public Class CalendarFolder
    	Inherits Folder
C++ __Копировать
     public ref class CalendarFolder : public Folder
F# __Копировать
     type CalendarFolder = 
        class
            inherit Folder
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ServiceObject](T_Tessa_Exchange_WebServices_Data_ServiceObject.htm) __[Folder](T_Tessa_Exchange_WebServices_Data_Folder.htm) __ CalendarFolder
##  __Конструкторы
[CalendarFolder](M_Tessa_Exchange_WebServices_Data_CalendarFolder__ctor.htm)|
Initializes an unsaved local instance of CalendarFolder. To bind to an
existing calendar folder, use CalendarFolder.Bind() instead.  
---|---  
## __Свойства
[ArchiveTag](P_Tessa_Exchange_WebServices_Data_Folder_ArchiveTag.htm)|  Gets
or sets the archive tag.  
(Унаследован от [Folder](T_Tessa_Exchange_WebServices_Data_Folder.htm))  
---|---  
[ChildFolderCount](P_Tessa_Exchange_WebServices_Data_Folder_ChildFolderCount.htm)|
Gets the number of child folders this folder has.  
(Унаследован от [Folder](T_Tessa_Exchange_WebServices_Data_Folder.htm))  
[DisplayName](P_Tessa_Exchange_WebServices_Data_Folder_DisplayName.htm)|  Gets
or sets the display name of the folder.  
(Унаследован от [Folder](T_Tessa_Exchange_WebServices_Data_Folder.htm))  
[EffectiveRights](P_Tessa_Exchange_WebServices_Data_Folder_EffectiveRights.htm)|
Gets a value indicating the effective rights the current authenticated user
has on the folder.  
(Унаследован от [Folder](T_Tessa_Exchange_WebServices_Data_Folder.htm))  
[ExtendedProperties](P_Tessa_Exchange_WebServices_Data_Folder_ExtendedProperties.htm)|
Gets a list of extended properties associated with the folder.  
(Унаследован от [Folder](T_Tessa_Exchange_WebServices_Data_Folder.htm))  
[FolderClass](P_Tessa_Exchange_WebServices_Data_Folder_FolderClass.htm)|  Gets
or sets the custom class name of this folder.  
(Унаследован от [Folder](T_Tessa_Exchange_WebServices_Data_Folder.htm))  
[Id](P_Tessa_Exchange_WebServices_Data_Folder_Id.htm)|  Gets the Id of the
folder.  
(Унаследован от [Folder](T_Tessa_Exchange_WebServices_Data_Folder.htm))  
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
[ManagedFolderInformation](P_Tessa_Exchange_WebServices_Data_Folder_ManagedFolderInformation.htm)|
Gets the Email Lifecycle Management (ELC) information associated with the
folder.  
(Унаследован от [Folder](T_Tessa_Exchange_WebServices_Data_Folder.htm))  
[ParentFolderId](P_Tessa_Exchange_WebServices_Data_Folder_ParentFolderId.htm)|
Gets the Id of this folder's parent folder.  
(Унаследован от [Folder](T_Tessa_Exchange_WebServices_Data_Folder.htm))  
[Permissions](P_Tessa_Exchange_WebServices_Data_Folder_Permissions.htm)|  Gets
a list of permissions for the folder.  
(Унаследован от [Folder](T_Tessa_Exchange_WebServices_Data_Folder.htm))  
[PolicyTag](P_Tessa_Exchange_WebServices_Data_Folder_PolicyTag.htm)|  Gets or
sets the policy tag.  
(Унаследован от [Folder](T_Tessa_Exchange_WebServices_Data_Folder.htm))  
[Schema](P_Tessa_Exchange_WebServices_Data_ServiceObject_Schema.htm)|  Gets
the schema associated with this type of object.  
(Унаследован от
[ServiceObject](T_Tessa_Exchange_WebServices_Data_ServiceObject.htm))  
[Service](P_Tessa_Exchange_WebServices_Data_ServiceObject_Service.htm)|  Gets
the ExchangeService the object is bound to.  
(Унаследован от
[ServiceObject](T_Tessa_Exchange_WebServices_Data_ServiceObject.htm))  
[TotalCount](P_Tessa_Exchange_WebServices_Data_Folder_TotalCount.htm)|  Gets
the total number of items contained in the folder.  
(Унаследован от [Folder](T_Tessa_Exchange_WebServices_Data_Folder.htm))  
[UnreadCount](P_Tessa_Exchange_WebServices_Data_Folder_UnreadCount.htm)|  Gets
the number of unread items in the folder.  
(Унаследован от [Folder](T_Tessa_Exchange_WebServices_Data_Folder.htm))  
[WellKnownFolderName](P_Tessa_Exchange_WebServices_Data_Folder_WellKnownFolderName.htm)|
Gets the well known name of this folder, if any.  
(Унаследован от [Folder](T_Tessa_Exchange_WebServices_Data_Folder.htm))  
[WellKnownFolderNameAsString](P_Tessa_Exchange_WebServices_Data_Folder_WellKnownFolderNameAsString.htm)|
Gets the well known name of this folder, if any, as a string.  
(Унаследован от [Folder](T_Tessa_Exchange_WebServices_Data_Folder.htm))  
##  __Методы
[Bind(ExchangeService, FolderId,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_CalendarFolder_Bind.htm)|
Binds to an existing calendar folder and loads its first class properties.
Calling this method results in a call to EWS.  
---|---  
[Bind(ExchangeService, WellKnownFolderName,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_CalendarFolder_Bind_2.htm)|
Binds to an existing calendar folder and loads its first class properties.
Calling this method results in a call to EWS.  
[Bind(ExchangeService, FolderId, PropertySet,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_CalendarFolder_Bind_1.htm)|
Binds to an existing calendar folder and loads the specified set of
properties. Calling this method results in a call to EWS.  
[Bind(ExchangeService, WellKnownFolderName, PropertySet,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_CalendarFolder_Bind_3.htm)|
Binds to an existing calendar folder and loads the specified set of
properties. Calling this method results in a call to EWS.  
[Copy(WellKnownFolderName)](M_Tessa_Exchange_WebServices_Data_Folder_Copy_1.htm)|
Copies this folder into the specified folder. Calling this method results in a
call to EWS.  
(Унаследован от [Folder](T_Tessa_Exchange_WebServices_Data_Folder.htm))  
[Copy(FolderId,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_Folder_Copy.htm)|
Copies this folder into a specific folder. Calling this method results in a
call to EWS.  
(Унаследован от [Folder](T_Tessa_Exchange_WebServices_Data_Folder.htm))  
[Delete](M_Tessa_Exchange_WebServices_Data_Folder_Delete.htm)|  Deletes the
folder. Calling this method results in a call to EWS.  
(Унаследован от [Folder](T_Tessa_Exchange_WebServices_Data_Folder.htm))  
[Empty](M_Tessa_Exchange_WebServices_Data_Folder_Empty.htm)|  Empties the
folder. Calling this method results in a call to EWS.  
(Унаследован от [Folder](T_Tessa_Exchange_WebServices_Data_Folder.htm))  
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
[FindAppointments](M_Tessa_Exchange_WebServices_Data_CalendarFolder_FindAppointments.htm)|
Obtains a list of appointments by searching the contents of this folder and
performing recurrence expansion for recurring appointments. Calling this
method results in a call to EWS.  
[FindFolders(FolderView)](M_Tessa_Exchange_WebServices_Data_Folder_FindFolders.htm)|
Obtains a list of folders by searching the sub-folders of this folder. Calling
this method results in a call to EWS.  
(Унаследован от [Folder](T_Tessa_Exchange_WebServices_Data_Folder.htm))  
[FindFolders(SearchFilter,
FolderView)](M_Tessa_Exchange_WebServices_Data_Folder_FindFolders_1.htm)|
Obtains a list of folders by searching the sub-folders of this folder. Calling
this method results in a call to EWS.  
(Унаследован от [Folder](T_Tessa_Exchange_WebServices_Data_Folder.htm))  
[FindItems(ItemView,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_Folder_FindItems_2.htm)|
Obtains a list of items by searching the contents of this folder. Calling this
method results in a call to EWS.  
(Унаследован от [Folder](T_Tessa_Exchange_WebServices_Data_Folder.htm))  
[FindItems(ItemView,
Grouping)](M_Tessa_Exchange_WebServices_Data_Folder_FindItems_3.htm)|  Obtains
a grouped list of items by searching the contents of this folder. Calling this
method results in a call to EWS.  
(Унаследован от [Folder](T_Tessa_Exchange_WebServices_Data_Folder.htm))  
[FindItems(SearchFilter, ItemView,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_Folder_FindItems_4.htm)|
Obtains a list of items by searching the contents of this folder. Calling this
method results in a call to EWS.  
(Унаследован от [Folder](T_Tessa_Exchange_WebServices_Data_Folder.htm))  
[FindItems(String, ItemView,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_Folder_FindItems.htm)|
Obtains a list of items by searching the contents of this folder. Calling this
method results in a call to EWS.  
(Унаследован от [Folder](T_Tessa_Exchange_WebServices_Data_Folder.htm))  
[FindItems(SearchFilter, ItemView, Grouping,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_Folder_FindItems_5.htm)|
Obtains a grouped list of items by searching the contents of this folder.
Calling this method results in a call to EWS.  
(Унаследован от [Folder](T_Tessa_Exchange_WebServices_Data_Folder.htm))  
[FindItems(String, ItemView, Grouping,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_Folder_FindItems_1.htm)|
Obtains a grouped list of items by searching the contents of this folder.
Calling this method results in a call to EWS.  
(Унаследован от [Folder](T_Tessa_Exchange_WebServices_Data_Folder.htm))  
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
[MarkAllItemsAsRead](M_Tessa_Exchange_WebServices_Data_Folder_MarkAllItemsAsRead.htm)|
Marks all items in folder as read. Calling this method results in a call to
EWS.  
(Унаследован от [Folder](T_Tessa_Exchange_WebServices_Data_Folder.htm))  
[MarkAllItemsAsUnread](M_Tessa_Exchange_WebServices_Data_Folder_MarkAllItemsAsUnread.htm)|
Marks all items in folder as read. Calling this method results in a call to
EWS.  
(Унаследован от [Folder](T_Tessa_Exchange_WebServices_Data_Folder.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Move(WellKnownFolderName)](M_Tessa_Exchange_WebServices_Data_Folder_Move_1.htm)|
Moves this folder to the specified folder. Calling this method results in a
call to EWS.  
(Унаследован от [Folder](T_Tessa_Exchange_WebServices_Data_Folder.htm))  
[Move(FolderId,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_Folder_Move.htm)|  Moves
this folder to a specific folder. Calling this method results in a call to
EWS.  
(Унаследован от [Folder](T_Tessa_Exchange_WebServices_Data_Folder.htm))  
[RemoveExtendedProperty](M_Tessa_Exchange_WebServices_Data_Folder_RemoveExtendedProperty.htm)|
Removes an extended property.  
(Унаследован от [Folder](T_Tessa_Exchange_WebServices_Data_Folder.htm))  
[Save(WellKnownFolderName)](M_Tessa_Exchange_WebServices_Data_Folder_Save_1.htm)|
Saves this folder in a specific folder. Calling this method results in a call
to EWS.  
(Унаследован от [Folder](T_Tessa_Exchange_WebServices_Data_Folder.htm))  
[Save(FolderId,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_Folder_Save.htm)|  Saves
this folder in a specific folder. Calling this method results in a call to
EWS.  
(Унаследован от [Folder](T_Tessa_Exchange_WebServices_Data_Folder.htm))  
[SetExtendedProperty](M_Tessa_Exchange_WebServices_Data_Folder_SetExtendedProperty.htm)|
Sets the extended property.  
(Унаследован от [Folder](T_Tessa_Exchange_WebServices_Data_Folder.htm))  
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
[Update](M_Tessa_Exchange_WebServices_Data_Folder_Update.htm)|  Applies the
local changes that have been made to this folder. Calling this method results
in a call to EWS.  
(Унаследован от [Folder](T_Tessa_Exchange_WebServices_Data_Folder.htm))  
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
