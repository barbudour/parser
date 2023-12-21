# IConditionSourceHandlerResolver - интерфейс
Резолвер обработчиков источников данных условий, возвращающий обработчики по
идентификатору типа карточки.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Conditions](N_Tessa_Platform_Conditions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IConditionSourceHandlerResolver : IResolver<Guid, IConditionSourceHandler>
VB __Копировать
     Public Interface IConditionSourceHandlerResolver
    	Inherits IResolver(Of Guid, IConditionSourceHandler)
C++ __Копировать
     public interface class IConditionSourceHandlerResolver : IResolver<Guid, IConditionSourceHandler^>
F# __Копировать
     type IConditionSourceHandlerResolver = 
        interface
            interface IResolver<Guid, IConditionSourceHandler>
        end
Implements
    [IResolver](T_Tessa_Platform_IResolver_2.htm)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid), [IConditionSourceHandler](T_Tessa_Platform_Conditions_IConditionSourceHandler.htm)>
##  __Методы
[Clear](M_Tessa_Platform_IResolver_2_Clear.htm)| Удаляет информацию по всем
выполненным регистрациям.  
(Унаследован от [IResolver<TKey, TValue>](T_Tessa_Platform_IResolver_2.htm))  
---|---  
[GetAllKeys](M_Tessa_Platform_IResolver_2_GetAllKeys.htm)| Возвращает список
всех зарегистрированных ключей.  
(Унаследован от [IResolver<TKey, TValue>](T_Tessa_Platform_IResolver_2.htm))  
[Register(Type, TKey)](M_Tessa_Platform_IResolver_2_Register.htm)|
Регистрирует тип объекта по заданному ключу. Резолв возможен только для
зарегистрированных типов. Обычно резолв сервиса выполняется из контейнера
Unity каждый раз при вызове этого метода, при этом объект запрашивается по
зарегистрированному типу (классу) без имени в контейнере.  
(Унаследован от [IResolver<TKey, TValue>](T_Tessa_Platform_IResolver_2.htm))  
[Register<TConcrete>(TKey)](M_Tessa_Platform_IResolver_2_Register__1.htm)|
Регистрирует тип объекта по заданному ключу. Резолв возможен только для
зарегистрированных типов. Обычно резолв сервиса выполняется из контейнера
Unity каждый раз при вызове этого метода, при этом объект запрашивается по
зарегистрированному типу (классу) без имени в контейнере.  
(Унаследован от [IResolver<TKey, TValue>](T_Tessa_Platform_IResolver_2.htm))  
[Remove](M_Tessa_Platform_IResolver_2_Remove.htm)| Удаляет информацию по
регистрации с заданным ключом.  
(Унаследован от [IResolver<TKey, TValue>](T_Tessa_Platform_IResolver_2.htm))  
[Resolve](M_Tessa_Platform_IResolver_2_Resolve.htm)|  Выполняет резолв
экземпляра заданного сервиса по заданному ключу. Если сервис не был
зарегистрирован, то выбрасывается исключение
[Unity.ResolutionFailedException]. Обычно резолв сервиса выполняется из
контейнера Unity каждый раз при вызове этого метода, при этом объект
запрашивается по зарегистрированному типу (классу) без имени в контейнере.  
(Унаследован от [IResolver<TKey, TValue>](T_Tessa_Platform_IResolver_2.htm))  
[TryResolve](M_Tessa_Platform_IResolver_2_TryResolve.htm)|  Выполняет резолв
экземпляра заданного сервиса по имени. Если сервис не был зарегистрирован, то
возвращает null. Обычно резолв сервиса выполняется из контейнера Unity каждый
раз при вызове этого метода, при этом объект запрашивается по
зарегистрированному типу (классу) без имени в контейнере.  
(Унаследован от [IResolver<TKey, TValue>](T_Tessa_Platform_IResolver_2.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform.Conditions - пространство
имён](N_Tessa_Platform_Conditions.htm)
