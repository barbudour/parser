# Keys - поля
##  __Поля
[AutomaticallyChangedValues](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_Keys_AutomaticallyChangedValues.htm)|
Ключ по которому в InfoStorage хранится список автоматически изменённых
значений этапа. Тип значения:
[IList](https://learn.microsoft.com/dotnet/api/system.collections.ilist), где
тип элемента - [String](https://learn.microsoft.com/dotnet/api/system.string).  
---|---  
[Compile](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_Keys_Compile.htm)|  
[CompileAll](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_Keys_CompileAll.htm)|  
[CompileAllWithValidationResult](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_Keys_CompileAllWithValidationResult.htm)|  
[CompileWithValidationResult](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_Keys_CompileWithValidationResult.htm)|  
[CompletionOptionSettings](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_Keys_CompletionOptionSettings.htm)|
Ключ по которому в
[Parameters](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessClientCommand_Parameters.htm)
содержатся параметры диалога. Тип значения: хранилище объекта типа
[CardTaskCompletionOptionSettings](T_Tessa_Cards_CardTaskCompletionOptionSettings.htm).  
[Cycle](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_Keys_Cycle.htm)|
Имя ключа, по которому в InfoStorage содержится номер текущего цикла
согласования. Тип значения:
[Int32](https://learn.microsoft.com/dotnet/api/system.int32).  
[DirectionAfterInterruptParam](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_Keys_DirectionAfterInterruptParam.htm)|  
[Disapproved](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_Keys_Disapproved.htm)|
Ключ по которому в InfoStorage содержится значение, показывающее наличие
несогласовавших - значение true. Тип значения:
[Nullable<T>](https://learn.microsoft.com/dotnet/api/system.nullable-1), где T
- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean).  
[DocTypeID](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_Keys_DocTypeID.htm)|  
[DocTypeTitle](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_Keys_DocTypeTitle.htm)|  
[ExtraSourcesChanged](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_Keys_ExtraSourcesChanged.htm)|  
[FinalStageRowIDParam](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_Keys_FinalStageRowIDParam.htm)|  
[ForceStartGroupParam](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_Keys_ForceStartGroupParam.htm)|  
[ForkNestedProcessInfo](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_Keys_ForkNestedProcessInfo.htm)|
Ключ по которому в InfoStorage содержится дополнительная информация по
вложенному процессу. Тип значения: [IDictionary<TKey,
TValue>](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2),
где TKey - [String](https://learn.microsoft.com/dotnet/api/system.string),
TValue - [Object](https://learn.microsoft.com/dotnet/api/system.object).  
[IgnoreChangeState](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_Keys_IgnoreChangeState.htm)|
Имя ключа, по которому в Info содержится значение, показывающее надо ли
игнорировать значение флага "Изменять состояние" в настройках этапа
"Доработка". Тип значения:
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean). Если
значение не найдено, то считается, что оно равно false.  
[KeepStageStatesParam](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_Keys_KeepStageStatesParam.htm)|
Ключ, по которому в дополнительных параметрах состояния (Parameters)
содержится флаг, показывающий, что при переходе должно быть сохранено текущее
состояние этапов. Тип значения:
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean). Если
значение не найдено, то считается, что оно равно false.  
[KrStageRowsSignatures](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_Keys_KrStageRowsSignatures.htm)|  
[MainProcessType](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_Keys_MainProcessType.htm)|  
[NestedProcessID](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_Keys_NestedProcessID.htm)|  
[NestedStage](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_Keys_NestedStage.htm)|  
[NewCard](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_Keys_NewCard.htm)|  
[NewCardID](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_Keys_NewCardID.htm)|
Ключ по которому хранится идентификатор карточки.  
[NewCardSignature](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_Keys_NewCardSignature.htm)|  
[NotMessageHasNoActiveStages](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_Keys_NotMessageHasNoActiveStages.htm)|
Ключ по которому содержится значение, показывающее, что при отсутствии этапов,
доступных для выполнения, не должно отображаться сообщение. Тип значения:
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean).  
[NotReturnEdit](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_Keys_NotReturnEdit.htm)|
Ключ по которому в
[ProcessParameters](P_Tessa_Cards_Workflow_IWorkflowProcessInfo_ProcessParameters.htm)
содержится значение переопределяющее параметр "Не возвращать на доработку".
Если значение - true, то проверяется значение параметра в этапе, иначе - false
\- нет. Тип значения:
[Nullable<T>](https://learn.microsoft.com/dotnet/api/system.nullable-1), где T
- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean).  
[ParentProcessID](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_Keys_ParentProcessID.htm)|  
[ParentProcessType](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_Keys_ParentProcessType.htm)|  
[ParentStageRowID](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_Keys_ParentStageRowID.htm)|  
[PreparingGroupRecalcStrategyParam](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_Keys_PreparingGroupRecalcStrategyParam.htm)|  
[ProcessHolderID](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_Keys_ProcessHolderID.htm)|  
[ProcessID](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_Keys_ProcessID.htm)|  
[ProcessInfoAtEnd](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_Keys_ProcessInfoAtEnd.htm)|  
[ProcessInstance](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_Keys_ProcessInstance.htm)|
Ключ по которому в
[Parameters](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessClientCommand_Parameters.htm)
содержится информация о процессе маршрута. Тип значения: хранилище объекта
типа
[KrProcessInstance](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessInstance.htm).  
[RootStage](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_Keys_RootStage.htm)|  
[StageRowID](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_Keys_StageRowID.htm)|
Ключ по которому содержится идентификатор строки этапа. Тип значения:
[Guid](https://learn.microsoft.com/dotnet/api/system.guid).  
[StateBeforeRegistration](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_Keys_StateBeforeRegistration.htm)|  
[Tasks](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_Keys_Tasks.htm)|
Ключ по которому в InfoStorage хранится список завершённых заданий. Тип
значения:
[IList](https://learn.microsoft.com/dotnet/api/system.collections.ilist), где
тип элемента -
System.Collections.Generic.IDictionary<[String](https://learn.microsoft.com/dotnet/api/system.string),[Object](https://learn.microsoft.com/dotnet/api/system.object)>
\- хранилище объекта [CardTask](T_Tessa_Cards_CardTask.htm).  
[TemplateID](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_Keys_TemplateID.htm)|
Ключ по которому хранится идентификатор шаблона карточки.  
[TypeCaption](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_Keys_TypeCaption.htm)|
Ключ по которому хранится отображаемое имя типа карточки.  
[TypeID](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_Keys_TypeID.htm)|
Ключ по которому хранится идентификатор типа карточки.  
[TypeName](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_Keys_TypeName.htm)|
Ключ по которому хранится имя типа карточки.  
## __См. также
#### Ссылки
[KrConstants.Keys -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_Keys.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)
