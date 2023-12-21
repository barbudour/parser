# KrConstants.KrCardStorePriority - поле
Коллекция идентификаторов типов карточек, определяющая порядок сохранения
карточек заданных типов.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static readonly ReadOnlyCollection<Guid> KrCardStorePriority
VB __Копировать
     Public Shared ReadOnly KrCardStorePriority As ReadOnlyCollection(Of Guid)
C++ __Копировать
     public:
    static initonly ReadOnlyCollection<Guid>^ KrCardStorePriority
F# __Копировать
     static val KrCardStorePriority: ReadOnlyCollection<Guid>
#### Значение поля
[ReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
##  __Заметки
Чем меньше порядковый номер типа, тем раньше будет выполнено сохранение
карточки данного типа.
## __См. также
#### Ссылки
[KrConstants -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)
