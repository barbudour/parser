# IActionTypeRegistry - интерфейс
Реестр типов действий в истории
[ActionType](T_Tessa_Platform_Runtime_ActionType.htm).
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IActionTypeRegistry : IRegistry<int, ActionType>
VB __Копировать
     Public Interface IActionTypeRegistry
    	Inherits IRegistry(Of Integer, ActionType)
C++ __Копировать
     public interface class IActionTypeRegistry : IRegistry<int, ActionType^>
F# __Копировать
     type IActionTypeRegistry = 
        interface
            interface IRegistry<int, ActionType>
        end
Implements
    [IRegistry](T_Tessa_Platform_IRegistry_2.htm)<[Int32](https://learn.microsoft.com/dotnet/api/system.int32), [ActionType](T_Tessa_Platform_Runtime_ActionType.htm)>
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
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
