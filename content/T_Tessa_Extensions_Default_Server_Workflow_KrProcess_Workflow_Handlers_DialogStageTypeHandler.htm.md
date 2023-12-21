# DialogStageTypeHandler - класс
Обработчик этапа
[DialogDescriptor](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_StageTypeDescriptors_DialogDescriptor.htm).
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.Handlers](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public class DialogStageTypeHandler : StageTypeHandlerBase
VB __Копировать
     Public Class DialogStageTypeHandler
    	Inherits StageTypeHandlerBase
C++ __Копировать
     public ref class DialogStageTypeHandler : public StageTypeHandlerBase
F# __Копировать
     type DialogStageTypeHandler = 
        class
            inherit StageTypeHandlerBase
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[StageTypeHandlerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase.htm) __ DialogStageTypeHandler
##  __Конструкторы
[DialogStageTypeHandler](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_DialogStageTypeHandler__ctor.htm)|
Инициализирует новый экземпляр класса DialogStageTypeHandler  
---|---  
##  __Свойства
[CardFileManager](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_DialogStageTypeHandler_CardFileManager.htm)|  
---|---  
[CardRepository](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_DialogStageTypeHandler_CardRepository.htm)|  
[CardRepositoryDwt](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_DialogStageTypeHandler_CardRepositoryDwt.htm)|  
[CompilationCache](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_DialogStageTypeHandler_CompilationCache.htm)|  
[CtcBuilderFactory](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_DialogStageTypeHandler_CtcBuilderFactory.htm)|  
[DbScope](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_DialogStageTypeHandler_DbScope.htm)|  
[KrScope](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_DialogStageTypeHandler_KrScope.htm)|  
[ProcessCache](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_DialogStageTypeHandler_ProcessCache.htm)|  
[Session](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_DialogStageTypeHandler_Session.htm)|  
[SignatureProvider](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_DialogStageTypeHandler_SignatureProvider.htm)|  
[TasksRevoker](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_DialogStageTypeHandler_TasksRevoker.htm)|  
[TypesCache](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_DialogStageTypeHandler_TypesCache.htm)|  
[UnityContainer](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_DialogStageTypeHandler_UnityContainer.htm)|  
## __Методы
[AddAliasedDialog](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_DialogStageTypeHandler_AddAliasedDialog.htm)|
Сохраняет идентификатор карточки диалога по его алиасу в персистентном
хранилище параметров процесса
([InfoStorage](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_WorkflowProcess_InfoStorage.htm)).  
---|---  
[AfterPostprocessingAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_DialogStageTypeHandler_AfterPostprocessingAsync.htm)|
Метод, вызываемый после вызова скрипта постобработки этапа.  
(Переопределяет
[StageTypeHandlerBase.AfterPostprocessingAsync(IStageTypeHandlerContext)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase_AfterPostprocessingAsync.htm))  
[BeforeInitializationAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_DialogStageTypeHandler_BeforeInitializationAsync.htm)|
Метод, вызываемый перед вызовом скрипта инициализации этапа.  
(Переопределяет
[StageTypeHandlerBase.BeforeInitializationAsync(IStageTypeHandlerContext)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase_BeforeInitializationAsync.htm))  
[CreateCompletionOptionSettingsAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_DialogStageTypeHandler_CreateCompletionOptionSettingsAsync.htm)|
Создаёт параметры диалога.  
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
[GetAliasedDialogID](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_DialogStageTypeHandler_GetAliasedDialogID.htm)|
Возвращает идентификатор карточки диалога по его алиасу.  
[GetCard](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_DialogStageTypeHandler_GetCard.htm)|
Возвращает стратегию доступа карточки диалога.  
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
[HandleResurrectionAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_DialogStageTypeHandler_HandleResurrectionAsync.htm)|
Обработка восстановления процесса.  
(Переопределяет
[StageTypeHandlerBase.HandleResurrectionAsync(IStageTypeHandlerContext)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase_HandleResurrectionAsync.htm))  
[HandleSignalAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase_HandleSignalAsync.htm)|
Обработка сигнала.  
(Унаследован от
[StageTypeHandlerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase.htm))  
[HandleStageInterruptAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_DialogStageTypeHandler_HandleStageInterruptAsync.htm)|
Обработка отмены этапа. Данный метод должен утилизировать все используемые
этапом ресурсы.  
(Переопределяет
[StageTypeHandlerBase.HandleStageInterruptAsync(IStageTypeHandlerContext)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase_HandleStageInterruptAsync.htm))  
[HandleStageStartAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_DialogStageTypeHandler_HandleStageStartAsync.htm)|
Обработка старта этапа.  
(Переопределяет
[StageTypeHandlerBase.HandleStageStartAsync(IStageTypeHandlerContext)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase_HandleStageStartAsync.htm))  
[HandleTaskCompletionAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_DialogStageTypeHandler_HandleTaskCompletionAsync.htm)|
Обработка завершения задания.  
(Переопределяет
[StageTypeHandlerBase.HandleTaskCompletionAsync(IStageTypeHandlerContext)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase_HandleTaskCompletionAsync.htm))  
[HandleTaskReinstateAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase_HandleTaskReinstateAsync.htm)|
Обработка возврата задания на роль.  
(Унаследован от
[StageTypeHandlerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[StartAsyncDialogAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_DialogStageTypeHandler_StartAsyncDialogAsync.htm)|
Запускает диалог в асинхронном режиме.  
[StartSyncDialogAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_DialogStageTypeHandler_StartSyncDialogAsync.htm)|
Запускает диалог в синхронном режиме.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Поля
[DialogsProcessInfoKey](F_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_DialogStageTypeHandler_DialogsProcessInfoKey.htm)|
Ключ, по которому в
[InfoStorage](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_WorkflowProcess_InfoStorage.htm)
хранится соответствие алиас диалога - идентификатор карточки диалога. Тип
значения: [IDictionary<TKey,
TValue>](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2),
где TKey - [String](https://learn.microsoft.com/dotnet/api/system.string),
TValue - [Object](https://learn.microsoft.com/dotnet/api/system.object).  
---|---  
[SavingMethodDescriptor](F_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_DialogStageTypeHandler_SavingMethodDescriptor.htm)|
Дескриптор метода "Сценарий сохранения".  
[ValidationMethodDescriptor](F_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_DialogStageTypeHandler_ValidationMethodDescriptor.htm)|
Дескриптор метода "Сценарий валидации".  
## __Методы расширения
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
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.Handlers -
пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers.htm)
