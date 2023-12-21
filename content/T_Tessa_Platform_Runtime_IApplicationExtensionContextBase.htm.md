# IApplicationExtensionContextBase - интерфейс
Базовый интерфейс для событий, связанных с приложением, таких как
открытие/закрытие приложения и его инициализация.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IApplicationExtensionContextBase : ITraceableExtensionContext, 
    	IExtensionContext
VB __Копировать
     Public Interface IApplicationExtensionContextBase
    	Inherits ITraceableExtensionContext, IExtensionContext
C++ __Копировать
     public interface class IApplicationExtensionContextBase : ITraceableExtensionContext, 
    	IExtensionContext
F# __Копировать
     type IApplicationExtensionContextBase = 
        interface
            interface ITraceableExtensionContext
            interface IExtensionContext
        end
Implements
    [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm), [ITraceableExtensionContext](T_Tessa_Extensions_ITraceableExtensionContext.htm)
##  __Свойства
[ApplicationID](P_Tessa_Platform_Runtime_IApplicationExtensionContextBase_ApplicationID.htm)|
Идентификатор приложения, для которого выполняются расширения. Стандартные
идентификаторы приложений указаны в полях класса
[Tessa.Platform.Runtime.ApplicationIdentifiers].  
---|---  
[CancellationToken](P_Tessa_Extensions_IExtensionContext_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
(Унаследован от [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm))  
[EnableTracing](P_Tessa_Extensions_ITraceableExtensionContext_EnableTracing.htm)|
Признак того, что для текущего метода расширений разрешена запись сообщения
трассировки при включённой в системе трассировке. Установка значения равным
false позволяет запретить запись сообщения, например, для реализации метода,
которая по умолчанию не выполняет полезной работы. При отключённой сортировке
значение равно false.  
(Унаследован от
[ITraceableExtensionContext](T_Tessa_Extensions_ITraceableExtensionContext.htm))  
[Info](P_Tessa_Platform_Runtime_IApplicationExtensionContextBase_Info.htm)|
Дополнительная информация, связанная с контекстом расширений.  
[Session](P_Tessa_Platform_Runtime_IApplicationExtensionContextBase_Session.htm)|
Сессия текущего пользователя.  
[ValidationResult](P_Tessa_Extensions_ITraceableExtensionContext_ValidationResult.htm)|
Объект, выполняющий построение результата валидации. Может использоваться для
того, чтобы запретить выполнение процесса стандартными средствами.  
(Унаследован от
[ITraceableExtensionContext](T_Tessa_Extensions_ITraceableExtensionContext.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
