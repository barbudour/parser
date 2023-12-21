# ApplicationPackage - класс
Пакет приложения
## __Definition
 **Пространство имён:**
[Tessa.Applications.Package](N_Tessa_Applications_Package.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [SerializableAttribute]
    [DataContractAttribute]
    public class ApplicationPackage : StorageSerializable, 
    	ICloneable, IStorageElementSerialization
VB __Копировать
    <SerializableAttribute>
    <DataContractAttribute>
    Public Class ApplicationPackage
    	Inherits StorageSerializable
    	Implements ICloneable, IStorageElementSerialization
C++ __Копировать
    [SerializableAttribute]
    [DataContractAttribute]
    public ref class ApplicationPackage : public StorageSerializable, 
    	ICloneable, IStorageElementSerialization
F# __Копировать
     [<SerializableAttribute>]
    [<DataContractAttribute>]
    type ApplicationPackage = 
        class
            inherit StorageSerializable
            interface ICloneable
            interface IStorageElementSerialization
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[StorageSerializable](T_Tessa_Platform_Storage_StorageSerializable.htm) __ ApplicationPackage
Implements
    [ICloneable](https://learn.microsoft.com/dotnet/api/system.icloneable), [IStorageElementSerialization](T_Tessa_Applications_Containers_Storage_IStorageElementSerialization.htm)
##  __Конструкторы
[ApplicationPackage](M_Tessa_Applications_Package_ApplicationPackage__ctor.htm)|
Initializes a new instance of the ApplicationPackage class. Initializes a new
instance of the [Object](https://learn.microsoft.com/dotnet/api/system.object)
class.  
---|---  
## __Свойства
[ActionHistoryRowID](P_Tessa_Applications_Package_ApplicationPackage_ActionHistoryRowID.htm)|
Gets or sets Идентификатор записи в истории  
---|---  
[Alias](P_Tessa_Applications_Package_ApplicationPackage_Alias.htm)|  Gets or
sets Псевдоним приложения  
[ApplicationId](P_Tessa_Applications_Package_ApplicationPackage_ApplicationId.htm)|
Gets or sets Идентификатор приложения  
[AppManagerApiV2](P_Tessa_Applications_Package_ApplicationPackage_AppManagerApiV2.htm)|
Признак того, что публикуемое приложение использует новый API для
взаимодействия с менеджером приложений.  
[AppVersion](P_Tessa_Applications_Package_ApplicationPackage_AppVersion.htm)|
Gets or sets Версия приложения  
[Client64Bit](P_Tessa_Applications_Package_ApplicationPackage_Client64Bit.htm)|
Признак того, что публикуемое приложение использует 64-битную архитектуру.  
[ExecutableFileName](P_Tessa_Applications_Package_ApplicationPackage_ExecutableFileName.htm)|
Gets or sets Имя исполняемого файла  
[ExtensionVersion](P_Tessa_Applications_Package_ApplicationPackage_ExtensionVersion.htm)|
Gets or sets Версия расширения  
Устарело.  
[Files](P_Tessa_Applications_Package_ApplicationPackage_Files.htm)|  Gets or
sets Список файлов  
[ForAdmin](P_Tessa_Applications_Package_ApplicationPackage_ForAdmin.htm)|
Gets or sets a value indicating whether Признак доступности приложения только
администратору  
[GroupName](P_Tessa_Applications_Package_ApplicationPackage_GroupName.htm)|
Gets or sets Имя группы  
[Icon](P_Tessa_Applications_Package_ApplicationPackage_Icon.htm)|  Gets or
sets Значок приложения  
[LocalFilesHash](P_Tessa_Applications_Package_ApplicationPackage_LocalFilesHash.htm)|
Возвращает или задаёт массив байт содержащий значения хеш-кодов доступных
локально файлов.  
[LocalizedGroupName](P_Tessa_Applications_Package_ApplicationPackage_LocalizedGroupName.htm)|
Gets or sets Локализованное имя группы  
[Modified](P_Tessa_Applications_Package_ApplicationPackage_Modified.htm)|
Gets or sets Дата изменения пакета  
[Name](P_Tessa_Applications_Package_ApplicationPackage_Name.htm)|  Gets or
sets Название приложения  
[PlatformVersion](P_Tessa_Applications_Package_ApplicationPackage_PlatformVersion.htm)|
Gets or sets Версия платформы  
## __Методы
[Clone](M_Tessa_Applications_Package_ApplicationPackage_Clone.htm)| Создает
новый объект, который является копией текущего экземпляра.  
---|---  
[Deserialize](M_Tessa_Platform_Storage_StorageSerializable_Deserialize.htm)|
Выполняет десериализацию полей объекта из заданного хранилища.  
(Унаследован от
[StorageSerializable](T_Tessa_Platform_Storage_StorageSerializable.htm))  
[DeserializeAndGetCore](M_Tessa_Platform_Storage_StorageSerializable_DeserializeAndGetCore.htm)|
Выполняет десериализацию полей объекта из заданного хранилища.  
(Унаследован от
[StorageSerializable](T_Tessa_Platform_Storage_StorageSerializable.htm))  
[DeserializeCore](M_Tessa_Applications_Package_ApplicationPackage_DeserializeCore.htm)|  
(Переопределяет [StorageSerializable.DeserializeCore(Dictionary<String,
Object>)](M_Tessa_Platform_Storage_StorageSerializable_DeserializeCore.htm))  
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
[IsLocalFile](M_Tessa_Applications_Package_ApplicationPackage_IsLocalFile.htm)|
Возвращает значение, показывающее, содержится ли указанный хеш в
[LocalFilesHash](P_Tessa_Applications_Package_ApplicationPackage_LocalFilesHash.htm),
если содержится, то файл имеющий указанный хеш присутствует на клиенте.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Serialize(Dictionary<String,
Object>)](M_Tessa_Platform_Storage_StorageSerializable_Serialize.htm)|
Выполняет сериализацию полей объекта в заданное хранилище.  
(Унаследован от
[StorageSerializable](T_Tessa_Platform_Storage_StorageSerializable.htm))  
[Serialize(IStorageElement)](M_Tessa_Applications_Package_ApplicationPackage_Serialize.htm)|
Осуществляет запись свойств объекта в элемент container  
[SerializeCore](M_Tessa_Applications_Package_ApplicationPackage_SerializeCore.htm)|  
(Переопределяет [StorageSerializable.SerializeCore(Dictionary<String,
Object>)](M_Tessa_Platform_Storage_StorageSerializable_SerializeCore.htm))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[GetTotalBytes](M_Tessa_Applications_Package_ApplicationPackageBuilderExtender_GetTotalBytes_1.htm)|
Подсчитывает размер файлов в пакете приложения  
(Определяется
[ApplicationPackageBuilderExtender](T_Tessa_Applications_Package_ApplicationPackageBuilderExtender.htm))  
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
[Tessa.Applications.Package - пространство
имён](N_Tessa_Applications_Package.htm)
