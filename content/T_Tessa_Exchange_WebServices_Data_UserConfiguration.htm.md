# UserConfiguration - класс
Represents an object that can be used to store user-defined configuration
settings.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public class UserConfiguration
VB __Копировать
     Public Class UserConfiguration
C++ __Копировать
     public ref class UserConfiguration
F# __Копировать
     type UserConfiguration = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ UserConfiguration
##  __Конструкторы
[UserConfiguration](M_Tessa_Exchange_WebServices_Data_UserConfiguration__ctor.htm)|
Initializes a new instance of UserConfiguration class.  
---|---  
## __Свойства
[BinaryData](P_Tessa_Exchange_WebServices_Data_UserConfiguration_BinaryData.htm)|
Gets or sets the binary data of the user configuration.  
---|---  
[Dictionary](P_Tessa_Exchange_WebServices_Data_UserConfiguration_Dictionary.htm)|
Gets the dictionary of the user configuration.  
[IsDirty](P_Tessa_Exchange_WebServices_Data_UserConfiguration_IsDirty.htm)|
Gets a value indicating whether this user configuration has been modified.  
[ItemId](P_Tessa_Exchange_WebServices_Data_UserConfiguration_ItemId.htm)|
Gets the Id of the user configuration.  
[Name](P_Tessa_Exchange_WebServices_Data_UserConfiguration_Name.htm)|  Gets
the name of the user configuration.  
[ParentFolderId](P_Tessa_Exchange_WebServices_Data_UserConfiguration_ParentFolderId.htm)|
Gets the Id of the folder containing the user configuration.  
[XmlData](P_Tessa_Exchange_WebServices_Data_UserConfiguration_XmlData.htm)|
Gets or sets the xml data of the user configuration.  
## __Методы
[Bind(ExchangeService, String, WellKnownFolderName,
UserConfigurationProperties)](M_Tessa_Exchange_WebServices_Data_UserConfiguration_Bind_1.htm)|
Binds to an existing user configuration and loads the specified properties.
Calling this method results in a call to EWS.  
---|---  
[Bind(ExchangeService, String, FolderId, UserConfigurationProperties,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_UserConfiguration_Bind.htm)|
Binds to an existing user configuration and loads the specified properties.
Calling this method results in a call to EWS.  
[Delete](M_Tessa_Exchange_WebServices_Data_UserConfiguration_Delete.htm)|
Deletes the user configuration. Calling this method results in a call to EWS.  
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
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Load](M_Tessa_Exchange_WebServices_Data_UserConfiguration_Load.htm)|  Loads
the specified properties on the user configuration. Calling this method
results in a call to EWS.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Save(String,
WellKnownFolderName)](M_Tessa_Exchange_WebServices_Data_UserConfiguration_Save_1.htm)|
Saves the user configuration. Calling this method results in a call to EWS.  
[Save(String, FolderId,
CancellationToken)](M_Tessa_Exchange_WebServices_Data_UserConfiguration_Save.htm)|
Saves the user configuration. Calling this method results in a call to EWS.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Update](M_Tessa_Exchange_WebServices_Data_UserConfiguration_Update.htm)|
Updates the user configuration by applying local changes to the Exchange
server. Calling this method results in a call to EWS.  
## __Методы расширения
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
