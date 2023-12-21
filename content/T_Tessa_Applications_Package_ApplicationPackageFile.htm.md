# ApplicationPackageFile - класс
Файл пакета приложения
## __Definition
 **Пространство имён:**
[Tessa.Applications.Package](N_Tessa_Applications_Package.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [SerializableAttribute]
    [DataContractAttribute]
    public sealed class ApplicationPackageFile : StorageSerializable, 
    	IEquatable<ApplicationPackageFile>, ICloneable, IStorageElementSerialization
VB __Копировать
    <SerializableAttribute>
    <DataContractAttribute>
    Public NotInheritable Class ApplicationPackageFile
    	Inherits StorageSerializable
    	Implements IEquatable(Of ApplicationPackageFile), ICloneable, 
    	IStorageElementSerialization
C++ __Копировать
    [SerializableAttribute]
    [DataContractAttribute]
    public ref class ApplicationPackageFile sealed : public StorageSerializable, 
    	IEquatable<ApplicationPackageFile^>, ICloneable, IStorageElementSerialization
F# __Копировать
     [<SealedAttribute>]
    [<SerializableAttribute>]
    [<DataContractAttribute>]
    type ApplicationPackageFile = 
        class
            inherit StorageSerializable
            interface IEquatable<ApplicationPackageFile>
            interface ICloneable
            interface IStorageElementSerialization
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[StorageSerializable](T_Tessa_Platform_Storage_StorageSerializable.htm) __ ApplicationPackageFile
Implements
    [ICloneable](https://learn.microsoft.com/dotnet/api/system.icloneable), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<ApplicationPackageFile>, [IStorageElementSerialization](T_Tessa_Applications_Containers_Storage_IStorageElementSerialization.htm)
##  __Конструкторы
[ApplicationPackageFile()](M_Tessa_Applications_Package_ApplicationPackageFile__ctor.htm)|
Initializes a new instance of the ApplicationPackageFile class. Initializes a
new instance of the
[Object](https://learn.microsoft.com/dotnet/api/system.object) class.  
---|---  
[ApplicationPackageFile(String, String, Guid, Int64, Byte[], Nullable<Guid>,
Nullable<Guid>, Nullable<CardFileSourceType>, PackageFileState,
Boolean)](M_Tessa_Applications_Package_ApplicationPackageFile__ctor_1.htm)|
Initializes a new instance of the ApplicationPackageFile class. Инициализирует
новый экземпляр класса
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
## __Свойства
[ApplicationId](P_Tessa_Applications_Package_ApplicationPackageFile_ApplicationId.htm)|
Gets or sets Идентификатор пакета  
---|---  
[FullName](P_Tessa_Applications_Package_ApplicationPackageFile_FullName.htm)|
Gets or sets Полное имя файла  
[Hash](P_Tessa_Applications_Package_ApplicationPackageFile_Hash.htm)|  Gets or
sets Контрольная сумма элемента или null  
[Id](P_Tessa_Applications_Package_ApplicationPackageFile_Id.htm)|  Gets or
sets Уникальный идентификатор файла  
[IsLocal](P_Tessa_Applications_Package_ApplicationPackageFile_IsLocal.htm)|
Возвращает или задаёт значение, показывающее, доступен ли файл локально.  
[Name](P_Tessa_Applications_Package_ApplicationPackageFile_Name.htm)|  Gets or
sets Имя файла  
[Size](P_Tessa_Applications_Package_ApplicationPackageFile_Size.htm)|  Gets or
sets Размер занимаемый содержимым элемента  
[SourceType](P_Tessa_Applications_Package_ApplicationPackageFile_SourceType.htm)|
Gets Источник файла.  
[SourceTypeId](P_Tessa_Applications_Package_ApplicationPackageFile_SourceTypeId.htm)|
Gets or sets Идентификатор типа источника файла  
[State](P_Tessa_Applications_Package_ApplicationPackageFile_State.htm)|  Gets
or sets Состояние файла  
[VersionId](P_Tessa_Applications_Package_ApplicationPackageFile_VersionId.htm)|
Gets or sets Идентификатор версии файла  
## __Методы
[Clone](M_Tessa_Applications_Package_ApplicationPackageFile_Clone.htm)|
Создает новый объект, который является копией текущего экземпляра.  
---|---  
[Deserialize](M_Tessa_Platform_Storage_StorageSerializable_Deserialize.htm)|
Выполняет десериализацию полей объекта из заданного хранилища.  
(Унаследован от
[StorageSerializable](T_Tessa_Platform_Storage_StorageSerializable.htm))  
[DeserializeAndGetCore](M_Tessa_Platform_Storage_StorageSerializable_DeserializeAndGetCore.htm)|
Выполняет десериализацию полей объекта из заданного хранилища.  
(Унаследован от
[StorageSerializable](T_Tessa_Platform_Storage_StorageSerializable.htm))  
[DeserializeCore](M_Tessa_Applications_Package_ApplicationPackageFile_DeserializeCore.htm)|
Выполняет десериализацию полей объекта из заданного хранилища.  
(Переопределяет [StorageSerializable.DeserializeCore(Dictionary<String,
Object>)](M_Tessa_Platform_Storage_StorageSerializable_DeserializeCore.htm))  
[Equals(ApplicationPackageFile)](M_Tessa_Applications_Package_ApplicationPackageFile_Equals.htm)|
Указывает, равен ли текущий объект другому объекту того же типа.  
[Equals(Object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[FromStorage](M_Tessa_Applications_Package_ApplicationPackageFile_FromStorage.htm)|
Создаёт новый объект ApplicationPackageFile и инициализирует его данными из
указанного элемента хранилища.  
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
[Serialize(Dictionary<String,
Object>)](M_Tessa_Platform_Storage_StorageSerializable_Serialize.htm)|
Выполняет сериализацию полей объекта в заданное хранилище.  
(Унаследован от
[StorageSerializable](T_Tessa_Platform_Storage_StorageSerializable.htm))  
[Serialize(IStorageElement)](M_Tessa_Applications_Package_ApplicationPackageFile_Serialize.htm)|
Осуществляет запись свойств объекта в элемент container  
[SerializeCore](M_Tessa_Applications_Package_ApplicationPackageFile_SerializeCore.htm)|
Выполняет сериализацию полей объекта в заданное хранилище.  
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
