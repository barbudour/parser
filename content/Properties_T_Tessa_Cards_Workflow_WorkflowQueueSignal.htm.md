# WorkflowQueueSignal - свойства
##  __Свойства
[Dynamic](P_Tessa_Cards_CardInfoStorageObject_Dynamic.htm)|  Объект,
осуществляющий доступ к текущему объекту через позднее связывание свойств.  
(Унаследован от
[CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm))  
---|---  
[DynamicInfo](P_Tessa_Cards_CardInfoStorageObject_DynamicInfo.htm)|  Объект,
осуществляющий доступ к дополнительной пользовательской информации по текущему
объекту через позднее связывание свойств.  
(Унаследован от
[CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm))  
[ID](P_Tessa_Cards_Workflow_WorkflowQueueSignal_ID.htm)|  Идентификатор
сигнала.  
[Info](P_Tessa_Cards_CardInfoStorageObject_Info.htm)|  Дополнительная
пользовательская информация.  
(Унаследован от
[CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm))  
[Name](P_Tessa_Cards_Workflow_WorkflowQueueSignal_Name.htm)|  Имя (алиас)
сигнала, с которым может быть связана произвольная логика обработки, т.е.
сигналы одного типа с разными именами могут обрабатываться по-разному. По
умолчанию значение равно null.  
[Number](P_Tessa_Cards_Workflow_WorkflowQueueSignal_Number.htm)|  Номер
сигнала, по которому может определяться способ его прохождения. Можно задать
совместно или вместо имени сигнала
[Name](P_Tessa_Cards_Workflow_WorkflowQueueSignal_Name.htm). По умолчанию
значение равно 0.  
[Parameters](P_Tessa_Cards_Workflow_WorkflowQueueSignal_Parameters.htm)|
Параметры сигнала.  
[ProcessID](P_Tessa_Cards_Workflow_WorkflowQueueSignal_ProcessID.htm)|
Идентификатор подпроцесса, к которому относится сигнал, или null, если
подпроцесс определяется не по идентификатору, а по имени типа
[ProcessTypeName](P_Tessa_Cards_Workflow_WorkflowQueueSignal_ProcessTypeName.htm).
По умолчанию значение равно null.  
[ProcessTypeName](P_Tessa_Cards_Workflow_WorkflowQueueSignal_ProcessTypeName.htm)|
Имя типа подпроцесса, на экземпляр которого отправляется сигнал. Актуально для
процессов, существующих в единственном экземпляре для карточки. Если в текущий
момент активно несколько подпроцессов данного типа, то только один экземпляр
(случайный) получит сигнал для обработки. По умолчанию значение равно null.  
[Type](P_Tessa_Cards_Workflow_WorkflowQueueSignal_Type.htm)|  Тип сигнала,
влияет на способ его обработки.  
## __См. также
#### Ссылки
[WorkflowQueueSignal - ](T_Tessa_Cards_Workflow_WorkflowQueueSignal.htm)
[Tessa.Cards.Workflow - пространство имён](N_Tessa_Cards_Workflow.htm)
