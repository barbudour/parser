# IRegistryItem<TIdentifier> \- интерфейс
Объект, регистрируемый в реестре [IRegistry<TIdentifier,
TItem>](T_Tessa_Platform_IRegistry_2.htm).
## __Definition
 **Пространство имён:** [Tessa.Platform](N_Tessa_Platform.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IRegistryItem<out TIdentifier>
VB __Копировать
     Public Interface IRegistryItem(Of Out TIdentifier)
C++ __Копировать
    generic<typename TIdentifier>
    public interface class IRegistryItem
F# __Копировать
     type IRegistryItem<'TIdentifier> = interface end
#### Параметры типа
TIdentifier
     Тип уникального идентификатора, по которому сравниваются объекта. Обычно это [Guid](https://learn.microsoft.com/dotnet/api/system.guid) или [Int32](https://learn.microsoft.com/dotnet/api/system.int32). 
## __Свойства
[ID](P_Tessa_Platform_IRegistryItem_1_ID.htm)| Идентификатор объекта, по
которому выполняется регистрация в реестре.  
---|---  
##  __См. также
#### Ссылки
[Tessa.Platform - пространство имён](N_Tessa_Platform.htm)
