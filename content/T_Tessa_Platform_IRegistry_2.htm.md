# IRegistry<TIdentifier, TItem> \- интерфейс
Потокобезопасный реестр объектов, идентифицируемых по
[Guid](https://learn.microsoft.com/dotnet/api/system.guid).
## __Definition
 **Пространство имён:** [Tessa.Platform](N_Tessa_Platform.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IRegistry<in TIdentifier, TItem>
    where TItem : Object, IRegistryItem<TIdentifier>
VB __Копировать
     Public Interface IRegistry(Of In TIdentifier, TItem As {Object, IRegistryItem(Of TIdentifier)})
C++ __Копировать
    generic<typename TIdentifier, typename TItem>
    where TItem : Object, IRegistryItem<TIdentifier>
    public interface class IRegistry
F# __Копировать
     type IRegistry<'TIdentifier, 'TItem when 'TItem : Object and IRegistryItem<'TIdentifier>> = interface end
#### Параметры типа
TIdentifier
     Тип уникального идентификатора, по которому сравниваются объекта. Обычно это [Guid](https://learn.microsoft.com/dotnet/api/system.guid) или [Int32](https://learn.microsoft.com/dotnet/api/system.int32). 
TItem
     Тип объектов, содержащихся в реестре и реализующих интерфейс [IRegistryItem<TIdentifier>](T_Tessa_Platform_IRegistryItem_1.htm). 
## __Методы
[Get](M_Tessa_Platform_IRegistry_2_Get.htm)| Возвращает объект,
зарегистрированный в реестре по заданному идентификатору.  
---|---  
[GetAll](M_Tessa_Platform_IRegistry_2_GetAll.htm)| Возвращает все
зарегистрированные в реестре объекты.  
[IsDefined(TIdentifier)](M_Tessa_Platform_IRegistry_2_IsDefined.htm)|
Возвращает признак того, что в реестре был зарегистрирован объект по заданному
идентификатору.  
[IsDefined(TItem)](M_Tessa_Platform_IRegistry_2_IsDefined_1.htm)| Возвращает
признак того, что заданный объект был зарегистрирован в реестре.  
[Register](M_Tessa_Platform_IRegistry_2_Register.htm)| Регистрирует объект по
его идентификатору. Метод замещает предыдущую регистрацию при её наличии.  
[TryGet](M_Tessa_Platform_IRegistry_2_TryGet.htm)|  Возвращает объект в
параметре result, зарегистрированный в реестре по заданному идентификатору.
Метод возвращает false, если объект отсутствует в реестре.  
## __См. также
#### Ссылки
[Tessa.Platform - пространство имён](N_Tessa_Platform.htm)
