# KrProcessSharedHelper.CanBeHidden - метод
Возвращает значение, показывающее, разрешено ли скрытие этапа в дескрипторе
типа этапа или нет.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool CanBeHidden(
    	CardRow row,
    	ICollection<StageTypeDescriptor> descriptors
    )
VB __Копировать
     Public Shared Function CanBeHidden ( 
    	row As CardRow,
    	descriptors As ICollection(Of StageTypeDescriptor)
    ) As Boolean
C++ __Копировать
     public:
    static bool CanBeHidden(
    	CardRow^ row, 
    	ICollection<StageTypeDescriptor^>^ descriptors
    )
F# __Копировать
     static member CanBeHidden : 
            row : CardRow * 
            descriptors : ICollection<StageTypeDescriptor> -> bool 
#### Параметры
row [CardRow](T_Tessa_Cards_CardRow.htm)
    Строка этапа.
descriptors
[ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<[StageTypeDescriptor](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_StageTypeDescriptor.htm)>
    Коллекция дескрипторов типов этапов, в которой выполняется поиск информации.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
Значение true, если скрытие этапа разрешено в дескрипторе типа этапа, иначе -
false.
##  __См. также
#### Ссылки
[KrProcessSharedHelper -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedHelper.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)
