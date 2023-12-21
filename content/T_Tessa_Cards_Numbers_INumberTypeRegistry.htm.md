# INumberTypeRegistry - интерфейс
Реестр типов номеров [NumberType](T_Tessa_Cards_Numbers_NumberType.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface INumberTypeRegistry : INamedRegistry<NumberType>, 
    	IRegistry<Guid, NumberType>
VB __Копировать
     Public Interface INumberTypeRegistry
    	Inherits INamedRegistry(Of NumberType), IRegistry(Of Guid, NumberType)
C++ __Копировать
     public interface class INumberTypeRegistry : INamedRegistry<NumberType^>, 
    	IRegistry<Guid, NumberType^>
F# __Копировать
     type INumberTypeRegistry = 
        interface
            interface INamedRegistry<NumberType>
            interface IRegistry<Guid, NumberType>
        end
Implements
    [INamedRegistry](T_Tessa_Platform_INamedRegistry_1.htm)<[NumberType](T_Tessa_Cards_Numbers_NumberType.htm)>, [IRegistry](T_Tessa_Platform_IRegistry_2.htm)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid), [NumberType](T_Tessa_Cards_Numbers_NumberType.htm)>
##  __Методы
[Get(TIdentifier)](M_Tessa_Platform_IRegistry_2_Get.htm)| Возвращает объект,
зарегистрированный в реестре по заданному идентификатору.  
(Унаследован от [IRegistry<TIdentifier,
TItem>](T_Tessa_Platform_IRegistry_2.htm))  
---|---  
[Get(String)](M_Tessa_Platform_INamedRegistry_1_Get.htm)| Возвращает объект,
зарегистрированный в реестре по заданному имени.  
(Унаследован от
[INamedRegistry<TItem>](T_Tessa_Platform_INamedRegistry_1.htm))  
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
(Унаследован от
[INamedRegistry<TItem>](T_Tessa_Platform_INamedRegistry_1.htm))  
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
