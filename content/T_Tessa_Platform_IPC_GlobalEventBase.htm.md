# GlobalEventBase - класс
Базовая реализация интерфейса
[IGlobalEvent](T_Tessa_Platform_IPC_IGlobalEvent.htm).
## __Definition
 **Пространство имён:** [Tessa.Platform.IPC](N_Tessa_Platform_IPC.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class GlobalEventBase : IGlobalEvent, 
    	IAsyncDisposable
VB __Копировать
     Public MustInherit Class GlobalEventBase
    	Implements IGlobalEvent, IAsyncDisposable
C++ __Копировать
     public ref class GlobalEventBase abstract : IGlobalEvent, 
    	IAsyncDisposable
F# __Копировать
     [<AbstractClassAttribute>]
    type GlobalEventBase = 
        class
            interface IGlobalEvent
            interface IAsyncDisposable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ GlobalEventBase
Derived
[Tessa.Platform.IPC.DefaultGlobalEvent](T_Tessa_Platform_IPC_DefaultGlobalEvent.htm)
[Tessa.Platform.IPC.LinuxGlobalEvent](T_Tessa_Platform_IPC_LinuxGlobalEvent.htm)
Implements
    [IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable), [IGlobalEvent](T_Tessa_Platform_IPC_IGlobalEvent.htm)
##  __Конструкторы
[GlobalEventBase](M_Tessa_Platform_IPC_GlobalEventBase__ctor.htm)|
Инициализирует новый экземпляр класса GlobalEventBase  
---|---  
##  __Свойства
[IsDisposed](P_Tessa_Platform_IPC_GlobalEventBase_IsDisposed.htm)| Признак
того, что ресурсы объекта были освобождены.  
---|---  
##  __Методы
[CheckDisposed](M_Tessa_Platform_IPC_GlobalEventBase_CheckDisposed.htm)|
Выбрасывает исключение [ObjectDisposedException], если ресурсы текущего
объекта были освобождены.  
---|---  
[CleanAsync](M_Tessa_Platform_IPC_GlobalEventBase_CleanAsync.htm)|
Освобождает ресурсы события, делая невозможным его дальнейшее использование, и
удаляет связанный с ним файл при его наличии. В реализации по умолчанию
выполняет работу по очистке на Linux и игнорируется на Windows.  
[CleanCoreAsync](M_Tessa_Platform_IPC_GlobalEventBase_CleanCoreAsync.htm)|
Освобождает ресурсы события, делая невозможным его дальнейшее использование, и
удаляет связанный с ним файл при его наличии. В реализации по умолчанию
выполняет работу по очистке на Linux и игнорируется на Windows.  
[CloseFromMainProcessAsync](M_Tessa_Platform_IPC_GlobalEventBase_CloseFromMainProcessAsync.htm)|
Выполняет глобальное закрытие всех ресурсов, связанных с событием. Процессы,
выполняющие ожидание события, могут прекратить ожидание, но на это поведение
нельзя опираться. Рекомендуется не вызывать этот метод, если нельзя определить
текущий процесс как единственный процесс, переводящий событие в сигнальное
состояние. Метод актуален для глобальных событий на Linux.  
[CloseFromMainProcessCoreAsync](M_Tessa_Platform_IPC_GlobalEventBase_CloseFromMainProcessCoreAsync.htm)|
Выполняет глобальное закрытие всех ресурсов, связанных с событием. Процессы,
выполняющие ожидание события, могут прекратить ожидание, но на это поведение
нельзя опираться. Рекомендуется не вызывать этот метод, если нельзя определить
текущий процесс как единственный процесс, переводящий событие в сигнальное
состояние. Метод актуален для глобальных событий на Linux.  
[DisposeAsync()](M_Tessa_Platform_IPC_GlobalEventBase_DisposeAsync.htm)|
Освобождает ресурсы, занимаемые объектом.  
[DisposeAsync(Boolean)](M_Tessa_Platform_IPC_GlobalEventBase_DisposeAsync_1.htm)|
Освобождает ресурсы, занимаемые объектом.  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Reset](M_Tessa_Platform_IPC_GlobalEventBase_Reset.htm)|  Переводит событие в
несигнальное состояние, при этом все ожидающие событие подписчики получают
управление.  
[ResetCore](M_Tessa_Platform_IPC_GlobalEventBase_ResetCore.htm)|  Переводит
событие в несигнальное состояние, при этом все ожидающие событие подписчики
получают управление.  
[Set](M_Tessa_Platform_IPC_GlobalEventBase_Set.htm)|  Переводит событие в
сигнальное состояние, при этом все ожидающие событие подписчики получают
управление.  
[SetCore](M_Tessa_Platform_IPC_GlobalEventBase_SetCore.htm)|  Переводит
событие в сигнальное состояние, при этом все ожидающие событие подписчики
получают управление.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGetWaitHandle](M_Tessa_Platform_IPC_GlobalEventBase_TryGetWaitHandle.htm)|
Возвращает объект WaitHandle для ожидания сигнального состояния у события, или
null, если используемый объект синхронизации не предоставляет объекта
WaitHandle и требуется вызвать метод Wait для ожидания.  
[TryGetWaitHandleCore](M_Tessa_Platform_IPC_GlobalEventBase_TryGetWaitHandleCore.htm)|
Возвращает объект WaitHandle для ожидания сигнального состояния у события, или
null, если используемый объект синхронизации не предоставляет объекта
WaitHandle и требуется вызвать метод Wait для ожидания.  
[WaitAsync](M_Tessa_Platform_IPC_GlobalEventBase_WaitAsync.htm)| Выполняет
ожидание момента, когда событие перейдёт в сигнальное состояние.  
[WaitCoreAsync](M_Tessa_Platform_IPC_GlobalEventBase_WaitCoreAsync.htm)|
Выполняет ожидание момента, когда событие перейдёт в сигнальное состояние.  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform.IPC - пространство имён](N_Tessa_Platform_IPC.htm)
