# DescendantSectionsVisitor.VisitAsync - метод
Выполняет обход всех коллекционных секций, для которых предком является строка
из секции topLevelSectionName.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow](N_Tessa_Extensions_Default_Shared_Workflow.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask VisitAsync(
    	StringDictionaryStorage<CardSection> cardSections,
    	Guid typeID,
    	string topLevelSectionName,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function VisitAsync ( 
    	cardSections As StringDictionaryStorage(Of CardSection),
    	typeID As Guid,
    	topLevelSectionName As String,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask
C++ __Копировать
     public:
    ValueTask VisitAsync(
    	StringDictionaryStorage<CardSection^>^ cardSections, 
    	Guid typeID, 
    	String^ topLevelSectionName, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     member VisitAsync : 
            cardSections : StringDictionaryStorage<CardSection> * 
            typeID : Guid * 
            topLevelSectionName : string * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask 
#### Параметры
cardSections
[StringDictionaryStorage](T_Tessa_Platform_Storage_StringDictionaryStorage_1.htm)<[CardSection](T_Tessa_Cards_CardSection.htm)>
    Секции карточки.
typeID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор типа карточки.
topLevelSectionName
[String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя секции с которой начинается обход.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить выполнение асинхронной задачи.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)  
Асинхронная задача.
##  __См. также
#### Ссылки
[DescendantSectionsVisitor -
](T_Tessa_Extensions_Default_Shared_Workflow_DescendantSectionsVisitor.htm)
[Tessa.Extensions.Default.Shared.Workflow - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow.htm)
