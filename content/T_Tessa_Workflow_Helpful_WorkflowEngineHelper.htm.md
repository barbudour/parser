# WorkflowEngineHelper - класс
Класс для дополнительных методов для работы с WorkflowEngine
## __Definition
 **Пространство имён:** [Tessa.Workflow.Helpful](N_Tessa_Workflow_Helpful.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class WorkflowEngineHelper
VB __Копировать
     Public NotInheritable Class WorkflowEngineHelper
C++ __Копировать
     public ref class WorkflowEngineHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type WorkflowEngineHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ WorkflowEngineHelper
##  __Методы
[CheckInstanceExistsAsync](M_Tessa_Workflow_Helpful_WorkflowEngineHelper_CheckInstanceExistsAsync.htm)|
Метод для проверки наличия активных экземпляров версии или шаблона процесса  
---|---  
[CheckLicense](M_Tessa_Workflow_Helpful_WorkflowEngineHelper_CheckLicense.htm)|
Метод для проверки лицензии  
[Get<T>(IDictionary<String, Object>,
String[])](M_Tessa_Workflow_Helpful_WorkflowEngineHelper_Get__1.htm)|
Возвращает значение расположенное по указанному пути.  
[Get<T>(IList, Int32,
String[])](M_Tessa_Workflow_Helpful_WorkflowEngineHelper_Get__1_2.htm)|
Возвращает значение распологающееся в указаному списке по индексу index по
пути hashPath. Применяется для получения значения из коллекционной секции,
тогда fromList список строк  
[Get<T>(IDictionary<String, Object>, String[], Int32,
String[])](M_Tessa_Workflow_Helpful_WorkflowEngineHelper_Get__1_1.htm)|  
[GetBindingType](M_Tessa_Workflow_Helpful_WorkflowEngineHelper_GetBindingType.htm)|
Возвращает тип источника данных привязки.  
[GetExtendedFieldName](M_Tessa_Workflow_Helpful_WorkflowEngineHelper_GetExtendedFieldName.htm)|
Метод для формирования расширенного имени для поля строкой секции  
[GetExtendedSectionName](M_Tessa_Workflow_Helpful_WorkflowEngineHelper_GetExtendedSectionName.htm)|
Метод для формирования расширенного имени для табличной секции  
[GetOrAdd<T>(IDictionary<String, Object>, String[],
T)](M_Tessa_Workflow_Helpful_WorkflowEngineHelper_GetOrAdd__1_1.htm)|
Возвращает значение расположенное по указанному пути. Если значение не найдено
в словаре, то в него будет добавлено значение по умолчанию расположенное по
указаному пути.  
[GetOrAdd<T>(IList, Int32, String[],
T)](M_Tessa_Workflow_Helpful_WorkflowEngineHelper_GetOrAdd__1_2.htm)|  
[GetOrAdd<T>(IDictionary<String, Object>, String[], Int32, String[],
T)](M_Tessa_Workflow_Helpful_WorkflowEngineHelper_GetOrAdd__1.htm)|  
[GetTileInfos](M_Tessa_Workflow_Helpful_WorkflowEngineHelper_GetTileInfos.htm)|  
[GetTrace](M_Tessa_Workflow_Helpful_WorkflowEngineHelper_GetTrace.htm)|  
[GetValidateFieldMessage](M_Tessa_Workflow_Helpful_WorkflowEngineHelper_GetValidateFieldMessage.htm)|
Метод для формирования сообщения валидации о не заполненом поле  
[GetWithWildCard<T>](M_Tessa_Workflow_Helpful_WorkflowEngineHelper_GetWithWildCard__1.htm)|  
[GetWorkflowCardID](M_Tessa_Workflow_Helpful_WorkflowEngineHelper_GetWorkflowCardID.htm)|
Метод для получения ID карточки процесса из контекста WorkflowAPI  
[PathEquals](M_Tessa_Workflow_Helpful_WorkflowEngineHelper_PathEquals.htm)|
Возвращает значение, показывающее, равны ли два указанных пути в хеше.  
[PrepareActionsForSaveAsync](M_Tessa_Workflow_Helpful_WorkflowEngineHelper_PrepareActionsForSaveAsync.htm)|
Выполняет подготовку строки с версией шаблона бизнес-процесса для сохранения
путём вызова [PrepareForSaveTemplate(WorkflowActionStorage,
WorkflowNodeStorage,
WorkflowProcessStorage)](M_Tessa_Workflow_Actions_IWorkflowAction_PrepareForSaveTemplate.htm)
для всех действий шаблона процесса.  
[Set<T>(IDictionary<String, Object>, T,
String[])](M_Tessa_Workflow_Helpful_WorkflowEngineHelper_Set__1.htm)|
Устанавливает значение по указанному пути.  
[Set<T>(IList, T, Int32,
String[])](M_Tessa_Workflow_Helpful_WorkflowEngineHelper_Set__1_2.htm)|  
[Set<T>(IDictionary<String, Object>, T, String[], Int32,
String[])](M_Tessa_Workflow_Helpful_WorkflowEngineHelper_Set__1_1.htm)|  
[SetWorkflowCardID](M_Tessa_Workflow_Helpful_WorkflowEngineHelper_SetWorkflowCardID.htm)|
Метод для установки ID карточки процесса в контекст WorkflowAPI  
[TryGet<T>](M_Tessa_Workflow_Helpful_WorkflowEngineHelper_TryGet__1.htm)|
Возвращает значение показывающее удалось ли получить значение по указаннму
пути и само значение.  
[ValidatePlaceholderText](M_Tessa_Workflow_Helpful_WorkflowEngineHelper_ValidatePlaceholderText.htm)|  
[ValidatePlaceholderTextList](M_Tessa_Workflow_Helpful_WorkflowEngineHelper_ValidatePlaceholderTextList.htm)|  
## __Поля
[ActiveViewName](F_Tessa_Workflow_Helpful_WorkflowEngineHelper_ActiveViewName.htm)|
Имя представления для просмотра активных бизнес-процессов  
---|---  
[AdditionalInformationInfoMark](F_Tessa_Workflow_Helpful_WorkflowEngineHelper_AdditionalInformationInfoMark.htm)|
Имя поля для хранения дополнительной информации  
[BindingPrefix](F_Tessa_Workflow_Helpful_WorkflowEngineHelper_BindingPrefix.htm)|
Префикс для обозначения привязки данных в хеше к другому полю  
[BindingSectionKey](F_Tessa_Workflow_Helpful_WorkflowEngineHelper_BindingSectionKey.htm)|
Ключ для обозначения привязки всей секции к хешу  
[ButtonIDKey](F_Tessa_Workflow_Helpful_WorkflowEngineHelper_ButtonIDKey.htm)|
Имя поля для хранения ID нажатой кнопки  
[ErrorViewName](F_Tessa_Workflow_Helpful_WorkflowEngineHelper_ErrorViewName.htm)|
Имя представления для просмотра бизнес-прцоессов с ошибками  
[ExtendedBusinessProcessTemplateTypeID](F_Tessa_Workflow_Helpful_WorkflowEngineHelper_ExtendedBusinessProcessTemplateTypeID.htm)|
Card type identifier for "ExtendedBusinessProcessTemplateTypeID":
{D05799BD-35B6-43B4-97DD-B6D0E683EFF3}.  
Устарело.  
[PrepareActionsForSaveKey](F_Tessa_Workflow_Helpful_WorkflowEngineHelper_PrepareActionsForSaveKey.htm)|
Ключ, по которому в Info карточки хранится признак, что при сохранении
карточки бизнес-процесса необходимо выполнить подготовку действия для
сохранения.  
[TagKey](F_Tessa_Workflow_Helpful_WorkflowEngineHelper_TagKey.htm)|  Имя поля
для настроек контрола для хранения ID расширення кнопки  
[TaskCompletedByWorkflowEngineKey](F_Tessa_Workflow_Helpful_WorkflowEngineHelper_TaskCompletedByWorkflowEngineKey.htm)|
Имя поля для хранения флага, что задание было выполнено из WorkflowEngine  
[TileExtensionPrefix](F_Tessa_Workflow_Helpful_WorkflowEngineHelper_TileExtensionPrefix.htm)|
Префикс для секций и полей в сгенерированных расширениях тайлов в шаблонах
карточек процессов  
[WildCardHashMark](F_Tessa_Workflow_Helpful_WorkflowEngineHelper_WildCardHashMark.htm)|
Метка в привязке, определяющая, что данный путь может быть отличным от
заданного. Например, путь Some.*Param.ID будет искать в структуре с ключом
Some структуру с ключом Param, или если такой нет, то первую попавшуются
структуру, и в ней уже значение с именем ID. Это нужно для возможности
привязки к спискам с одним типом, но разными ключами объекта.  
[WorkflowEngineEditorTileNamePrefix](F_Tessa_Workflow_Helpful_WorkflowEngineHelper_WorkflowEngineEditorTileNamePrefix.htm)|
Префикс к имени тайла в WorkflowEngine, отвечающего за редактор. Имя строится
как Prefix + processTemplateID  
[WorkflowEngineProcessesKey](F_Tessa_Workflow_Helpful_WorkflowEngineHelper_WorkflowEngineProcessesKey.htm)|
Ключ, по которому сохраняются экземпляры процессов в карточке при экcпорте
карточки и удалении в корзину.  
[WorkflowEngineProcessName](F_Tessa_Workflow_Helpful_WorkflowEngineHelper_WorkflowEngineProcessName.htm)|
Имя процесса, обрабатываемого через обработчик WorkflowEngine в терминах
WorkflowAPI  
[WorkflowEngineProcessTileNamePrefix](F_Tessa_Workflow_Helpful_WorkflowEngineHelper_WorkflowEngineProcessTileNamePrefix.htm)|
Префикс к имени тайла в WorkflowEngine, отвечающего за процесс. Имя строится
как Prefix + tileID  
[WorkflowEngineSettingsTypeID](F_Tessa_Workflow_Helpful_WorkflowEngineHelper_WorkflowEngineSettingsTypeID.htm)|
Card type identifier for "WorkflowEngineSettings":
{A73DA16B-D69B-4957-A2DE-B35ADEBCD85E}.  
[WorkflowEngineSettingsTypeName](F_Tessa_Workflow_Helpful_WorkflowEngineHelper_WorkflowEngineSettingsTypeName.htm)|
Card type name for "WorkflowEngineSettings".  
[WorkflowEngineType](F_Tessa_Workflow_Helpful_WorkflowEngineHelper_WorkflowEngineType.htm)|
Строка типа Workflow для WorkflowEngine  
[WorkflowProcessTypeID](F_Tessa_Workflow_Helpful_WorkflowEngineHelper_WorkflowProcessTypeID.htm)|
Card type identifier for "WorkflowProcess":
{BB3E1452-30DA-4EB2-A4FE-10871608BED3}.  
[WorkflowProcessTypeName](F_Tessa_Workflow_Helpful_WorkflowEngineHelper_WorkflowProcessTypeName.htm)|
Card type name for "WorkflowProcess".  
[WorkflowTileKey](F_Tessa_Workflow_Helpful_WorkflowEngineHelper_WorkflowTileKey.htm)|
Имя поля для хранения информации о тайле  
[WorkflowTilesKey](F_Tessa_Workflow_Helpful_WorkflowEngineHelper_WorkflowTilesKey.htm)|
Имя поля для хранения информации о тайлах  
[WorkflowTypeInfoMark](F_Tessa_Workflow_Helpful_WorkflowEngineHelper_WorkflowTypeInfoMark.htm)|
Имя типа Workflow, определяющее обработчик на сервере при нажатии кнопки  
## __См. также
#### Ссылки
[Tessa.Workflow.Helpful - пространство имён](N_Tessa_Workflow_Helpful.htm)
