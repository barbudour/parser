# CreateCardExtensionSettings - класс
The create card extension settings.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Views](N_Tessa_Extensions_Default_Shared_Views.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class CreateCardExtensionSettings : IStorageSerializable
VB __Копировать
     Public NotInheritable Class CreateCardExtensionSettings
    	Implements IStorageSerializable
C++ __Копировать
     public ref class CreateCardExtensionSettings sealed : IStorageSerializable
F# __Копировать
     [<SealedAttribute>]
    type CreateCardExtensionSettings = 
        class
            interface IStorageSerializable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CreateCardExtensionSettings
Implements
    [IStorageSerializable](T_Tessa_Platform_Storage_IStorageSerializable.htm)
##  __Конструкторы
[CreateCardExtensionSettings](M_Tessa_Extensions_Default_Shared_Views_CreateCardExtensionSettings__ctor.htm)|
Инициализирует новый экземпляр класса CreateCardExtensionSettings  
---|---  
##  __Свойства
[CardCreationKind](P_Tessa_Extensions_Default_Shared_Views_CreateCardExtensionSettings_CardCreationKind.htm)|
Режим создания карточки.  
---|---  
[CardOpeningKind](P_Tessa_Extensions_Default_Shared_Views_CreateCardExtensionSettings_CardOpeningKind.htm)|
Режим открытия созданной карточки карточки. Игнорируется, если расширение
используется для выбора ссылки по троеточию.  
[DocTypeIdentifier](P_Tessa_Extensions_Default_Shared_Views_CreateCardExtensionSettings_DocTypeIdentifier.htm)|
Идентификатор типа документа (но не типа карточки), если режим создания
карточки
[CardCreationKind](P_Tessa_Extensions_Default_Shared_Views_CreateCardExtensionSettings_CardCreationKind.htm)
равен
[ByDocTypeIdentifier](T_Tessa_Extensions_Default_Shared_Views_CardCreationKind.htm).  
[IDParam](P_Tessa_Extensions_Default_Shared_Views_CreateCardExtensionSettings_IDParam.htm)|
Название параметра, по которому можно получить запись по первичному ключу.
Необходимо для поведения "Создать новую карточку и выбрать" при выборе ссылки
по троеточию.  
[TypeAlias](P_Tessa_Extensions_Default_Shared_Views_CreateCardExtensionSettings_TypeAlias.htm)|
Алиас типа карточки, если режим создания карточки
[CardCreationKind](P_Tessa_Extensions_Default_Shared_Views_CreateCardExtensionSettings_CardCreationKind.htm)
равен
[ByTypeAlias](T_Tessa_Extensions_Default_Shared_Views_CardCreationKind.htm).  
## __Методы
[Deserialize](M_Tessa_Extensions_Default_Shared_Views_CreateCardExtensionSettings_Deserialize.htm)|  
---|---  
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
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Serialize](M_Tessa_Extensions_Default_Shared_Views_CreateCardExtensionSettings_Serialize.htm)|  
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
[ToSerializedDictionary](M_Tessa_Platform_Storage_StorageExtensions_ToSerializedDictionary.htm)|
Сериализует объект в нетипизированный словарь.  
(Определяется
[StorageExtensions](T_Tessa_Platform_Storage_StorageExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Extensions.Default.Shared.Views - пространство
имён](N_Tessa_Extensions_Default_Shared_Views.htm)
