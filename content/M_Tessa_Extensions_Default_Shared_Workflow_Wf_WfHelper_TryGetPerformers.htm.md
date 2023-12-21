# WfHelper.TryGetPerformers - метод
Возвращает массив строк с ролями исполнителей, используемыми при отправке
резолюции, или null, если получить список невозможно или список пуст.
Возвращаемое значение не может быть пустым массивом.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.Wf](N_Tessa_Extensions_Default_Shared_Workflow_Wf.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static CardRow[] TryGetPerformers(
    	CardTask resolutionPerformerTask
    )
VB __Копировать
     Public Shared Function TryGetPerformers ( 
    	resolutionPerformerTask As CardTask
    ) As CardRow()
C++ __Копировать
     public:
    static array<CardRow^>^ TryGetPerformers(
    	CardTask^ resolutionPerformerTask
    )
F# __Копировать
     static member TryGetPerformers : 
            resolutionPerformerTask : CardTask -> CardRow[] 
#### Параметры
resolutionPerformerTask [CardTask](T_Tessa_Cards_CardTask.htm)
     Задание резолюции, в котором содержится информация по исполнителям. 
#### Возвращаемое значение
[CardRow](T_Tessa_Cards_CardRow.htm)[]  
Массив строк с ролями исполнителей, используемыми при отправке резолюции, или
null, если получить список невозможно или список пуст.
## __См. также
#### Ссылки
[WfHelper - ](T_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper.htm)
[Tessa.Extensions.Default.Shared.Workflow.Wf - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_Wf.htm)
