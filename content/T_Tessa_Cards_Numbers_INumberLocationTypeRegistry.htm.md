# INumberLocationTypeRegistry - интерфейс
Реестр типов местоположений номеров
[NumberLocationType](T_Tessa_Cards_Numbers_NumberLocationType.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface INumberLocationTypeRegistry : IRegistry<Guid, NumberLocationType>
VB __Копировать
     Public Interface INumberLocationTypeRegistry
    	Inherits IRegistry(Of Guid, NumberLocationType)
C++ __Копировать
     public interface class INumberLocationTypeRegistry : IRegistry<Guid, NumberLocationType^>
F# __Копировать
     type INumberLocationTypeRegistry = 
        interface
            interface IRegistry<Guid, NumberLocationType>
        end
Implements
    [IRegistry](T_Tessa_Platform_IRegistry_2.htm)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid), [NumberLocationType](T_Tessa_Cards_Numbers_NumberLocationType.htm)>
##  __Методы
[Get](M_Tessa_Platform_IRegistry_2_Get.htm)| Возвращает объект,
зарегистрированный в реестре по заданному идентификатору.  
(Унаследован от [IRegistry<TIdentifier,
TItem>](T_Tessa_Platform_IRegistry_2.htm))  
---|---  
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
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
