# FolderPermission - класс
Represents a permission on a folder.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class FolderPermission : ComplexProperty
VB __Копировать
     Public NotInheritable Class FolderPermission
    	Inherits ComplexProperty
C++ __Копировать
     public ref class FolderPermission sealed : public ComplexProperty
F# __Копировать
     [<SealedAttribute>]
    type FolderPermission = 
        class
            inherit ComplexProperty
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ComplexProperty](T_Tessa_Exchange_WebServices_Data_ComplexProperty.htm) __ FolderPermission
##  __Конструкторы
[FolderPermission()](M_Tessa_Exchange_WebServices_Data_FolderPermission__ctor.htm)|
Initializes a new instance of the FolderPermission class.  
---|---  
[FolderPermission(StandardUser,
FolderPermissionLevel)](M_Tessa_Exchange_WebServices_Data_FolderPermission__ctor_2.htm)|
Initializes a new instance of the FolderPermission class.  
[FolderPermission(String,
FolderPermissionLevel)](M_Tessa_Exchange_WebServices_Data_FolderPermission__ctor_1.htm)|
Initializes a new instance of the FolderPermission class.  
[FolderPermission(UserId,
FolderPermissionLevel)](M_Tessa_Exchange_WebServices_Data_FolderPermission__ctor_3.htm)|
Initializes a new instance of the FolderPermission class.  
## __Свойства
[CanCreateItems](P_Tessa_Exchange_WebServices_Data_FolderPermission_CanCreateItems.htm)|
Gets or sets a value indicating whether the user can create new items.  
---|---  
[CanCreateSubFolders](P_Tessa_Exchange_WebServices_Data_FolderPermission_CanCreateSubFolders.htm)|
Gets or sets a value indicating whether the user can create sub-folders.  
[DeleteItems](P_Tessa_Exchange_WebServices_Data_FolderPermission_DeleteItems.htm)|
Gets or sets a value indicating if/how the user can delete existing items.  
[DisplayPermissionLevel](P_Tessa_Exchange_WebServices_Data_FolderPermission_DisplayPermissionLevel.htm)|
Gets the permission level that Outlook would display for this folder
permission.  
[EditItems](P_Tessa_Exchange_WebServices_Data_FolderPermission_EditItems.htm)|
Gets or sets a value indicating if/how the user can edit existing items.  
[IsFolderContact](P_Tessa_Exchange_WebServices_Data_FolderPermission_IsFolderContact.htm)|
Gets or sets a value indicating whether the user is a contact for the folder.  
[IsFolderOwner](P_Tessa_Exchange_WebServices_Data_FolderPermission_IsFolderOwner.htm)|
Gets or sets a value indicating whether the user owns the folder.  
[IsFolderVisible](P_Tessa_Exchange_WebServices_Data_FolderPermission_IsFolderVisible.htm)|
Gets or sets a value indicating whether the folder is visible to the user.  
[PermissionLevel](P_Tessa_Exchange_WebServices_Data_FolderPermission_PermissionLevel.htm)|
Gets or sets the permission level.  
[ReadItems](P_Tessa_Exchange_WebServices_Data_FolderPermission_ReadItems.htm)|
Gets or sets the read items access permission.  
[UserId](P_Tessa_Exchange_WebServices_Data_FolderPermission_UserId.htm)|  Gets
the Id of the user the permission applies to.  
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
