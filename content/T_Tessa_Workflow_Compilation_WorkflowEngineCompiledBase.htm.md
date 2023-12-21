# WorkflowEngineCompiledBase - класс
Базовый класс для объекта компиляции, выполняемого при обработке процесса в
[IWorkflowEngineProcessor](T_Tessa_Workflow_IWorkflowEngineProcessor.htm).
## __Definition
 **Пространство имён:**
[Tessa.Workflow.Compilation](N_Tessa_Workflow_Compilation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class WorkflowEngineCompiledBase : IWorkflowEngineCompiled
VB __Копировать
     Public MustInherit Class WorkflowEngineCompiledBase
    	Implements IWorkflowEngineCompiled
C++ __Копировать
     public ref class WorkflowEngineCompiledBase abstract : IWorkflowEngineCompiled
F# __Копировать
     [<AbstractClassAttribute>]
    type WorkflowEngineCompiledBase = 
        class
            interface IWorkflowEngineCompiled
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ WorkflowEngineCompiledBase
Implements
    [IWorkflowEngineCompiled](T_Tessa_Workflow_Compilation_IWorkflowEngineCompiled.htm)
##  __Конструкторы
[WorkflowEngineCompiledBase](M_Tessa_Workflow_Compilation_WorkflowEngineCompiledBase__ctor.htm)|
Инициализирует новый экземпляр класса WorkflowEngineCompiledBase  
---|---  
##  __Свойства
[Action](P_Tessa_Workflow_Compilation_WorkflowEngineCompiledBase_Action.htm)|
Параметры текущего действия в виде dynamic над
[ActionHash](P_Tessa_Workflow_Compilation_WorkflowEngineCompiledBase_ActionHash.htm).  
---|---  
[ActionHash](P_Tessa_Workflow_Compilation_WorkflowEngineCompiledBase_ActionHash.htm)|
Параметры текущего действия.  
[ActionObject](P_Tessa_Workflow_Compilation_WorkflowEngineCompiledBase_ActionObject.htm)|
Текущий экземпляр действия.  
[Cancel](P_Tessa_Workflow_Compilation_WorkflowEngineCompiledBase_Cancel.htm)|
Определяет, требуется ли остановка обработки.  
[Card](P_Tessa_Workflow_Compilation_WorkflowEngineCompiledBase_Card.htm)|
dynamic-обёртка над строковыми секциями основной карточки, или null, если
карточку не удалось загрузить.  
Устарело.  
[CardID](P_Tessa_Workflow_Compilation_WorkflowEngineCompiledBase_CardID.htm)|
Идентификатор текущего процесса.  
[CardObject](P_Tessa_Workflow_Compilation_WorkflowEngineCompiledBase_CardObject.htm)|
Карточка, обрабатываемая процессом. Устарел. Используйте вместо этого
[GetMainCardAsync(CancellationToken)](M_Tessa_Workflow_IWorkflowEngineContext_GetMainCardAsync.htm)  
Устарело.  
[Container](P_Tessa_Workflow_Compilation_WorkflowEngineCompiledBase_Container.htm)|
Контейнер зависимостей.  
[Context](P_Tessa_Workflow_Compilation_WorkflowEngineCompiledBase_Context.htm)|
Контекст обработки процесса в WorkflowEngine.  
[DbScope](P_Tessa_Workflow_Compilation_WorkflowEngineCompiledBase_DbScope.htm)|
Объект, обеспечивающий взаимодействие с базой данных.  
[FileContainer](P_Tessa_Workflow_Compilation_WorkflowEngineCompiledBase_FileContainer.htm)|
Контейнер файлов для обрабатываемой карточки. Устарел. Используйте вместо
этого
[GetFileContainerAsync(CancellationToken)](M_Tessa_Workflow_IWorkflowEngineContext_GetFileContainerAsync.htm)  
Устарело.  
[Node](P_Tessa_Workflow_Compilation_WorkflowEngineCompiledBase_Node.htm)|
Параметры текущего узла в виде dynamic над
[NodeHash](P_Tessa_Workflow_Compilation_WorkflowEngineCompiledBase_NodeHash.htm).  
[NodeHash](P_Tessa_Workflow_Compilation_WorkflowEngineCompiledBase_NodeHash.htm)|
Параметры текущего узла.  
[NodeObject](P_Tessa_Workflow_Compilation_WorkflowEngineCompiledBase_NodeObject.htm)|
Текущий экземпляр узла.  
[Parameters](P_Tessa_Workflow_Compilation_WorkflowEngineCompiledBase_Parameters.htm)|
Список параметров текущего обрабатываемого скрипта.  
[Process](P_Tessa_Workflow_Compilation_WorkflowEngineCompiledBase_Process.htm)|
Параметры текущего процесса в виде dynamic над
[ProcessHash](P_Tessa_Workflow_Compilation_WorkflowEngineCompiledBase_ProcessHash.htm).  
[ProcessHash](P_Tessa_Workflow_Compilation_WorkflowEngineCompiledBase_ProcessHash.htm)|
Параметры текущего процесса.  
[ProcessObject](P_Tessa_Workflow_Compilation_WorkflowEngineCompiledBase_ProcessObject.htm)|
Текущий экземпляр процесса.  
[Session](P_Tessa_Workflow_Compilation_WorkflowEngineCompiledBase_Session.htm)|
Текущая сессия.  
[Signal](P_Tessa_Workflow_Compilation_WorkflowEngineCompiledBase_Signal.htm)|
Параметры обрабатываемого сигнала в виде dynamic над
[SignalHash](P_Tessa_Workflow_Compilation_WorkflowEngineCompiledBase_SignalHash.htm).  
[SignalHash](P_Tessa_Workflow_Compilation_WorkflowEngineCompiledBase_SignalHash.htm)|
Параметры обрабатываемого сигнала.  
[SignalObject](P_Tessa_Workflow_Compilation_WorkflowEngineCompiledBase_SignalObject.htm)|
Текущий сигнал.  
[StoreCardObject](P_Tessa_Workflow_Compilation_WorkflowEngineCompiledBase_StoreCardObject.htm)|
Сохраняемая карточка, обрабатываемая процессом.  
[Tables](P_Tessa_Workflow_Compilation_WorkflowEngineCompiledBase_Tables.htm)|
dynamic-обёртка над коллекционными секциями основной карточки, или null, если
карточку не удалось загрузить.  
Устарело.  
[Task](P_Tessa_Workflow_Compilation_WorkflowEngineCompiledBase_Task.htm)|
Первое задание из списка обрабатываемых заданий
[Tasks](P_Tessa_Workflow_IWorkflowEngineContext_Tasks.htm) или null, если
список пуст.  
[Tasks](P_Tessa_Workflow_Compilation_WorkflowEngineCompiledBase_Tasks.htm)|
Список обрабатываемых заданий. Может быть пустым, но не может быть равным
null.  
[ValidationResult](P_Tessa_Workflow_Compilation_WorkflowEngineCompiledBase_ValidationResult.htm)|
Билдер результата валидации.  
## __Методы
[AddError(String)](M_Tessa_Workflow_Compilation_WorkflowEngineCompiledBase_AddError.htm)|
Метод для добавления результата валидации с типом
[Error](T_Tessa_Platform_Validation_ValidationResultType.htm) и текстом text в
[ValidationResult](P_Tessa_Workflow_Compilation_WorkflowEngineCompiledBase_ValidationResult.htm).  
---|---  
[AddError(String,
Object[])](M_Tessa_Workflow_Compilation_WorkflowEngineCompiledBase_AddError_1.htm)|
Метод для добавления результата валидации с типом
[Error](T_Tessa_Platform_Validation_ValidationResultType.htm) и текстом,
построенным из строки форматирования format и параметров args, в
[ValidationResult](P_Tessa_Workflow_Compilation_WorkflowEngineCompiledBase_ValidationResult.htm).  
[AddInfo(String)](M_Tessa_Workflow_Compilation_WorkflowEngineCompiledBase_AddInfo.htm)|
Метод для добавления результата валидации с типом
[Info](T_Tessa_Platform_Validation_ValidationResultType.htm) и текстом text в
[ValidationResult](P_Tessa_Workflow_Compilation_WorkflowEngineCompiledBase_ValidationResult.htm).  
[AddInfo(String,
Object[])](M_Tessa_Workflow_Compilation_WorkflowEngineCompiledBase_AddInfo_1.htm)|
Метод для добавления результата валидации с типом
[Info](T_Tessa_Platform_Validation_ValidationResultType.htm) и текстом,
построенным из строки форматирования format и параметров args, в
[ValidationResult](P_Tessa_Workflow_Compilation_WorkflowEngineCompiledBase_ValidationResult.htm).  
[AddWarning(String)](M_Tessa_Workflow_Compilation_WorkflowEngineCompiledBase_AddWarning.htm)|
Метод для добавления результата валидации с типом
[Warning](T_Tessa_Platform_Validation_ValidationResultType.htm) и текстом text
в
[ValidationResult](P_Tessa_Workflow_Compilation_WorkflowEngineCompiledBase_ValidationResult.htm).  
[AddWarning(String,
Object[])](M_Tessa_Workflow_Compilation_WorkflowEngineCompiledBase_AddWarning_1.htm)|
Метод для добавления результата валидации с типом
[Warning](T_Tessa_Platform_Validation_ValidationResultType.htm) и текстом,
построенным из строки форматирования format и параметров args, в
[ValidationResult](P_Tessa_Workflow_Compilation_WorkflowEngineCompiledBase_ValidationResult.htm).  
[Condition](M_Tessa_Workflow_Compilation_WorkflowEngineCompiledBase_Condition.htm)|
Скрипт условия.  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ExecuteActionAsync](M_Tessa_Workflow_Compilation_WorkflowEngineCompiledBase_ExecuteActionAsync.htm)|
Запускает выполнение метода скомпилированного объекта с указанным именем и
параметрами.  
[ExecuteActionCoreAsync](M_Tessa_Workflow_Compilation_WorkflowEngineCompiledBase_ExecuteActionCoreAsync.htm)|
Запускает выполнение метода скомпилированного объекта с указанным именем и
параметрами.  
[ExecuteFuncAsync<T>](M_Tessa_Workflow_Compilation_WorkflowEngineCompiledBase_ExecuteFuncAsync__1.htm)|
Запускает выполнение метода скомпилированного объекта, возвращающего значение,
с указанным именем и параметрами.  
[ExecuteFuncCoreAsync](M_Tessa_Workflow_Compilation_WorkflowEngineCompiledBase_ExecuteFuncCoreAsync.htm)|
Запускает выполнение метода скомпилированного объекта, возвращающего значение,
с указанным именем и параметрами.  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetCardAsync](M_Tessa_Workflow_Compilation_WorkflowEngineCompiledBase_GetCardAsync.htm)|
Метод, возвращающий dynamic-обёртку над строковыми секциями основной карточки.  
[GetCardObjectAsync](M_Tessa_Workflow_Compilation_WorkflowEngineCompiledBase_GetCardObjectAsync.htm)|
Метод для получения основной карточки. Метод загружает карточку с сервера,
если она еще не была загружена.  
[GetFileContainerAsync](M_Tessa_Workflow_Compilation_WorkflowEngineCompiledBase_GetFileContainerAsync.htm)|
Метод для получения файлового контейнера основной карточки.  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetTablesAsync](M_Tessa_Workflow_Compilation_WorkflowEngineCompiledBase_GetTablesAsync.htm)|
Метод, возвращающий dynamic-обёртку над коллекционными секциями основной
карточки.  
[GetTask](M_Tessa_Workflow_Compilation_WorkflowEngineCompiledBase_GetTask.htm)|
Метод для получения объекта задания карточки по его идентификатору. Возвращает
задание из сохраняемой карточки, если оно там есть, иначе из основной
карточки.  
Устарело.  
[GetTaskAsync](M_Tessa_Workflow_Compilation_WorkflowEngineCompiledBase_GetTaskAsync.htm)|
Метод для получения объекта задания карточки по его идентификатору. Возвращает
задание из сохраняемой карточки, если оно там есть, иначе из основной
карточки.  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[InConditionAsync](M_Tessa_Workflow_Compilation_WorkflowEngineCompiledBase_InConditionAsync.htm)|
Скрипт условия входа в узел.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[OutConditionAsync](M_Tessa_Workflow_Compilation_WorkflowEngineCompiledBase_OutConditionAsync.htm)|
Скрипт условия выхода из узла  
[PostScriptAsync](M_Tessa_Workflow_Compilation_WorkflowEngineCompiledBase_PostScriptAsync.htm)|
Скрипт постобработки.  
[PreScriptAsync](M_Tessa_Workflow_Compilation_WorkflowEngineCompiledBase_PreScriptAsync.htm)|
Скрипт предобработки.  
[SetContext](M_Tessa_Workflow_Compilation_WorkflowEngineCompiledBase_SetContext.htm)|
Метод для установки текущего контекста.  
[SetMainCard](M_Tessa_Workflow_Compilation_WorkflowEngineCompiledBase_SetMainCard.htm)|
Метод для установки новой карточки как основной.  
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
[Tessa.Workflow.Compilation - пространство
имён](N_Tessa_Workflow_Compilation.htm)
