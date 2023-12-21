# IKrProcessContainer - интерфейс
Описывает объект содержащий информацию о обработчиках используемых в
подсистеме маршрутов.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IKrProcessContainer
VB __Копировать
     Public Interface IKrProcessContainer
C++ __Копировать
     public interface class IKrProcessContainer
F# __Копировать
     type IKrProcessContainer = interface end
##  __Методы
[AddFilter<T>](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrProcessContainer_AddFilter__1.htm)|
Добавляет указанный фильтр.  
---|---  
[GetHandlerDescriptor](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrProcessContainer_GetHandlerDescriptor.htm)|
Возвращает зарегистрированный дескриптор типа этапа.  
[GetHandlerDescriptors](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrProcessContainer_GetHandlerDescriptors.htm)|
Возвращает коллекцию зарегистрированных дескрипторов обработчиков типов
этапов.  
[IsTaskTypeRegisteredAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrProcessContainer_IsTaskTypeRegisteredAsync.htm)|
Возвращает значение, показывающее, что указанный тип задания зарегистрирован
для использования в подсистеме маршрутов.  
[RegisterGlobalSignal(String,
Type)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrProcessContainer_RegisterGlobalSignal.htm)|
Регистрирует тип обработчика глобального сигнала.  
[RegisterGlobalSignal<T>(String)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrProcessContainer_RegisterGlobalSignal__1.htm)|
Регистрирует тип обработчика глобального сигнала.  
[RegisterHandler(StageTypeDescriptor,
Type)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrProcessContainer_RegisterHandler.htm)|
Регистрирует обработчик типа этапа по дескриптору.  
[RegisterHandler<T>(StageTypeDescriptor)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrProcessContainer_RegisterHandler__1.htm)|
Регистрирует обработчик типа этапа по дескриптору.  
[RegisterTaskType(Guid)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrProcessContainer_RegisterTaskType_1.htm)|
Регистрирует тип задания для обработки его в подсистеме маршрутов.  
[RegisterTaskType(IEnumerable<Guid>)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrProcessContainer_RegisterTaskType.htm)|
Регистрирует указанное пересчисление типов заданий для их обработки в
подсистеме маршрутов.  
[ResetExtraTaskTypes](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrProcessContainer_ResetExtraTaskTypes.htm)|
Сбрасывает типы заданий, загруженные из настроек типового решения.  
[ResolveHandler](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrProcessContainer_ResolveHandler.htm)|
Возвращает обработчик типа этапа по его дескриптору.  
[ResolveSignal](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrProcessContainer_ResolveSignal.htm)|
Возвращает обработчик типа сигнала по заданному типу.  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow.htm)
