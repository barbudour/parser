# INotificationRecipientsSourceResolver - интерфейс
Объект для получения источника получателей уведомления по параметру.
## __Definition
 **Пространство имён:** [Tessa.Notices.Sources](N_Tessa_Notices_Sources.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface INotificationRecipientsSourceResolver : IResolver<Type, INotificationRecipientsSource>
VB __Копировать
     Public Interface INotificationRecipientsSourceResolver
    	Inherits IResolver(Of Type, INotificationRecipientsSource)
C++ __Копировать
     public interface class INotificationRecipientsSourceResolver : IResolver<Type^, INotificationRecipientsSource^>
F# __Копировать
     type INotificationRecipientsSourceResolver = 
        interface
            interface IResolver<Type, INotificationRecipientsSource>
        end
Implements
    [IResolver](T_Tessa_Platform_IResolver_2.htm)<[Type](https://learn.microsoft.com/dotnet/api/system.type), [INotificationRecipientsSource](T_Tessa_Notices_Sources_INotificationRecipientsSource.htm)>
##  __Методы
[Clear](M_Tessa_Platform_IResolver_2_Clear.htm)| Удаляет информацию по всем
выполненным регистрациям.  
(Унаследован от [IResolver<TKey, TValue>](T_Tessa_Platform_IResolver_2.htm))  
---|---  
[GetAllKeys](M_Tessa_Platform_IResolver_2_GetAllKeys.htm)| Возвращает список
всех зарегистрированных ключей.  
(Унаследован от [IResolver<TKey, TValue>](T_Tessa_Platform_IResolver_2.htm))  
[GetSource](M_Tessa_Notices_Sources_INotificationRecipientsSourceResolver_GetSource.htm)|
Метод для получения источника получателей уведомления по переданному
параметру.  
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
TSource>](M_Tessa_Notices_Sources_INotificationRecipientsSourceResolver_RegisterParameter__2.htm)|
Метод для регистрации источника для получения шаблонов уведомлений для типа
параметра.  
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
