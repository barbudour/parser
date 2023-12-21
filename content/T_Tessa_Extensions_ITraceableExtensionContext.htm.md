# ITraceableExtensionContext - интерфейс
Контекст расширения, который отслеживается универсальными объектами
[IExtensionTraceListener](T_Tessa_Extensions_IExtensionTraceListener.htm),
доступными в платформе.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ITraceableExtensionContext : IExtensionContext
VB __Копировать
     Public Interface ITraceableExtensionContext
    	Inherits IExtensionContext
C++ __Копировать
     public interface class ITraceableExtensionContext : IExtensionContext
F# __Копировать
     type ITraceableExtensionContext = 
        interface
            interface IExtensionContext
        end
Implements
    [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm)
##  __Свойства
[CancellationToken](P_Tessa_Extensions_IExtensionContext_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
(Унаследован от [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm))  
---|---  
[EnableTracing](P_Tessa_Extensions_ITraceableExtensionContext_EnableTracing.htm)|
Признак того, что для текущего метода расширений разрешена запись сообщения
трассировки при включённой в системе трассировке. Установка значения равным
false позволяет запретить запись сообщения, например, для реализации метода,
которая по умолчанию не выполняет полезной работы. При отключённой сортировке
значение равно false.  
[ValidationResult](P_Tessa_Extensions_ITraceableExtensionContext_ValidationResult.htm)|
Объект, выполняющий построение результата валидации. Может использоваться для
того, чтобы запретить выполнение процесса стандартными средствами.  
## __См. также
#### Ссылки
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
