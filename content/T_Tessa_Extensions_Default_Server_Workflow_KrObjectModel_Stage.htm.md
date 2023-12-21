# Stage - класс
Предоставляет информацию о этапе маршрута.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrObjectModel](N_Tessa_Extensions_Default_Server_Workflow_KrObjectModel.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class Stage : IEquatable<Stage>, 
    	ISealable
VB __Копировать
     Public NotInheritable Class Stage
    	Implements IEquatable(Of Stage), ISealable
C++ __Копировать
     public ref class Stage sealed : IEquatable<Stage^>, 
    	ISealable
F# __Копировать
     [<SealedAttribute>]
    type Stage = 
        class
            interface IEquatable<Stage>
            interface ISealable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ Stage
Implements
    [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<Stage>, [ISealable](T_Tessa_Platform_ISealable.htm)
##  __Конструкторы
[Stage()](M_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage__ctor.htm)|
Инициализирует новый пустой экземпляр класса Stage.  
---|---  
[Stage(Stage)](M_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage__ctor_3.htm)|
Инициализирует новый экземпляр класса Stage на основе другого экземпляра.
Запечатанность не переносится.  
[Stage(String, Guid,
String)](M_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage__ctor_2.htm)|
Инициализирует новый экземпляр класса Stage.  
[Stage(Guid, String, Guid, String, Guid, String, Int32, Nullable<Guid>,
String, Nullable<Int32>, Boolean, GroupPosition, Stage, Boolean, Int32,
Nullable<DateTime>, Boolean, Boolean,
Boolean)](M_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage__ctor_1.htm)|
Инициализирует новый экземпляр класса Stage с привязкой к шаблону этапов.  
## __Свойства
[Author](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_Author.htm)|
Автор этапа или значение null, если он не задан. Переопределяет автора
заданного в параметрах этапа.  
---|---  
[BasedOnTemplate](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_BasedOnTemplate.htm)|
Значение, показывающее, что этап добавлен из шаблона этапов - задан шаблон
этапов.  
[BasedOnTemplateStage](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_BasedOnTemplateStage.htm)|
Значение, показывающее, что этап добавлен из шаблона этапов - задан
идентификатор строки шаблона этапов из карточки шаблона этапов.  
[CanBeSkipped](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_CanBeSkipped.htm)|
Значение, показывающее, разрешен ли пропуск этапа.  
[CanChangeOrder](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_CanChangeOrder.htm)|
Значение, показывающее, может ли пользователь менять порядок текущего этапа.  
[GroupPosition](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_GroupPosition.htm)|  
[Hidden](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_Hidden.htm)|
Значение, показывающее, что этап является скрытым.  
[ID](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_ID.htm)|
Идентификатор этапа.  
[Info](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_Info.htm)|
Dynamic-обёртка над
[InfoStorage](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_InfoStorage.htm).  
[InfoStorage](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_InfoStorage.htm)|
Дополнительная информация о этапе.  
[IsPositionUnspecified](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_IsPositionUnspecified.htm)|
Признак того, что значения
[GroupPosition](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_GroupPosition.htm),
[TemplateOrder](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_TemplateOrder.htm)
и
[TemplateStageOrder](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_TemplateStageOrder.htm)
не учитываются при сортировке этапов.  
[IsSealed](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_IsSealed.htm)|
Признак того, что объект был защищён от изменений.  
[IsStageReadonly](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_IsStageReadonly.htm)|
Значение, показывающее, может ли пользователь редактировать этап.  
[Name](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_Name.htm)|
Название этапа.  
[OrderChanged](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_OrderChanged.htm)|
Признак того, что порядок менялся пользователем.  
[Performer](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_Performer.htm)|
Исполнитель текущего этапа или значение null, если он не задан.  
[Performers](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_Performers.htm)|
Список исполнителей текущего этапа.  
[Planned](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_Planned.htm)|
Дата выполнения или значение null, если значение не задано.  
[PlannedQuants](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_PlannedQuants.htm)|
Срок в квантах, если нет даты окончания задания
[Planned](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_Planned.htm).  
[RowChanged](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_RowChanged.htm)|
Признак того, что этап менялся пользователем.  
[RowID](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_RowID.htm)|
Идентификатор строки этапа ([RowID](P_Tessa_Cards_CardRow_RowID.htm)) в
конкретном документе.  
[Settings](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_Settings.htm)|
Dynamic-обёртка над
[SettingsStorage](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_SettingsStorage.htm).  
[SettingsStorage](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_SettingsStorage.htm)|
Параметры этапа.  
[Skip](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_Skip.htm)|
Признак пропуска этапа.  
[SqlPerformers](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_SqlPerformers.htm)|
Запрос на получение SQL-согласующих.  
[SqlPerformersIndex](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_SqlPerformersIndex.htm)|
Положение SQL-согласующих.  
[StageGroupID](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_StageGroupID.htm)|
Идентификатор группы этапов, к которой принадлежит этап.  
[StageGroupName](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_StageGroupName.htm)|
Название группы этапов, к которой принадлежит этап.  
[StageGroupOrder](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_StageGroupOrder.htm)|
Порядок сортировки группы этапов, к которой принадлежит этап.  
[StageTypeCaption](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_StageTypeCaption.htm)|
Отображаемое имя типа этапа.  
[StageTypeID](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_StageTypeID.htm)|
Идентификатор типа этапа.  
[State](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_State.htm)|  
[TemplateID](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_TemplateID.htm)|
Идентификатор шаблона этапов или значение null, если этап не связан с шаблоном
этапов.  
[TemplateName](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_TemplateName.htm)|
Название шаблона этапов или значение null, если этап не связан с шаблоном
этапов.  
[TemplateOrder](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_TemplateOrder.htm)|
Порядок этапа в шаблоне этапов или значение поля
[BasedOnStageTemplateOrder](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_KrStages_BasedOnStageTemplateOrder.htm)
или значение null, если порядок этапа был изменён или если этап больше не
связан с шаблоном этапов.  
[TemplateStageOrder](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_TemplateStageOrder.htm)|
Порядок сортировки для этапа в рамках шаблона этапов или значение null, если
этап ручной или шаблон этапов удалён.  
[TimeLimit](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_TimeLimit.htm)|
Срок (рабочие дни) или значение null, если значение не задано.  
[TimeLimitOrDefault](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_TimeLimitOrDefault.htm)|
Срок (рабочие дни), если указан, иначе стандартное значение DefaultTimeLimit.  
[WriteTaskFullInformation](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_WriteTaskFullInformation.htm)|
Значение, определяющее, в каком объеме информация о заданиях будет указываться
по ключу
[Tasks](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_Keys_Tasks.htm)
в
[InfoStorage](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_InfoStorage.htm).
Если указано true \- информация будет полной, включая карточку задания. Иначе
перед записью будут удалены некоторые поля.  
## __Методы
[AddAutomaticallyChangedValue](M_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_AddAutomaticallyChangedValue.htm)|
Добавляет указанное свойство в список автоматически изменённых значений этапа.  
---|---  
[ClearAutomaticallyChangedValues](M_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_ClearAutomaticallyChangedValues.htm)|
Очищает список автоматически изменённых значений этапа.  
[CreateFromStageRowAsync](M_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_CreateFromStageRowAsync.htm)|
Создаёт новый экземпляр класса Stage по строке, содержащей информацию о этапе.  
[CreateFromStageTemplateAsync](M_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_CreateFromStageTemplateAsync.htm)|
Создаёт новый экземпляр класса Stage по шаблону этапов (templateStage).  
[Equals(Object)](M_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_Equals.htm)|
Determines whether the specified object is equal to the current object.  
(Переопределяет
[Object.Equals(Object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\)))  
[Equals(Stage)](M_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_Equals_1.htm)|
Сравнивает этап по значимым полям.  
[EqualsWithAutomaticallyChangedValues](M_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_EqualsWithAutomaticallyChangedValues.htm)|
Сравнивает этап по значимым полям с учётом автоматически изменённых значений.  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](M_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_GetHashCode.htm)|
Serves as the default hash function.  
(Переопределяет
[Object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Inherit](M_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_Inherit.htm)|
Переносит служебную информацию из указанного этапа в этот экземпляр.  
[InheritPosition](M_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_InheritPosition.htm)|
Переносит информацию о положении этапа из указанного этапа.  
[IsInfoChanged](M_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_IsInfoChanged.htm)|
Возвращает значение, показывающее, что изменилась дополнительная информация
этапа
([InfoStorage](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_InfoStorage.htm)).  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[RemoveAutomaticallyChangedValue](M_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_RemoveAutomaticallyChangedValue.htm)|
Удаляет указанное свойство из списка автоматически изменённых значений этапа.  
[Seal](M_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_Seal.htm)|
Защищает объект от изменений.  
[ToString](M_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_ToString.htm)|
Returns a string that represents the current object.  
(Переопределяет
[Object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring))  
##  __Операторы
[Equality(Stage,
Stage)](M_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_op_Equality.htm)|
Сравнивает два экземпляра объектов типа Stage.  
---|---  
[Inequality(Stage,
Stage)](M_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_op_Inequality.htm)|
Сравнивает два экземпляра объектов типа Stage.  
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
[ToStringDetailed](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrCompilersExtensions_ToStringDetailed_1.htm)|  
(Определяется
[KrCompilersExtensions](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrCompilersExtensions.htm))  
[ToStringSummary](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrCompilersExtensions_ToStringSummary_1.htm)|  
(Определяется
[KrCompilersExtensions](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_KrCompilersExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Workflow.KrObjectModel - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrObjectModel.htm)
