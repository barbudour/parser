# INotificationEmailSourceResolver - интерфейс
Объект для получения источника шаблонов уведомлений по параметру уведомления.
## __Definition
 **Пространство имён:** [Tessa.Notices.Sources](N_Tessa_Notices_Sources.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface INotificationEmailSourceResolver : IResolver<Type, INotificationEmailSource>
VB __Копировать
     Public Interface INotificationEmailSourceResolver
    	Inherits IResolver(Of Type, INotificationEmailSource)
C++ __Копировать
     public interface class INotificationEmailSourceResolver : IResolver<Type^, INotificationEmailSource^>
F# __Копировать
     type INotificationEmailSourceResolver = 
        interface
            interface IResolver<Type, INotificationEmailSource>
        end
Implements
    [IResolver](T_Tessa_Platform_IResolver_2.htm)<[Type](https://learn.microsoft.com/dotnet/api/system.type), [INotificationEmailSource](T_Tessa_Notices_Sources_INotificationEmailSource.htm)>
##  __Методы
[Clear](M_Tessa_Platform_IResolver_2_Clear.htm)| Удаляет информацию по всем
выполненным регистрациям.  
(Унаследован от [IResolver<TKey, TValue>](T_Tessa_Platform_IResolver_2.htm))  
---|---  
[GetAllKeys](M_Tessa_Platform_IResolver_2_GetAllKeys.htm)| Возвращает список
всех зарегистрированных ключей.  
(Унаследован от [IResolver<TKey, TValue>](T_Tessa_Platform_IResolver_2.htm))  
[GetSource](M_Tessa_Notices_Sources_INotificationEmailSourceResolver_GetSource.htm)|
Метод для получения источника шаблонов уведомлений по переданному параметру
уведомления.  
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
[RegisterParameter<TParam,
TSource>](M_Tessa_Notices_Sources_INotificationEmailSourceResolver_RegisterParameter__2.htm)|
Метод для регистрации источника для получения шаблонов уведомлений для типа
параметров уведомления.  
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
[Tessa.Notices.Sources - пространство имён](N_Tessa_Notices_Sources.htm)
