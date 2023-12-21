# NamedRegistry<T> \- класс
Потокобезопасный реестр объектов, идентифицируемых по
[Guid](https://learn.microsoft.com/dotnet/api/system.guid) и по строковому
имени.
## __Definition
 **Пространство имён:** [Tessa.Platform](N_Tessa_Platform.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class NamedRegistry<T> : Registry<Guid, T>, 
    	INamedRegistry<T>, IRegistry<Guid, T>
    where T : Object, IRegistryItem<Guid>, INamedItem
VB __Копировать
     Public MustInherit Class NamedRegistry(Of T As {Object, IRegistryItem(Of Guid), INamedItem})
    	Inherits Registry(Of Guid, T)
    	Implements INamedRegistry(Of T), IRegistry(Of Guid, T)
C++ __Копировать
    generic<typename T>
    where T : Object, IRegistryItem<Guid>, INamedItem
    public ref class NamedRegistry abstract : public Registry<Guid, T>, 
    	INamedRegistry<T>, IRegistry<Guid, T>
F# __Копировать
     [<AbstractClassAttribute>]
    type NamedRegistry<'T when 'T : Object and IRegistryItem<Guid> and INamedItem> = 
        class
            inherit Registry<Guid, 'T>
            interface INamedRegistry<'T>
            interface IRegistry<Guid, 'T>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[Registry](T_Tessa_Platform_Registry_2.htm)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid), T> __ NamedRegistry<T>
Derived
[Tessa.Cards.Numbers.NumberTypeRegistry](T_Tessa_Cards_Numbers_NumberTypeRegistry.htm)
[Tessa.Platform.Validation.ValidationKeyRegistry](T_Tessa_Platform_Validation_ValidationKeyRegistry.htm)
Implements
    [INamedRegistry](T_Tessa_Platform_INamedRegistry_1.htm)<T>, [IRegistry](T_Tessa_Platform_IRegistry_2.htm)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid), T>
#### Параметры типа
T
     Тип объектов, содержащихся в реестре и реализующих интерфейсы [IRegistryItem<TIdentifier>](T_Tessa_Platform_IRegistryItem_1.htm) и [INamedItem](T_Tessa_Platform_Collections_INamedItem.htm). 
## __Конструкторы
[NamedRegistry<T>](M_Tessa_Platform_NamedRegistry_1__ctor.htm)| Инициализирует
новый экземпляр класса NamedRegistry<T>  
---|---  
##  __Методы
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
[Get(TIdentifier)](M_Tessa_Platform_Registry_2_Get.htm)| Возвращает объект,
зарегистрированный в реестре по заданному идентификатору.  
(Унаследован от [Registry<TIdentifier,
TItem>](T_Tessa_Platform_Registry_2.htm))  
[Get(String)](M_Tessa_Platform_NamedRegistry_1_Get.htm)| Возвращает объект,
зарегистрированный в реестре по заданному имени.  
[GetAll](M_Tessa_Platform_Registry_2_GetAll.htm)| Возвращает все
зарегистрированные в реестре объекты.  
(Унаследован от [Registry<TIdentifier,
TItem>](T_Tessa_Platform_Registry_2.htm))  
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
[IsDefined(TIdentifier)](M_Tessa_Platform_Registry_2_IsDefined.htm)|
Возвращает признак того, что в реестре был зарегистрирован объект по заданному
идентификатору.  
(Унаследован от [Registry<TIdentifier,
TItem>](T_Tessa_Platform_Registry_2.htm))  
[IsDefined(TItem)](M_Tessa_Platform_Registry_2_IsDefined_1.htm)| Возвращает
признак того, что заданный объект был зарегистрирован в реестре.  
(Унаследован от [Registry<TIdentifier,
TItem>](T_Tessa_Platform_Registry_2.htm))  
[IsDefined(String)](M_Tessa_Platform_NamedRegistry_1_IsDefined.htm)|
Возвращает признак того, что в реестре был зарегистрирован объект по заданному
имени.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Register](M_Tessa_Platform_Registry_2_Register.htm)| Регистрирует объект по
его идентификатору. Метод замещает предыдущую регистрацию при её наличии.  
(Унаследован от [Registry<TIdentifier,
TItem>](T_Tessa_Platform_Registry_2.htm))  
[RegisterCore](M_Tessa_Platform_NamedRegistry_1_RegisterCore.htm)|
Регистрирует объект по его идентификатору. Метод замещает предыдущую
регистрацию при её наличии.  
(Переопределяет [Registry<TIdentifier,
TItem>.RegisterCore(TItem)](M_Tessa_Platform_Registry_2_RegisterCore.htm))  
[RegisterNew](M_Tessa_Platform_NamedRegistry_1_RegisterNew.htm)|  Регистрирует
новый объект в реестре. Если элемент уже присутствует, то никаких действий не
производится.  
(Переопределяет [Registry<TIdentifier,
TItem>.RegisterNew(TItem)](M_Tessa_Platform_Registry_2_RegisterNew.htm))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGet](M_Tessa_Platform_Registry_2_TryGet.htm)|  Возвращает объект в
параметре result, зарегистрированный в реестре по заданному идентификатору.
Метод возвращает false, если объект отсутствует в реестре.  
(Унаследован от [Registry<TIdentifier,
TItem>](T_Tessa_Platform_Registry_2.htm))  
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
[Tessa.Platform - пространство имён](N_Tessa_Platform.htm)
