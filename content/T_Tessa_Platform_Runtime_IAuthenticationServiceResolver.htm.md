# IAuthenticationServiceResolver - интерфейс
Объект, используемый для запроса сервисов
[IAuthenticationService](T_Tessa_Platform_Runtime_IAuthenticationService.htm),
зарегистрированных по имени значения в
[UserLoginType](T_Tessa_Platform_Runtime_UserLoginType.htm).
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IAuthenticationServiceResolver : IResolver<string, IAuthenticationService>
VB __Копировать
     Public Interface IAuthenticationServiceResolver
    	Inherits IResolver(Of String, IAuthenticationService)
C++ __Копировать
     public interface class IAuthenticationServiceResolver : IResolver<String^, IAuthenticationService^>
F# __Копировать
     type IAuthenticationServiceResolver = 
        interface
            interface IResolver<string, IAuthenticationService>
        end
Implements
    [IResolver](T_Tessa_Platform_IResolver_2.htm)<[String](https://learn.microsoft.com/dotnet/api/system.string), [IAuthenticationService](T_Tessa_Platform_Runtime_IAuthenticationService.htm)>
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
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
