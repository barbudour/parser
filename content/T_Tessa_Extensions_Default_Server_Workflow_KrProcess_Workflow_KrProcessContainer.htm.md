# KrProcessContainer - класс
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class KrProcessContainer : IKrProcessContainer, 
    	IDisposable
VB __Копировать
     Public NotInheritable Class KrProcessContainer
    	Implements IKrProcessContainer, IDisposable
C++ __Копировать
     public ref class KrProcessContainer sealed : IKrProcessContainer, 
    	IDisposable
F# __Копировать
     [<SealedAttribute>]
    type KrProcessContainer = 
        class
            interface IKrProcessContainer
            interface IDisposable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ KrProcessContainer
Implements
    [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable), [IKrProcessContainer](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrProcessContainer.htm)
##  __Конструкторы
[KrProcessContainer](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessContainer__ctor.htm)|
Инициализирует новый экземпляр класса KrProcessContainer  
---|---  
##  __Методы
[AddFilter<T>](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessContainer_AddFilter__1.htm)|
Добавляет указанный фильтр.  
---|---  
[Dispose](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessContainer_Dispose.htm)|
Performs application-defined tasks associated with freeing, releasing, or
resetting unmanaged resources.  
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
[GetHandlerDescriptor](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessContainer_GetHandlerDescriptor.htm)|
Возвращает зарегистрированный дескриптор типа этапа.  
[GetHandlerDescriptors](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessContainer_GetHandlerDescriptors.htm)|
Возвращает коллекцию зарегистрированных дескрипторов обработчиков типов
этапов.  
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
[IsTaskTypeRegisteredAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessContainer_IsTaskTypeRegisteredAsync.htm)|
Возвращает значение, показывающее, что указанный тип задания зарегистрирован
для использования в подсистеме маршрутов.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[RegisterGlobalSignal(String,
Type)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessContainer_RegisterGlobalSignal.htm)|
Регистрирует тип обработчика глобального сигнала.  
[RegisterGlobalSignal<T>(String)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessContainer_RegisterGlobalSignal__1.htm)|
Регистрирует тип обработчика глобального сигнала.  
[RegisterHandler(StageTypeDescriptor,
Type)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessContainer_RegisterHandler.htm)|
Регистрирует обработчик типа этапа по дескриптору.  
[RegisterHandler<T>(StageTypeDescriptor)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessContainer_RegisterHandler__1.htm)|
Регистрирует обработчик типа этапа по дескриптору.  
[RegisterTaskType(Guid)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessContainer_RegisterTaskType_1.htm)|
Регистрирует тип задания для обработки его в подсистеме маршрутов.  
[RegisterTaskType(IEnumerable<Guid>)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessContainer_RegisterTaskType.htm)|
Регистрирует указанное пересчисление типов заданий для их обработки в
подсистеме маршрутов.  
[ResetExtraTaskTypes](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessContainer_ResetExtraTaskTypes.htm)|
Сбрасывает типы заданий, загруженные из настроек типового решения.  
[ResolveHandler](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessContainer_ResolveHandler.htm)|
Возвращает обработчик типа этапа по его дескриптору.  
[ResolveSignal](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessContainer_ResolveSignal.htm)|
Возвращает обработчик типа сигнала по заданному типу.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
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
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow.htm)
