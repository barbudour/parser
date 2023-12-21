# DeregistrationStageTypeHandler - класс
Обработчик этапа
[DeregistrationDescriptor](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_StageTypeDescriptors_DeregistrationDescriptor.htm).
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.Handlers](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public class DeregistrationStageTypeHandler : StageTypeHandlerBase
VB __Копировать
     Public Class DeregistrationStageTypeHandler
    	Inherits StageTypeHandlerBase
C++ __Копировать
     public ref class DeregistrationStageTypeHandler : public StageTypeHandlerBase
F# __Копировать
     type DeregistrationStageTypeHandler = 
        class
            inherit StageTypeHandlerBase
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[StageTypeHandlerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase.htm) __ DeregistrationStageTypeHandler
##  __Конструкторы
[DeregistrationStageTypeHandler](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_DeregistrationStageTypeHandler__ctor.htm)|
Инициализирует новый экземпляр класса DeregistrationStageTypeHandler.  
---|---  
## __Свойства
[CalendarService](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_DeregistrationStageTypeHandler_CalendarService.htm)|
Возвращает или задаёт интерфейс API бизнес календаря.  
---|---  
[CardMetadata](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_DeregistrationStageTypeHandler_CardMetadata.htm)|
Возвращает или задаёт метаинформацию, необходимую для использования типов
карточек совместно с пакетом карточек.  
[EventManager](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_DeregistrationStageTypeHandler_EventManager.htm)|
Возвращает или задаёт объект предоставляющий методы для отправки событий
маршрутов документов.  
[KrScope](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_DeregistrationStageTypeHandler_KrScope.htm)|
Возвращает или задаёт объект предоставляющий методы для работы с текущим
контекстом расширений типового расширения и использования разделяемых объектов
карточек.  
[NumberDirectorContainer](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_DeregistrationStageTypeHandler_NumberDirectorContainer.htm)|
Возвращает или задаёт объект, выполняющий регистрацию и предоставляющий доступ
к подсистеме номеров для типов карточек, включая объекты
[INumberDirector](T_Tessa_Cards_Numbers_INumberDirector.htm),
[INumberComposer](T_Tessa_Cards_Numbers_INumberComposer.htm) и
[INumberQueueProcessor](T_Tessa_Cards_Numbers_INumberQueueProcessor.htm).  
[Serializer](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_DeregistrationStageTypeHandler_Serializer.htm)|
Возвращает или задаёт объект предоставляющий методы для сериализации
параметров этапов.  
[Session](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_DeregistrationStageTypeHandler_Session.htm)|
Возвращает или задаёт сессию пользователя.  
## __Методы
[AfterPostprocessingAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase_AfterPostprocessingAsync.htm)|
Метод, вызываемый после вызова скрипта постобработки этапа.  
(Унаследован от
[StageTypeHandlerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase.htm))  
---|---  
[BeforeInitializationAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase_BeforeInitializationAsync.htm)|
Метод, вызываемый перед вызовом скрипта инициализации этапа.  
(Унаследован от
[StageTypeHandlerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase.htm))  
[CreateRegistrationTaskHistoryItemAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_DeregistrationStageTypeHandler_CreateRegistrationTaskHistoryItemAsync.htm)|
Создаёт элемент истории заданий информарующий о регистрации документа.  
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
[GetCycle](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_DeregistrationStageTypeHandler_GetCycle.htm)|
Возвращает номер цикла согласования.  
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
[HandleResurrectionAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase_HandleResurrectionAsync.htm)|
Обработка восстановления процесса.  
(Унаследован от
[StageTypeHandlerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase.htm))  
[HandleSignalAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase_HandleSignalAsync.htm)|
Обработка сигнала.  
(Унаследован от
[StageTypeHandlerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase.htm))  
[HandleStageInterruptAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase_HandleStageInterruptAsync.htm)|
Обработка отмены этапа. Данный метод должен утилизировать все используемые
этапом ресурсы.  
(Унаследован от
[StageTypeHandlerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase.htm))  
[HandleStageStartAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_DeregistrationStageTypeHandler_HandleStageStartAsync.htm)|
Обработка старта этапа.  
(Переопределяет
[StageTypeHandlerBase.HandleStageStartAsync(IStageTypeHandlerContext)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase_HandleStageStartAsync.htm))  
[HandleTaskCompletionAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase_HandleTaskCompletionAsync.htm)|
Обработка завершения задания.  
(Унаследован от
[StageTypeHandlerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase.htm))  
[HandleTaskReinstateAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase_HandleTaskReinstateAsync.htm)|
Обработка возврата задания на роль.  
(Унаследован от
[StageTypeHandlerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
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
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.Handlers -
пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers.htm)
