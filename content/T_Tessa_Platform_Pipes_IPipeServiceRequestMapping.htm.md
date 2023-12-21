# IPipeServiceRequestMapping - интерфейс
Объект, преобразующий параметры запроса, связанные с методом сервиса.
## __Definition
 **Пространство имён:** [Tessa.Platform.Pipes](N_Tessa_Platform_Pipes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IPipeServiceRequestMapping
VB __Копировать
     Public Interface IPipeServiceRequestMapping
C++ __Копировать
     public interface class IPipeServiceRequestMapping
F# __Копировать
     type IPipeServiceRequestMapping = interface end
##  __Методы
[CoerceMethodName](M_Tessa_Platform_Pipes_IPipeServiceRequestMapping_CoerceMethodName.htm)|
Корректирует имя передаваемого метода. В реализации по умолчанию удаляет
суффикс Async.  
---|---  
[GetServiceTypeName](M_Tessa_Platform_Pipes_IPipeServiceRequestMapping_GetServiceTypeName.htm)|
Возвращает имя сервиса по его типу. По умолчанию возвращается полное имя без
учёта сборки
[FullName](https://learn.microsoft.com/dotnet/api/system.type.fullname#system-
type-fullname).  
## __См. также
#### Ссылки
[Tessa.Platform.Pipes - пространство имён](N_Tessa_Platform_Pipes.htm)
