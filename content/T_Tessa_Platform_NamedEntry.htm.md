# NamedEntry - класс
Именованный объект с идентификатором.
## __Definition
 **Пространство имён:** [Tessa.Platform](N_Tessa_Platform.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [DataContractAttribute]
    public abstract class NamedEntry : INamedObject, 
    	INamedEntry, INamedItem, IEquatable<INamedEntry>
VB __Копировать
    <DataContractAttribute>
    Public MustInherit Class NamedEntry
    	Implements INamedObject, INamedEntry, INamedItem, IEquatable(Of INamedEntry)
C++ __Копировать
    [DataContractAttribute]
    public ref class NamedEntry abstract : INamedObject, 
    	INamedEntry, INamedItem, IEquatable<INamedEntry^>
F# __Копировать
     [<AbstractClassAttribute>]
    [<DataContractAttribute>]
    type NamedEntry = 
        class
            interface INamedObject
            interface INamedEntry
            interface INamedItem
            interface IEquatable<INamedEntry>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ NamedEntry
Derived
[Tessa.Roles.Role](T_Tessa_Roles_Role.htm)
[Tessa.Roles.RoleGenerator](T_Tessa_Roles_RoleGenerator.htm)
Implements
    [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<[INamedEntry](T_Tessa_Platform_INamedEntry.htm)>, [INamedItem](T_Tessa_Platform_Collections_INamedItem.htm), [INamedObject](T_Tessa_Platform_Collections_INamedObject.htm), [INamedEntry](T_Tessa_Platform_INamedEntry.htm)
##  __Конструкторы
[NamedEntry](M_Tessa_Platform_NamedEntry__ctor.htm)| Инициализирует новый
экземпляр класса NamedEntry  
---|---  
##  __Свойства
[ID](P_Tessa_Platform_NamedEntry_ID.htm)| Идентификатор объекта.  
---|---  
[Name](P_Tessa_Platform_NamedEntry_Name.htm)| Отображаемое имя объекта.  
##  __Методы
[Equals(INamedEntry)](M_Tessa_Platform_NamedEntry_Equals_1.htm)| Сравнивает
текущий объект с заданным.  
---|---  
[Equals(Object)](M_Tessa_Platform_NamedEntry_Equals.htm)| Сравнивает текущий
объект с заданным.  
(Переопределяет
[Object.Equals(Object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\)))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](M_Tessa_Platform_NamedEntry_GetHashCode.htm)| Возвращает хеш-код
объекта.  
(Переопределяет
[Object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode))  
[GetName](M_Tessa_Platform_NamedEntry_GetName.htm)|  Возвращает имя объекта.  
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
[ToString](M_Tessa_Platform_NamedEntry_ToString.htm)| Возвращает строковое
представление объекта.  
(Переопределяет
[Object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring))  
[UpdateFromAssociations](M_Tessa_Platform_NamedEntry_UpdateFromAssociations.htm)|
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
