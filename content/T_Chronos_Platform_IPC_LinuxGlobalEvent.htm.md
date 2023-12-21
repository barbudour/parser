# LinuxGlobalEvent - класс
Событие с глобально уникальным именем, используемое для синхронизации между
процессами в Linux.
## __Definition
 **Пространство имён:** [Chronos.Platform.IPC](N_Chronos_Platform_IPC.htm)  
 **Сборка:** Chronos.Platform.Linux (в Chronos.Platform.Linux.dll) Версия:
3.6.0.17
C# __Копировать
     public class LinuxGlobalEvent : GlobalEventBase
VB __Копировать
     Public Class LinuxGlobalEvent
    	Inherits GlobalEventBase
C++ __Копировать
     public ref class LinuxGlobalEvent : public GlobalEventBase
F# __Копировать
     type LinuxGlobalEvent = 
        class
            inherit GlobalEventBase
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[GlobalEventBase](T_Chronos_Platform_IPC_GlobalEventBase.htm) __ LinuxGlobalEvent
##  __Конструкторы
[LinuxGlobalEvent](M_Chronos_Platform_IPC_LinuxGlobalEvent__ctor.htm)|
Создаёт экземпляр класса с указанием его параметров.  
---|---  
## __Свойства
[EventFileName](P_Chronos_Platform_IPC_LinuxGlobalEvent_EventFileName.htm)|
Имя файла, используемое для генерации события.  
---|---  
[EventFilePath](P_Chronos_Platform_IPC_LinuxGlobalEvent_EventFilePath.htm)|
Полный путь к файлу, используемому для генерации события.  
[EventFolderPath](P_Chronos_Platform_IPC_LinuxGlobalEvent_EventFolderPath.htm)|
Полный путь к папке с файлами событий
[EventFilePath](P_Chronos_Platform_IPC_LinuxGlobalEvent_EventFilePath.htm).  
[IsDisposed](P_Chronos_Platform_IPC_GlobalEventBase_IsDisposed.htm)| Признак
того, что ресурсы объекта были освобождены.  
(Унаследован от [GlobalEventBase](T_Chronos_Platform_IPC_GlobalEventBase.htm))  
##  __Методы
[CheckDisposed](M_Chronos_Platform_IPC_GlobalEventBase_CheckDisposed.htm)|
Выбрасывает исключение [ObjectDisposedException], если ресурсы текущего
объекта были освобождены.  
(Унаследован от [GlobalEventBase](T_Chronos_Platform_IPC_GlobalEventBase.htm))  
---|---  
[CleanAsync](M_Chronos_Platform_IPC_GlobalEventBase_CleanAsync.htm)|
Освобождает ресурсы события, делая невозможным его дальнейшее использование, и
удаляет связанный с ним файл при его наличии. В реализации по умолчанию
выполняет работу по очистке на Linux и игнорируется на Windows.  
(Унаследован от [GlobalEventBase](T_Chronos_Platform_IPC_GlobalEventBase.htm))  
[CleanCoreAsync](M_Chronos_Platform_IPC_LinuxGlobalEvent_CleanCoreAsync.htm)|
Освобождает ресурсы события, делая невозможным его дальнейшее использование, и
удаляет связанный с ним файл при его наличии. В реализации по умолчанию
выполняет работу по очистке на Linux и игнорируется на Windows.  
(Переопределяет
[GlobalEventBase.CleanCoreAsync(CancellationToken)](M_Chronos_Platform_IPC_GlobalEventBase_CleanCoreAsync.htm))  
[CloseFromMainProcessAsync](M_Chronos_Platform_IPC_GlobalEventBase_CloseFromMainProcessAsync.htm)|
Выполняет глобальное закрытие всех ресурсов, связанных с событием. Процессы,
выполняющие ожидание события, могут прекратить ожидание, но на это поведение
нельзя опираться. Рекомендуется не вызывать этот метод, если нельзя определить
текущий процесс как единственный процесс, переводящий событие в сигнальное
состояние. Метод актуален для глобальных событий на Linux.  
(Унаследован от [GlobalEventBase](T_Chronos_Platform_IPC_GlobalEventBase.htm))  
[CloseFromMainProcessCoreAsync](M_Chronos_Platform_IPC_LinuxGlobalEvent_CloseFromMainProcessCoreAsync.htm)|
Выполняет глобальное закрытие всех ресурсов, связанных с событием. Процессы,
выполняющие ожидание события, могут прекратить ожидание, но на это поведение
нельзя опираться. Рекомендуется не вызывать этот метод, если нельзя определить
текущий процесс как единственный процесс, переводящий событие в сигнальное
состояние. Метод актуален для глобальных событий на Linux.  
(Переопределяет
[GlobalEventBase.CloseFromMainProcessCoreAsync(CancellationToken)](M_Chronos_Platform_IPC_GlobalEventBase_CloseFromMainProcessCoreAsync.htm))  
[DisposeAsync()](M_Chronos_Platform_IPC_GlobalEventBase_DisposeAsync.htm)|
Освобождает ресурсы, занимаемые объектом.  
(Унаследован от [GlobalEventBase](T_Chronos_Platform_IPC_GlobalEventBase.htm))  
[DisposeAsync(Boolean)](M_Chronos_Platform_IPC_LinuxGlobalEvent_DisposeAsync.htm)|
Освобождает ресурсы, занимаемые объектом.  
(Переопределяет
[GlobalEventBase.DisposeAsync(Boolean)](M_Chronos_Platform_IPC_GlobalEventBase_DisposeAsync_1.htm))  
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
[Reset](M_Chronos_Platform_IPC_GlobalEventBase_Reset.htm)|  Переводит событие
в несигнальное состояние, при этом все ожидающие событие подписчики получают
управление.  
(Унаследован от [GlobalEventBase](T_Chronos_Platform_IPC_GlobalEventBase.htm))  
[ResetCore](M_Chronos_Platform_IPC_LinuxGlobalEvent_ResetCore.htm)|  Переводит
событие в несигнальное состояние, при этом все ожидающие событие подписчики
получают управление.  
(Переопределяет
[GlobalEventBase.ResetCore()](M_Chronos_Platform_IPC_GlobalEventBase_ResetCore.htm))  
[Set](M_Chronos_Platform_IPC_GlobalEventBase_Set.htm)|  Переводит событие в
сигнальное состояние, при этом все ожидающие событие подписчики получают
управление.  
(Унаследован от [GlobalEventBase](T_Chronos_Platform_IPC_GlobalEventBase.htm))  
[SetCore](M_Chronos_Platform_IPC_LinuxGlobalEvent_SetCore.htm)|  Переводит
событие в сигнальное состояние, при этом все ожидающие событие подписчики
получают управление.  
(Переопределяет
[GlobalEventBase.SetCore()](M_Chronos_Platform_IPC_GlobalEventBase_SetCore.htm))  
[ToString](M_Chronos_Platform_IPC_LinuxGlobalEvent_ToString.htm)|  
(Переопределяет
[Object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring))  
[TryGetWaitHandle](M_Chronos_Platform_IPC_GlobalEventBase_TryGetWaitHandle.htm)|
Возвращает объект WaitHandle для ожидания сигнального состояния у события, или
null, если используемый объект синхронизации не предоставляет объекта
WaitHandle и требуется вызвать метод Wait для ожидания.  
(Унаследован от [GlobalEventBase](T_Chronos_Platform_IPC_GlobalEventBase.htm))  
[TryGetWaitHandleCore](M_Chronos_Platform_IPC_GlobalEventBase_TryGetWaitHandleCore.htm)|
Возвращает объект WaitHandle для ожидания сигнального состояния у события, или
null, если используемый объект синхронизации не предоставляет объекта
WaitHandle и требуется вызвать метод Wait для ожидания.  
(Унаследован от [GlobalEventBase](T_Chronos_Platform_IPC_GlobalEventBase.htm))  
[WaitAsync](M_Chronos_Platform_IPC_GlobalEventBase_WaitAsync.htm)| Выполняет
ожидание момента, когда событие перейдёт в сигнальное состояние.  
(Унаследован от [GlobalEventBase](T_Chronos_Platform_IPC_GlobalEventBase.htm))  
[WaitCoreAsync](M_Chronos_Platform_IPC_LinuxGlobalEvent_WaitCoreAsync.htm)|
Выполняет ожидание момента, когда событие перейдёт в сигнальное состояние.  
(Переопределяет
[GlobalEventBase.WaitCoreAsync(CancellationToken)](M_Chronos_Platform_IPC_GlobalEventBase_WaitCoreAsync.htm))  
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
[Chronos.Platform.IPC - пространство имён](N_Chronos_Platform_IPC.htm)
