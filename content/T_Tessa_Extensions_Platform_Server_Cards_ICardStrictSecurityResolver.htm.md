# ICardStrictSecurityResolver - интерфейс
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.Cards](N_Tessa_Extensions_Platform_Server_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardStrictSecurityResolver : IResolver<string, ICardStrictSecurity>
VB __Копировать
     Public Interface ICardStrictSecurityResolver
    	Inherits IResolver(Of String, ICardStrictSecurity)
C++ __Копировать
     public interface class ICardStrictSecurityResolver : IResolver<String^, ICardStrictSecurity^>
F# __Копировать
     type ICardStrictSecurityResolver = 
        interface
            interface IResolver<string, ICardStrictSecurity>
        end
Implements
    [IResolver](T_Tessa_Platform_IResolver_2.htm)<[String](https://learn.microsoft.com/dotnet/api/system.string), [ICardStrictSecurity](T_Tessa_Extensions_Platform_Server_Cards_ICardStrictSecurity.htm)>
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
[Tessa.Extensions.Platform.Server.Cards - пространство
имён](N_Tessa_Extensions_Platform_Server_Cards.htm)
