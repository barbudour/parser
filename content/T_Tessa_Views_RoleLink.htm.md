# RoleLink - класс
Объект, хранящий привязку роли к объекту.
## __Definition
 **Пространство имён:** [Tessa.Views](N_Tessa_Views.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [SerializableAttribute]
    [DataContractAttribute]
    public sealed class RoleLink : ICloneable, 
    	IStorageSerializable
VB __Копировать
    <SerializableAttribute>
    <DataContractAttribute>
    Public NotInheritable Class RoleLink
    	Implements ICloneable, IStorageSerializable
C++ __Копировать
    [SerializableAttribute]
    [DataContractAttribute]
    public ref class RoleLink sealed : ICloneable, 
    	IStorageSerializable
F# __Копировать
     [<SealedAttribute>]
    [<SerializableAttribute>]
    [<DataContractAttribute>]
    type RoleLink = 
        class
            interface ICloneable
            interface IStorageSerializable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ RoleLink
Implements
    [ICloneable](https://learn.microsoft.com/dotnet/api/system.icloneable), [IStorageSerializable](T_Tessa_Platform_Storage_IStorageSerializable.htm)
##  __Конструкторы
[RoleLink()](M_Tessa_Views_RoleLink__ctor.htm)|  Initializes a new instance of
the RoleLink class. Инициализирует новый экземпляр класса
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
---|---  
[RoleLink(Guid, String, Guid)](M_Tessa_Views_RoleLink__ctor_1.htm)|
Initializes a new instance of the RoleLink class. Инициализирует новый
экземпляр класса
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
[RoleLink(Guid, String, Guid, DeltaKind)](M_Tessa_Views_RoleLink__ctor_2.htm)|
Initializes a new instance of the RoleLink class. Инициализирует новый
экземпляр класса
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
## __Свойства
[DeltaKind](P_Tessa_Views_RoleLink_DeltaKind.htm)|  Gets or sets Вид изменений  
---|---  
[ObjectId](P_Tessa_Views_RoleLink_ObjectId.htm)|  Gets or sets Идентификатор
объекта  
[RoleId](P_Tessa_Views_RoleLink_RoleId.htm)|  Gets or sets Идентификатор роли  
[RoleName](P_Tessa_Views_RoleLink_RoleName.htm)|  Gets or sets Имя роли  
## __Методы
[Clone](M_Tessa_Views_RoleLink_Clone.htm)|  Создает новый объект, который
является копией текущего экземпляра.  
---|---  
[Deserialize](M_Tessa_Views_RoleLink_Deserialize.htm)|  
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
[Serialize](M_Tessa_Views_RoleLink_Serialize.htm)|  
[ToString](M_Tessa_Views_RoleLink_ToString.htm)|  Возвращает объект
[String](https://learn.microsoft.com/dotnet/api/system.string), который
представляет текущий объект
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Переопределяет
[Object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring))  
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
[Tessa.Views - пространство имён](N_Tessa_Views.htm)
