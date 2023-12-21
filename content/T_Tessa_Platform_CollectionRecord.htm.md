# CollectionRecord - класс
Элемент коллекционной секции.
## __Definition
 **Пространство имён:** [Tessa.Platform](N_Tessa_Platform.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [DataContractAttribute]
    public abstract class CollectionRecord : ICollectionRecord, 
    	IEquatable<ICollectionRecord>
VB __Копировать
    <DataContractAttribute>
    Public MustInherit Class CollectionRecord
    	Implements ICollectionRecord, IEquatable(Of ICollectionRecord)
C++ __Копировать
    [DataContractAttribute]
    public ref class CollectionRecord abstract : ICollectionRecord, 
    	IEquatable<ICollectionRecord^>
F# __Копировать
     [<AbstractClassAttribute>]
    [<DataContractAttribute>]
    type CollectionRecord = 
        class
            interface ICollectionRecord
            interface IEquatable<ICollectionRecord>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CollectionRecord
Derived
[Tessa.Roles.RoleDeputyRecord](T_Tessa_Roles_RoleDeputyRecord.htm)
[Tessa.Roles.RoleUserRecord](T_Tessa_Roles_RoleUserRecord.htm)
Implements
    [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<[ICollectionRecord](T_Tessa_Platform_ICollectionRecord.htm)>, [ICollectionRecord](T_Tessa_Platform_ICollectionRecord.htm)
##  __Конструкторы
[CollectionRecord](M_Tessa_Platform_CollectionRecord__ctor.htm)|
Инициализирует новый экземпляр класса CollectionRecord  
---|---  
##  __Свойства
[ID](P_Tessa_Platform_CollectionRecord_ID.htm)| Идентификатор записи.  
---|---  
[RowID](P_Tessa_Platform_CollectionRecord_RowID.htm)| Идентификатор объекта,
которому соответствует запись.  
##  __Методы
[Equals(ICollectionRecord)](M_Tessa_Platform_CollectionRecord_Equals_1.htm)|
Сравнивает текущий объект с заданным.  
---|---  
[Equals(Object)](M_Tessa_Platform_CollectionRecord_Equals.htm)| Сравнивает
текущий объект с заданным.  
(Переопределяет
[Object.Equals(Object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\)))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](M_Tessa_Platform_CollectionRecord_GetHashCode.htm)| Возвращает
хеш-код объекта.  
(Переопределяет
[Object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode))  
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
[UpdateFromAssociations](M_Tessa_Platform_CollectionRecord_UpdateFromAssociations.htm)|
Обновляет значения ссылочных полей из всех объектов-ассоциаций, на которые
установлены ссылки.  
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
[Tessa.Platform - пространство имён](N_Tessa_Platform.htm)
