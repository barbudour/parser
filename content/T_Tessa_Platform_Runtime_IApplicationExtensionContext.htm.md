# IApplicationExtensionContext - интерфейс
Контекст расширений, связанных с жизненным циклом приложения.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IApplicationExtensionContext : IApplicationExtensionContextBase, 
    	ITraceableExtensionContext, IExtensionContext
VB __Копировать
     Public Interface IApplicationExtensionContext
    	Inherits IApplicationExtensionContextBase, ITraceableExtensionContext, IExtensionContext
C++ __Копировать
     public interface class IApplicationExtensionContext : IApplicationExtensionContextBase, 
    	ITraceableExtensionContext, IExtensionContext
F# __Копировать
     type IApplicationExtensionContext = 
        interface
            interface IApplicationExtensionContextBase
            interface ITraceableExtensionContext
            interface IExtensionContext
        end
Implements
    [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm), [ITraceableExtensionContext](T_Tessa_Extensions_ITraceableExtensionContext.htm), [IApplicationExtensionContextBase](T_Tessa_Platform_Runtime_IApplicationExtensionContextBase.htm)
##  __Свойства
[ApplicationClosingAfterCheck](P_Tessa_Platform_Runtime_IApplicationExtensionContext_ApplicationClosingAfterCheck.htm)|
Событие по закрытию окна приложения, выполняемое после того, как пользователь
был проинформирован о необходимости сохранить изменения во вкладках и
подтвердил закрытие, несмотря на это. Если обработчики события
[IApplicationExtensionContext.ClosingBeforeCheck] уже отменили закрытие,
установив e.Cancel = true, или обработчики вызвали исключение, то это событие
не будет вызвано, а закрытие будет отменено. Если пользователь подтвердил
закрытие или обработчики события
[IApplicationExtensionContext.ClosingBeforeCheck] установили e.ForceClosing =
true, то это событие будет вызвано, но в этом случае будет установлено
e.Cancel = true в аргументах события. В платформе по умолчанию событие
вызывается только в приложении TessaClient.  
---|---  
[ApplicationClosingBeforeCheck](P_Tessa_Platform_Runtime_IApplicationExtensionContext_ApplicationClosingBeforeCheck.htm)|
Событие по закрытию окна приложения, выполняемое до того, как будут сделаны
проверки по умолчанию, и пользователь будет проинформирован о необходимости
сохранить изменения во вкладках. В платформе по умолчанию событие вызывается
только в приложении TessaClient.  
[ApplicationID](P_Tessa_Platform_Runtime_IApplicationExtensionContextBase_ApplicationID.htm)|
Идентификатор приложения, для которого выполняются расширения. Стандартные
идентификаторы приложений указаны в полях класса
[Tessa.Platform.Runtime.ApplicationIdentifiers].  
(Унаследован от
[IApplicationExtensionContextBase](T_Tessa_Platform_Runtime_IApplicationExtensionContextBase.htm))  
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
(Унаследован от
[IApplicationExtensionContextBase](T_Tessa_Platform_Runtime_IApplicationExtensionContextBase.htm))  
[Session](P_Tessa_Platform_Runtime_IApplicationExtensionContextBase_Session.htm)|
Сессия текущего пользователя.  
(Унаследован от
[IApplicationExtensionContextBase](T_Tessa_Platform_Runtime_IApplicationExtensionContextBase.htm))  
[ValidationResult](P_Tessa_Extensions_ITraceableExtensionContext_ValidationResult.htm)|
Объект, выполняющий построение результата валидации. Может использоваться для
того, чтобы запретить выполнение процесса стандартными средствами.  
(Унаследован от
[ITraceableExtensionContext](T_Tessa_Extensions_ITraceableExtensionContext.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
