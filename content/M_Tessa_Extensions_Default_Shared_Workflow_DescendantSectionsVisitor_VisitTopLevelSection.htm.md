# DescendantSectionsVisitor.VisitTopLevelSection - метод
Выполняет посещение строки секции верхнего уровня.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow](N_Tessa_Extensions_Default_Shared_Workflow.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     protected abstract void VisitTopLevelSection(
    	CardRow row,
    	CardSection section,
    	IDictionary<Guid, Guid> stageMapping
    )
VB __Копировать
     Protected MustOverride Sub VisitTopLevelSection ( 
    	row As CardRow,
    	section As CardSection,
    	stageMapping As IDictionary(Of Guid, Guid)
    )
C++ __Копировать
     protected:
    virtual void VisitTopLevelSection(
    	CardRow^ row, 
    	CardSection^ section, 
    	IDictionary<Guid, Guid>^ stageMapping
    ) abstract
F# __Копировать
     abstract VisitTopLevelSection : 
            row : CardRow * 
            section : CardSection * 
            stageMapping : IDictionary<Guid, Guid> -> unit 
#### Параметры
row [CardRow](T_Tessa_Cards_CardRow.htm)
    Посещаемая строка.
section [CardSection](T_Tessa_Cards_CardSection.htm)
    Посещаемая секция.
stageMapping
[IDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid),
[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
    Коллекция <ключ-значение>, содержащая соответствие <идентификатор текущей строки - идентификатор строки верхнего уровня>.
##  __См. также
#### Ссылки
[DescendantSectionsVisitor -
](T_Tessa_Extensions_Default_Shared_Workflow_DescendantSectionsVisitor.htm)
[Tessa.Extensions.Default.Shared.Workflow - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow.htm)
