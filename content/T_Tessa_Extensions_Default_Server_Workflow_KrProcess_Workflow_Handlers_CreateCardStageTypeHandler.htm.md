# CreateCardStageTypeHandler - класс
Предоставляет обработчик этапа "Создание карточки"
([CreateCardDescriptor](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_StageTypeDescriptors_CreateCardDescriptor.htm)).
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.Handlers](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public class CreateCardStageTypeHandler : StageTypeHandlerBase
VB __Копировать
     Public Class CreateCardStageTypeHandler
    	Inherits StageTypeHandlerBase
C++ __Копировать
     public ref class CreateCardStageTypeHandler : public StageTypeHandlerBase
F# __Копировать
     type CreateCardStageTypeHandler = 
        class
            inherit StageTypeHandlerBase
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[StageTypeHandlerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase.htm) __ CreateCardStageTypeHandler
##  __Конструкторы
[CreateCardStageTypeHandler](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_CreateCardStageTypeHandler__ctor.htm)|
Инициализирует новый экземпляр класса CreateCardStageTypeHandler.  
---|---  
## __Свойства
[CardRepositoryDwt](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_CreateCardStageTypeHandler_CardRepositoryDwt.htm)|
Возвращает или задаёт репозиторий для управления карточками
([DefaultWithoutTransaction](F_Tessa_Cards_CardRepositoryNames_DefaultWithoutTransaction.htm)).  
---|---  
[CardRepositoryEwt](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_CreateCardStageTypeHandler_CardRepositoryEwt.htm)|
Возвращает или задаёт репозиторий для управления карточками
([ExtendedWithoutTransaction](F_Tessa_Cards_CardRepositoryNames_ExtendedWithoutTransaction.htm)).  
[DbScope](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_CreateCardStageTypeHandler_DbScope.htm)|
Возвращает или задаёт объект для взаимодействия с базой данных.  
[FileManager](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_CreateCardStageTypeHandler_FileManager.htm)|
Возвращает или задаёт объект, который управляет объектами контейнеров
[ICardFileContainer](T_Tessa_Cards_ICardFileContainer.htm), объединяющих
карточку с её файлами
([ExtendedWithoutTransaction](F_Tessa_Cards_CardRepositoryNames_ExtendedWithoutTransaction.htm)).  
[KrScope](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_CreateCardStageTypeHandler_KrScope.htm)|
Возвращает или задаёт объект предоставляющий методы для работы с текущим
контекстом расширений типового расширения и использования разделяемых объектов
карточек.  
[SignatureProvider](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_CreateCardStageTypeHandler_SignatureProvider.htm)|
Возвращает или задаёт объект, предоставляющий криптографические средства для
подписания и проверки подписи.  
[TokenProvider](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_CreateCardStageTypeHandler_TokenProvider.htm)|
Возвращает или задаёт объект, обеспечивающий создание и валидацию токена
безопасности для типового решения.  
[TypesCache](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_CreateCardStageTypeHandler_TypesCache.htm)|
Возвращает или задаёт кэш по типам карточек и документов, содержащих
информацию по типовому решению.  
## __Методы
[AfterPostprocessingAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_CreateCardStageTypeHandler_AfterPostprocessingAsync.htm)|
Метод, вызываемый после вызова скрипта постобработки этапа.  
(Переопределяет
[StageTypeHandlerBase.AfterPostprocessingAsync(IStageTypeHandlerContext)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase_AfterPostprocessingAsync.htm))  
---|---  
[BeforeInitializationAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase_BeforeInitializationAsync.htm)|
Метод, вызываемый перед вызовом скрипта инициализации этапа.  
(Унаследован от
[StageTypeHandlerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase.htm))  
[CreateEmptyCardAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_CreateCardStageTypeHandler_CreateEmptyCardAsync.htm)|
Инициализирует стратегию доступа к новой карточке доступной по ключу
[NewCard](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_Keys_NewCard.htm)
в
[InfoStorage](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_InfoStorage.htm).  
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
[GetCardTypeAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_CreateCardStageTypeHandler_GetCardTypeAsync.htm)|
Асинхронно возвращает идентификатор типа карточки соответствующий указанному
типу документа, если указанному значению не соответствует типу документа, то
оно возвращается без изменений.  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetLocalContext](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_CreateCardStageTypeHandler_GetLocalContext.htm)|
Возвращает объект
[CreateCardStageTypeHandler.CreateCardStageLocalContext](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_CreateCardStageTypeHandler_CreateCardStageLocalContext.htm)
содержащий контекст этапа.  
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
[HandleStageStartAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_CreateCardStageTypeHandler_HandleStageStartAsync.htm)|
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
[StartProcessAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_CreateCardStageTypeHandler_StartProcessAsync.htm)|
Асинхронно запускает основной процесс по указанной карточке.  
[StoreCardAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_CreateCardStageTypeHandler_StoreCardAsync.htm)|
Асинхронно сохраняет указанную карточку с учётом приложенных файлов.  
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
