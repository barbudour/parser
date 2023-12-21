# INamedRegistry<TItem> \- интерфейс
Потокобезопасный реестр объектов, идентифицируемых по
[Guid](https://learn.microsoft.com/dotnet/api/system.guid) и по строковому
имени.
## __Definition
 **Пространство имён:** [Tessa.Platform](N_Tessa_Platform.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface INamedRegistry<TItem> : IRegistry<Guid, TItem>
    where TItem : Object, IRegistryItem<Guid>, INamedItem
VB __Копировать
     Public Interface INamedRegistry(Of TItem As {Object, IRegistryItem(Of Guid), INamedItem})
    	Inherits IRegistry(Of Guid, TItem)
C++ __Копировать
    generic<typename TItem>
    where TItem : Object, IRegistryItem<Guid>, INamedItem
    public interface class INamedRegistry : IRegistry<Guid, TItem>
F# __Копировать
     type INamedRegistry<'TItem when 'TItem : Object and IRegistryItem<Guid> and INamedItem> = 
        interface
            interface IRegistry<Guid, 'TItem>
        end
Implements
    [IRegistry](T_Tessa_Platform_IRegistry_2.htm)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid), TItem>
#### Параметры типа
TItem
     Тип объектов, содержащихся в реестре и реализующих интерфейсы [IRegistryItem<TIdentifier>](T_Tessa_Platform_IRegistryItem_1.htm) и [INamedItem](T_Tessa_Platform_Collections_INamedItem.htm). 
## __Методы
[Get(TIdentifier)](M_Tessa_Platform_IRegistry_2_Get.htm)| Возвращает объект,
зарегистрированный в реестре по заданному идентификатору.  
(Унаследован от [IRegistry<TIdentifier,
TItem>](T_Tessa_Platform_IRegistry_2.htm))  
---|---  
[Get(String)](M_Tessa_Platform_INamedRegistry_1_Get.htm)| Возвращает объект,
зарегистрированный в реестре по заданному имени.  
[GetAll](M_Tessa_Platform_IRegistry_2_GetAll.htm)| Возвращает все
зарегистрированные в реестре объекты.  
(Унаследован от [IRegistry<TIdentifier,
TItem>](T_Tessa_Platform_IRegistry_2.htm))  
[IsDefined(TIdentifier)](M_Tessa_Platform_IRegistry_2_IsDefined.htm)|
Возвращает признак того, что в реестре был зарегистрирован объект по заданному
идентификатору.  
(Унаследован от [IRegistry<TIdentifier,
TItem>](T_Tessa_Platform_IRegistry_2.htm))  
[IsDefined(TItem)](M_Tessa_Platform_IRegistry_2_IsDefined_1.htm)| Возвращает
признак того, что заданный объект был зарегистрирован в реестре.  
(Унаследован от [IRegistry<TIdentifier,
TItem>](T_Tessa_Platform_IRegistry_2.htm))  
[IsDefined(String)](M_Tessa_Platform_INamedRegistry_1_IsDefined.htm)|
Возвращает признак того, что в реестре был зарегистрирован объект по заданному
имени.  
[Register](M_Tessa_Platform_IRegistry_2_Register.htm)| Регистрирует объект по
его идентификатору. Метод замещает предыдущую регистрацию при её наличии.  
(Унаследован от [IRegistry<TIdentifier,
TItem>](T_Tessa_Platform_IRegistry_2.htm))  
[TryGet](M_Tessa_Platform_IRegistry_2_TryGet.htm)|  Возвращает объект в
параметре result, зарегистрированный в реестре по заданному идентификатору.
Метод возвращает false, если объект отсутствует в реестре.  
(Унаследован от [IRegistry<TIdentifier,
TItem>](T_Tessa_Platform_IRegistry_2.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform - пространство имён](N_Tessa_Platform.htm)
