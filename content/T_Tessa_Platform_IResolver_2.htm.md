# IResolver<TKey, TValue> \- интерфейс
Объект, используемый для запросов типов сервисов по ключу, например, по имени.
## __Definition
 **Пространство имён:** [Tessa.Platform](N_Tessa_Platform.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IResolver<TKey, TValue>
    where TValue : class
VB __Копировать
     Public Interface IResolver(Of TKey, TValue As Class)
C++ __Копировать
    generic<typename TKey, typename TValue>
    where TValue : ref class
    public interface class IResolver
F# __Копировать
     type IResolver<'TKey, 'TValue when 'TValue : not struct> = interface end
#### Параметры типа
TKey
    Ключ для запроса значения.
TValue
    Интерфейс запрашиваемого сервиса. Должен быть ссылочным типом.
##  __Методы
[Clear](M_Tessa_Platform_IResolver_2_Clear.htm)| Удаляет информацию по всем
выполненным регистрациям.  
---|---  
[GetAllKeys](M_Tessa_Platform_IResolver_2_GetAllKeys.htm)| Возвращает список
всех зарегистрированных ключей.  
[Register(Type, TKey)](M_Tessa_Platform_IResolver_2_Register.htm)|
Регистрирует тип объекта по заданному ключу. Резолв возможен только для
зарегистрированных типов. Обычно резолв сервиса выполняется из контейнера
Unity каждый раз при вызове этого метода, при этом объект запрашивается по
зарегистрированному типу (классу) без имени в контейнере.  
[Register<TConcrete>(TKey)](M_Tessa_Platform_IResolver_2_Register__1.htm)|
Регистрирует тип объекта по заданному ключу. Резолв возможен только для
зарегистрированных типов. Обычно резолв сервиса выполняется из контейнера
Unity каждый раз при вызове этого метода, при этом объект запрашивается по
зарегистрированному типу (классу) без имени в контейнере.  
[Remove](M_Tessa_Platform_IResolver_2_Remove.htm)| Удаляет информацию по
регистрации с заданным ключом.  
[Resolve](M_Tessa_Platform_IResolver_2_Resolve.htm)|  Выполняет резолв
экземпляра заданного сервиса по заданному ключу. Если сервис не был
зарегистрирован, то выбрасывается исключение
[Unity.ResolutionFailedException]. Обычно резолв сервиса выполняется из
контейнера Unity каждый раз при вызове этого метода, при этом объект
запрашивается по зарегистрированному типу (классу) без имени в контейнере.  
[TryResolve](M_Tessa_Platform_IResolver_2_TryResolve.htm)|  Выполняет резолв
экземпляра заданного сервиса по имени. Если сервис не был зарегистрирован, то
возвращает null. Обычно резолв сервиса выполняется из контейнера Unity каждый
раз при вызове этого метода, при этом объект запрашивается по
зарегистрированному типу (классу) без имени в контейнере.  
## __См. также
#### Ссылки
[Tessa.Platform - пространство имён](N_Tessa_Platform.htm)
