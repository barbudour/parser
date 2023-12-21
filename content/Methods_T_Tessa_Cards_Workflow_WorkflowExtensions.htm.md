# WorkflowExtensions - методы
##  __Методы
[AddTask](M_Tessa_Cards_Workflow_WorkflowExtensions_AddTask.htm)|  Добавляет
задание в состоянии [Inserted](T_Tessa_Cards_CardRowState.htm) к следующей
сохраняемой карточке
[NextRequest](P_Tessa_Cards_Workflow_IWorkflowContext_NextRequest.htm).  
---|---  
[GetWorkflowQueue](M_Tessa_Cards_Workflow_WorkflowExtensions_GetWorkflowQueue.htm)|
Возвращает очередь действий с Workflow, отложенных для выполнения на сервере
для текущей карточки. Если очередь отсутствует, то создаётся и возвращается
пустая очередь для этой карточки.  
[RegisterWorkflow](M_Tessa_Cards_Workflow_WorkflowExtensions_RegisterWorkflow.htm)|
Выполняет регистрацию Workflow API. Метод автоматически вызывается при
регистрации серверного или клиентского API по работе с карточками.  
[RemoveStartingProcessTaskGroupRowID](M_Tessa_Cards_Workflow_WorkflowExtensions_RemoveStartingProcessTaskGroupRowID.htm)|
Удаляет идентификатор группы в истории заданий для первого задания бизнес-
процесса, запускаемого посредством
[WorkflowStoreExtension](T_Tessa_Cards_Workflow_WorkflowStoreExtension.htm).
Это определяет, что будет использована группа по умолчанию.  
[RemoveWorkflowQueue](M_Tessa_Cards_Workflow_WorkflowExtensions_RemoveWorkflowQueue.htm)|
Удаляет очередь действий с Workflow для текущей карточки. Возвращает признак
того, что такая очередь присутствовала в карточке перед удалением.  
[SetStartingProcessID](M_Tessa_Cards_Workflow_WorkflowExtensions_SetStartingProcessID.htm)|
Устанавливает идентификатор для запускаемого бизнес-процесса.  
[SetStartingProcessName(CardStoreRequest,
String)](M_Tessa_Cards_Workflow_WorkflowExtensions_SetStartingProcessName_1.htm)|
Устанавливает имя бизнес-процесса, запускаемого посредством
[WorkflowStoreExtension](T_Tessa_Cards_Workflow_WorkflowStoreExtension.htm).  
[SetStartingProcessName(Dictionary<String, Object>,
String)](M_Tessa_Cards_Workflow_WorkflowExtensions_SetStartingProcessName.htm)|
Устанавливает имя бизнес-процесса, запускаемого посредством
[WorkflowStoreExtension](T_Tessa_Cards_Workflow_WorkflowStoreExtension.htm).  
[SetStartingProcessNextTask(CardStoreRequest,
CardTask)](M_Tessa_Cards_Workflow_WorkflowExtensions_SetStartingProcessNextTask_1.htm)|
Устанавливает задание, которое будет использоваться при первом сохранении
сразу же после запуска процесса. Например, задание определяет секции
"постановки задачи", которые заполняются при отправке задач. Метод есть смысл
использовать только для тех процессов, которые его поддерживают.  
[SetStartingProcessNextTask(Dictionary<String, Object>,
CardTask)](M_Tessa_Cards_Workflow_WorkflowExtensions_SetStartingProcessNextTask.htm)|
Устанавливает задание, которое будет использоваться при первом сохранении
сразу же после запуска процесса. Например, задание определяет секции
"постановки задачи", которые заполняются при отправке задач. Метод есть смысл
использовать только для тех процессов, которые его поддерживают.  
[SetStartingProcessTaskGroupRowID](M_Tessa_Cards_Workflow_WorkflowExtensions_SetStartingProcessTaskGroupRowID.htm)|
Устанавливает идентификатор группы в истории заданий для первого задания
бизнес-процесса, запускаемого посредством
[WorkflowStoreExtension](T_Tessa_Cards_Workflow_WorkflowStoreExtension.htm).  
[SetStartingProcessTaskRowID(CardStoreRequest,
Nullable<Guid>)](M_Tessa_Cards_Workflow_WorkflowExtensions_SetStartingProcessTaskRowID_1.htm)|
Устанавливает идентификатор первого задания бизнес-процесса, запускаемого
посредством
[WorkflowStoreExtension](T_Tessa_Cards_Workflow_WorkflowStoreExtension.htm).  
[SetStartingProcessTaskRowID(Dictionary<String, Object>,
Nullable<Guid>)](M_Tessa_Cards_Workflow_WorkflowExtensions_SetStartingProcessTaskRowID.htm)|
Устанавливает идентификатор первого задания бизнес-процесса, запускаемого
посредством
[WorkflowStoreExtension](T_Tessa_Cards_Workflow_WorkflowStoreExtension.htm).  
[SetWorkflowQueue](M_Tessa_Cards_Workflow_WorkflowExtensions_SetWorkflowQueue.htm)|
Устанавливает очередь действий с Workflow для текущей карточки.  
[ToTaskInfo](M_Tessa_Cards_Workflow_WorkflowExtensions_ToTaskInfo.htm)|
Преобразует заданный объект
[IWorkflowProcessInfo](T_Tessa_Cards_Workflow_IWorkflowProcessInfo.htm) с
информацией по подпроцессу к объекту типа
[IWorkflowTaskInfo](T_Tessa_Cards_Workflow_IWorkflowTaskInfo.htm) с
информацией по заданию. При невозможности преобразовать тип будет выдано
исключение
[InvalidCastException](https://learn.microsoft.com/dotnet/api/system.invalidcastexception).
Значение null возвращается только в том случае, если объект processInfo равен
null.  
[TryGetStartingProcessID](M_Tessa_Cards_Workflow_WorkflowExtensions_TryGetStartingProcessID.htm)|
Возвращает идентификатор бизнес-процесса, запускаемого посредством
[WorkflowStoreExtension](T_Tessa_Cards_Workflow_WorkflowStoreExtension.htm),  
[TryGetStartingProcessName](M_Tessa_Cards_Workflow_WorkflowExtensions_TryGetStartingProcessName.htm)|
Возвращает имя бизнес-процесса, запускаемого посредством
[WorkflowStoreExtension](T_Tessa_Cards_Workflow_WorkflowStoreExtension.htm),
или null, если бизнес-процесс не запускается.  
[TryGetStartingProcessNextTask](M_Tessa_Cards_Workflow_WorkflowExtensions_TryGetStartingProcessNextTask.htm)|
Возвращает задание, которое будет использоваться при первом сохранении сразу
же после запуска процесса, или null, если такое задание не было установлено.
Например, задание определяет секции "постановки задачи", которые заполняются
при отправке задач. Метод есть смысл использовать только для тех процессов,
которые его поддерживают.  
[TryGetStartingProcessTaskGroupRowID](M_Tessa_Cards_Workflow_WorkflowExtensions_TryGetStartingProcessTaskGroupRowID.htm)|
Метод запрашивает идентификатор группы в истории заданий для первого задания
бизнес-процесса, запускаемого посредством
[WorkflowStoreExtension](T_Tessa_Cards_Workflow_WorkflowStoreExtension.htm).
Если метод вернул true, то в параметре groupRowID содержится идентификатор
группы, в которую добавляется запись в истории заданий (значение null
означает, что запись добавляется без группы, но не в группу по умолчанию).
Если метод вернул false, то запись добавляется в группу по умолчанию, которая
может отличаться от null.  
[TryGetStartingProcessTaskRowID](M_Tessa_Cards_Workflow_WorkflowExtensions_TryGetStartingProcessTaskRowID.htm)|
Возвращает идентификатор первого задания в бизнес-процессе, запускаемом
посредством
[WorkflowStoreExtension](T_Tessa_Cards_Workflow_WorkflowStoreExtension.htm),
или null, если бизнес-процесс не запускается или идентификатор определяется
самостоятельно в рамках процесса.  
[TryGetWorkflowQueue](M_Tessa_Cards_Workflow_WorkflowExtensions_TryGetWorkflowQueue.htm)|
Возвращает очередь действий с Workflow, отложенных для выполнения на сервере
для текущей карточки, или null, если для текущей карточки очередь ещё не была
создана.  
## __См. также
#### Ссылки
[WorkflowExtensions - ](T_Tessa_Cards_Workflow_WorkflowExtensions.htm)
[Tessa.Cards.Workflow - пространство имён](N_Tessa_Cards_Workflow.htm)
