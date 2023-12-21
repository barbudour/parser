# GroupPosition.AtLast - свойство
В конце группы.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrCompilers](N_Tessa_Extensions_Default_Shared_Workflow_KrCompilers.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static GroupPosition AtLast { get; }
VB __Копировать
     Public Shared ReadOnly Property AtLast As GroupPosition
    	Get
C++ __Копировать
     public:
    static property GroupPosition AtLast {
    	GroupPosition get ();
    }
F# __Копировать
     static member AtLast : GroupPosition with get
#### Значение свойства
[GroupPosition](T_Tessa_Extensions_Default_Shared_Workflow_KrCompilers_GroupPosition.htm)
##  __Заметки
Этапы из этого шаблона в маршруте документа будут всегда в конце своей группы
и, даже если пользователь после пересчета вручную будет добавлять новые этапы,
они добавятся не в конец списка, а будут расположены в списке перед этапами из
шаблона.
## __См. также
#### Ссылки
[GroupPosition -
](T_Tessa_Extensions_Default_Shared_Workflow_KrCompilers_GroupPosition.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrCompilers - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrCompilers.htm)
