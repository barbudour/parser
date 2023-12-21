# WorkflowSignal - свойства
##  __Свойства
[ID](P_Tessa_Cards_Workflow_WorkflowSignal_ID.htm)| Идентификатор сигнала.  
---|---  
[Info](P_Tessa_Cards_Workflow_WorkflowSignal_Info.htm)| Дополнительная
информация для расширений, связанная с сигналом.  
[IsSealed](P_Tessa_Cards_Workflow_WorkflowSignal_IsSealed.htm)| Признак того,
что объект был защищён от изменений.  
[Name](P_Tessa_Cards_Workflow_WorkflowSignal_Name.htm)|  Имя (алиас) сигнала,
с которым может быть связана произвольная логика обработки, т.е. сигналы
одного типа с разными именами могут обрабатываться по-разному.  
[Number](P_Tessa_Cards_Workflow_WorkflowSignal_Number.htm)|  Номер сигнала, по
которому может определяться способ его прохождения. Можно задать совместно или
вместо имени сигнала [Tessa.Cards.Workflow.IWorkflowSignal.Name].  
[Parameters](P_Tessa_Cards_Workflow_WorkflowSignal_Parameters.htm)| Параметры
поступившего сигнала в произвольном формате.  
[ProcessID](P_Tessa_Cards_Workflow_WorkflowSignal_ProcessID.htm)|
Идентификатор подпроцесса, к которому относится сигнал, или null, если
подпроцесс определяется не по идентификатору, а по имени типа
[Tessa.Cards.Workflow.IWorkflowSignal.ProcessTypeName].  
[ProcessTypeName](P_Tessa_Cards_Workflow_WorkflowSignal_ProcessTypeName.htm)|
Имя типа подпроцесса, на экземпляр которого отправляется сигнал. Имя должно
быть указано для любых экземпляров сигналов: как для подпроцессов с указанным
идентификатором, так и для подпроцессов, существующих в единственном
экземпляре для карточки. Если в текущий момент активно несколько подпроцессов
данного типа и не был указан идентификатор подпроцесса, то только один
экземпляр (случайный) получит сигнал для обработки.  
[Type](P_Tessa_Cards_Workflow_WorkflowSignal_Type.htm)| Тип сигнала, влияет на
способ его обработки.  
##  __См. также
#### Ссылки
[WorkflowSignal - ](T_Tessa_Cards_Workflow_WorkflowSignal.htm)
[Tessa.Cards.Workflow - пространство имён](N_Tessa_Cards_Workflow.htm)
